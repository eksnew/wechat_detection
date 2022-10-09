// pages/camera/camera.js
const { set } = require("mobx-miniprogram");
var common=require("../../utils/common")

import { storeBindingsBehavior } from 'mobx-miniprogram-bindings'
import { store } from '../../store/store'

Page({

  //全局变量绑定
  //挂载一下全局变量
  behaviors:[storeBindingsBehavior],
  storeBindings:{
    store,
  },

  /**
   * 页面的初始数据
   */
  data: {
      code:"",   //相机获得的相片base64格式
      times:1,   //定时器计数变量
      result_base64:"", //检测后的结果图片的base64格式
      request_allow:1, //是否允许向服务器发送request_POST请求
      methodName:""
  },

  /**
   * 点击拍照函数
   */
  getPhoto:function(){
      this.setData({
        'request_allow': 1
      })
      var flag1 = 1
      this.data.times = flag1
      var timer = setInterval(()=>{ //建立计时器
        var that = this //创建一个名为that的变量来保存this当前的值  
         const ctx = wx.createCameraContext()  //获得创建照相机的容器
         if (that.data.request_allow == 1)
         {
           that.setData({
             'request_allow': 0
           })
         ctx.takePhoto({
            quality:'low', //质量
            success:(res) =>{
              //console.log("图片的临时地址为------："+res.tempImagePath);//图片的临时地址
              common.getPicBase64(res.tempImagePath).then(function(res){ //图片转成base64编码
                //console.log("图片的base64编码------:"+res.data)
                that.data.code = res.data
                //console.log(that.data.code)
              })
            }
          })
                 
          wx.request({     
          url: 'http://10.198.67.131:8088/api/login/',  
          //url: 'http://127.0.0.1:8088/api/login/',
          method: 'POST',  
          data: {
          type:"camera",    
          base1:that.data.code,
          methodChoice:store.methodChoice
          },
          success:  (res)=> {  
            console.log("POST请求成功")     
            //console.log(res.data.result_base64)
            that.setData({
              'result_base64': res.data.result_base64
            })

            if(res.data.state == 1){
              that.setData({
                'request_allow': 1
              })
            }
            else{
              that.setData({
                'request_allow': 0
              })
            }
          },  
          fail:(res)=> {  
            console.log("POST请求失败",res)
            if(res.data.state == 1){
              that.setData({
                'request_allow': 1
              })
            }
            else{
              that.setData({
                'request_allow': 0
              })
            }     
          },    
          });

          }

          var ti = this.data.times
          if(ti == 0){
            clearInterval(timer) //点击停止检测时清除计时器timer
          }
      },3000)//计时器的间隔时间，单位为ms
  },
  stopPhoto:function(){
    var flag = 0
    this.data.times = flag
  },
    /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    if (store.methodChoice == 0){
      this.setData({
        methodName: " rcnn " 
      })
    }
    else if(store.methodChoice == 1){
      this.setData({
        methodName: " detectors " 
      })
    }
    else{
      this.setData({
        methodName: " yolo " 
      })
    }

  },
    /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {
    var flag = 0
    this.data.times = flag
  },



})

