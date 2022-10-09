// custom-tab-bar/index.js

//导入两个成员
import { storeBindingsBehavior } from 'mobx-miniprogram-bindings'
import { store } from '../store/store'

Component({
  /**
   * 组件的属性列表
   */
  properties: {

  },

  //挂载一下
  behaviors:[storeBindingsBehavior],
  
  storeBindings:{
    store,
    fields:{
      active:'activeTabBarIndex'
    },

    actions:{
      updateActive:'updateActiveTabBarIndex'
    },
  },

  /**
   * 组件的初始数据
   */
  data: {
    "list":[
      {
        "pagePath": "/pages/text/text",
        "text": "检测"
      },

      {
        "pagePath": "/pages/history/history",
        "text": "历史记录"
      },
      
      
      {
        "pagePath": "/pages/login2/login2",
        "text": "个人中心"
   
      },

      {
        "pagePath": "/pages/config/config",
        "text": "设置"
      }
    ]

  },

  /**
   * 组件的方法列表
   */
  methods: {

    onChange(event) {
      // event.detail 的值为当前选中项的索引
      //this.setData({ active: event.detail });
      this.updateActive(event.detail)
      wx.switchTab({
        url:this.data.list[event.detail].pagePath,
      })
    },


  }
})
