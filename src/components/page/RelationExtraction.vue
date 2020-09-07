<template>
  <div>
    <el-container>
      <el-header style="height: max-content">
        <el-card
          class="noBorderInput"
          style="border: 0px; margin-top: 20px;border-radius: 0;
      background-color: #fff;
      box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
        >
          <!--<div slot="header" class="diyCardHead" >-->
          <h1
            style="color: gray; letter-spacing: 10px; font-weight: normal; font-size: 25px; margin-top: -20px"
          >关系抽取</h1>
          <!--<el-divider style="width: 30px"></el-divider>-->
          <!--</div>-->
          <!--<h1 style="color: gray">实体识别</h1>-->
          <el-input
            type="textarea"
            placeholder="请输入内容"
            v-model="content"
            maxlength="80"
            show-word-limit
            :autosize="{ minRows: 4, maxRows: 8}"
            clearable
            style="font-size: 15px"
          >
            <!--style=" font-size: 15px; margin-top: 0px;border-radius: 0;-->
            <!--background-color: #fff;-->
            <!--box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"-->
            >
          </el-input>
          <el-row style="margin-top: 17px; display: flex; justify-content: center">
            <el-button
              v-on:click="getData"
              type="primary"
              style="background: #242f42; border: 0px; font-size: 15px; letter-spacing: 5px"
            >开始提取</el-button>
            <!--<el-button v-on:click="mockData">随机样例</el-button>-->
          </el-row>
        </el-card>
      </el-header>
      <el-main
        ref="mainContainer"
        style="text-align:center;margin-top: 20px;height: 100%;padding:0 20px"
      >
        <el-row>
          <el-col :span="16">
            <el-card
              class="box-card"
              style="margin-top: 0px;border-radius: 0;background-color: #fff;
              box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
            >
              <div slot="header" class="clearfix">
                <span style="font-size: 18px">人物关系图</span>
              </div>
              <el-row>
                <div id="showRelation" :style="{width: '100%', height: '460px'}"></div>
              </el-row>
              <hr style="border:0;height:1px;background-color:#606266" />
              <el-row style="padding-top:40px">
                <div id="showRelation2" :style="{width: '100%', height: '500px'}"></div>
              </el-row>
            </el-card>
          </el-col>

          <el-col :span="8" style="padding-left:20px">
            <el-card
              class="box-card"
              style="margin-top: 0px;border-radius: 0;background-color: #fff;
              box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);"
            >
              <div slot="header" class="clearfix">
                <span style="font-size: 18px">人物关系列表</span>
              </div>
              <el-table
                :show-header="true"
                :data="items"
                style="height: 1000px;max-height: 1000px;overflow: auto"
              >
                <el-table-column prop="person1" align="center" label="人物1"></el-table-column>
                <el-table-column prop="relation" label="关系" align="center" width="50"></el-table-column>
                <el-table-column prop="person2" align="center" label="人物2"></el-table-column>
              </el-table>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
      <!--<el-footer>Footer</el-footer>-->
    </el-container>
  </div>
</template>

<script>
import { fetchData } from "../../api/index";
import echarts from "echarts/lib/echarts";
import "echarts/dist/extension/dataTool";

const typelist = [
  "夫妻",
  "亲子",
  "兄弟姐妹",
  "上下级",
  "师生",
  "好友",
  "同学",
  "合作",
  "同人",
  "情侣",
  "祖孙",
  "同门",
  "亲戚",
];

const relationUrl = "http://49.234.217.110:5000/api/relation";

function getPersonList(links) {
  var personList = [];
  var personDict = {};
  for (var i = 0; i < links.length; ++i) {
    if (personList.indexOf(links[i].person1) < 0) {
      personList.push(links[i].person1);
      personDict[links[i].person1] = 1;
    } else {
      personDict[links[i].person1] += 1;
    }
    if (personList.indexOf(links[i].person2) < 0) {
      personList.push(links[i].person2);
      personDict[links[i].person2] = 1;
    } else {
      personDict[links[i].person2] += 1;
    }
  }
  return [personList, personDict];
}

/*
洗牌节点列表
 */
function shuffle(arr) {
  for (let i = arr.length - 1; i >= 0; i--) {
    let rIndex = Math.floor(Math.random() * (i + 1));
    let temp = arr[rIndex];
    arr[rIndex] = arr[i];
    arr[i] = temp;
  }
  return arr;
}

export default {
  name: "basetable",
  data() {
    return {
      content:
        "贾政与王夫人的三个孩子分别是贾珠、贾元春和贾宝玉，贾政与赵姨娘的孩子分别是贾探春和贾环，而贾政与周姨娘并未诞下一子。（请输入文本）",
      items: [
        { person1: "贾政", person2: "王夫人", relation: "夫妻" },
        { person1: "贾政", person2: "贾珠", relation: "亲子" },
        { person1: "贾政", person2: "贾元春", relation: "亲子" },
        { person1: "贾政", person2: "贾宝玉", relation: "亲子" },
        { person1: "贾政", person2: "赵姨娘", relation: "夫妻" },
        { person1: "贾政", person2: "贾探春", relation: "亲子" },
        { person1: "贾政", person2: "贾环", relation: "亲子" },
        { person1: "贾政", person2: "周姨娘", relation: "夫妻" },
        { person1: "王夫人", person2: "贾珠", relation: "亲子" },
        { person1: "王夫人", person2: "贾元春", relation: "亲子" },
        { person1: "王夫人", person2: "贾宝玉", relation: "亲子" },
        { person1: "贾珠", person2: "贾元春", relation: "兄弟姐妹" },
        { person1: "贾珠", person2: "贾宝玉", relation: "兄弟姐妹" },
        { person1: "贾珠", person2: "贾环", relation: "兄弟姐妹" },
        { person1: "贾元春", person2: "贾宝玉", relation: "兄弟姐妹" },
        { person1: "赵姨娘", person2: "贾探春", relation: "亲子" },
        { person1: "赵姨娘", person2: "贾环", relation: "亲子" },
        { person1: "贾探春", person2: "贾环", relation: "兄弟姐妹" },
      ],
    };
  },
  created() {
    // this.getData();
  },
  methods: {
    drawArrowRelation() {
      // 初始化echarts实例
      let myChart = echarts.init(document.getElementById("showRelation"));

      var restmp = getPersonList(this.items);
      var personList = restmp[0];
      var personDict = restmp[1];

      var theData = getCircularCoordinate(this.items);
      var categories = [];
      for (var i = 0; i < 8; i++) {
        categories[i] = {
          name: "类目" + i,
        };
      }

      // 绘制图表
      var option = {
        series: [
          {
            type: "graph",
            layout: "force",
            symbolSize: 20,
            label: {
              show: true,
              fontSize: 14,
            },
            top: "60",
            bottom: "50",
            roam: true,
            //categories: categories,
            itemStyle: {
              borderColor: "#fff",
              borderWidth: 1,
              shadowBlur: 10,
              shadowColor: "rgba(0, 0, 0, 0.3)",
            },
            lineStyle: {
              color: "source",
              //curveness: 0.3,
            },
            force: {
              repulsion: 500,
              initLayout: "circular",
              gravity: 0.05,
              edgeLength: 150,
              friction: 0.8,
              focusNodeAdjacency: true,
            },
            edgeSymbol: ["", "arrow"],
            edgeLabel: {
              // 连接两个关系对象的线上的标签
              normal: {
                show: true,
                textStyle: {
                  fontSize: 14,
                },
                formatter: function (param) {
                  // 关系标签内容
                  return param.data.relation;
                },
              },
            },
            data: theData.nodes,
            links: theData.links,
          },
        ],
      };
      //防止越界，重绘canvas
      window.onresize = myChart.resize;
      myChart.setOption(option);

      function getCircularCoordinate(items) {
        var resData = { nodes: [], links: [] };
        let personNum = personList.length;
        var a = 0;

        personList.forEach(function (p) {
          resData.nodes.push({
            name: p,
            /*x: 80 * Math.cos((a * Math.PI) / 180),
            y: 80 * Math.sin((a * Math.PI) / 180),*/
            category: 1,
            label: {
              show: true,
            },
            draggable: true,
            symbolSize: p.length * 15 + 6,
          });
          a += 360 / personNum;
        });
        console.log(resData.nodes);
        items.forEach(function (item) {
          resData.links.push({
            source: personList.indexOf(item.person1),
            target: personList.indexOf(item.person2),
            relation: item.relation,
            //value:10,
            lineStyle: {
              width: 1,
            },
          });
        });
        return resData;
      }
    },
    drawCircular() {
      // 初始化echarts实例
      let myChart = echarts.init(document.getElementById("showRelation2"));

      var restmp = getPersonList(this.items);
      var personList = restmp[0];
      var personDict = restmp[1];
      restmp = getCircular(this.items);

      var categories = [];
      for (var i = 0; i < typelist.length; i++) {
        categories[i] = {
          name: typelist[i],
        };
      }
      categories[typelist.length] = {
        name: "人物",
      };

      // 绘制图表
      var option = {
        legend: [
          {
            bottom: "10",
            data: categories.map(function (a) {
              return a.name;
            }),
          },
        ],
        tooltip: {},
        animationDurationUpdate: 1500,
        animationEasingUpdate: "quinticInOut",
        series: [
          {
            top: "80",
            bottom: "150",
            name: "Les Miserables",
            type: "graph",
            layout: "circular",
            circular: {
              rotateLabel: true,
            },
            data: restmp.nodes,
            links: restmp.links,
            categories: categories,
            //roam: true,
            label: {
              position: "right",
              formatter: "{b}",
            },
            lineStyle: {
              color: "source",
              curveness: 0.3,
            },
          },
        ],
      };
      //防止越界，重绘canvas
      window.onresize = myChart.resize;
      myChart.setOption(option);

      function getCircular(items) {
        var nodeNum = typelist.length + personList.length;
        var nodelist = [];
        var nodedict = [];

        var a = 0;
        for (var i = 0; i < nodeNum; i++) {
          if (i < typelist.length) {
            var category = i;
            var name = typelist[i];
            nodedict.push(name);
          } else {
            var category = typelist.length;
            var name = personList[i - typelist.length];
            nodedict.push(name);
          }

          nodelist.push({
            id: i,
            ac: i,
            x: 20 * Math.sin((a * Math.PI) / 180),
            y: 20 * Math.cos((a * Math.PI) / 180),
            category: category,
            name: name,
          });
          a += 360 / nodeNum; // Math.sin(2*Math.PI / 360)
        }

        nodedict = shuffle(nodedict);
        var i = 0;
        nodelist.forEach(function (node) {
          var val_ = 0;
          if (personDict[nodedict[i]]) {
            val_ = personDict[nodedict[i]];
          }
          node.value = val_;
          node.name = nodedict[i];
          node.tooltip = {
            formatter: personDict[nodedict[i]]
              ? nodedict[i] + " : " + val_
              : "关系 : " + nodedict[i],
          };
          node.category =
            typelist.indexOf(nodedict[i]) < 0
              ? typelist.length
              : typelist.indexOf(nodedict[i]);
          node.symbolSize = 20 + 5 * val_; //10 * Math.log(10 + val_);
          node.label = {
            normal: {
              show: node.symbolSize > 0,
            },
          };
          i++;
        });

        var linklist = [];
        var personRelationLabel = {};
        var lineCnt = {};
        // 总结各个人物与关系，为其生成提示信息
        items.forEach(function (item) {
          var tKey = item.person1 + "-" + item.relation;
          if (personRelationLabel[tKey]) {
            lineCnt[tKey]++;
            personRelationLabel[tKey] =
              personRelationLabel[tKey] +
              "<br>" +
              item.person1 +
              "-" +
              item.relation +
              "-" +
              item.person2;
          } else {
            lineCnt[tKey] = 1;
            personRelationLabel[tKey] =
              item.person1 + "-" + item.relation + "-" + item.person2;
          }
          tKey = item.person2 + "-" + item.relation;
          if (personRelationLabel[tKey]) {
            lineCnt[tKey]++;
            personRelationLabel[tKey] =
              personRelationLabel[tKey] +
              "<br>" +
              item.person1 +
              "-" +
              item.relation +
              "-" +
              item.person2;
          } else {
            lineCnt[tKey] = 1;
            personRelationLabel[tKey] =
              item.person1 + "-" + item.relation + "-" + item.person2;
          }
        });

        var id = 0;
        // 依据关系列表生成连线
        items.forEach(function (item) {
          if (personRelationLabel[item.person1 + "-" + item.relation]) {
            id++;
            linklist.push({
              source: nodedict.indexOf(item.person1),
              target: nodedict.indexOf(item.relation),
              id: id,
              tooltip: {
                formatter:
                  personRelationLabel[item.person1 + "-" + item.relation],
              },
              lineStyle: {
                type: "solid",
                width: 1,
              },
              emphasis: {
                lineStyle: {
                  width: 2 + 2 * lineCnt[item.person1 + "-" + item.relation],
                  type: "solid",
                },
              },
            });
            delete personRelationLabel[item.person1 + "-" + item.relation];
          }
          if (personRelationLabel[item.person2 + "-" + item.relation]) {
            id++;
            linklist.push({
              target: nodedict.indexOf(item.person2),
              source: nodedict.indexOf(item.relation),
              id: id,
              tooltip: {
                formatter:
                  personRelationLabel[item.person2 + "-" + item.relation],
              },
              lineStyle: {
                type: "solid",
                width: 1,
              },
              emphasis: {
                lineStyle: {
                  width: 2 + 2 * lineCnt[item.person2 + "-" + item.relation],
                  type: "solid",
                },
              },
            });
            delete personRelationLabel[item.person2 + "-" + item.relation];
          }
        });
        return { nodes: nodelist, links: linklist };
      }
    },
    // 获取 easy-mock 的模拟数据
    getData() {
      this.items = [];
      fetch(relationUrl, {
        method: "POST",
        body: JSON.stringify({
          docs: [
            {
              id: 123,
              doc: this.content,
            },
          ],
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((res) => res.json())
        .catch((error) => {
          console.error("Error:", error);
          this.drawArrowRelation();
          this.drawCircular();
        })
        .then((response) => {
          console.log(response);
          this.items = response.results[0].result;
          this.drawArrowRelation();
          this.drawCircular();
        });
    },
  },

  mounted() {
    this.drawArrowRelation();
    this.drawCircular();
  },
};
</script>

<style scoped>
@import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
.el-header,
.el-footer {
  font-size: 20px;
  color: black;
  text-align: center;
  line-height: 60px;
}
.res-textarea {
  color: black;
  margin-top: 30px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.12), 0 0 6px rgba(0, 0, 0, 0.04);
}
</style>
