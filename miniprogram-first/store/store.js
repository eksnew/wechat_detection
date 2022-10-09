//在当前js文件中，我们储存一些帮助不同页面不同部分的数据共用的东西
//为了全局数据共享
import { observable, action } from 'mobx-miniprogram'

export const store = observable({
  
  //数据字段
  activeTabBarIndex:0,//导航栏选中的标签索引
  ifLogin:0,//默认0未登录
  methodChoice:0,//选中的检测方法 0：faster_rcnn   1：detectors_rcnn   2：yolo

  //计算属性
  //actions函数，专门来修改store中数据的值
  updateActiveTabBarIndex: action(function(index){
    this.activeTabBarIndex = index
  }),
  //更新store中的methodChoice变量
  updateChoice:action(function(index){
    this.methodChoice = index
  })

})