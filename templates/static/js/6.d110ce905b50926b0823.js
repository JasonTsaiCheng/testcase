webpackJsonp([6],{OQQe:function(e,t){},m3Zk:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n={name:"previewPdf",mounted:function(){this.src=this.$route.query.src},data:function(){return{src:""}},methods:{goBack:function(){window.close()},createPdf:function(){var e=localStorage.getItem("pdf");e="true"===e?"false":"true"===e?"false":"true",localStorage.setItem("pdf",e),window.open(this.src,"_self")}}},s={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",[t("el-row",[t("iframe",{attrs:{src:this.src,frameborder:"0"}}),this._v(" "),t("el-button",{on:{click:this.createPdf}},[this._v("生成报告")]),this._v(" "),t("el-button",{on:{click:this.goBack}},[this._v("返回修改")])],1)],1)},staticRenderFns:[]};var c=r("VU/8")(n,s,!1,function(e){r("OQQe")},"data-v-7b74f407",null);t.default=c.exports}});
//# sourceMappingURL=6.d110ce905b50926b0823.js.map