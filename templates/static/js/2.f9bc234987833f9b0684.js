webpackJsonp([2],{Cdx3:function(t,e,i){var n=i("sB3e"),a=i("lktj");i("uqUo")("keys",function(){return function(t){return a(n(t))}})},fZjL:function(t,e,i){t.exports={default:i("jFbC"),__esModule:!0}},jFbC:function(t,e,i){i("Cdx3"),t.exports=i("FeBl").Object.keys},l8gn:function(t,e){},uqUo:function(t,e,i){var n=i("kM2E"),a=i("FeBl"),s=i("S82l");t.exports=function(t,e){var i=(a.Object||{})[t]||Object[t],o={};o[t]=e(i),n(n.S+n.F*s(function(){i(1)}),"Object",o)}},zKBK:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var n=i("fZjL"),a=i.n(n),s=i("Xxa5"),o=i.n(s),l=i("//Fk"),r=i.n(l),c=i("exGp"),_=i.n(c),p=i("mtWM"),u=i.n(p),g=i("O2WP"),h=(i("u4WU"),i("t5DY")),d=i("P9l9"),f=g.a.url,v={data:function(){return{jwsDisplayInfo:"无",warning:"",warningShow:!1,hospital_name:"",patient_info:{},restaurants:[],AIdata:{},state:"",timeout:null,suggestions:["定时随访","进一步就诊检查","正常,无需随访"],diseases:["高血压视网膜病变","糖尿病视网膜病变","豹纹状眼底","渗出","青光眼","年龄相关性视网膜病变"],fits:["fill"],right_src:"https://www.orbisbiotech.cn/media/noimg.jpg",left_src:"https://www.orbisbiotech.cn/media/noimg.jpg",right_srcList:[],left_srcList:[],dynamicTagsR:[],dynamicTagsL:[],dynamicTagsA:[],diaStrR:"",diaStrL:"",diaStrA:"",finishSeen:!1,beforeSeen:!0,inputVisibleR:!1,inputVisibleL:!1,inputVisibleA:!1,leftEye:!1,rightEye:!1,advice:!1,inputValueR:"",inputValueL:"",inputValueA:"",seen:!0,seen2:!1,eyeSeen:!1,diaSeen:!0,activeColor1:"azure",activeColor2:"azure",dialogVisible:!1,uplevelVisible:!1,uplevelHospital:"",fullscreenLoading:!1,centerDialogVisible:!1,pickerOptions:{disabledDate:function(t){return t.getTime()<Date.now()},shortcuts:[{text:"今天",onClick:function(t){t.$emit("pick",new Date)}},{text:"明天",onClick:function(t){var e=new Date;e.setTime(e.getTime()+864e5),t.$emit("pick",e)}},{text:"一周后",onClick:function(t){var e=new Date;e.setTime(e.getTime()+6048e5),t.$emit("pick",e)}}]},value1:"",value2:"",strengthen:!1}},methods:{handleCloseR:function(t){this.dynamicTagsR.splice(this.dynamicTagsR.indexOf(t),1)},showInputR:function(){var t=this;this.activeColor2="lightblue",this.inputVisibleR=!0,this.rightEye=!0,this.leftEye=!1,this.$nextTick(function(e){t.$refs.saveTagInputR.$refs.input.focus()})},handleInputConfirmR:function(){this.activeColor2="azure";var t=this.inputValueR;t&&this.dynamicTagsR.push(t),this.inputVisibleR=!1,this.inputValueR="",this.dynamicTagsR.toString().length>40&&this.$alert("建议不可超过40个字符","提示",{confirmButtonText:"确定"})},handleCloseL:function(t){this.dynamicTagsL.splice(this.dynamicTagsL.indexOf(t),1)},showInputL:function(){var t=this;this.activeColor2="lightblue",this.inputVisibleL=!0,this.rightEye=!1,this.leftEye=!0,this.$nextTick(function(e){t.$refs.saveTagInputL.$refs.input.focus()})},handleInputConfirmL:function(){this.activeColor2="azure";var t=this.inputValueL;t&&this.dynamicTagsL.push(t),this.dynamicTagsL.toString().length>40&&this.$alert("建议不可超过40个字符","提示",{confirmButtonText:"确定"}),this.inputVisibleL=!1,this.inputValueL=""},handleCloseA:function(t){this.dynamicTagsA.splice(this.dynamicTagsA.indexOf(t),1),this.seen=!0,this.seen2=!1,this.value2=""},showInputA:function(){var t=this;this.leftEye=!1,this.rightEye=!1,this.activeColor1="lightblue",this.inputVisibleA=!0,this.advice=!0,this.$nextTick(function(e){t.$refs.saveTagInputA.$refs.input.focus()})},handleInputConfirmA:function(){this.activeColor1="azure";var t=this.inputValueA,e=this.dynamicTagsA;t&&this.dynamicTagsA.push(t),this.inputValueA.toString().length>40&&this.$alert("建议不可超过40个字符","提示",{confirmButtonText:"确定"}),0!==e.length&&(this.seen=!1),this.inputVisibleA=!1,this.inputValueA=""},addDiagnose:function(t){this.leftEye?(this.dynamicTagsL.push(t),this.dynamicTagsL=this.duplicateRemove(this.dynamicTagsL),this.handleInputConfirmL()):this.rightEye&&(this.dynamicTagsR.push(t),this.dynamicTagsR=this.duplicateRemove(this.dynamicTagsR),this.handleInputConfirmR())},addAdvice:function(t){var e=this.dynamicTagsA;if(this.advice){if(0!==e.length)return;this.dynamicTagsA.push(t),this.handleInputConfirmA(),"定时随访"===t&&(this.dialogVisible=!0),"进一步就诊检查"===t&&(this.uplevelVisible=!1)}},formatSex:function(t){return"0"===t.patient_gender?"男":"1"===t.patient_gender?"女":"未知"},finishDiagnose:function(){var t=this;return _()(o.a.mark(function e(){var i,n,a;return o.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(i=t.dynamicTagsR.toString(),n=t.dynamicTagsL.toString(),""===i&&(i="无"),""===n&&(n="无"),a=t.dynamicTagsA[0].toString(),!(i.length>40||n.length>40||a.length>40)){e.next=8;break}return t.$alert("建议和左右眼诊断内容每条不可超过40个字符","提示",{confirmButtonText:"确定"}),e.abrupt("return",r.a.resolve(!1));case 8:return t.diaStrR=i,t.diaStrL=n,e.next=12,t._submitDiagnose();case 12:if(1!==e.sent){e.next=18;break}return e.next=16,Object(h.a)();case 16:e.next=19;break;case 18:return e.abrupt("return",!1);case 19:t.eyeSeen=!0,t.diaSeen=!1,t.finishSeen=!0,t.beforeSeen=!1;case 23:case"end":return e.stop()}},e,t)}))()},openFullScreen:function(){var t=this;if(0===this.dynamicTagsA.length)this.open();else{var e=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});setTimeout(function(){e.close(),t.finishDiagnose()},500)}},clickCreateImgBtn:function(){var t=this,e=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"}),i=this.patient_info.patient_id,n=this.getDiagnoseResult(),a=n.other_data.right_origin_src,s=n.other_data.left_origin_src,o=localStorage.getItem("last_name")+localStorage.getItem("first_name"),l=localStorage.getItem("superior_hospital_name"),r={};r.patient_id=i,r.right_origin_src=a,r.left_origin_src=s,r.username=o,r.hospital_name=l,Object(d.d)(r).then(function(i){if(console.log("res=>",i),0===i)e.close(),t.$alert("生成失败","提示",{confirmButtonText:"确定"});else{e.close();var n=Math.random().toString(36).substr(2),a=window.open("",n,"");a.document.title="profession",a.location=f+i}}).catch(function(i){e.close(),t.$alert("生成失败","提示",{confirmButtonText:"确定"})})},backToUndiagnosed:function(){var t=this;return _()(o.a.mark(function e(){var i,n,a,s;return o.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(0!==t.dynamicTagsA.length){e.next=4;break}t.open(),e.next=16;break;case 4:return(i={}).page_size=t.patient_info.page_size,i.currentPage=t.patient_info.currentPage,e.next=9,t.finishDiagnose();case 9:if(n=e.sent,a=t.$store.state.page_from,!1!==n){e.next=14;break}return e.abrupt("return");case 14:s=t.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"}),setTimeout(function(){s.close(),t.$router.push("/"+a)},1e3);case 16:case"end":return e.stop()}},e,t)}))()},onlyBack:function(){var t=this,e={};e.page_size=this.patient_info.page_size,e.currentPage=this.patient_info.currentPage;var i=this.$store.state.page_from,n=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});setTimeout(function(){n.close(),t.$router.push("/"+i)},1e3)},getConclusion:function(){var t=this;u.a.get(f+"/diagnosis/?&ordering=-times").then(function(e){console.log(e.data);for(var i=e.data,n=[],a=0;a<i.length;a++)n.push(i[a].conclusion);t.diseases=n.slice(0,9),t.replaceDictKey(i)}).catch(function(t){console.log(t)})},getDiagnoseResult:function(){var t={},e={},i={};if(t.patient_id=this.patient_info.patient_id,t.diagnose_doctor=localStorage.getItem("user_id"),t.diagnose_record=this.patient_info.diagnose_record,t.apply_time=this.patient_info.apply_time,t.patient_name=this.patient_info.patient_name,t.patient_gender=this.patient_info.patient_gender,t.patient_age=this.patient_info.patient_age,t.left_diagnose=this.diaStrL,t.right_diagnose=this.diaStrR,t.diagnose_advice=this.dynamicTagsA[0],t.jwsInfo=this.jwsDisplayInfo,e.superior_hospital=localStorage.getItem("superior_hospital"),e.right_origin_src=this.right_src.split("media")[this.right_src.split("media").length-1],e.left_origin_src=this.left_src.split("media")[this.left_src.split("media").length-1],-1===e.right_origin_src.search("noimg")){var n=e.right_origin_src.lastIndexOf("."),a=e.right_origin_src.substr(n);console.log("新式眼底格式2",a),e.right_AI_src=e.right_origin_src.replace(a,"_AI"+a)}else e.right_AI_src=this.right_src.split("media")[this.right_src.split("media").length-1];if(-1===e.left_origin_src.search("noimg")){var s=e.left_origin_src.lastIndexOf("."),o=e.left_origin_src.substr(s);console.log("新式眼底格式1",o),e.left_AI_src=e.left_origin_src.replace(o,"_AI"+o)}else e.left_AI_src=this.left_src.split("media")[this.left_src.split("media").length-1];return this.value2&&(t.review_time=this.value2,t.transform="1"),this.uplevelHospital&&(t.review_hospital=this.uplevelHospital,t.transform="1"),e.oozed_amount=this.AIdata.oozed_amount,e.bleeding_amount=this.AIdata.bleeding_amount,e.oozed_area=this.AIdata.oozed_area,e.bleeding_area=this.AIdata.bleeding_area,e.max_oozed_area=this.AIdata.max_oozed_area,e.max_bleeding_area=this.AIdata.max_bleeding_area,e.other_advice="",i.basic_data=t,i.other_data=e,i},_submitDiagnose:function(){var t=this,e=this.getDiagnoseResult();return new r.a(function(i,n){Object(d.w)(e).then(function(e){console.log("res=>",e),0===e?(t.$alert("阅片失败","提示",{confirmButtonText:"确定"}),i(0)):2===e?(t.$alert("该患者已被诊断，可在已诊列表查看","提示",{confirmButtonText:"确定"}),i(2)):i(1)}).catch(function(e){console.log(e),t.$alert("阅片错误","提示",{confirmButtonText:"确定"}),n()})})},submitDiagnose:function(){var t,e=this,i=this.getDiagnoseResult();Object(d.w)(i).then((t=_()(o.a.mark(function t(i){var n;return o.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:if(console.log("res=>",i),0!==i){t.next=5;break}e.$alert("阅片失败","提示",{confirmButtonText:"确定"}),t.next=18;break;case 5:if(2!==i){t.next=11;break}return!0,t.next=9,e.$alert("该患者已被诊断，可在已诊列表查看","提示",{confirmButtonText:"确定"});case 9:t.next=18;break;case 11:return n=JSON.parse(localStorage.getItem("patient_info")),n.minusMessage,t.next=16,Object(d.p)(n).then(function(t){1===t?console.log("消息减去成功"):console.log("消息减去失败")});case 16:return t.next=18,Object(h.a)();case 18:case"end":return t.stop()}},t,e)})),function(e){return t.apply(this,arguments)})).catch(function(t){console.log(t),e.$alert("阅片错误","提示",{confirmButtonText:"确定"})})},messageAmountProcess:function(t){return new r.a(function(e){Object(d.p)(t).then(function(t){1===t?console.log("消息减去成功"):console.log("消息减去失败"),e(t)})})},duplicateRemove:function(t){for(var e=[],i=0;i<t.length;i++)-1===e.indexOf(t[i])&&e.push(t[i]);return console.log(e),e},createReport:function(){var t=this,e=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"}),i=this.getDiagnoseResult();Object(d.e)(i).then(function(n){if(e.close(),console.log("res=>",n),n.length>1){var a=Math.random().toString(36).substr(2),s=window.open("",a,"");s.document.title="pdf";var o=i.basic_data.patient_name,l=i.basic_data.patient_id;s.location=f+"media/patient_pdf/"+n+"/"+o+"_"+l+".pdf"}else t.$alert("诊断报告生成失败","提示",{confirmButtonText:"确定"})}).catch(function(i){e.close(),console.log(i),t.$alert("请允许弹窗","提示",{confirmButtonText:"确定"})})},finishAndCreatePdf:function(){var t=this;if(0===this.dynamicTagsA.length)this.open();else try{console.log("start submit");var e=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});setTimeout(_()(o.a.mark(function i(){return o.a.wrap(function(i){for(;;)switch(i.prev=i.next){case 0:return e.close(),i.next=3,t.finishDiagnose();case 3:if(!1!==i.sent){i.next=6;break}return i.abrupt("return");case 6:t.createReport();case 7:case"end":return i.stop()}},i,t)})),500)}catch(t){console.log(t)}},cancelSelectDate:function(){this.dialogVisible=!1,this.seen2=!1,this.value2=""},confirmSelectDate:function(){this.dialogVisible=!1,this.seen2=!0,this.value2||(this.seen2=!1,this.value2="")},cancelInputHospital:function(){this.uplevelVisible=!1,this.uplevelHospital=""},confirmInputHospital:function(){this.uplevelVisible=!1},open:function(){this.$alert("请添加建议","提示",{confirmButtonText:"确定"})},loadAll:function(){var t=this;u.a.get(f+"/conclusion/?&ordering=-times").then(function(e){for(var i=e.data,n=[],s=function(t){delete i[t].id,delete i[t].times;var e={conclusion:"value"},s=a()(i[t]).reduce(function(n,a){return n[e[a]||a]=i[t][a],n},{});n.push(s)},o=0;o<i.length;o++)s(o);t.restaurants=n}).catch(function(e){console.log(e),t.restaurants=[]})},replaceDictKey:function(t){for(var e=[],i=0;i<t.length;i++)delete t[i].id,delete t[i].times,e.push(t[i]);for(var n={conclusion:"value"},s=[],o=function(t){a()(e[t]).reduce(function(i,a){i[n[a]||a]=e[t][a],s.push(i)},{})},l=0;l<e.length;l++)o(l);this.restaurants=s},querySearchAsync:function(t,e){var i=this.restaurants,n=t?i.filter(this.createStateFilter(t)):i;clearTimeout(this.timeout),e(n)},createStateFilter:function(t){return function(e){return 0===e.value.toLowerCase().indexOf(t.toLowerCase())}},handleSelect:function(t){console.log(t.value),this.addDiagnose(t.value)},AiDiagnose:function(t){console.log("病理近视",t);t.left_rm,t.left_pm,t.right_rm,t.right_pm;var e=t.left_oozed_amount,i=t.right_oozed_amount,n=t.left_oozed_area,a=t.right_oozed_area,s=t.left_bleeding_amount,o=t.right_bleeding_amount,l=t.left_bleeding_area,r=t.right_bleeding_area,c=t.left_max_bleeding_area,_=t.right_max_bleeding_area,p=t.left_max_oozed_area,u=t.right_max_oozed_area;t.left_prob_dr,t.right_prob_dr,t.left_glaucoma,t.right_glaucoma,t.left_warning,t.right_warning;this.AIdata.iqa_score_left=t.left_iqa_score<60?"不佳":t.left_iqa_score>=75?"良好":"一般",this.AIdata.iqa_score_right=t.right_iqa_score<60?"不佳":t.right_iqa_score>=75?"良好":"一般",this.AIdata.oozed_area=(10*n+10*a)/10,this.AIdata.oozed_amount=e+i,this.AIdata.max_oozed_area=(10*p+10*u)/10,this.AIdata.bleeding_area=(10*l+10*r)/10,this.AIdata.bleeding_amount=s+o,this.AIdata.max_bleeding_area=(10*c+10*_)/10,this.handleInputConfirmA()},picture_strengthen:function(){var t=this,e=this.strengthen,i=this.right_src.split("media")[this.right_src.split("media").length-1],n=this.left_src.split("media")[this.left_src.split("media").length-1],a={};if(a.left_src=n,a.right_src=i,e){var s=this.$loading({lock:!0,text:"一键增强中",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});Object(d.r)(a).then(function(e){if(console.log("res=>",e),0===e.data)s.close(),t.$alert("一键增强失败","提示",{confirmButtonText:"确定"});else{if(s.close(),-1===n.search("noimg")){var a=t.left_src.lastIndexOf("."),o=t.left_src.substr(a);t.left_src=t.left_src.replace(o,"_strengthen"+o),t.left_srcList[0]=t.left_src}if(-1===i.search("noimg")){var l=t.right_src.lastIndexOf("."),r=t.right_src.substr(l);t.right_src=t.right_src.replace(r,"_strengthen"+r),t.right_srcList[0]=t.right_src}}}).catch(function(e){console.log(e),s.close(),t.$alert("一键增强失败","提示",{confirmButtonText:"确定"})})}else-1===i.search("noimg")&&(this.right_src=this.right_src.replace("_strengthen",""),this.right_srcList[0]=this.right_src),-1===n.search("noimg")&&(this.left_src=this.left_src.replace("_strengthen",""),this.left_srcList[0]=this.left_src)},display_history_diseases:function(){var t=this.patient_info.historyDisease;if(0===t.length)this.jwsDisplayInfo="无";else{this.jwsDisplayInfo="有",console.log("既往史细节",t[0]);var e="";if(1===t[0].DM_year?e="糖尿病 ":!0===t[0].DM_year&&(e="糖尿病 "),1===t[0].HPL_year?e+="高血脂 ":!0===t[0].HPL_year&&(e+="高血脂 "),1===t[0].HTN_year?e+="高血压 ":!0===t[0].HTN_year&&(e+="高血压 "),t[0].left_diopter&&("0"===t[0].left_diopter?e+="左眼:正视 ":"1"===t[0].left_diopter?e+="左眼:低度近视(75~300) ":"2"===t[0].left_diopter?e+="左眼:中度近视(300~600) ":"3"===t[0].left_diopter?e+="左眼:高度近视(>600) ":"4"===t[0].left_diopter&&(e+="左眼:远视 ")),t[0].right_diopter&&("0"===t[0].right_diopter?e+="右眼:正视 ":"1"===t[0].right_diopter?e+="右眼:低度近视(75~300) ":"2"===t[0].right_diopter?e+="右眼:中度近视(300~600) ":"3"===t[0].right_diopter?e+="右眼:高度近视(>600) ":"4"===t[0].right_diopter&&(e+="右眼:远视 ")),t[0].pregnant_weeks)e=e+"妊娠"+t[0].pregnant_weeks+"周 ";if(t[0].other)e=e+"其他:"+t[0].other+" ";this.jwsDisplayInfo=e}}},mounted:function(){this.getConclusion(),this.hospital_name=localStorage.getItem("final_hospital_name"),this.patient_info=JSON.parse(localStorage.getItem("patient_info"));var t=this.patient_info.diagnose.length-1;this.AIdata=this.patient_info.diagnose[t],this.AiDiagnose(this.patient_info.diagnose[t]),this.display_history_diseases();try{var e=this.patient_info.picture;console.log("所有照片信息",e);var i=e.length-1,n=[],a=[],s=e[i].own_to;console.log("latest",s);for(var o=0;o<e.length;o++)if(console.log(e[o].pic_name),e[o].own_to===s)if(-1===e[o].pic_name.search("infrared"))if(-1!==e[o].pic_name.search("Left")){var l=f+"media/patient_img/"+e[o].pic_name;n.push(l),console.log("照片在服务器的位置",l)}else{var r=f+"media/patient_img/"+e[o].pic_name;a.push(r)}else console.log("i find infrared and filter it");if(n=n.reverse(),0===(a=a.reverse()).length){console.log("左眼没有照片");var c=[];c[0]=f+"media/image/noimg.jpg",console.log(c),this.right_src=c[0],this.right_srcList=[]}else this.right_src=a[0],this.right_srcList=a;if(0===n.length){console.log("右眼没有照片");var _=[];_[0]=f+"media/image/noimg.jpg",console.log(_),this.left_src=_[0],this.left_srcList=[]}else this.left_src=n[0],this.left_srcList=n}catch(t){console.log(t)}},beforeDestroy:function(){var t=this.patient_info.patient_id,e=(localStorage.getItem("superior_hospital"),localStorage.getItem("user_id"),{});e.patient_id=t,Object(d.m)(e)}},m={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("el-container",[i("div",{staticClass:"aside"},[i("el-row",{staticClass:"column_style",style:{backgroundColor:t.activeColor2}},[i("i",{staticClass:"icon iconfont icon-icon-test"}),t._v("单击可将词条插入诊断内容\n  ")]),t._v(" "),i("el-row",{staticStyle:{"margin-top":"20px"}},[i("el-autocomplete",{attrs:{"fetch-suggestions":t.querySearchAsync,placeholder:"可模糊搜索疑似病种","prefix-icon":"el-icon-search"},on:{select:t.handleSelect},model:{value:t.state,callback:function(e){t.state=e},expression:"state"}})],1),t._v(" "),i("el-row",{staticClass:"column_style",staticStyle:{"margin-top":"20px","background-color":"azure"},style:{backgroundColor:t.activeColor2}},[t._v("\n    病种栏\n  ")]),t._v(" "),t._l(t.diseases,function(e){return i("el-row",{key:e.id,staticClass:"diseases_section"},[i("el-col",{attrs:{span:3}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:18}},[i("a",{attrs:{href:"javascript:;"},on:{click:function(i){return t.addDiagnose(e)}}},[i("div",{staticClass:"media_change1"},[t._v(t._s(e))])])]),t._v(" "),i("el-col",{attrs:{span:3}},[t._v(" ")])],1)}),t._v(" "),i("el-row",{staticClass:"column_style",staticStyle:{"margin-top":"20px"},style:{backgroundColor:t.activeColor1}},[t._v("\n      建议栏\n    ")]),t._v(" "),t._l(t.suggestions,function(e){return i("el-row",{key:e.id,staticClass:"suggestion_section"},[i("el-col",{attrs:{span:3}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:18}},[i("a",{attrs:{href:"javascript:;"},on:{click:function(i){return t.addAdvice(e)}}},[i("div",{staticClass:"media_change1"},[t._v(t._s(e))])])]),t._v(" "),i("el-col",{attrs:{span:3}},[t._v(" ")])],1)})],2),t._v(" "),i("div",{staticClass:"main"},[i("el-row",[i("span",[t._v(t._s(t.hospital_name))])]),t._v(" "),i("el-row",{staticStyle:{"margin-top":"10px",height:"40px","line-height":"40px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{staticStyle:{"border-top":"lightgrey 1px solid","border-bottom":"lightgrey 1px solid","text-align":"left"},attrs:{span:16}},[i("div",{staticClass:"button_area"},[i("div",[t._v("姓名:"),i("span",[t._v(t._s(t.patient_info.patient_name))])]),t._v(" "),i("div",[t._v("性别:"),"1"===t.patient_info.patient_gender?i("span",[t._v("女")]):i("span",[t._v("男")])]),t._v(" "),i("div",[t._v("年龄:"),i("span",[t._v(t._s(t.patient_info.patient_age))])]),t._v(" "),i("div",[t._v("录入时间:"),i("span",{attrs:{id:"apply_time"}},[t._v(t._s(t.patient_info.apply_time))])])])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("el-row",{staticStyle:{"text-align":"left","font-weight":"bold"}},[i("el-col",{attrs:{span:11}},[t._v("OD(图像质量:"+t._s(t.AIdata.iqa_score_right)+")")]),t._v(" "),i("el-col",{attrs:{span:2}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:11}},[t._v("OS(图像质量:"+t._s(t.AIdata.iqa_score_left)+")")])],1)],1),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("el-row",{staticStyle:{"text-align":"left","font-weight":"bold"}},[i("el-col",{attrs:{span:11}},[i("div",{staticClass:"demo-image__preview"},[i("el-image",{staticStyle:{width:"100%",height:"auto"},attrs:{src:t.right_src,"preview-src-list":t.right_srcList}})],1)]),t._v(" "),i("el-col",{attrs:{span:2}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:11}},[i("div",{staticClass:"demo-image__preview"},[i("el-image",{staticStyle:{width:"100%",height:"auto"},attrs:{src:t.left_src,"preview-src-list":t.left_srcList}})],1)])],1)],1),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px",display:"none"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("智能图像处理:")])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px",display:"none"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("el-switch",{attrs:{"active-text":"增强","inactive-text":"重置"},on:{change:t.picture_strengthen},model:{value:t.strengthen,callback:function(e){t.strengthen=e},expression:"strengthen"}})],1),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("既往史:")]),t._v("   \n        "),i("i",{staticClass:"el-icon-warning",staticStyle:{color:"goldenrod","font-size":"small"}},[t._v(" "+t._s(t.jwsDisplayInfo))])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("诊断:")]),t._v("   \n        "),t.warningShow?i("i",{staticClass:"el-icon-warning",staticStyle:{color:"goldenrod","font-size":"small"}},[t._v(" "+t._s(t.warning))]):t._e()]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),t.diaSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"10px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[t._v("右眼:\n        "),t._l(t.dynamicTagsR,function(e){return i("el-tag",{key:e,attrs:{closable:"","disable-transitions":!1,type:"info",effect:"plain"},on:{close:function(i){return t.handleCloseR(e)}}},[t._v("\n          "+t._s(e)+"\n        ")])}),t._v(" "),t.inputVisibleR?i("el-input",{ref:"saveTagInputR",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:t.handleInputConfirmR},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleInputConfirmR(e)}},model:{value:t.inputValueR,callback:function(e){t.inputValueR=e},expression:"inputValueR"}}):i("el-tooltip",{attrs:{placement:"right"}},[i("div",{attrs:{slot:"content"},slot:"content"},[t._v("点击后可手动输入病种"),i("br"),t._v("点击后也可从左侧病种栏选择病种")]),t._v(" "),i("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:t.showInputR}},[t._v("+ 添加诊断")])],1)],2),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.diaSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"10px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[t._v("左眼:\n        "),t._l(t.dynamicTagsL,function(e){return i("el-tag",{key:e,attrs:{closable:"","disable-transitions":!1,effect:"plain",type:"info"},on:{close:function(i){return t.handleCloseL(e)}}},[t._v("\n          "+t._s(e)+"\n        ")])}),t._v(" "),t.inputVisibleL?i("el-input",{ref:"saveTagInputL",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:t.handleInputConfirmL},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleInputConfirmL(e)}},model:{value:t.inputValueL,callback:function(e){t.inputValueL=e},expression:"inputValueL"}}):i("el-tooltip",{attrs:{placement:"right"}},[i("div",{attrs:{slot:"content"},slot:"content"},[t._v("点击后可手动输入病种"),i("br"),t._v("点击后也可从左侧病种栏选择病种")]),t._v(" "),i("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:t.showInputL}},[t._v("+ 添加诊断")])],1)],2),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.eyeSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"10px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[t._v("右眼:"+t._s(t.diaStrR))]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.eyeSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"10px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[t._v("左眼:"+t._s(t.diaStrL))]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.diaSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("建议:\n       "),t._l(t.dynamicTagsA,function(e){return i("el-tag",{key:e,attrs:{closable:"","disable-transitions":!1,type:"info",effect:"plain"},on:{close:function(i){return t.handleCloseA(e)}}},[t._v("\n          "+t._s(e)+"\n        ")])}),t._v(" "),t.inputVisibleA?i("el-input",{ref:"saveTagInputA",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:t.handleInputConfirmA},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleInputConfirmA(e)}},model:{value:t.inputValueA,callback:function(e){t.inputValueA=e},expression:"inputValueA"}}):t._e(),t._v(" "),i("el-tooltip",{attrs:{placement:"right"}},[i("div",{attrs:{slot:"content"},slot:"content"},[t._v("点击后可手动输入诊疗建议"),i("br"),t._v("点击后也可从左侧建议栏选择建议")]),t._v(" "),t.seen?i("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:t.showInputA}},[t._v("+ 添加建议")]):t._e()],1),t._v("\n           "),t.seen2?i("span",[t._v("日期:"+t._s(t.value2))]):t._e()],2)]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.eyeSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("建议:"+t._s(t.dynamicTagsA[0])+"\n\n           "),t.seen2?i("span",[t._v("日期:")]):t._e(),t._v(t._s(t.value2)+"\n      ")])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.beforeSeen?i("el-row",{staticStyle:{"margin-top":"20px",height:"40px","line-height":"40px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{staticStyle:{"text-align":"left",height:"60px","line-height":"60px","border-top":"1px solid lightgray","border-bottom":"1px solid lightgray"},attrs:{span:16}},[i("div",{staticClass:"button_area"},[i("div",[i("el-button",{on:{click:t.clickCreateImgBtn}},[t._v("生成照片")])],1),t._v(" "),i("div",[i("el-button",{on:{click:t.backToUndiagnosed}},[t._v("完成并返回")])],1),t._v(" "),i("div",[i("el-button",{on:{click:t.finishAndCreatePdf}},[t._v("完成并生成报告")])],1),t._v(" "),i("div",[i("el-button",{on:{click:t.onlyBack}},[t._v("返回")])],1)])]),t._v(" "),i("el-col",{attrs:{span:4}})],1):t._e(),t._v(" "),t.finishSeen?i("el-row",{staticStyle:{"margin-top":"20px",height:"40px","line-height":"40px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{staticStyle:{"text-align":"left",height:"60px","line-height":"60px","border-top":"1px solid lightgray","border-bottom":"1px solid lightgray"},attrs:{span:16}},[i("el-row",[i("el-col",{attrs:{span:8}},[i("el-button",{on:{click:t.onlyBack}},[t._v("返回")])],1),t._v(" "),i("el-col",{attrs:{span:8}},[i("el-button",{on:{click:t.createReport}},[t._v("生成报告")])],1),t._v(" "),i("el-col",{attrs:{span:8}},[t._v(" ")])],1)],1),t._v(" "),i("el-col",{attrs:{span:4}})],1):t._e()],1),t._v(" "),i("el-dialog",{attrs:{title:"请输入随访时间",visible:t.dialogVisible,"show-close":!1,width:"30%"},on:{"update:visible":function(e){t.dialogVisible=e}}},[i("div",{staticClass:"block"},[i("el-date-picker",{attrs:{align:"right",type:"date","value-format":"yyyy-MM-dd",placeholder:"选择日期","picker-options":t.pickerOptions},model:{value:t.value2,callback:function(e){t.value2=e},expression:"value2"}})],1),t._v(" "),i("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{attrs:{type:"primary"},on:{click:t.confirmSelectDate}},[t._v("确 定")])],1)]),t._v(" "),i("el-dialog",{attrs:{title:"请输入医院名称",visible:t.uplevelVisible,width:"30%"},on:{"update:visible":function(e){t.uplevelVisible=e}}},[i("div",{staticClass:"block"},[i("el-form",[i("el-form-item",{attrs:{label:"医院名称"}},[i("el-input",{attrs:{"auto-complete":"off",placeholder:"请输入医院名称(限制字数20以内)",maxlength:"20"},model:{value:t.uplevelHospital,callback:function(e){t.uplevelHospital=e},expression:"uplevelHospital"}})],1)],1)],1),t._v(" "),i("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{on:{click:t.cancelInputHospital}},[t._v("取 消")]),t._v(" "),i("el-button",{attrs:{type:"primary"},on:{click:t.confirmInputHospital}},[t._v("确 定")])],1)]),t._v(" "),i("el-dialog",{attrs:{title:"提示",visible:t.centerDialogVisible,width:"30%",center:""},on:{"update:visible":function(e){t.centerDialogVisible=e}}},[i("span",[t._v("生成报告失败")]),t._v(" "),i("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{attrs:{type:"primary"},on:{click:function(e){t.centerDialogVisible=!1}}},[t._v("确 定")])],1)])],1)},staticRenderFns:[]};var b=i("VU/8")(v,m,!1,function(t){i("l8gn")},"data-v-3b683018",null);e.default=b.exports}});
//# sourceMappingURL=2.f9bc234987833f9b0684.js.map