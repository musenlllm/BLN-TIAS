(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["entrypage"],{c0c4:function(e,t,n){"use strict";n.r(t);var a=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticStyle:{display:"flex",height:"inherit"}},[n("iframe",{ref:"iframe",staticStyle:{width:"100%"},attrs:{src:e.getPageUrl,frameborder:"0"}})])},i=[],s={data:function(){return{getPageUrl:"https://kingsunfather.github.io/buaa-tias-preview/",iframeWin:{}}},name:"entrypage",methods:{openEntrypage:function(){window.location.href="https://kingsunfather.github.io/buaa-tias-preview/"},sendMessage2Vue:function(){this.iframeWin.postMessage({cmd:"sendMessage2Iframe",params:{}},"*")},handleMessage:function(e){var t=e.data;switch(t.cmd){case"loginRequest":console.log("login!!"),this.$router.push("/login");break}}},mounted:function(){window.addEventListener("message",this.handleMessage),this.iframeWin=this.$refs.iframe.contentWindow}},r=s,o=n("2877"),c=Object(o["a"])(r,a,i,!1,null,"4644ee3c",null);t["default"]=c.exports}}]);