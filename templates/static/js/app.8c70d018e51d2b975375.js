webpackJsonp([9],{"9viy":function(n,e){},NHnr:function(n,e,t){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var o=t("7+uW"),i={name:"App",mounted:function(){},methods:{},components:{},data:function(){return{seen:!1,msg:"Hello Vuex"}},store:t("YtJ0").a},a={render:function(){var n=this.$createElement,e=this._self._c||n;return e("div",{attrs:{id:"app"}},[e("transition",{attrs:{name:"fade",mode:"out-in"}},[e("router-view")],1)],1)},staticRenderFns:[]};var r=t("VU/8")(i,a,!1,function(n){t("9viy")},null,null).exports,c=t("/ocq");o.default.use(c.a);var s=new c.a({routes:[{path:"/",name:"login",component:function(){return Promise.all([t.e(0),t.e(1)]).then(t.bind(null,"uIdB"))},hidden:!0},{path:"/",name:"home",component:function(){return Promise.all([t.e(0),t.e(1)]).then(t.bind(null,"UqDP"))},beforeEnter:function(n,e,t){localStorage.getItem("token")?t():t("/")},children:[{path:"/undia",component:function(){return Promise.all([t.e(0),t.e(3)]).then(t.bind(null,"ZH0V"))},name:"undia"},{path:"/dia",component:function(){return Promise.all([t.e(0),t.e(1)]).then(t.bind(null,"tGeh"))},name:"dia"},{path:"/undiaWechat",component:function(){return Promise.all([t.e(0),t.e(4)]).then(t.bind(null,"JeAD"))},name:"undiaWechat"},{path:"/diaWechat",component:function(){return Promise.all([t.e(0),t.e(5)]).then(t.bind(null,"xk+S"))},name:"diaWechat"},{path:"/report",component:function(){return Promise.all([t.e(0),t.e(2)]).then(t.bind(null,"zKBK"))},name:"report"},{path:"/inform",component:function(){return Promise.all([t.e(0),t.e(6)]).then(t.bind(null,"AzWr"))},name:"inform"},{path:"/informWechat",component:function(){return Promise.all([t.e(0),t.e(7)]).then(t.bind(null,"yzzD"))},name:"informWe"}]},{path:"*",hidden:!0,redirect:{path:"/"}}]}),u=t("zL8q"),l=t.n(u);t("tvR6"),t("ezJm"),t("7t+N");o.default.config.productionTip=!1,o.default.use(l.a),new o.default({el:"#app",router:s,components:{App:r},template:"<App/>"})},YtJ0:function(n,e,t){"use strict";var o=t("7+uW"),i=t("NYxO"),a=t("u4WU");o.default.use(i.a);var r={clickUndiagnosed:function(n){n.undiagnosed=!0,n.diagnosed=!1,n.transform=!1,n.statistics=!1,n.report=!1},clickDiagnosed:function(n){n.undiagnosed=!1,n.diagnosed=!0,n.transform=!1,n.statistics=!1,n.report=!1},clickStatistics:function(n){n.undiagnosed=!1,n.diagnosed=!1,n.transform=!1,n.report=!1,n.statistics=!0},clickTransform:function(n){n.undiagnosed=!1,n.diagnosed=!1,n.transform=!0,n.statistics=!1,n.report=!1},clickReport:function(n,e){n.undiagnosed=!1,n.diagnosed=!1,n.transform=!1,n.statistics=!1,n.report=!0,n.patient_info=e},backToUndiagnosed:function(n){n.undiagnosed=!0,n.diagnosed=!1,n.transform=!1,n.statistics=!1,n.report=!1},rememberPageAndSize:function(n,e){n.page_info=e},setInfo:function(n,e){n.user_info={name:a.a.getCookie("name"),token:a.a.getCookie("token")},n.checked=e,console.log("checked",e)},saveHospitalId:function(n,e){n.hospital_id=e,console.log("state.hospital",e)},login:function(n){n.loginPage=!1},changeFlag:function(n,e){n.flag=e},changeSuperShow:function(n,e){n.super_show=e},changeNotification:function(n,e){n.com_notification=e.com_notification,n.we_notification=e.we_notification,n.total_notification=e.total_notification},changePageFrom:function(n,e){n.page_from=e}};e.a=new i.a.Store({state:{patient_info:{},page_info:{},user_info:{},page_from:"",undiagnosed:!1,diagnosed:!1,transform:!1,statistics:!1,report:!1,leftNav:!1,topHeader:!1,login:!0,loginPage:!0,hospital_id:0,checked:!1,flag:!1,position:!1,we_notification:!1,com_notification:!1,total_notification:!1,super_show:!1},mutations:r})},ezJm:function(n,e){},tvR6:function(n,e){},u4WU:function(n,e,t){"use strict";var o={setCookie:function(n,e,t){var o=new Date;o.setTime(o.getTime()+t),o.setDate(o.getDate()+t),document.cookie=n+"="+escape(e)+(null==t?"":";expires="+o.toGMTString())},getCookie:function(n){var e,t=new RegExp("(^| )"+n+"=([^;]*)(;|$)");return(e=document.cookie.match(t))?e[2]:null},delCookie:function(n){var e=new Date;e.setTime(e.getTime()-1),null!=o.getCookie(n)&&(document.cookie=n+"=; expires=Thu, 01 Jan 1970 00:00:01 GMT;"),console.log("delete successfully")}};e.a=o}},["NHnr"]);
//# sourceMappingURL=app.8c70d018e51d2b975375.js.map