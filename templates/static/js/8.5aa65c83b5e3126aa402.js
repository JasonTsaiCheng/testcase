webpackJsonp([8],{AzWr:function(t,e,n){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var a=n("woOf"),i=n.n(a),r=n("mvHQ"),o=n.n(r),s=n("//Fk"),c=n.n(s),l=n("Xxa5"),u=n.n(l),p=n("exGp"),d=n.n(p),f=n("P9l9"),_=n("O2WP"),g=(n("87lX"),n("t5DY")),m=(_.a.url,{name:"inform",created:function(){this.currentPage=1,this.get_info_list(1,10)},mounted:function(){},methods:{get_info_list:function(t,e){var n=this,a={},i=localStorage.getItem("superior_hospital");a.p=t,a.inform_hospital=i,a.page_size=e,a.ordering="-inform_time",Object(f.j)(a).then(function(t){n.information_list=t.results,n.totalNum=t.count})},handleCurrentChange:function(t){this.currentPage=t,this.get_info_list(t,10)},deleteInform:function(t){var e=this,n={};n.id=t.id,this.$confirm("确认删除该记录吗?","提示",{type:"warning"}).then(function(){var t;Object(f.v)(n).then((t=d()(u.a.mark(function t(n){return u.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:if(1!==n){t.next=6;break}return t.next=3,Object(g.a)();case 3:e.$message({message:"删除成功",type:"success"}),t.next=7;break;case 6:e.$message({message:"删除失败",type:"error"});case 7:e.handleCurrentChange(e.currentPage,10);case 8:case"end":return t.stop()}},t,e)})),function(e){return t.apply(this,arguments)}))})},transferPinfo:function(t){var e=this;return new c.a(function(n){var a={};a.page_size=e.page_size,a.currentPage=e.currentPage,a.patient_name=t.patient.patient_name,a.patient_gender=t.patient.patient_gender,a.patient_age=t.patient.patient_age,a.patient_id=t.patient.patient_id,a.diagnose_record=t.patient.diagnose_record,a.apply_time=t.patient.apply_time,a.picture=t.patient.picture,a.diagnose=t.patient.diagnose,a.historyDisease=t.patient.historyDisease,a.hospital_id=t.patient.hospital,a.minusMessage=t.patient.minusMessage;for(var i=t.inform_hospital,r=[],s=0;s<i.length;s++)r.push(i[s].id);a.id_list=r,localStorage.setItem("patient_info",o()(a)),n("done")})},getDiagnoseStatus:function(t){var e=this;return new c.a(function(n){Object(f.d)(t).then(function(t){0===t?e.$alert("该名患者正在被诊断，您暂时无法诊断","温馨提示",{confirmButtonText:"确定",callback:function(t){console.log(t)}}):2===t&&e.$alert("该名患者已经被诊断","温馨提示",{confirmButtonText:"确定",callback:function(t){console.log(t)}}),n(t)})})},messageAmountProcess:function(t){var e={};e.patient_id=t.patient.patient_id;for(var n=t.inform_hospital,a=[],i=0;i<n.length;i++)a.push(n[i].id);return e.id_list=a,new c.a(function(t){Object(f.r)(e).then(function(e){1===e?console.log("消息减去成功"):console.log("消息减去失败"),t(e)})})},clickToDiagnose:function(t){var e=this;return d()(u.a.mark(function n(){var a,r,o,s;return u.a.wrap(function(n){for(;;)switch(n.prev=n.next){case 0:return(a={}).patient_id=t[["patient"]].patient_id,a.doctor2=localStorage.getItem("user_id"),e.$store.commit("changePageFrom","inform"),r=i()({},a),{},n.next=8,e.getDiagnoseStatus(r);case 8:if(o=n.sent,console.log("1获取诊断状态",o),1!==o){n.next=17;break}return n.next=13,e.transferPinfo(t);case 13:return s=n.sent,console.log("3获取跳转状态",s),n.next=17,e.$router.push("report");case 17:case"end":return n.stop()}},n,e)}))()}},data:function(){return{information_list:"",totalNum:0,currentPage:"",isActive1:!1,isActive2:!0}}}),h={render:function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"container"},[n("el-row",[n("el-col",{attrs:{span:12}},[n("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[n("el-breadcrumb-item",{attrs:{to:{path:"inform"}}},[t._v("消息列表")]),t._v(" "),n("el-breadcrumb-item",[t._v("来自社区")])],1)],1),t._v(" "),n("el-col",{staticClass:"badge",attrs:{span:12}},[n("el-breadcrumb",[n("el-link",{attrs:{underline:!1,type:"primary"}},[n("span",{staticStyle:{"font-weight":"bolder"}})])],1)],1)],1),t._v(" "),n("el-row",[n("el-divider")],1),t._v(" "),n("el-row",{staticClass:"divider"},[t._l(t.information_list,function(e){return n("div",[n("el-row",[n("el-col",{attrs:{span:18}},[n("span",{class:1===e.read?"light_gray":""},[t._v("\n          来自  "+t._s(e.inform_from.hospital_name)+"\n          的  "+t._s(e.patient.patient_name)+"  向您发起催诊提醒，\n          请您尽快诊断\n          ")])]),t._v(" "),n("el-col",{attrs:{span:4}},[n("el-row",{class:1===e.read?"light_gray":"",staticStyle:{"min-width":"200px"}},[t._v(t._s(e.inform_time))])],1),t._v(" "),n("el-col",{attrs:{span:2}},[n("el-row",{staticStyle:{"text-align":"center","min-width":"100px"}},[n("el-col",{attrs:{span:12}},[n("el-link",{attrs:{underline:!1,disabled:1===e.read,icon:"el-icon-view",type:"primary"},on:{click:function(n){return t.clickToDiagnose(e)}}},[t._v("查看")])],1),t._v(" "),n("el-col",{attrs:{span:12}},[n("el-link",{attrs:{underline:!1,icon:"el-icon-delete",type:"info"},on:{click:function(n){return t.deleteInform(e)}}},[t._v("删除")])],1)],1)],1)],1),t._v(" "),n("el-divider")],1)})],2),t._v(" "),n("div",{staticClass:"block"},[n("el-pagination",{attrs:{layout:"prev, pager, next",total:t.totalNum},on:{"current-change":t.handleCurrentChange}})],1)],1)},staticRenderFns:[]};var v=n("VU/8")(m,h,!1,function(t){n("QNlr")},"data-v-79def37e",null);e.default=v.exports},QNlr:function(t,e){}});
//# sourceMappingURL=8.5aa65c83b5e3126aa402.js.map