<template>
    <div>
        <el-container>
            <el-header>
                <h1 style="color: gray">关系抽取</h1>
            </el-header>
            <el-main style="text-align: center">
                <span style="font-size: 15px; color: gray">
                    关系抽取能够自动识别文本中实体之间所隐含的语义关系，如人物关系、从属关系、目的关系等。
                </span>
                
                <el-row style="margin-top: 20px">
                    <el-col :span="16">
                        <el-input
                        type="textarea"
                        placeholder="请输入内容"
                        v-model="content"
                        maxlength="400"
                        show-word-limit
                        :rows=16
                        clearable
                        style="box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)"
                        >
                        </el-input>
                        
                    </el-col>
                    
                    <el-col :span="8" style="padding-left:10px">
                        
                <el-card shadow="hover">
                    <div slot="header" class="clearfix">
                        <span>人物列表</span>
                    </div>
                    
                    <el-row id="character-list" style="display: flex; justify-content: center">
                        <form>
                            <el-input
                                v-model="newPersonName"
                                id="new-person"
                                placeholder="E.g. Joe Black"
                            >
                                <p slot="prepend" >Add a person</p>
                                <el-button slot="append" @click="addNewPerson" icon="el-icon-circle-plus"></el-button>
                            </el-input>
                        </form>
                    </el-row>

                    <el-table :show-header="false" :data="personList" 
                        style="width:100%;height: 180px;max-height: 180px;overflow: auto">
                        <el-table-column min-width="200">
                            <template slot-scope="scope">
                                <div
                                    class="todo-item"
                                >{{scope.row.name}}</div>
                            </template>
                        </el-table-column>
                        <el-table-column min-width="100" align="right">
                            <template slot-scope="scope">
                                <i class="el-icon-edit"></i>
                                <el-button icon="el-icon-delete" @click="personList.splice(scope.$index, 1)"></el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </el-card>
                    </el-col>
                </el-row>
                
                <el-row style="margin-top: 30px; display: flex; justify-content: center">
                    <el-button v-on:click="getData" type="primary">开始提取</el-button>
                </el-row>
                
                <div class="tag-group" style="margin-top: 30px; display: flex; flex-direction: row; flex-wrap: wrap;">
                    <template v-for="item in items">
                        <el-tag style="margin: 2px; border-radius: 0px; font-size: 15px"
                                :key="item.person1+item.id"
                                type="warning"
                                size="medium"
                                effect="dark">
                            {{ item.person1 }}
                        </el-tag>
                        ----
                        <el-tag style="margin: 2px; border-radius: 0px; font-size: 15px"
                                :key="item.relation+item.id"
                                type="danger"
                                size="medium"
                                effect="plain">
                            {{ item.relation }}
                        </el-tag>
                        ----
                        <el-tag style="margin: 2px; border-radius: 0px; font-size: 15px"
                                :key="item.person2+item.id"
                                type="warning"
                                size="medium"
                                effect="dark">
                            {{ item.person2 }}
                        </el-tag>
                    </template>
                    
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
            content: '',
            queryURL:'http://61.135.242.193:5000/api/summarization',
            
            items: [
                // { type: '', label: '标签一' },
                // { type: 'success', label: '标签二' },
                {person1: '曹操', person2: '曹丕', relation: '父子', id:'1'}
            ],
            newPersonName: '',
            personList: [
            {
                id: 1,
                name: '赵立坚',
            },
            {
                id: 2,
                name: '埃斯珀',
            },
            
            {
                id: 3,
                name: '赵立坚2',
            },
            {
                id: 4,
                name: '埃斯珀2',
            }
            ],
            nextPersonId: 5
        };
    },
    created() {
        // this.getData();
    },
    methods: {
        // 获取 easy-mock 的模拟数据
        getData() {
            fetch(this.queryURL, {
                method: "POST",
                body: JSON.stringify({
                    docs: [{
                        "id":123,
                        "doc":this.content,
                    }],
                    "person": this.personList
                    
                }),
                headers: {
                    "Content-Type": "application/json"
                },

            }).then(res => res.json())
                .catch(error => console.error('Error:', error))
                .then(response => console.log(response.data[0].summary));
        },
        addNewPerson() {
            this.personList.push({
            id: this.nextPersonId++,
            name: this.newPersonName
            });
            this.newPersonName = '';
            console.log(this.personList);
        }

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
