<template>
    <div>
        <el-container>
            <el-header>
                <h1 style="color: gray">自动摘要</h1>
            </el-header>
            <el-main style="text-align: center">
                <span style="font-size: 15px; color: gray;">
                    文本摘要生成能够实现文本内容的理解、精简提炼，生成简短、准确、流畅的摘要，并能根据需求灵活控制生成的摘要长度。文本摘要生成可用于文本内容理解、新闻自动生成、冗余文档检测、智能写作等，是智能媒体行业必备的AI能力之一。
                </span>
                <!--<span style="font-size: 15px; color: gray;">-->

                <!--</span>-->
                <el-input
                        type="textarea"
                        placeholder="请输入内容"
                        v-model="summaryText"
                        maxlength="400"
                        show-word-limit
                        :autosize="{ minRows: 5, maxRows: 8}"
                        clearable
                        style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"
                >
                </el-input>
                <el-row style="margin-top: 30px; display: flex; justify-content: center">
                    <el-button v-on:click="getData" type="primary">开始摘要</el-button>
                    <el-button type="success">随便试试</el-button>
                </el-row>
                <el-input
                        type="textarea"
                        placeholder="摘要生成结果"
                        v-model="summaryRes"
                        maxlength="400"
                        disabled
                        :autosize="{ minRows: 5, maxRows: 5 }"
                        clearable
                        class="res-textarea"
                >
                </el-input>

            </el-main>
            <!--<el-footer>Footer</el-footer>-->
        </el-container>
    </div>
</template>

<script>
import { fetchData } from '../../api/index';
export default {
    name: 'basetable',
    data() {
        return {
            text: '',
            summaryText: '',
            summaryRes:'摘要结果',
            queryURL:'http://61.135.242.193:5000/api/summarization'
        };
    },
    created() {
        // this.getData();
    },
    methods: {
        // 获取 easy-mock 的模拟数据
        getData() {
            // this.summaryRes = this.summaryText
            fetch(this.queryURL, {
                method: "POST",
                body: JSON.stringify({
                    docs: [{
                        "id":123,
                        "doc":this.summaryText,
                    }]
                }),
                headers: {
                    "Content-Type": "application/json"
                },

            }).then(res => res.json())
                .catch(error => console.error('Error:', error))
                .then(response => this.summaryRes =  response.data[0].summary);
        },

    }
};
</script>

<style scoped>
    @import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
    .el-header, .el-footer {
        font-size: 20px;
        color: black;
        text-align: center;
        line-height: 60px;
    }
    .res-textarea {
        color: black; margin-top: 30px;box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
    }





</style>
