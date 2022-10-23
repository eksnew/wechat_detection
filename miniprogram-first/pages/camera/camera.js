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
      tempImagePath:"",
      canvasId: "myCanvas",
      canvas:{test:''},//画布-canvas 对象
      ctx2: {test:''},//画布-ctx 渲染上下文


      times:1,   //定时器计数变量
      result_base64:"", //检测后的结果图片的base64格式
      request_allow:1, //是否允许向服务器发送request_POST请求
      methodName:"",
      detectionFps:"",
      detectionTime1:0,
      detectionTime2:0,
      score_thr:0 //检测置信度阈值
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
        
        //收到服务器答复时运行
        if (that.data.request_allow == 1)
        {

          that.setData({
          'request_allow': 0
          })

          //显示帧率部分
          var v1 = 1000.0/(that.data.detectionTime1-that.data.detectionTime2)
          var v2 = parseFloat(v1).toFixed(3)
          that.setData({
            detectionFps: v2
          })

          //计算帧率部分
          var myDate = new Date();
          that.setData({
            detectionTime2: that.data.detectionTime1, 
            detectionTime1: myDate.getTime(), //获取当前时间(从1970.1.1开始的毫秒数) 
          })

          //获取相机图片部分
          ctx.takePhoto({
            quality:'low', //质量
            success:(res) =>{
              //console.log("图片的临时地址为------："+res.tempImagePath);//图片的临时地址
              that.setData({
                tempImagePath : res.tempImagePath
              })
              common.getPicBase64(res.tempImagePath).then(function(res){ //图片转成base64编码
                //console.log("图片的base64编码------:"+res.data)
                that.data.code = res.data
                //console.log(that.data.code)
              })
            }
          })


          wx.request({     
            url: 'http://10.198.67.46:8080/api/login/',  
            //url: 'http://127.0.0.1:8080/api/login/',
            method: 'POST',  
            data: {
            type:"camera",    
            base1:that.data.code,
            methodChoice:store.methodChoice,
            score_thr:store.score_thr
            },
            success:  (res)=> {  
              console.log("POST请求成功")
              console.log("res.data.result_base64----------")  
              console.log(res.data.result_base64)     
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

          //获取canvas和ctx2并初始化画布
          const query = wx.createSelectorQuery()
          query.select('#myCanvas')// 在 WXML 中填入的 id
          .fields({ node: true, size: true })
          .exec((res) => {
            // Canvas 对象
            const canvas = res[0].node
            // 渲染上下文
            const ctx2 = canvas.getContext('2d')
            // Canvas 画布的实际绘制宽高
            const width = res[0].width
            const height = res[0].height
            // 初始化画布大小
            const dpr = 750 / wx.getSystemInfoSync().windowWidth;
            console.log(dpr)
            //const dpr = wx.getSystemInfoSync().pixelRatio
            canvas.width = res[0].width * dpr
            canvas.height = res[0].height * dpr
            ctx2.scale(dpr, dpr)
          
          //-------------------------------------------------------------------
            ctx2.strokeStyle = 'rgb(0, 255, 0) '; //矩形框颜色
            ctx2.lineWidth = 2; //矩形框粗细
            //ctx2.strokeText(string text, number x, number y, number maxWidth)
            ctx2.font = 'normal  15px sans-serif ';//字体字号
            ctx2.fillStyle="#FFFF00";//文字颜色
            var width_px = res[0].width
            var height_px = res[0].height
            var result = that.data.result_base64
            
            for (let key in result) {
              console.log(result[key][1])
              console.log(width_px)
              console.log(height_px)
              ctx2.fillText(key, result[key][1]*width_px, result[key][2]*height_px)//汉字标注
              ctx2.strokeRect((result[key][1]*width_px).toFixed(), (result[key][2]*height_px).toFixed(), ((result[key][3]-result[key][1])*width_px).toFixed(), ((result[key][4]-result[key][2])*height_px).toFixed()); //绘制矩形框
            }
            //-------------------------------------------------------------------
          })
        }
    
        var ti = this.data.times
        if(ti == 0){
          clearInterval(timer) //点击停止检测时清除计时器timer
        }
      },10)//间隔时间
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
    else if(store.methodChoice == 2){
      this.setData({
        methodName: " yolo " 
      })
    }
    else{
      this.setData({
        methodName: " transfer " 
      })
    }
    //检测置信度阈值
    //console.log(store.score_thr)
    this.setData({
      'score_thr': store.score_thr
    })
  },
    /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {
    var flag = 0
    this.data.times = flag
 

  },



})

