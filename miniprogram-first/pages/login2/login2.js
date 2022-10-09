// pages/login2/login2.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    nickName: "",  
    avatarUrl: "/pages/images/touxiang.jpg",//存储拿到的用户信息
    hasUserInfo: false,
    canIUseGetUserProfile: false,
  },

//获取用户信息
 login:function(){
    console.log('点击了登录')  
    wx.openSetting({})
    var that = this; 
    wx.getUserInfo({
      desc: '获取用户信息', // 声明获取用户个人信息后的用途，后续会展示在弹窗中，请谨慎填写
      success: function (res) {
        console.log('success', res.userInfo)  
        that.setData({
          nickName: res.userInfo.nickName,
          avatarUrl: res.userInfo.avatarUrl,
          hasUserInfo: true
        })
      },

      fail: function (res) {
        console.log('fail',res)  
        //wx.openSetting({})
      }

    })
  },
    

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
    if (wx.getUserProfile) {
      this.setData({
        canIUseGetUserProfile: true
      })
  }
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