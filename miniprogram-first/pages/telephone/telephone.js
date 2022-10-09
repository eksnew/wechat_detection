// pages/telephone/telephone.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    phone:"",
    code:"",
  },
  bindPhone:function(e){
    this.setData({ phone:e.detail.value});
  },
  bindCode:function(e){
    this.setData({ code:e.detail.value})
  },
  login:function(e){
    console.log(this.data.phone,this.data.code);
    //手机号和验证码发送到后端，后端进行登录
    wx.request({
      url: 'http://127.0.0.1:8088/api/login/',  //地址************
      data: {tpye:"telephone", phone:this.data.phone, code:this.data.code},  //传的参数*********
      method: 'POST',  //请求方式***********
      success: (res) => {
        console.log(res)
      },
      //fail: (res) => {},
      //complete: (res) => {},
      //dataType: dataType, //返回的数据类型，做数据校验的?
      //enableCache: true,
      //enableHttp2: true,
      //enableQuic: true,
      //header: header,
      //responseType: responseType,//其实没啥用？
      //timeout: 0,
    })
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