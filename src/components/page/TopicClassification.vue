<template>
    <div>
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item>文本主题分类</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="container">
            <div class="plugins-tips">
                <el-link type="primary" @click="openTips">使用帮助</el-link>
            </div>

            <div style="margin:20px 0">
                <el-row>
                    <strong style="margin-left: 10px;margin-right: 18px">文本类型</strong>
                    <el-button-group>
                        <template  v-for="type in types">
                            <el-button type="success" size="medium" :key="type" round 
                                v-if="form.type.indexOf(type)>=0" @click="onClick(type)">{{type}}</el-button>
                            <el-button type="info" size="medium" :key="type" round v-else disabled>{{type}}</el-button>
                        </template >
                    </el-button-group>
                </el-row>
            </div>

            <quill-editor ref="myTextEditor" v-model="content" :options="editorOption" @change="initType"></quill-editor>
            <el-button class="editor-btn" type="primary" @click="submit">提交</el-button>
            
        </div>
    </div>
</template>

<script>
    import 'quill/dist/quill.core.css';
    import 'quill/dist/quill.snow.css';
    import 'quill/dist/quill.bubble.css';
    import { quillEditor } from 'vue-quill-editor';
    
    const typelist = ['政治', '军事', '娱乐', '科技', '教育', '人文', 'case', 'asgdg', 'gasdwe', 'vcd', 'gagaes', 'teqryj', 'werlo'];

    export default {
        name: 'markdown',
        data: function(){
            return {
                form: {
                    type: [],
                },
                content:'',
                editorOption: {
                    placeholder: '请在这里输入待分类的文本'
                },
                types: typelist
            }
        },
        components: {
            quillEditor
        },
        methods: {
            initType(){
                this.form.type = [];
            },
            openTips() {
                this.$alert('在下方文本框中输入待分类的文本，点击提交后文本的分类结果将在下方“文本类型”后以颜色改变的形式展示。', 
                    '文本主题分类使用方法', {
                confirmButtonText: '确定',
                callback: action => {
                    /*this.$message({
                    type: 'info',
                    message: `action: ${ action }`
                    });*/
                }
                });
            },
            onClick(value){
                alert("你点击了 " + value);
            },
            onEditorChange({ editor, html, text }) {
                this.content = html;
            },
            submit(){
                console.log(this.content);
                this.form.type = ['政治', '教育'];
                this.$message.success('提交成功！');
            }
        }
    }
</script>
<style scoped>
    .editor-btn{
        margin-top: 20px;
    }
</style>