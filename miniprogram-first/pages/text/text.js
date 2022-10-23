// pages/text/text.js
//导入两个成员
import { storeBindingsBehavior } from 'mobx-miniprogram-bindings'
import { store } from '../../store/store'


Page({

  /**
   * 页面的初始数据
   */ 
  //挂载一下全局变量
  behaviors:[storeBindingsBehavior],
  storeBindings:{
    store,
    fields:{
      methodChoice:'methodChoice',
      score_thr:'score_thr'
    },

    actions:{
      updateChoice:'updateChoice',
      updateScore:'updateScore'
    },
  },

  data: {

  },

  /**
   * 打开摄像头函数--
   */
  openCamera:function(){
    wx.navigateTo({
      url:'../camera/camera',
    })
  },
  
  //轮播图切换时调用的函数
  handleSwiperChange:function(e){
    this.updateChoice(e.detail.current)
    this.setData({
      methodChoice:e.detail.current
    })
    //console.log(  store.methodChoice)
    //console.log( e.detail.current)

  },
  //改变检测置信度阈值时调用的函数
  formSubmit:function(e){
    this.updateScore(e.detail.value.score)
    //console.log(e.detail.value.score)
    this.setData({
      score_thr:e.detail.value.score
    })
    console.log(  store.score_thr)
    
  },




  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady() {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow() {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide() {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload() {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh() {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom() {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage() {

  }
})