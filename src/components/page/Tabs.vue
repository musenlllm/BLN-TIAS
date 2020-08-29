<template>
    <div>
        <el-container>
            <el-header>
                <h1 style="color: gray">实体识别</h1>
            </el-header>
            <el-main style="text-align: center">
                <!--<span style="font-size: 15px; color: gray;">-->
                <!--文本摘要生成能够实现文本内容的理解、精简提炼，生成简短、准确、流畅的摘要，并能根据需求灵活控制生成的摘要长度。文本摘要生成可用于文本内容理解、新闻自动生成、冗余文档检测、智能写作等，是智能媒体行业必备的AI能力之一。-->
                <!--</span>-->
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
                        style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04); font-size: 15px"
                >
                </el-input>
                <el-row style="margin-top: 30px; display: flex; justify-content: center">
                    <el-button v-on:click="getData" type="primary" style="background: #242f42; border: 0px">开始识别</el-button>
                    <el-button >随便试试</el-button>
                </el-row>
                <div class="tag-group" style="margin-top: 30px; display: flex; flex-direction: row; flex-wrap: wrap;">
                    <el-tag style="margin: 2px; border-radius: 0px; font-size: 15px"
                            v-for="item in itemtypes"
                            :key="item.label"
                            :type="item.type"
                            size="medium"
                            effect="dark">
                        {{ item.label }}
                    </el-tag>
                </div>

                <div class="tag-group" style="margin-top: 30px; display: flex; flex-direction: row; flex-wrap: wrap;">
                    <!--<span class="tag-group__title">Dark</span>-->

                    <el-tag style="margin: 2px; border-radius: 0px; font-size: 15px"
                            v-for="item in items"
                            :key="item.label"
                            :type="item.type"
                            size="medium"
                            effect="plain">
                        {{ item.label }}
                    </el-tag>
                </div>

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
                queryURL:'http://61.135.242.193:5000/api/summarization',
                items: [
                    // { type: '', label: '标签一' },
                    // { type: 'success', label: '标签二' },
                    { type: 'info', label: '继不久前始于' },
                    { type: 'danger', label: '中国'},
                    { type: 'info', label: '的召回风波，'},
                    { type: 'success', label: '宝马'},
                    { type: 'info', label: '因为车辆的发动机故障，在'},
                    { type: 'danger', label: '全球'},
                    { type: 'info', label: '范围召回408万辆车'},
                    { type: 'success', label: '宝马'},
                    { type: 'info', label: '总裁'},
                    { type: 'warning', label: '瞿云涛'},
                    { type: 'info', label: '表示'},
                    { type: 'success', label: '宝马' },
                    { type: 'info', label: '将会对' },
                    { type: 'danger', label: '中国' },
                    { type: 'info', label: '用户' },
                    { type: 'info', label: '用户负责到底' },
                ],
                itemtypes:[
                    { label: '人名', type: 'warning' },
                    { label: '地名', type: 'danger' },
                    { label: '组织机构名', type: 'success' },
                ]

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

