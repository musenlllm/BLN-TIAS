<template>
    <div style="display: flex;height: inherit">
        <!--<a id="go" href='../../public/entrypage.html'/>-->
        <iframe ref="iframe" v-bind:src="getPageUrl" frameborder="0"style="width: 100%"></iframe>
    </div>

</template>

<script>
    export default {
        data: function() {
            return {
                getPageUrl: 'https://kingsundad.gitee.io/ldmc-tias-index/',
                iframeWin: {},
                // publicPath: process.env.BASE_URL
            };
        },
        name: 'entrypage',
        methods: {
            // openEntrypage(){
            //     window.location.href="https://kingsunfather.github.io/buaa-tias-preview/"
            // },
            //向iframe传数据
            sendMessage2Vue(){
                this.iframeWin.postMessage(
                    {
                        cmd: "sendMessage2Iframe",
                        params: {}
                    },
                    "*"
                );
            },
            //解析iframe内部发回来的消息
            handleMessage(event) {
                const data = event.data;
                switch (data.cmd) {
                    case "loginRequest":
                        var url = data.url;
                        //得到登陆请求
                        console.log("login!!")
                        localStorage.setItem('ms_username', 'ldmc');

                        this.$router.push('/'+'ner');
                        break;
                }
            },

        },
        //注册事件
        mounted(){
            window.addEventListener("message",this.handleMessage);
            this.iframeWin = this.$refs.iframe.contentWindow;
            // this.openEntrypage();
        }
    };
</script>

<style scoped>

</style>
