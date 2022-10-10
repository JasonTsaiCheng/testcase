webpackJsonp([4],{"+7Be":function(e,t){},JeAD:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i=a("U0uc"),r={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"undiagnosed"},[a("el-row",[a("el-breadcrumb",{attrs:{"separator-class":"el-icon-arrow-right"}},[a("el-breadcrumb-item",{attrs:{to:{path:"undia"}}},[e._v("未诊列表")]),e._v(" "),a("el-breadcrumb-item",[e._v("来自微信")])],1)],1),e._v(" "),a("el-row",{staticClass:"operationNew"},[a("el-col",{staticStyle:{"text-align":"left"},attrs:{span:3}},[a("el-button",{attrs:{type:"primary"},on:{click:e.refresh}},[e._v("查看全部")])],1),e._v(" "),a("el-col",{staticClass:"timepicker",staticStyle:{"text-align":"left"},attrs:{span:3}},[a("el-date-picker",{attrs:{type:"date",align:"right",placeholder:"选择日期","picker-options":e.pickerOptions},on:{change:e.selectDate},model:{value:e.dateValue,callback:function(t){e.dateValue=t},expression:"dateValue"}})],1),e._v(" "),a("el-col",{attrs:{span:5}},[e._v(" ")]),e._v(" "),a("el-col",{attrs:{span:4}},[e._v(" ")]),e._v(" "),a("div",{staticStyle:{"text-align":"center"}},[a("el-col",{attrs:{span:2}},[a("a",{attrs:{href:"javascript:;"},on:{click:e.refresh}},[a("i",{staticClass:"icon iconfont icon-shuaxin1"}),e._v("刷新")])]),e._v(" "),a("el-col",{attrs:{span:5}},[a("el-input",{attrs:{placeholder:"输入患者姓名/手机号/身份证号 可模糊检索"},model:{value:e.inputVal,callback:function(t){e.inputVal=t},expression:"inputVal"}})],1),e._v(" "),a("el-col",{attrs:{span:2}},[a("el-button",{attrs:{type:"primary",icon:"el-icon-search"},on:{click:e.searchBtn}},[e._v("搜索")])],1)],1)],1),e._v(" "),a("el-row",[a("form",{staticStyle:{width:"auto"},attrs:{action:"",method:"POST",id:"jvForm",enctype:"multipart/form-data"}},[a("input",{staticStyle:{display:"none"},attrs:{type:"file",name:"patient_img",accept:"image/*",multiple:"multiple",id:"fileToUpload"},on:{change:e.uploadPic}})])]),e._v(" "),a("el-row",{staticClass:"dataZone"},[[a("el-table",{staticStyle:{width:"100%"},attrs:{data:e.tableData,stripe:""}},[a("el-table-column",{attrs:{prop:"patient_name",label:"姓名"}}),e._v(" "),a("el-table-column",{attrs:{prop:"patient_gender",label:"性别",formatter:e.formatSex}}),e._v(" "),a("el-table-column",{attrs:{prop:"patient_age",label:"年龄"}}),e._v(" "),a("el-table-column",{attrs:{prop:"patient_tel",label:"手机号"}}),e._v(" "),a("el-table-column",{attrs:{prop:"apply_time",label:"录入时间"}}),e._v(" "),a("el-table-column",{attrs:{prop:"status",label:"诊断状态",formatter:e.formatStatus}}),e._v(" "),a("el-table-column",{attrs:{prop:"payment",label:"付费状态",formatter:e.formatPayment}}),e._v(" "),a("el-table-column",{attrs:{label:"操作",width:"180"},scopedSlots:e._u([{key:"default",fn:function(t){return[e.superHos?a("div",[a("el-tooltip",{attrs:{content:"诊断",placement:"left"}},[e.formatButton(t.row)?a("el-button",{attrs:{type:"warning",size:"small",icon:"el-icon-first-aid-kit",circle:""},on:{click:function(a){return e.clickToDiagnose(t.$index,t.row)}}}):e._e()],1),e._v(" "),a("el-tooltip",{attrs:{content:"删除",placement:"left"}},[e.formatButton(t.row)?e._e():a("el-button",{attrs:{type:"danger",size:"small",icon:"el-icon-delete",circle:""},on:{click:function(a){return e.handleDel(t.$index,t.row)}}})],1),e._v(" "),a("el-tooltip",{attrs:{content:"编辑",placement:"right"}},[a("el-button",{attrs:{type:"success",size:"small",icon:"el-icon-edit",circle:""},on:{click:function(a){return e.handleEdit(t.$index,t.row)}}})],1),e._v(" "),a("el-tooltip",{attrs:{content:"上传照片",placement:"right"}},[a("el-button",{attrs:{type:"primary",size:"small",icon:"el-icon-upload2",circle:""},on:{click:function(a){return e.uploadPicture(t.$index,t.row)}}})],1)],1):e._e(),e._v(" "),e.normalHos?a("div",[a("el-tooltip",{attrs:{content:"删除",placement:"left"}},[e.formatButton(t.row)?e._e():a("el-button",{attrs:{type:"danger",size:"small",icon:"el-icon-delete",circle:""},on:{click:function(a){return e.handleDel(t.$index,t.row)}}})],1),e._v(" "),a("el-tooltip",{attrs:{content:"编辑",placement:"right"}},[a("el-button",{attrs:{type:"success",size:"small",icon:"el-icon-edit",circle:""},on:{click:function(a){return e.handleEdit(t.$index,t.row)}}})],1),e._v(" "),a("el-tooltip",{attrs:{content:"上传照片",placement:"right"}},[a("el-button",{attrs:{type:"primary",size:"small",icon:"el-icon-upload2",circle:""},on:{click:function(a){return e.uploadPicture(t.$index,t.row)}}})],1)],1):e._e()]}}])})],1)]],2),e._v(" "),a("el-row",{staticClass:"pagination"},[a("el-pagination",{attrs:{"current-page":e.currentPage,"page-sizes":[5,10],"page-size":e.page_size,"pager-count":7,layout:"total, sizes, prev, pager, next, jumper",total:e.totalNum},on:{"size-change":e.handleSizeChange,"current-change":e.handleCurrentChange,"update:currentPage":function(t){e.currentPage=t},"update:current-page":function(t){e.currentPage=t}}})],1),e._v(" "),a("el-dialog",{attrs:{title:"添加患者",visible:e.addFormVisible,"close-on-click-modal":!1},on:{"update:visible":function(t){e.addFormVisible=t}},model:{value:e.addFormVisible,callback:function(t){e.addFormVisible=t},expression:"addFormVisible"}},[a("el-form",{ref:"addForm",attrs:{model:e.addForm,"label-width":"80px",rules:e.addFormRules}},[a("el-form-item",{staticStyle:{width:"25%"},attrs:{label:"姓名",prop:"patient_name"}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.addForm.patient_name,callback:function(t){e.$set(e.addForm,"patient_name",t)},expression:"addForm.patient_name"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"手机号",prop:"patient_tel"}},[a("el-input",{staticStyle:{width:"25%"},attrs:{type:"text",placeholder:"手机号",oninput:"value=value.replace(/[^\\d]/g,'')",maxlength:"11","show-word-limit":""},model:{value:e.addForm.patient_tel,callback:function(t){e.$set(e.addForm,"patient_tel",t)},expression:"addForm.patient_tel"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"年龄",prop:"patient_age"}},[a("el-input-number",{staticStyle:{width:"25%"},attrs:{min:0,max:200},model:{value:e.addForm.patient_age,callback:function(t){e.$set(e.addForm,"patient_age",t)},expression:"addForm.patient_age"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"身份证号",prop:"ID_number"}},[a("el-input",{staticStyle:{width:"25%"},attrs:{type:"text",placeholder:"身份证",oninput:"value=value.replace(/[\\W]/g,'')",maxlength:"18","show-word-limit":""},model:{value:e.addForm.ID_number,callback:function(t){e.$set(e.addForm,"ID_number",t)},expression:"addForm.ID_number"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"性别"}},[a("el-radio-group",{attrs:{onclick:e.disabledPregnant()},model:{value:e.addForm.patient_gender,callback:function(t){e.$set(e.addForm,"patient_gender",t)},expression:"addForm.patient_gender"}},[a("el-radio",{staticClass:"radio",attrs:{label:0},model:{value:e.addForm.genderRadio,callback:function(t){e.$set(e.addForm,"genderRadio",t)},expression:"addForm.genderRadio"}},[e._v("男")]),e._v(" "),a("el-radio",{staticClass:"radio",attrs:{label:1},model:{value:e.addForm.genderRadio,callback:function(t){e.$set(e.addForm,"genderRadio",t)},expression:"addForm.genderRadio"}},[e._v("女")])],1)],1),e._v(" "),a("el-form-item",{attrs:{label:"支付状态"}},[a("el-radio-group",{model:{value:e.addForm.payment,callback:function(t){e.$set(e.addForm,"payment",t)},expression:"addForm.payment"}},[a("el-radio",{staticClass:"radio",attrs:{label:0},model:{value:e.addForm.paymentRadio,callback:function(t){e.$set(e.addForm,"paymentRadio",t)},expression:"addForm.paymentRadio"}},[e._v("未支付")]),e._v(" "),a("el-radio",{staticClass:"radio",attrs:{label:1},model:{value:e.addForm.paymentRadio,callback:function(t){e.$set(e.addForm,"paymentRadio",t)},expression:"addForm.paymentRadio"}},[e._v("已支付")])],1)],1),e._v(" "),a("el-form-item",{attrs:{label:"既往史",prop:"jwsExist"}},[a("el-radio-group",{attrs:{onclick:e.jwsClick()},model:{value:e.addForm.jwsExist,callback:function(t){e.$set(e.addForm,"jwsExist",t)},expression:"addForm.jwsExist"}},[a("el-radio",{staticClass:"radio",attrs:{label:1},model:{value:e.addForm.jwsRadio,callback:function(t){e.$set(e.addForm,"jwsRadio",t)},expression:"addForm.jwsRadio"}},[e._v("有")]),e._v(" "),a("el-radio",{staticClass:"radio",attrs:{label:0},model:{value:e.addForm.jwsRadio,callback:function(t){e.$set(e.addForm,"jwsRadio",t)},expression:"addForm.jwsRadio"}},[e._v("无")])],1),e._v(" "),a("br"),e._v(" "),e.addForm.jwsVisible?a("el-form-item",[a("el-checkbox",{model:{value:e.jwsForm.DM_year,callback:function(t){e.$set(e.jwsForm,"DM_year",t)},expression:"jwsForm.DM_year"}},[e._v("糖尿病")]),e._v(" "),a("el-checkbox",{model:{value:e.jwsForm.HTN_year,callback:function(t){e.$set(e.jwsForm,"HTN_year",t)},expression:"jwsForm.HTN_year"}},[e._v("高血压")]),e._v(" "),a("el-checkbox",{model:{value:e.jwsForm.HPL_year,callback:function(t){e.$set(e.jwsForm,"HPL_year",t)},expression:"jwsForm.HPL_year"}},[e._v("高血脂")]),e._v(" "),a("span",[e._v("        妊娠:")]),a("el-input-number",{attrs:{disabled:e.pregnant_seen,"controls-position":"right",size:"mini",min:0,max:100},model:{value:e.jwsForm.pregnant_weeks,callback:function(t){e.$set(e.jwsForm,"pregnant_weeks",t)},expression:"jwsForm.pregnant_weeks"}}),e._v("周\n          "),a("br"),e._v(" "),a("span",[e._v("其他:   ")]),a("el-input",{staticStyle:{width:"434px"},attrs:{size:"mini",placeholder:"请输入内容(20个字符以内)",maxlength:"20",clearable:""},model:{value:e.jwsForm.other,callback:function(t){e.$set(e.jwsForm,"other",t)},expression:"jwsForm.other"}}),e._v(" "),a("br"),e._v(" "),a("span",[e._v("屈光度:")]),e._v("\n          左眼:"),[a("el-select",{staticStyle:{width:"160px"},attrs:{size:"mini",clearable:"",placeholder:"请选择"},model:{value:e.leftDiopterValue,callback:function(t){e.leftDiopterValue=t},expression:"leftDiopterValue"}},e._l(e.leftDiopter,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)],e._v("\n                    右眼:"),[a("el-select",{staticStyle:{width:"160px"},attrs:{size:"mini",clearable:"",placeholder:"请选择"},model:{value:e.rightDiopterValue,callback:function(t){e.rightDiopterValue=t},expression:"rightDiopterValue"}},e._l(e.rightDiopter,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)]],2):e._e()],1),e._v(" "),a("br"),e._v(" "),a("el-form-item",{attrs:{label:"地址",prop:"address"}},[a("el-input",{attrs:{type:"textarea"},model:{value:e.addForm.address,callback:function(t){e.$set(e.addForm,"address",t)},expression:"addForm.address"}})],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{nativeOn:{click:function(t){e.addFormVisible=!1}}},[e._v("取消")]),e._v(" "),a("el-button",{attrs:{type:"primary",loading:e.addLoading},nativeOn:{click:function(t){return e.addSubmit(t)}}},[e._v("提交")])],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"编辑",visible:e.editFormVisible,"close-on-click-modal":!1},on:{"update:visible":function(t){e.editFormVisible=t}},model:{value:e.editFormVisible,callback:function(t){e.editFormVisible=t},expression:"editFormVisible"}},[a("el-form",{ref:"editForm",attrs:{model:e.editForm,"label-width":"80px",rules:e.editFormRules}},[a("el-form-item",{staticStyle:{width:"25%"},attrs:{label:"姓名",prop:"patient_name"}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.editForm.patient_name,callback:function(t){e.$set(e.editForm,"patient_name",t)},expression:"editForm.patient_name"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"手机号",prop:"patient_tel"}},[a("el-input",{staticStyle:{width:"25%"},attrs:{type:"text",placeholder:"手机号",oninput:"value=value.replace(/[^\\d]/g,'')",maxlength:"11","show-word-limit":""},model:{value:e.editForm.patient_tel,callback:function(t){e.$set(e.editForm,"patient_tel",t)},expression:"editForm.patient_tel"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"年龄",prop:"patient_age"}},[a("el-input-number",{staticStyle:{width:"25%"},attrs:{min:0,max:200},model:{value:e.editForm.patient_age,callback:function(t){e.$set(e.editForm,"patient_age",t)},expression:"editForm.patient_age"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"身份证号",prop:"ID_number"}},[a("el-input",{staticStyle:{width:"25%"},attrs:{type:"text",placeholder:"身份证",oninput:"value=value.replace(/[\\W]/g,'')",maxlength:"18","show-word-limit":""},model:{value:e.editForm.ID_number,callback:function(t){e.$set(e.editForm,"ID_number",t)},expression:"editForm.ID_number"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"性别"}},[a("el-radio-group",{attrs:{onchange:e.handlePregnant()},model:{value:e.editForm.patient_gender,callback:function(t){e.$set(e.editForm,"patient_gender",t)},expression:"editForm.patient_gender"}},[a("el-radio",{staticClass:"radio",attrs:{label:"0"}},[e._v("男")]),e._v(" "),a("el-radio",{staticClass:"radio",attrs:{label:"1"}},[e._v("女")])],1)],1),e._v(" "),a("el-form-item",{attrs:{label:"支付状态"}},[a("el-radio-group",{model:{value:e.editForm.payment,callback:function(t){e.$set(e.editForm,"payment",t)},expression:"editForm.payment"}},[a("el-radio",{staticClass:"radio",attrs:{label:"0"}},[e._v("未支付")]),e._v(" "),a("el-radio",{staticClass:"radio",attrs:{label:"1"}},[e._v("已支付")])],1)],1),e._v(" "),a("el-form-item",{attrs:{label:"既往史"}},[[a("el-radio-group",{attrs:{onchange:e.editjws()},model:{value:e.radio,callback:function(t){e.radio=t},expression:"radio"}},[a("el-radio",{attrs:{label:3}},[e._v("有")]),e._v(" "),a("el-radio",{attrs:{label:6}},[e._v("无")])],1)],e._v(" "),a("br"),e._v(" "),e.editFormjwsVisible?a("el-form-item",[a("el-checkbox",{model:{value:e.editFormJwsForm.DM_year,callback:function(t){e.$set(e.editFormJwsForm,"DM_year",t)},expression:"editFormJwsForm.DM_year"}},[e._v("糖尿病")]),e._v(" "),a("el-checkbox",{model:{value:e.editFormJwsForm.HTN_year,callback:function(t){e.$set(e.editFormJwsForm,"HTN_year",t)},expression:"editFormJwsForm.HTN_year"}},[e._v("高血压")]),e._v(" "),a("el-checkbox",{model:{value:e.editFormJwsForm.HPL_year,callback:function(t){e.$set(e.editFormJwsForm,"HPL_year",t)},expression:"editFormJwsForm.HPL_year"}},[e._v("高血脂")]),e._v(" "),a("span",[e._v("        妊娠:")]),a("el-input-number",{attrs:{disabled:e.pre_seen,"controls-position":"right",size:"mini",min:0,max:100},model:{value:e.editFormJwsForm.pregnant_weeks,callback:function(t){e.$set(e.editFormJwsForm,"pregnant_weeks",t)},expression:"editFormJwsForm.pregnant_weeks"}}),e._v("周\n          "),a("br"),e._v(" "),a("span",[e._v("其他:   ")]),a("el-input",{staticStyle:{width:"434px"},attrs:{size:"mini",placeholder:"请输入内容(20个字符以内)",maxlength:"20",clearable:""},model:{value:e.editFormJwsForm.other,callback:function(t){e.$set(e.editFormJwsForm,"other",t)},expression:"editFormJwsForm.other"}}),e._v(" "),a("br"),e._v(" "),a("span",[e._v("屈光度:")]),e._v("\n          左眼:"),[a("el-select",{staticStyle:{width:"160px"},attrs:{size:"mini",clearable:"",placeholder:"请选择"},model:{value:e.editFormLeftDiopterValue,callback:function(t){e.editFormLeftDiopterValue=t},expression:"editFormLeftDiopterValue"}},e._l(e.editFormLeftDiopter,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)],e._v("\n                    右眼:"),[a("el-select",{staticStyle:{width:"160px"},attrs:{size:"mini",clearable:"",placeholder:"请选择"},model:{value:e.editFormRightDiopterValue,callback:function(t){e.editFormRightDiopterValue=t},expression:"editFormRightDiopterValue"}},e._l(e.editFormLeftDiopter,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)]],2):e._e()],2),e._v(" "),a("br"),e._v(" "),a("el-form-item",{attrs:{label:"地址",prop:"address"}},[a("el-input",{attrs:{type:"textarea"},model:{value:e.editForm.address,callback:function(t){e.$set(e.editForm,"address",t)},expression:"editForm.address"}})],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{nativeOn:{click:function(t){e.editFormVisible=!1}}},[e._v("取消")]),e._v(" "),a("el-button",{attrs:{type:"primary",loading:e.editLoading},nativeOn:{click:function(t){return e.editSubmit(t)}}},[e._v("提交")])],1)],1)],1)},staticRenderFns:[]};var o=function(e){a("+7Be")},l=a("VU/8")(i.a,r,!1,o,"data-v-b4cb03dc",null);t.default=l.exports},U0uc:function(e,t,a){"use strict";(function(e){var i=a("Xxa5"),r=a.n(i),o=a("exGp"),l=a.n(o),n=a("mvHQ"),s=a.n(n),d=a("woOf"),c=a.n(d),m=a("mtWM"),p=a.n(m),u=a("P9l9"),_=a("O2WP"),g=a("u4WU"),h=(a("87lX"),_.a.url);t.a={name:"undiaWechat",created:function(){"1"===localStorage.getItem("type")?(this.superHos=!0,this.normalHos=!1):(this.normalHos=!0,this.superHos=!1);var e=this.$store.state.page_info_we,t=e.currentPage,a=e.page_size;this.currentPage=t,this.page_size=a,this.get_patients(t,a)},mounted:function(){},methods:{refresh:function(){e("#selectMenu").html("查看全部"),this.payment="";var t=this.$store.state.page_info_we.page_size;this.currentPage=1,this.inputVal="",this.dateValue="",this.tableData=[],this.get_patients(1,t,"","")},delieverPageAndSize:function(){var e=this.currentPage,t=this.page_size,a={};a.currentPage=e,a.page_size=t,this.$store.commit("rememberWePageAndSize",a)},handleSizeChange:function(e){this.$store.commit("changeFlag",!1);var t=e;this.page_size=t,this.currentPage=1;var a=this.currentPage,i=this.inputVal;this.delieverPageAndSize(),console.log(a,t),this.otherDate?(this.get_patients(a,t,this.dateValue,i),console.log("otherdate")):(this.get_patients(a,t,"",i),console.log("page_size total"))},handleCurrentChange:function(e){this.$store.commit("changeFlag",!1);var t=e,a=this.page_size,i=this.inputVal,r=this.payment;this.delieverPageAndSize(),this.otherDate?this.get_patients(t,a,this.dateValue,i,r):this.get_patients(t,a,"",i,r)},get_patients:function(e,t,a,i,r){var o=this,l={};l.doctor2=localStorage.getItem("user_id"),l.p=e,l.page_size=t,l.apply_time=a,l.search=i,l.ordering="-apply_time",l.status=0,l.payment=r,Object(u.k)(l).then(function(e){console.log("response",e),o.tableData=e.results,o.totalNum=e.count}).catch(function(a){console.log(a),e-=1,p.a.get(h+"/patients/?p="+e+"&page_size="+t+"&hospital_id="+hospital_id+"&ordering=-apply_time&status=0").then(function(e){console.log("response",e),o.tableData=e.patient_list,o.totalNum=e.count})})},get_patients_by_rules:function(e,t,a,i){var r=this,o={};o.p=e,o.page_size=t,o.apply_time=a,o.search=i,o.ordering="-apply_time",o.status=0,Object(u.k)(o).then(function(e){console.log("response",e),r.tableData=e,r.totalNum=e.length}).catch(function(e){console.log(e)})},selectDate:function(){this.otherDate=!0;var e=new Date(this.dateValue),t=e.getFullYear(),a=e.getMonth()+1,i=e.getDate(),r=this.payment;a>=1&&a<=9&&(a="0"+a),i>=0&&i<=9&&(i="0"+i);var o=t+"-"+a+"-"+i;this.dateValue=o,this.currentPage=1;var l=this.inputVal;"1970-01-01"===o&&(o=""),this.get_patients(1,this.page_size,o,l,r)},searchBtn:function(){var e=this.payment;this.currentPage=1,this.get_patients(1,this.page_size,this.dateValue,this.inputVal,e)},formatSex:function(e){var t=e.patient_gender;return"0"===t?"男":"1"===t?"女":"未知"},formatStatus:function(e){var t=e.status;return"0"===t?"未诊断":"2"===t?"已诊断":"诊断中"},formatPayment:function(e){var t=e.payment;return 0===t?"未付费":1===t?"已付费":"未知"},formatButton:function(e){return"1"===e.pic_upload||"0"!==e.pic_upload},handleEdit:function(e,t){var a=t.historyDisease;this.editForm=c()({},t),this.editForm.isFront=!0,a[0]?(this.editFormVisible=!0,1!==a[0].DM_year&&!0!==a[0].DM_year||(a[0].DM_year=!0),1!==a[0].HPL_year&&!0!==a[0].HPL_year||(a[0].HPL_year=!0),1!==a[0].HTN_year&&!0!==a[0].HTN_year||(a[0].HTN_year=!0),0===a[0].pregnant_weeks&&(a[0].pregnant_weeks=""),this.editFormJwsForm=a[0],this.editFormLeftDiopterValue=a[0].left_diopter,this.editFormRightDiopterValue=a[0].right_diopter,this.editForm.jwsExist=1,this.editFormjwsVisible=!0,this.radio=3):(this.editFormVisible=!0,this.editForm.jwsExist=0,this.editFormjwsVisible=!1,this.radio=6)},handleAdd:function(){this.addFormVisible=!0,this.addForm={patient_name:"",patient_gender:0,payment:0,patient_age:0,patient_tel:"",address:"",jwsRadio:0,genderRadio:0,paymentRadio:0,jwsVisible:!1,jwsExist:""}},checkIsDiagnoseAgain:function(){var e=this,t=c()({},this.addForm);t.username=g.a.getCookie("name"),Object(u.c)(t).then(function(t){"0"==t?console.log("查无此人"):"00"==t?e.$alert("该名患者已经上传照片但是未被诊断，请先诊断","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}}):e.$alert("经系统检测，该名患者已存在，确认历史信息无误后可直接提交","温馨提示",{confirmButtonText:"确定",callback:function(a){"cancel"!==a&&(console.log(t),e.addFormVisible=!1,e.editFormVisible=!0,e.editForm=t.fields,t.his_fields?(1!==t.his_fields.DM_year&&!0!==t.his_fields.DM_year||(t.his_fields.DM_year=!0),1!==t.his_fields.HPL_year&&!0!==t.his_fields.HPL_year||(t.his_fields.HPL_year=!0),1!==t.his_fields.HTN_year&&!0!==t.his_fields.HTN_year||(t.his_fields.HTN_year=!0),0===t.his_fields.pregnant_weeks&&(t.his_fields.pregnant_weeks=""),e.editFormJwsForm=t.his_fields,e.editFormLeftDiopterValue=t.his_fields.left_diopter,e.editFormRightDiopterValue=t.his_fields.right_diopter,e.editForm.jwsExist=1,e.editFormjwsVisible=!0,e.radio=3):(e.radio=6,e.editjws()),e.editForm.patient_id=t.patient_id,e.editForm.diagnose_again="1",e.editForm.isFront=!0,e.$refs.addForm.resetFields())}})})},uploadPicture:function(e,t){var a=c()({},t);this.upload_id=a.patient_id,this.diagnose_record=a.diagnose_record,this.sms_patient_name=a.patient_name,this.sms_patient_tel=a.patient_tel,document.getElementById("fileToUpload").click()},get_file_num:function(){for(var e=[],t=document.getElementById("fileToUpload").files.length,a=document.getElementById("fileToUpload").files,i=0;i<a.length;i++){if(console.log("1024",a[i].size),a[i].size/1048576>15){e[0]=!1;break}e[0]=!0}return e.push(t),e},uploadPic:function(){var t=this.$loading({lock:!0,text:"AI智能识别左右眼中",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});setTimeout(function(){t.setText("AI智能计算中")},3e3);var a=this.get_file_num()[1],i=this.get_file_num()[0];if(a>2)return this.$alert("单次上传照片数量不可超过两张","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}}),t.close(),!1;if(!1===i)this.$alert("单张照片大小不可超过10M","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}}),t.close();else{var r={url:h+"operation/web_upload_picture/",data:{userName:g.a.getCookie("name"),patient_id:this.upload_id,diagnose_record:this.diagnose_record},type:"post",dataType:"json",cache:!1,headers:{Authorization:localStorage.getItem("token")},processData:!1,contentType:!1,success:function(e,a,i){if(console.log("result",e),0===e)t.close(),this.$alert("上传失败,仅支持jpg,png,jpeg,bmp格式","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}});else if(1===e)t.close(),this.$alert("上传失败","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}});else if(2===e){t.close();this.$store.commit("changeFlag",!0),this.refresh(),"1"===localStorage.getItem("business_type")&&this.sendSms(this.sms_patient_name,this.sms_patient_tel),this.$alert("上传成功","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}})}else t.close(),this.$alert("上传失败","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}})}.bind(this),error:function(){t.close(),this.$alert("上传失败","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}})}.bind(this)};e("#jvForm").ajaxSubmit(r)}},addSubmit:function(){var e=this;this.$refs.addForm.validate(function(t){t&&e.$confirm("确认提交吗？","提示",{}).then(function(){e.addLoading=!0,console.log("this.jwsForm",e.jwsForm),console.log(e.leftDiopterValue,e.rightDiopterValue);var t=e.jwsForm,a={};""!==e.leftDiopterValue&&(t.left_diopter=e.leftDiopterValue),""!==e.rightDiopterValue&&(t.right_diopter=e.rightDiopterValue),a.jwsInfo=t;var i=e.addForm;delete i.genderRadio,delete i.paymentRadio,delete i.jwsRadio,a.basicInfo=i;var r=c()({},a);delete i.jwsVisible,Object(u.a)(r).then(function(t){if(e.addLoading=!1,1===t){e.$message({message:"提交成功",type:"success"}),e.$refs.addForm.resetFields(),e.addFormVisible=!1;e.$store.commit("changeFlag",!0),e.refresh()}else e.$message({message:"提交失败",type:"error"})})})})},handleDel:function(e,t){var a=this;this.$confirm("确认删除该记录吗?","提示",{type:"warning"}).then(function(){var e={id:t.patient_id};Object(u.w)(e).then(function(e){0===e?a.$message({message:"删除失败",type:"error"}):(a.$message({message:"删除成功",type:"success"}),a.refresh())})}).catch(function(){})},jwsClick:function(){var e=this.addForm.jwsExist;0===e?(this.addForm.jwsVisible=!1,this.jwsForm={},this.leftDiopterValue="",this.rightDiopterValue=""):1===e&&(this.addForm.jwsVisible=!0)},disabledPregnant:function(){var e=this.addForm.patient_gender;this.pregnant_seen=0===e},handlePregnant:function(){var e=this.editForm.patient_gender;this.pre_seen="0"===e},editjws:function(){var e=this.radio;console.log(this.$store.state.loginPage),3===e?(this.editForm.jwsExist=1,this.editFormjwsVisible=!0):6===e&&(this.editFormjwsVisible=!1,this.editFormJwsForm={},this.editFormRightDiopterValue="",this.editFormLeftDiopterValue="",this.editForm.jwsExist=0)},editSubmit:function(){var e=this;this.$refs.editForm.validate(function(t){t&&e.$confirm("确认提交吗？","提示",{}).then(function(){e.editLoading=!0;var t=e.editFormJwsForm,a={};t.left_diopter=e.editFormLeftDiopterValue,t.right_diopter=e.editFormRightDiopterValue,a.jwsInfo=t,a.basicInfo=e.editForm;var i=c()({},a);Object(u.g)(i).then(function(t){e.editLoading=!1,1===t?(e.$message({message:"修改成功",type:"success"}),e.$refs.editForm.resetFields(),e.editFormVisible=!1,e.refresh()):e.$message({message:"修改失败",type:"error"})})})})},transferPinfo:function(e){var t={};t.page_size=this.page_size,t.currentPage=this.currentPage,t.patient_name=e.patient_name,t.patient_gender=e.patient_gender,t.patient_age=e.patient_age,t.patient_id=e.patient_id,t.diagnose_record=e.diagnose_record,t.apply_time=e.apply_time,t.picture=e.picture,t.diagnose=e.diagnose,t.historyDisease=e.historyDisease,t.hospital_id=e.hospital,t.refine_days=e.refine_days,t.refine_weeks=e.refine_weeks,t.birth_days=e.birth_days,t.birth_weeks=e.birth_weeks,t.birth_weight=e.birth_weight;for(var a=e.superior_hospital,i=[],r=0;r<a.length;r++)i.push(a[r]);t.id_list=i,localStorage.setItem("patient_info",s()(t))},clickToDiagnose:function(e,t){var a=this;return l()(r.a.mark(function e(){var i,o;return r.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:return a.editForm=c()({},t),(i={}).patient_id=a.editForm.patient_id,i.doctor2=localStorage.getItem("user_id"),o=c()({},i),a.$store.commit("changePageFrom","undiaWechat"),e.next=8,a.transferPinfo(a.editForm);case 8:Object(u.d)(o).then(function(e){0===e?a.$alert("该名患者正在被诊断，您暂时无法诊断","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}}):2===e?(a.$alert("该名患者已经被其他医生诊断","温馨提示",{confirmButtonText:"确定",callback:function(e){console.log(e)}}),a.refresh()):a.$router.push("report")});case 9:case"end":return e.stop()}},e,a)}))()}},data:function(){var e=function(e,t,a){11!==t.length?a(new Error("手机号为11位")):a()},t=function(e,t,a){t?18!==t.length?a(new Error("中国大陆身份证号为18位")):a():a()},a=function(e,t,a){t.length>10?a(new Error("姓名长度需要小于10个字")):/^[\u4E00-\u9FA5A-Za-z0-9_]+$/.test(t)?a():a(new Error("禁止输入空格等特殊字符"))},i=function(e,t,a){t||a(),t.length>30?a(new Error("地址长度需要小于30个字")):a()},r=function(e,t,a){t<1?a(new Error("请填写正确年龄")):a()};return{upload_id:"",hospital_id:0,diagnose_record:0,superHos:!1,normalHos:!1,pregnant_seen:!1,pre_seen:!1,page_info:{},tableData:[],dateValue:"",isActive1:!0,isActive4:!1,currentPage:1,inputVal:"",input:"",page_size:10,totalNum:30,otherDate:!1,pic_upload:!1,editFormjwsVisible:!1,radio:3,payment:"",pickerOptions:{disabledDate:function(e){return e.getTime()>Date.now()},shortcuts:[{text:"今天",onClick:function(e){e.$emit("pick",new Date)}},{text:"昨天",onClick:function(e){var t=new Date;t.setTime(t.getTime()-864e5),e.$emit("pick",t)}},{text:"一周前",onClick:function(e){var t=new Date;t.setTime(t.getTime()-6048e5),e.$emit("pick",t)}}]},editFormVisible:!1,editLoading:!1,editFormRules:{patient_name:[{required:!0,message:"请输入姓名",trigger:"blur"},{validator:a,trigger:"change"}],patient_tel:[{required:!0,message:"请输入手机号",trigger:"blur"},{validator:e,trigger:"blur"}],ID_number:[{validator:t,trigger:"blur"},{pattern:/(^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$)|(^[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{2}$)/,message:"证件号码格式有误！",trigger:"blur"}],address:[{validator:i,trigger:"change"}],patient_age:[{required:!0,message:"请输入正确的年龄",trigger:"blur"},{validator:r,trigger:"blur"}]},editForm:{patient_id:0,patient_name:"测试",patient_gender:"0",patient_age:0,payment:0,patient_tel:18888888888,ID_number:"",birth:"",paymentRadio:0,jwsRadio:0,jwsExist:0,jwsVisible:!1,isFront:!0,address:"",picture:[]},addFormVisible:!1,addLoading:!1,addFormRules:{patient_name:[{required:!0,message:"请输入姓名",trigger:"change"},{validator:a,trigger:"change"}],patient_tel:[{required:!0,message:"请输入手机号",trigger:"change"},{validator:e,trigger:"change"}],ID_number:[{validator:t,trigger:"change"},{pattern:/(^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$)|(^[1-9]\d{5}\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{2}$)/,message:"证件号码格式有误！",trigger:"change"}],jwsExist:[{required:!0,message:"请选择既往史",trigger:"change"}],patient_age:[{required:!0,message:"请输入正确的年龄",trigger:"change"},{validator:r,trigger:"blur"}],address:[{validator:i,trigger:"change"}]},addForm:{patient_id:0,patient_name:"张三",patient_gender:1,patient_age:0,patient_tel:"",address:"",jwsExist:0,jwsVisible:!1,jwsRadio:0,genderRadio:0,ID_number:""},jwsForm:{other:"",DM_year:!1,HTN_year:!1,HPL_year:!1,pregnant_weeks:""},editFormJwsForm:{other:"",DM_year:!1,HTN_year:!1,HPL_year:!1,pregnant_weeks:""},leftDiopter:[{value:"0",label:"正视"},{value:"1",label:"低度近视(75~300)"},{value:"2",label:"中度近视(300~600)"},{value:"3",label:"高度近视(>600)"},{value:"4",label:"远视"}],rightDiopter:[{value:"0",label:"正视"},{value:"1",label:"低度近视(75~300)"},{value:"2",label:"中度近视(300~600)"},{value:"3",label:"高度近视(>600)"},{value:"4",label:"远视"}],editFormLeftDiopter:[{value:"0",label:"正视"},{value:"1",label:"低度近视(75~300)"},{value:"2",label:"中度近视(300~600)"},{value:"3",label:"高度近视(>600)"},{value:"4",label:"远视"}],editFormRightDiopter:[{value:"0",label:"正视"},{value:"1",label:"低度近视(75~300)"},{value:"2",label:"中度近视(300~600)"},{value:"3",label:"高度近视(>600)"},{value:"4",label:"远视"}],leftDiopterValue:"",rightDiopterValue:"",editFormLeftDiopterValue:"",editFormRightDiopterValue:""}}}}).call(t,a("7t+N"))}});
//# sourceMappingURL=4.33f6b8d491e644e40f1f.js.map