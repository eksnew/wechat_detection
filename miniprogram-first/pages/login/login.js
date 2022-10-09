// pages/login/login.js
const app = getApp()

Page({

  /**
   * 页面的初始数据
   */
  data: {
    userInfo:  {nikeName: "",  avatarUrl: "/pages/images/touxiang.jpg"}//存储拿到的用户信息

  },

  //点击登录函数  昵称 头像 性别信息传到回调参数e
  auth:function(e){
    console.log("666")
    //var userInfo = JSON.stringify(e.detail.userInfo)
    var userInfo = JSON.stringify(e.detail.userInfo)
    console.log(userInfo)
    this.setData({
      userInfo : e.detail.userInfo
    });  //获取到了用户信息 存起来到变量userInfo
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