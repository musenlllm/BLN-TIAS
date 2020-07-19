<template>
    <div style="display: flex;height: inherit">
        <!--<a id="go" href='../../public/entrypage.html'/>-->
        <iframe ref="iframe" src="/entrypage.html" frameborder="0"style="width: 100%"></iframe>
    </div>

</template>

<script>
    export default {
        data: function() {
            return {
                iframeWin: {}
            };
        },
        name: 'entrypage',
        methods: {
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
                        //得到登陆请求
                        console.log("login!!")
                        this.$router.push('/login');
                        break;
                }
            }

        },
        //注册事件
        mounted(){
            window.addEventListener("message",this.handleMessage);
            this.iframeWin = this.$refs.iframe.contentWindow;
        }
    };
</script>

<style scoped>

</style>
