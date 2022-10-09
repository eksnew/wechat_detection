//在当前js文件中，我们储存一些帮助不同页面不同部分的数据共用的东西
//为了全局数据共享
import { observable, action } from 'mobx-miniprogram'

export const store = observable({
  
  //数据字段
  activeTabBarIndex:0,
  ifLogin:0,//默认0未登录

  //计算属性

  //actions函数，专门来修改store中数据的值
  updateActiveTabBarIndex: action(function(index){
    this.activeTabBarIndex = index
  })

})