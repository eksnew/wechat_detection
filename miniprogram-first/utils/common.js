
//图片转base64函数
function getPicBase64(tempFilePath){
  //做成异步
  return new Promise(function(resolve,reject){
    wx.getFileSystemManager().readFile({
      filePath: tempFilePath,
      encoding:"base64",
      success:function(data){
        console.log(data) //返回base64编码结果
        resolve(data);
      }
    })
  })
}

//开放函数接口
module.exports = {
  getPicBase64:getPicBase64
}