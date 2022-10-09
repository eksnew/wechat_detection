// pages/camera/camera.js
const { set } = require("mobx-miniprogram");
var common=require("../../utils/common")
Page({

  /**
   * 页面的初始数据
   */
  data: {
      code:"",
  },

  /**
   * 点击拍照函数
   */
  getPhoto:function(){
    var mm = this.data.code
    var n
    const ctx = wx.createCameraContext()  //获得创建照相机的容器
    ctx.takePhoto({
      quality:'high', //质量
      success:(res) =>{
        console.log("图片的临时地址为------："+res.tempImagePath);//图片的临时地址
        //图片转为base64数据
        n = res.tempImagePath
        common.getPicBase64(res.tempImagePath).then(function(res){
          //console.log("图片的base64编码------:"+res.data)
          console.log(mm)
        })
      }
    })

    var that = this //创建一个名为that的变量来保存this当前的值  
    wx.request({  
       url: 'https://127.0.0.1:8080/',  
       method: 'POST',  
       data: {  
        name:'is',
        age:33
       },  
       success:  (res)=> {  
         console.log(res.data)  
       }  
   });
  },
})