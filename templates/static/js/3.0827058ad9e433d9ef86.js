webpackJsonp([3],{Cdx3:function(t,e,i){var s=i("sB3e"),n=i("lktj");i("uqUo")("keys",function(){return function(t){return n(s(t))}})},fZjL:function(t,e,i){t.exports={default:i("jFbC"),__esModule:!0}},jFbC:function(t,e,i){i("Cdx3"),t.exports=i("FeBl").Object.keys},otuT:function(t,e){},uqUo:function(t,e,i){var s=i("kM2E"),n=i("FeBl"),a=i("S82l");t.exports=function(t,e){var i=(n.Object||{})[t]||Object[t],o={};o[t]=e(i),s(s.S+s.F*a(function(){i(1)}),"Object",o)}},zKBK:function(t,e,i){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s=i("fZjL"),n=i.n(s),a=i("//Fk"),o=i.n(a),r=i("Xxa5"),l=i.n(r),c=i("exGp"),h=i.n(c),p=i("mtWM"),_=i.n(p),u=i("O2WP"),g=i("t5DY"),d=i("P9l9"),f=u.a.url,v={data:function(){return{textarea1:"视乳头界尚清，色可，血管分布尚规律，视网膜周边部血管发育可，余未见明显异常。黄斑部未见明显异常，黄斑中心凹反光存在，视网膜未见明显出血及渗出。",textarea2:"视乳头界尚清，色可，血管分布尚规律，视网膜周边部血管发育可，余未见明显异常。黄斑部未见明显异常，黄斑中心凹反光存在，视网膜未见明显出血及渗出。",jwsDisplayInfo:"无",warning:"",warningShow:!1,hospital_name:"",patient_info:{},restaurants:[],AIdata:{},state:"",timeout:null,suggestions:["定时复查","进一步就诊检查","未见明显异常"],diseases:["高血压视网膜病变","糖尿病视网膜病变","豹纹状眼底","渗出","青光眼","年龄相关性视网膜病变"],descriptions:[],fits:["fill"],right_src:"https://www.orbisbiotech.cn/media/noimg.jpg",left_src:"https://www.orbisbiotech.cn/media/noimg.jpg",right_srcList:[],left_srcList:[],descriptionTagsR:[],descriptionTagsL:[],dynamicTagsR:[],dynamicTagsL:[],dynamicTagsA:[],diaStrR:"",diaStrL:"",diaStrA:"",desStrR:"",desStrL:"",finishSeen:!1,beforeSeen:!0,inputVisibleR:!1,inputVisibleL:!1,inputVisibleDR:!1,inputVisibleDL:!1,inputVisibleA:!1,report_button:!1,AI_report_button:!1,leftEye:!1,rightEye:!1,leftEyeDesc:!1,rightEyeDesc:!1,advice:!1,text:0,inputValueR:"",inputValueL:"",inputValueDR:"",inputValueDL:"",inputValueA:"",seen:!0,seen2:!1,eyeSeen:!1,diaSeen:!0,activeColor1:"azure",activeColor2:"azure",activeColor3:"azure",dialogVisible:!1,uplevelVisible:!1,uplevelHospital:"",fullscreenLoading:!1,centerDialogVisible:!1,pickerOptions:{disabledDate:function(t){return t.getTime()<Date.now()},shortcuts:[{text:"今天",onClick:function(t){t.$emit("pick",new Date)}},{text:"明天",onClick:function(t){var e=new Date;e.setTime(e.getTime()+864e5),t.$emit("pick",e)}},{text:"一周后",onClick:function(t){var e=new Date;e.setTime(e.getTime()+6048e5),t.$emit("pick",e)}}]},value1:"",value2:"",strengthen:!1}},watch:{text:function(t,e){console.log(t,e)}},created:function(){var t=this;this.bus.$on("modify_scr",function(e){t.data_process(e)})},methods:{add_description_l:function(){this.$refs.descInput.focus(),this.leftEyeDesc=!0,this.rightEyeDesc=!1},add_description_r:function(){this.$refs.descInput.focus(),this.leftEyeDesc=!1,this.rightEyeDesc=!0},data_process:function(t){t.left_src&&(this.left_src=t.left_src),t.right_src&&(this.right_src=t.right_src)},displayAllPictures:function(){this.$displayPicture(!0);var t={};t.right_srcList=this.right_srcList,t.left_srcList=this.left_srcList,this.bus.$emit("displayAllPictures",t)},handleCloseR:function(t){this.dynamicTagsR.splice(this.dynamicTagsR.indexOf(t),1)},handleCloseDR:function(t){this.descriptionTagsR.splice(this.descriptionTagsR.indexOf(t),1)},showInputR:function(){var t=this;this.activeColor2="lightblue",this.inputVisibleR=!0,this.rightEye=!0,this.leftEye=!1,this.rightEyeDesc=!1,this.leftEyeDesc=!1,this.$nextTick(function(e){t.$refs.saveTagInputR.$refs.input.focus()})},handleInputConfirmR:function(){this.activeColor2="azure";var t=this.inputValueR;t&&this.dynamicTagsR.push(t),this.inputVisibleR=!1,this.inputValueR="",this.dynamicTagsR.toString().length>40&&(this.$alert("诊断描述不超过40个字符","提示",{confirmButtonText:"确定"}),this.dynamicTagsR.pop())},handleInputConfirmDR:function(){this.activeColor3="azure";var t=this.inputValueDR;t&&this.descriptionTagsR.push(t),this.inputVisibleDR=!1,this.inputValueDR="",this.descriptionTagsR.toString().length>120&&(this.$alert("诊断描述不超过120个字符","提示",{confirmButtonText:"确定"}),this.descriptionTagsR.pop())},handleCloseL:function(t){this.dynamicTagsL.splice(this.dynamicTagsL.indexOf(t),1)},handleCloseDL:function(t){this.descriptionTagsL.splice(this.descriptionTagsL.indexOf(t),1)},showInputL:function(){var t=this;this.activeColor2="lightblue",this.inputVisibleL=!0,this.rightEye=!1,this.leftEye=!0,this.rightEyeDesc=!1,this.leftEyeDesc=!1,this.$nextTick(function(e){t.$refs.saveTagInputL.$refs.input.focus()})},showInputDL:function(){var t=this;this.activeColor3="lightblue",this.inputVisibleDL=!0,this.rightEyeDesc=!1,this.leftEyeDesc=!0,this.leftEye=!1,this.rightEye=!1,this.state="",this.$nextTick(function(e){t.$refs.saveTagInputDL.$refs.input.focus()})},showInputDR:function(){var t=this;this.activeColor3="lightblue",this.inputVisibleDR=!0,this.rightEyeDesc=!0,this.leftEyeDesc=!1,this.leftEye=!1,this.rightEye=!1,this.state="",this.$nextTick(function(e){t.$refs.saveTagInputDR.$refs.input.focus()})},handleInputConfirmL:function(){this.activeColor2="azure";var t=this.inputValueL;t&&this.dynamicTagsL.push(t),this.inputVisibleL=!1,this.inputValueL="",this.dynamicTagsL.toString().length>40&&(this.$alert("诊断描述不超过40个字符","提示",{confirmButtonText:"确定"}),this.dynamicTagsL.pop())},handleInputConfirmDL:function(){this.activeColor3="azure";var t=this.inputValueDL;t&&this.descriptionTagsL.push(t),this.inputVisibleDL=!1,this.inputValueDL="",this.descriptionTagsL.toString().length>120&&(this.$alert("诊断描述不超过120个字符","提示",{confirmButtonText:"确定"}),this.descriptionTagsL.pop())},handleCloseA:function(t){this.dynamicTagsA.splice(this.dynamicTagsA.indexOf(t),1),this.seen=!0,this.seen2=!1,this.value2=""},showInputA:function(){var t=this;this.leftEye=!1,this.rightEye=!1,this.activeColor1="lightblue",this.inputVisibleA=!0,this.advice=!0,this.$nextTick(function(e){t.$refs.saveTagInputA.$refs.input.focus()})},handleInputConfirmA:function(){this.activeColor1="azure";var t=this.inputValueA,e=this.dynamicTagsA;t&&this.dynamicTagsA.push(t),0!==e.length&&(this.seen=!1),this.inputVisibleA=!1,this.inputValueA=""},addDiagnose:function(t){this.leftEye?(this.dynamicTagsL.push(t),this.dynamicTagsL=this.duplicateRemove(this.dynamicTagsL),this.handleInputConfirmL()):this.rightEye&&(this.dynamicTagsR.push(t),this.dynamicTagsR=this.duplicateRemove(this.dynamicTagsR),this.handleInputConfirmR())},addDescription:function(t){this.leftEyeDesc?(this.descriptionTagsL.push(t),this.descriptionTagsL=this.duplicateRemove(this.descriptionTagsL),this.handleInputConfirmDL()):this.rightEyeDesc&&(this.descriptionTagsR.push(t),this.descriptionTagsR=this.duplicateRemove(this.descriptionTagsR),this.handleInputConfirmDR())},addAdvice:function(t){var e=this.dynamicTagsA;if(this.advice){if(0!==e.length)return;this.dynamicTagsA.push(t),this.handleInputConfirmA(),"定时复查"===t&&(this.dialogVisible=!0),"进一步就诊检查"===t&&(this.uplevelVisible=!1)}},formatSex:function(t){return"0"===t.patient_gender?"男":"1"===t.patient_gender?"女":"未知"},finishDiagnose:function(){var t=this;return h()(l.a.mark(function e(){var i,s,n,a,o;return l.a.wrap(function(e){for(;;)switch(e.prev=e.next){case 0:if(i=t.dynamicTagsR.toString(),s=t.dynamicTagsL.toString(),n=t.descriptionTagsL.toString(),a=t.descriptionTagsR.toString(),""===i&&(i="无"),""===s&&(s="无"),""===n&&(n="无"),""===a&&(a="无"),o=t.dynamicTagsA[0].toString(),!(i.length>40||s.length>40||o.length>40)){e.next=12;break}return t.$alert("建议和左右眼诊断内容每条不可超过40个字符","提示",{confirmButtonText:"确定"}),e.abrupt("return",!1);case 12:return t.diaStrR=i,t.diaStrL=s,t.desStrR=a,t.desStrL=n,e.next=18,t._submitDiagnose();case 18:if(1!==e.sent){e.next=24;break}return e.next=22,Object(g.a)();case 22:e.next=25;break;case 24:return e.abrupt("return",!1);case 25:t.eyeSeen=!0,t.diaSeen=!1,t.finishSeen=!0,t.beforeSeen=!1;case 29:case"end":return e.stop()}},e,t)}))()},openFullScreen:function(){var t=this;if(0===this.dynamicTagsA.length)this.open();else{var e=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});setTimeout(function(){e.close(),t.finishDiagnose()},500)}},clickCreateImgBtn:function(){var t=this,e=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"}),i=this.patient_info.patient_id,s=this.getDiagnoseResult(),n=s.other_data.right_origin_src,a=s.other_data.left_origin_src,o=localStorage.getItem("last_name")+localStorage.getItem("first_name"),r=localStorage.getItem("superior_hospital_name");r||(r=localStorage.getItem("hospital_name"));var l={};l.patient_id=i,l.right_origin_src=n,l.left_origin_src=a,l.username=o,l.hospital_name=r,Object(d.e)(l).then(function(i){if(console.log("res=>",i),0===i)e.close(),t.$alert("生成失败","提示",{confirmButtonText:"确定"});else{e.close();var s=Math.random().toString(36).substr(2),n=window.open("",s,"");n.document.title="profession",n.location=f+i}}).catch(function(i){e.close(),t.$alert("生成失败","提示",{confirmButtonText:"确定"})})},backToUndiagnosed:function(){var t=this;if(0===this.dynamicTagsA.length)this.open();else{var e={};e.page_size=this.patient_info.page_size,e.currentPage=this.patient_info.currentPage;var i=this.finishDiagnose(),s=this.$store.state.page_from;if(!1===i)return;var n=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});setTimeout(function(){n.close(),t.$router.push("/"+s)},1e3)}},onlyBack:function(){var t=this,e={};e.page_size=this.patient_info.page_size,e.currentPage=this.patient_info.currentPage;var i=this.$store.state.page_from,s=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.9)"});setTimeout(function(){s.close(),t.$router.push("/"+i)},1e3)},getConclusion:function(){var t=this;_.a.get(f+"/diagnosis/?&ordering=-times").then(function(e){console.log(e.data);for(var i=e.data.results,s=[],n=0;n<i.length;n++)s.push(i[n].conclusion);t.diseases=s.slice(0,8)}).catch(function(t){console.log(t)})},getDescription:function(){var t=this;_.a.get(f+"/descriptions/?&ordering=-times").then(function(e){var i=e.data.results;t.replaceDictKey(i)}).catch(function(t){console.log(t)})},getDiagnoseResult:function(){var t={},e={},i={};if(t.patient_id=this.patient_info.patient_id,t.diagnose_doctor=localStorage.getItem("user_id"),t.diagnose_record=this.patient_info.diagnose_record,t.apply_time=this.patient_info.apply_time,t.patient_name=this.patient_info.patient_name,t.patient_gender=this.patient_info.patient_gender,t.patient_age=this.patient_info.patient_age,t.refine_days=this.patient_info.refine_days,t.refine_weeks=this.patient_info.refine_weeks,t.birth_days=this.patient_info.birth_days,t.birth_weeks=this.patient_info.birth_weeks,t.birth_weight=this.patient_info.birth_weight,t.left_diagnose=this.diaStrL,t.right_diagnose=this.diaStrR,t.left_desc=this.desStrL,t.right_desc=this.desStrR,t.diagnose_advice=this.dynamicTagsA[0],t.jwsInfo=this.jwsDisplayInfo,e.superior_hospital=localStorage.getItem("superior_hospital"),e.right_origin_src=this.right_src.split("media")[this.right_src.split("media").length-1],e.left_origin_src=this.left_src.split("media")[this.left_src.split("media").length-1],-1===e.right_origin_src.search("noimg")){var s=e.right_origin_src.lastIndexOf("."),n=e.right_origin_src.substr(s);console.log("新式眼底格式2",n),e.right_AI_src=e.right_origin_src.replace(n,"_AI"+n)}else e.right_AI_src=this.right_src.split("media")[this.right_src.split("media").length-1];if(-1===e.left_origin_src.search("noimg")){var a=e.left_origin_src.lastIndexOf("."),o=e.left_origin_src.substr(a);console.log("新式眼底格式1",o),e.left_AI_src=e.left_origin_src.replace(o,"_AI"+o)}else e.left_AI_src=this.left_src.split("media")[this.left_src.split("media").length-1];return this.value2&&(t.review_time=this.value2,t.transform="1"),this.uplevelHospital&&(t.review_hospital=this.uplevelHospital,t.transform="1"),e.oozed_amount=this.AIdata.oozed_amount,e.bleeding_amount=this.AIdata.bleeding_amount,e.oozed_area=this.AIdata.oozed_area,e.bleeding_area=this.AIdata.bleeding_area,e.max_oozed_area=this.AIdata.max_oozed_area,e.max_bleeding_area=this.AIdata.max_bleeding_area,e.other_advice="",i.basic_data=t,i.other_data=e,i},_submitDiagnose:function(){var t=this,e=this.getDiagnoseResult();return new o.a(function(i,s){Object(d.y)(e).then(function(e){console.log("res=>",e),0===e?(t.$alert("阅片失败","提示",{confirmButtonText:"确定"}),i(0)):2===e?(t.$alert("该患者已被诊断，可在已诊列表查看","提示",{confirmButtonText:"确定"}),i(2)):i(1)}).catch(function(e){console.log(e),t.$alert("阅片错误","提示",{confirmButtonText:"确定"}),s()})})},submitDiagnose:function(){var t,e=this,i=this.getDiagnoseResult();Object(d.y)(i).then((t=h()(l.a.mark(function t(i){var s;return l.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:if(console.log("res=>",i),0!==i){t.next=5;break}e.$alert("阅片失败","提示",{confirmButtonText:"确定"}),t.next=18;break;case 5:if(2!==i){t.next=11;break}return!0,t.next=9,e.$alert("该患者已被诊断，可在已诊列表查看","提示",{confirmButtonText:"确定"});case 9:t.next=18;break;case 11:return s=JSON.parse(localStorage.getItem("patient_info")),s.minusMessage,t.next=16,Object(d.r)(s).then(function(t){1===t?console.log("消息减去成功"):console.log("消息减去失败")});case 16:return t.next=18,Object(g.a)();case 18:case"end":return t.stop()}},t,e)})),function(e){return t.apply(this,arguments)})).catch(function(t){console.log(t),e.$alert("阅片错误","提示",{confirmButtonText:"确定"})})},messageAmountProcess:function(t){return new o.a(function(e){Object(d.r)(t).then(function(t){1===t?console.log("消息减去成功"):console.log("消息减去失败"),e(t)})})},duplicateRemove:function(t){for(var e=[],i=0;i<t.length;i++)-1===e.indexOf(t[i])&&e.push(t[i]);return console.log(e),e},createReport:function(t){var e=this,i=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"}),s=this.getDiagnoseResult();s.basic_data.reportType=t,Object(d.f)(s).then(function(t){if(i.close(),console.log("res=>",t),t.length>1){var n=Math.random().toString(36).substr(2),a=window.open("",n,"");a.document.title="pdf";var o=s.basic_data.patient_name,r=s.basic_data.patient_id;a.location=f+"media/patient_pdf/"+t+"/"+o+"_"+r+".pdf"}else e.$alert("诊断报告生成失败","提示",{confirmButtonText:"确定"})}).catch(function(t){i.close(),console.log(t),e.$alert("请允许弹窗","提示",{confirmButtonText:"确定"})})},finishAndCreatePdf:function(){var t=this;if(0===this.dynamicTagsA.length)this.open();else try{console.log("start submit");var e=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});setTimeout(h()(l.a.mark(function i(){return l.a.wrap(function(i){for(;;)switch(i.prev=i.next){case 0:return e.close(),i.next=3,t.finishDiagnose();case 3:if(!1!==i.sent){i.next=6;break}return i.abrupt("return");case 6:t.createReport(1);case 7:case"end":return i.stop()}},i,t)})),500)}catch(t){console.log(t)}},createAIreport:function(){var t=this;if(0===this.dynamicTagsA.length)this.open();else try{var e=this.$loading({lock:!0,text:"Loading",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});setTimeout(h()(l.a.mark(function i(){return l.a.wrap(function(i){for(;;)switch(i.prev=i.next){case 0:e.close(),t.createReport(0);case 2:case"end":return i.stop()}},i,t)})),500)}catch(t){console.log(t)}},cancelSelectDate:function(){this.dialogVisible=!1,this.seen2=!1,this.value2=""},confirmSelectDate:function(){this.dialogVisible=!1,this.seen2=!0,this.value2||(this.seen2=!1,this.value2="")},cancelInputHospital:function(){this.uplevelVisible=!1,this.uplevelHospital=""},confirmInputHospital:function(){this.uplevelVisible=!1},open:function(){this.$alert("请添加建议","提示",{confirmButtonText:"确定"})},replaceDictKey:function(t){for(var e=[],i=0;i<t.length;i++)delete t[i].id,delete t[i].times,e.push(t[i]);for(var s={description:"value"},a=[],o=function(t){n()(e[t]).reduce(function(i,n){i[s[n]||n]=e[t][n],a.push(i)},{})},r=0;r<e.length;r++)o(r);this.restaurants=a},querySearchAsync:function(t,e){var i=this.restaurants;e(t?i.filter(this.createStateFilter(t)):i)},createStateFilter:function(t){return function(e){return 0===e.value.toLowerCase().indexOf(t.toLowerCase())}},handleSelect:function(t){this.leftEyeDesc?this.textarea2.length+t.value.length>120?this.$alert("影像所见不超过120个字符","提示",{confirmButtonText:"确定"}):(this.textarea2=this.textarea2+t.value+"。",this.state=""):this.textarea1.length+t.value.length>120?this.$alert("影像所见不超过120个字符","提示",{confirmButtonText:"确定"}):(this.textarea1=this.textarea1+t.value+"。",this.state="")},AiDiagnose:function(t){console.log("病理近视",t);t.left_rm,t.left_pm,t.right_rm,t.right_pm;var e=t.left_oozed_amount,i=t.right_oozed_amount,s=t.left_oozed_area,n=t.right_oozed_area,a=t.left_bleeding_amount,o=t.right_bleeding_amount,r=t.left_bleeding_area,l=t.right_bleeding_area,c=t.left_max_bleeding_area,h=t.right_max_bleeding_area,p=t.left_max_oozed_area,_=t.right_max_oozed_area,u=(t.left_prob_dr,t.right_prob_dr,t.left_glaucoma,t.right_glaucoma,t.left_warning,t.right_warning,t.left_rop),g=t.right_rop;this.AIdata.iqa_score_left=t.left_iqa_score<60?"不佳":t.left_iqa_score>=75?"良好":"一般",this.AIdata.iqa_score_right=t.right_iqa_score<60?"不佳":t.right_iqa_score>=75?"良好":"一般",this.AIdata.oozed_area=(10*s+10*n)/10,this.AIdata.oozed_amount=e+i,this.AIdata.max_oozed_area=(10*p+10*_)/10,this.AIdata.bleeding_area=(10*r+10*l)/10,this.AIdata.bleeding_amount=a+o,this.AIdata.max_bleeding_area=(10*c+10*h)/10,1===u&&this.dynamicTagsL.push("疑似ROP"),1===g&&this.dynamicTagsR.push("疑似ROP"),1===r&&this.dynamicTagsL.push("疑似眼底出血"),1===l&&this.dynamicTagsR.push("疑似眼底出血"),1===g||1===u?this.dynamicTagsA.push("进一步就诊检查"):1!==r&&1!==l||this.dynamicTagsA.push("进一步就诊检查"),this.handleInputConfirmA()},picture_strengthen:function(){var t=this,e=this.strengthen,i=this.right_src.split("media")[this.right_src.split("media").length-1],s=this.left_src.split("media")[this.left_src.split("media").length-1],n={};if(n.left_src=s,n.right_src=i,e){var a=this.$loading({lock:!0,text:"一键增强中",spinner:"el-icon-loading",background:"rgba(0, 0, 0, 0.7)"});Object(d.t)(n).then(function(e){if(console.log("res=>",e),0===e.data)a.close(),t.$alert("一键增强失败","提示",{confirmButtonText:"确定"});else{if(a.close(),-1===s.search("noimg")){var n=t.left_src.lastIndexOf("."),o=t.left_src.substr(n);t.left_src=t.left_src.replace(o,"_strengthen"+o),t.left_srcList[0]=t.left_src}if(-1===i.search("noimg")){var r=t.right_src.lastIndexOf("."),l=t.right_src.substr(r);t.right_src=t.right_src.replace(l,"_strengthen"+l),t.right_srcList[0]=t.right_src}}}).catch(function(e){console.log(e),a.close(),t.$alert("一键增强失败","提示",{confirmButtonText:"确定"})})}else-1===i.search("noimg")&&(this.right_src=this.right_src.replace("_strengthen",""),this.right_srcList[0]=this.right_src),-1===s.search("noimg")&&(this.left_src=this.left_src.replace("_strengthen",""),this.left_srcList[0]=this.left_src)},determin_report_type:function(){"0"===localStorage.getItem("reportType")?(this.report_button=!1,this.AI_report_button=!0):(this.report_button=!0,this.AI_report_button=!1)},display_history_diseases:function(){var t=this.patient_info.historyDisease;if(0===t.length)this.jwsDisplayInfo="无";else{this.jwsDisplayInfo="有",console.log("既往史细节",t[0]);var e="";if(1===t[0].DM_year?e="糖尿病 ":!0===t[0].DM_year&&(e="糖尿病 "),1===t[0].HPL_year?e+="高血脂 ":!0===t[0].HPL_year&&(e+="高血脂 "),1===t[0].HTN_year?e+="高血压 ":!0===t[0].HTN_year&&(e+="高血压 "),t[0].left_diopter&&("0"===t[0].left_diopter?e+="左眼:正视 ":"1"===t[0].left_diopter?e+="左眼:低度近视(75~300) ":"2"===t[0].left_diopter?e+="左眼:中度近视(300~600) ":"3"===t[0].left_diopter?e+="左眼:高度近视(>600) ":"4"===t[0].left_diopter&&(e+="左眼:远视 ")),t[0].right_diopter&&("0"===t[0].right_diopter?e+="右眼:正视 ":"1"===t[0].right_diopter?e+="右眼:低度近视(75~300) ":"2"===t[0].right_diopter?e+="右眼:中度近视(300~600) ":"3"===t[0].right_diopter?e+="右眼:高度近视(>600) ":"4"===t[0].right_diopter&&(e+="右眼:远视 ")),t[0].pregnant_weeks)e=e+"妊娠"+t[0].pregnant_weeks+"周 ";if(t[0].other)e=e+"其他:"+t[0].other+" ";this.jwsDisplayInfo=e}}},mounted:function(){this.getConclusion(),this.getDescription(),this.determin_report_type(),this.hospital_name=localStorage.getItem("final_hospital_name"),this.patient_info=JSON.parse(localStorage.getItem("patient_info"));var t=this.patient_info.diagnose.length-1;this.AIdata=this.patient_info.diagnose[t],this.AiDiagnose(this.patient_info.diagnose[t]),this.display_history_diseases();try{var e=this.patient_info.picture;console.log("所有照片信息",e);var i=e.length-1,s=[],n=[],a=e[i].own_to;console.log("latest",a);for(var o=0;o<e.length;o++)if(console.log(e[o].pic_name),e[o].own_to===a)if(-1===e[o].pic_name.search("infrared"))if(-1!==e[o].pic_name.search("Left")){var r=f+"media/patient_img/"+e[o].pic_name;s.push(r),console.log("照片在服务器的位置",r)}else{var l=f+"media/patient_img/"+e[o].pic_name;n.push(l)}else console.log("i find infrared and filter it");if(s=s.reverse(),0===(n=n.reverse()).length){console.log("左眼没有照片");var c=[];c[0]=f+"media/image/noimg.jpg",console.log(c),this.right_src=c[0],this.right_srcList=[],this.textarea1="无照片"}else this.right_src=n[0],this.right_srcList=n;if(0===s.length){console.log("右眼没有照片");var h=[];h[0]=f+"media/image/noimg.jpg",console.log(h),this.left_src=h[0],this.left_srcList=[],this.textarea2="无照片"}else this.left_src=s[0],this.left_srcList=s}catch(t){console.log(t)}},beforeDestroy:function(){var t=this.patient_info.patient_id,e=(localStorage.getItem("superior_hospital"),localStorage.getItem("user_id"),{});e.patient_id=t,Object(d.n)(e)}},m={render:function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("el-container",[i("div",{staticClass:"aside"},[i("el-row",{staticClass:"column_style",style:{backgroundColor:t.activeColor3}},[i("i",{staticClass:"icon iconfont icon-icon-test"}),t._v("描述栏\n  ")]),t._v(" "),i("el-row",{staticStyle:{"margin-top":"20px"}},[i("el-autocomplete",{ref:"descInput",attrs:{"fetch-suggestions":t.querySearchAsync,clearable:!0,placeholder:"点击可显示影像所见描述","prefix-icon":"el-icon-search"},on:{select:t.handleSelect},model:{value:t.state,callback:function(e){t.state=e},expression:"state"}})],1),t._v(" "),i("el-row",{staticClass:"column_style",staticStyle:{"margin-top":"20px","background-color":"azure"},style:{backgroundColor:t.activeColor2}},[i("i",{staticClass:"icon iconfont icon-icon-test"}),t._v("印象栏\n  ")]),t._v(" "),t._l(t.diseases,function(e){return i("el-row",{key:e.id,staticClass:"diseases_section"},[i("el-col",{attrs:{span:3}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:18}},[i("a",{attrs:{href:"javascript:;"},on:{click:function(i){return t.addDiagnose(e)}}},[i("div",{staticClass:"media_change1"},[t._v(t._s(e))])])]),t._v(" "),i("el-col",{attrs:{span:3}},[t._v(" ")])],1)}),t._v(" "),i("el-row",{staticClass:"column_style",staticStyle:{"margin-top":"20px"},style:{backgroundColor:t.activeColor1}},[i("i",{staticClass:"icon iconfont icon-icon-test"}),t._v("建议栏\n    ")]),t._v(" "),t._l(t.suggestions,function(e){return i("el-row",{key:e.id,staticClass:"suggestion_section"},[i("el-col",{attrs:{span:3}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:18}},[i("a",{attrs:{href:"javascript:;"},on:{click:function(i){return t.addAdvice(e)}}},[i("div",{staticClass:"media_change1"},[t._v(t._s(e))])])]),t._v(" "),i("el-col",{attrs:{span:3}},[t._v(" ")])],1)})],2),t._v(" "),i("div",{staticClass:"main"},[i("el-row",[i("span",[t._v(t._s(t.hospital_name))])]),t._v(" "),i("el-row",{staticStyle:{"margin-top":"10px",height:"40px","line-height":"40px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{staticStyle:{"border-top":"lightgrey 1px solid","border-bottom":"lightgrey 1px solid","text-align":"left"},attrs:{span:16}},[i("div",{staticClass:"button_area"},[i("div",[t._v("姓名:"),i("span",[t._v(t._s(t.patient_info.patient_name))])]),t._v(" "),i("div",[t._v("性别:"),"1"===t.patient_info.patient_gender?i("span",[t._v("女")]):i("span",[t._v("男")])]),t._v(" "),i("div",[t._v("年龄:"),i("span",[t._v(t._s(t.patient_info.patient_age))])]),t._v(" "),i("div",[t._v("录入时间:"),i("span",{attrs:{id:"apply_time"}},[t._v(t._s(t.patient_info.apply_time))])])])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("el-row",{staticStyle:{"text-align":"left","font-weight":"bold"}},[i("el-col",{attrs:{span:11}},[t._v("OD(图像质量:"+t._s(t.AIdata.iqa_score_right)+")")]),t._v(" "),i("el-col",{attrs:{span:2}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:11}},[t._v("OS(图像质量:"+t._s(t.AIdata.iqa_score_left)+")")])],1)],1),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("el-row",{staticStyle:{"text-align":"left","font-weight":"bold"}},[i("el-col",{attrs:{span:11}},[i("div",{staticClass:"demo-image__preview",on:{click:t.displayAllPictures}},[i("el-image",{staticStyle:{width:"100%",height:"auto"},attrs:{src:t.right_src}})],1)]),t._v(" "),i("el-col",{attrs:{span:2}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:11}},[i("div",{staticClass:"demo-image__preview",on:{click:t.displayAllPictures}},[i("el-image",{staticStyle:{width:"100%",height:"auto"},attrs:{src:t.left_src}})],1)])],1)],1),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("智能图像处理:")])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("el-switch",{attrs:{"active-text":"增强","inactive-text":"重置"},on:{change:t.picture_strengthen},model:{value:t.strengthen,callback:function(e){t.strengthen=e},expression:"strengthen"}})],1),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("既往史:")]),t._v("   \n        "),i("i",{staticClass:"el-icon-warning",staticStyle:{color:"goldenrod","font-size":"small"}},[t._v(" "+t._s(t.jwsDisplayInfo))])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("影像所见:")])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:8}},[i("span",{staticStyle:{color:"#E6A23C","font-weight":"initial"}},[t._v("右眼OD:")]),t._v("\n         \n        "),i("span",{staticClass:"addDesc",staticStyle:{color:"#E6A23C"},on:{click:t.add_description_r}},[t._v("添加所见 +")])]),t._v(" "),i("el-col",{attrs:{span:8}},[i("span",{staticStyle:{color:"#5daf34","font-weight":"initial",padding:"0 0 0 1em"}},[t._v("左眼OS:")]),t._v("\n         \n        "),i("span",{staticClass:"addDesc",staticStyle:{color:"#5daf34"},on:{click:t.add_description_l}},[t._v("添加所见 +")])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left","margin-top":"10px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{staticStyle:{margin:"0 1em 0 0"},attrs:{span:8}},[i("el-input",{attrs:{type:"textarea",autosize:{minRows:4},maxlength:"120",placeholder:"请输入内容(限制120字符以内)"},model:{value:t.textarea1,callback:function(e){t.textarea1=e},expression:"textarea1"}}),t._v(" "),i("el-row",{staticClass:"fontNumber",staticStyle:{"text-align":"right"}},[i("span",[t._v("已输入"+t._s(this.textarea1.length)+"字/120字")])])],1),t._v(" "),i("el-col",{attrs:{span:8}},[i("el-input",{attrs:{type:"textarea",autosize:{minRows:4},maxlength:"120",placeholder:"请输入内容(限制120字符以内)"},model:{value:t.textarea2,callback:function(e){t.textarea2=e},expression:"textarea2"}}),t._v(" "),i("el-row",{staticClass:"fontNumber",staticStyle:{"text-align":"right"}},[i("span",[t._v("已输入"+t._s(this.textarea2.length)+"字/120字")])])],1),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),i("el-row",{staticStyle:{"text-align":"left"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("初步印象:")]),t._v("   \n        "),t.warningShow?i("i",{staticClass:"el-icon-warning",staticStyle:{color:"goldenrod","font-size":"small"}},[t._v(" "+t._s(t.warning))]):t._e()]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1),t._v(" "),t.diaSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"10px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[t._v("右眼:\n        "),t._l(t.dynamicTagsR,function(e){return i("el-tag",{key:e,attrs:{closable:"","disable-transitions":!1,type:"info",effect:"plain"},on:{close:function(i){return t.handleCloseR(e)}}},[t._v("\n          "+t._s(e)+"\n        ")])}),t._v(" "),t.inputVisibleR?i("el-input",{ref:"saveTagInputR",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:t.handleInputConfirmR},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleInputConfirmR(e)}},model:{value:t.inputValueR,callback:function(e){t.inputValueR=e},expression:"inputValueR"}}):i("el-tooltip",{attrs:{placement:"right"}},[i("div",{attrs:{slot:"content"},slot:"content"},[t._v("点击后可手动输入印象"),i("br"),t._v("点击后也可从左侧印象栏选择印象")]),t._v(" "),i("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:t.showInputR}},[t._v("+ 添加印象")])],1)],2),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.diaSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"10px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[t._v("左眼:\n        "),t._l(t.dynamicTagsL,function(e){return i("el-tag",{key:e,attrs:{closable:"","disable-transitions":!1,effect:"plain",type:"info"},on:{close:function(i){return t.handleCloseL(e)}}},[t._v("\n          "+t._s(e)+"\n        ")])}),t._v(" "),t.inputVisibleL?i("el-input",{ref:"saveTagInputL",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:t.handleInputConfirmL},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleInputConfirmL(e)}},model:{value:t.inputValueL,callback:function(e){t.inputValueL=e},expression:"inputValueL"}}):i("el-tooltip",{attrs:{placement:"right"}},[i("div",{attrs:{slot:"content"},slot:"content"},[t._v("点击后可手动输入印象"),i("br"),t._v("点击后也可从左侧印象栏选择印象")]),t._v(" "),i("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:t.showInputL}},[t._v("+ 添加印象")])],1)],2),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.eyeSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"10px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[t._v("右眼:"+t._s(t.diaStrR))]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.eyeSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"10px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[t._v("左眼:"+t._s(t.diaStrL))]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.diaSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("建议:\n       "),t._l(t.dynamicTagsA,function(e){return i("el-tag",{key:e,attrs:{closable:"","disable-transitions":!1,type:"info",effect:"plain"},on:{close:function(i){return t.handleCloseA(e)}}},[t._v("\n          "+t._s(e)+"\n        ")])}),t._v(" "),t.inputVisibleA?i("el-input",{ref:"saveTagInputA",staticClass:"input-new-tag",attrs:{size:"small"},on:{blur:t.handleInputConfirmA},nativeOn:{keyup:function(e){return!e.type.indexOf("key")&&t._k(e.keyCode,"enter",13,e.key,"Enter")?null:t.handleInputConfirmA(e)}},model:{value:t.inputValueA,callback:function(e){t.inputValueA=e},expression:"inputValueA"}}):t._e(),t._v(" "),i("el-tooltip",{attrs:{placement:"right"}},[i("div",{attrs:{slot:"content"},slot:"content"},[t._v("点击后可手动输入诊疗建议"),i("br"),t._v("点击后也可从左侧建议栏选择建议")]),t._v(" "),t.seen?i("el-button",{staticClass:"button-new-tag",attrs:{size:"small"},on:{click:t.showInputA}},[t._v("+ 添加建议")]):t._e()],1),t._v("\n           "),t.seen2?i("span",[t._v("日期:"+t._s(t.value2))]):t._e()],2)]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.eyeSeen?i("el-row",{staticStyle:{"text-align":"left","margin-top":"20px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{attrs:{span:16}},[i("span",[t._v("建议:"+t._s(t.dynamicTagsA[0])+"\n\n           "),t.seen2?i("span",[t._v("日期:")]):t._e(),t._v(t._s(t.value2)+"\n      ")])]),t._v(" "),i("el-col",{attrs:{span:4}},[t._v(" ")])],1):t._e(),t._v(" "),t.beforeSeen?i("el-row",{staticStyle:{"margin-top":"20px",height:"40px","line-height":"40px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{staticStyle:{"text-align":"left",height:"60px","line-height":"60px","border-top":"1px solid lightgray","border-bottom":"1px solid lightgray"},attrs:{span:16}},[i("div",{staticClass:"button_area"},[i("div",[i("el-button",{on:{click:t.clickCreateImgBtn}},[t._v("生成照片")])],1),t._v(" "),i("div",{directives:[{name:"show",rawName:"v-show",value:t.report_button,expression:"report_button"}]},[i("el-button",{on:{click:t.backToUndiagnosed}},[t._v("完成并返回")])],1),t._v(" "),i("div",{directives:[{name:"show",rawName:"v-show",value:t.report_button,expression:"report_button"}]},[i("el-button",{on:{click:t.finishAndCreatePdf}},[t._v("完成并生成报告")])],1),t._v(" "),i("div",{directives:[{name:"show",rawName:"v-show",value:t.AI_report_button,expression:"AI_report_button"}]},[i("el-button",{on:{click:t.createAIreport}},[t._v("生成报告")])],1),t._v(" "),i("div",[i("el-button",{on:{click:t.onlyBack}},[t._v("返回")])],1)])]),t._v(" "),i("el-col",{attrs:{span:4}})],1):t._e(),t._v(" "),t.finishSeen?i("el-row",{staticStyle:{"margin-top":"20px",height:"40px","line-height":"40px"}},[i("el-col",{attrs:{span:4}},[t._v(" ")]),t._v(" "),i("el-col",{staticStyle:{"text-align":"left",height:"60px","line-height":"60px","border-top":"1px solid lightgray","border-bottom":"1px solid lightgray"},attrs:{span:16}},[i("el-row",[i("el-col",{attrs:{span:8}},[i("el-button",{on:{click:t.onlyBack}},[t._v("返回")])],1),t._v(" "),i("el-col",{attrs:{span:8}},[i("el-button",{on:{click:t.createReport}},[t._v("生成报告")])],1),t._v(" "),i("el-col",{attrs:{span:8}},[t._v(" ")])],1)],1),t._v(" "),i("el-col",{attrs:{span:4}})],1):t._e()],1),t._v(" "),i("el-dialog",{attrs:{title:"请输入复查时间(可不填写)",visible:t.dialogVisible,"show-close":!1,width:"30%"},on:{"update:visible":function(e){t.dialogVisible=e}}},[i("div",{staticClass:"block"},[i("el-date-picker",{attrs:{align:"right",type:"date","value-format":"yyyy-MM-dd",placeholder:"选择日期","picker-options":t.pickerOptions},model:{value:t.value2,callback:function(e){t.value2=e},expression:"value2"}})],1),t._v(" "),i("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{attrs:{type:"primary"},on:{click:t.confirmSelectDate}},[t._v("确 定")])],1)]),t._v(" "),i("el-dialog",{attrs:{title:"请输入医院名称",visible:t.uplevelVisible,width:"30%"},on:{"update:visible":function(e){t.uplevelVisible=e}}},[i("div",{staticClass:"block"},[i("el-form",[i("el-form-item",{attrs:{label:"医院名称"}},[i("el-input",{attrs:{"auto-complete":"off",placeholder:"请输入医院名称(限制字数20以内)",maxlength:"20"},model:{value:t.uplevelHospital,callback:function(e){t.uplevelHospital=e},expression:"uplevelHospital"}})],1)],1)],1),t._v(" "),i("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{on:{click:t.cancelInputHospital}},[t._v("取 消")]),t._v(" "),i("el-button",{attrs:{type:"primary"},on:{click:t.confirmInputHospital}},[t._v("确 定")])],1)]),t._v(" "),i("el-dialog",{attrs:{title:"提示",visible:t.centerDialogVisible,width:"30%",center:""},on:{"update:visible":function(e){t.centerDialogVisible=e}}},[i("span",[t._v("生成报告失败")]),t._v(" "),i("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[i("el-button",{attrs:{type:"primary"},on:{click:function(e){t.centerDialogVisible=!1}}},[t._v("确 定")])],1)])],1)},staticRenderFns:[]};var y=i("VU/8")(v,m,!1,function(t){i("otuT")},"data-v-51fb63a1",null);e.default=y.exports}});
//# sourceMappingURL=3.0827058ad9e433d9ef86.js.map