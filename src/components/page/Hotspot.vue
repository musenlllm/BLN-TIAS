<template>
    <!--<link rel="stylesheet" type="text/css" href="http://at.alicdn.com/t/font_2015036_ral7di9rm4.css">-->
    <div>
        <el-container>
            <el-header style="height: max-content;text-align: center">
              <el-card class="noBorderInput"style="border: 0px; margin-top: 15px;border-radius: 0;
      background-color: #fff;
      box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">

                <div slot="header" class="diyCardHead" style="margin-bottom: -1%;margin-top: -1.5%">
                  <h1 style="color: black; letter-spacing: 10px; font-weight: normal; font-size: 25px; "> 热点挖掘</h1>
                </div>

                <div class="diyCardBody" style="margin-top: 0px">
                  <el-row :gutter="20" >
                    <el-col :span="8">
                      <!--<el-card shadow="always" class="box-card" :body-style="{padding: '0px'}" style="min-height: 458px;font-size: 18px">-->
                      <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                        <div slot="header" class="clearfix" style="font-size: 18px;height: 30px; margin-top: -25px; margin-bottom: 20px">

                            <span style="">
                                <!--<link rel="icon" href="../../assets/icon/news.icon" type="image/x-icon">-->
                              <!--<svg class="icon" aria-hidden="true">-->
                              <!--<use xlink:href="#iconxinwen"></use>-->
                              <!--</svg>-->
                                <i class="iconfont iconxinwen"></i>
                              <!--<i class="ldmcxinwen" style="font-size: 21px;"></i>-->
                                热点新闻
                            </span>
                        </div>
                        <div class="tag-group" style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;">
                          <el-table
                            :data="this.hotspotRes.hot_event"
                            style="width: 100%; text-align: center; "
                            stripe
                            :row-class-name="tableRowClassName"
                            @sort-change="changeSort"
                            :default-sort="{prop: 'rank', order: 'ascending'}"
                            :show-overflow-tooltip=true
                            max-height="400px"
                          >
                            <el-table-column align='center'
                                             header-align="center"
                                             prop="rank"
                                             label="排序"
                                             sortable
                                             :sort-orders="['ascending', 'descending']"
                                             width="80%"
                            >

                              <div slot-scope="scope" v-if="scope.row.rank<4">

                                <i class="iconfont iconmingcheng-huobao-t"></i>
                              </div>
                              <div slot-scope="scope" v-else>
                                {{scope.row.rank}}

                              </div>
                            </el-table-column>
                            <el-table-column align='left'
                                             header-align="center"
                                             prop="event"
                                             label="新闻话题"
                                             :show-overflow-tooltip=true
                                             width="200%"
                            >
                              <template slot-scope="scope">

                                <a :href="scope.row.url" target="_blank" class="buttonText" >{{scope.row.event}}</a>
                              </template>
                            </el-table-column>
                            <el-table-column align='center'
                                             prop="popularity"
                                             label="阅读量"
                                             :show-overflow-tooltip=true
                            >
                            </el-table-column>
                          </el-table>
                        </div>
                      </el-card>
                    </el-col>
                    <el-col :span="8">
                      <!--<el-card shadow="always" :body-style="{padding: '0px'}" style="min-height: 458px;">-->
                      <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                        <div slot="header" class="clearfix" style="font-size: 18px;height: 30px;margin-top: -25px; margin-bottom: 20px">
                            <span>

                                <i class="el-icon-chat-line-square" style="font-size: 21px"></i>

                              <!--<i class="iconfont iconhuati"></i>-->
                                热点话题
                            </span>
                        </div>
                        <div class="tag-group" style=" display: flex; justify-content: center; flex-direction: row; flex-wrap: wrap;">
                          <el-table
                            :data="hotspotRes.hot_topic"
                            style="width: 100%; text-align: center;"
                            header-cell-style="font-weight:500"
                            @sort-change="changeSort"
                            :default-sort="{prop: 'rank', order: 'ascending'}"
                            :row-class-name="tableRowClassName"
                            stripe
                            :show-overflow-tooltip=true
                            max-height="400px"
                          >
                            <el-table-column align='center'
                                             prop="rank"
                                             label="排序"
                                             sortable
                                             :sort-orders="['ascending', 'descending']"
                                             width="80%">
                              <div slot-scope="scope" v-if="scope.row.rank<4">

                                <i class="iconfont iconmingcheng-huobao-t"></i>
                              </div>
                              <div slot-scope="scope" v-else>
                                {{scope.row.rank}}

                              </div>

                            </el-table-column>
                            <el-table-column align='left'
                                             header-align="center"
                                             prop="topic"
                                             label="新闻话题"
                                             :show-overflow-tooltip=true
                            >
                              <template slot-scope="scope">
                                <a :href="scope.row.url" target="_blank" class="buttonText" >{{scope.row.topic}}</a>
                              </template>
                            </el-table-column>
                            <el-table-column align='center'
                                             prop="view_number"
                                             label="阅读量"
                                             width="100%"
                            >
                            </el-table-column>
                            <!--<el-table-column-->
                            <!--prop="url"-->
                            <!--label="链接"-->
                            <!--sortable="custom">-->
                            <!--</el-table-column>-->

                            <!--{{ item.label }}-->
                          </el-table>
                        </div>
                      </el-card>
                    </el-col>
                    <el-col :span="8">
                      <!--<el-card shadow="always" :body-style="{padding: '0px'}" style="min-height: 458px;">-->
                      <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="min-height: 466px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                        <div slot="header" class="clearfix" style="font-size: 18px;height: 30px;margin-top: -25px; margin-bottom: 20px">
                                <span>
                                    <i class="iconfont iconzengchang1" ></i>
                                  <!--</div>-->
                                    最近半小时增长新闻
                                </span>
                        </div>
                        <el-table
                          :data="this.recent_half_hour_increase_news"
                          style="width: 100%; text-align: center;"
                          stripe
                          @sort-change="changeSort"
                          :default-sort="{prop: 'publish_time', order: 'descending'}"
                          :row-class-name="tableRowClassName"
                          :show-overflow-tooltip=true
                          max-height="400px"
                        >
                          <el-table-column align='left'
                                           type="index"
                                           header-align="center"
                                           prop="news"
                                           label="新闻话题"
                                           :show-overflow-tooltip=true
                                           width="220%"
                          >
                            <template slot-scope="scope" v-if="scope.row.url">
                              <i :href="scope.row.url" class="iconfont iconzuixin" ></i>
                              <a :href="scope.row.url" target="_blank" class="buttonText" >【{{scope.row.news_type}}】{{scope.row.news}}</a>
                            </template>
                          </el-table-column>
                          <el-table-column align='center'
                                           prop="publish_time"
                                           label="发布时间"
                                           sortable
                                           :sort-orders="['ascending', 'descending']"
                                           :show-overflow-tooltip=true
                          >
                            <template slot-scope="scope">
                              <span >{{scope.row.publish_time}}</span>
                            </template>
                          </el-table-column>
                        </el-table>
                      </el-card>
                    </el-col>
                  </el-row>
                </div>
              </el-card>
            </el-header>
            <el-main  style="margin-left: 0px; margin-top: -30px; text-align: center">

                <!--<el-card class="box-card" style="min-height:200px; margin-top: 20px;text-align: center">-->
                <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                    <el-tabs type="card" v-model="activeName" @tab-click="handleClick" style="border: 0px;border-radius: 0">
                        <el-tab-pane label="今日" name="first">

                            <div class="wrap" v-if="isChildUpdate1" style="display: flex; justify-content: space-around">
                                <div id = "hot_key_words1" style="width:30%;min-height:400px;" ></div>
                                <div id="hot_freq_words1" style="width:30%;height:400px;"></div>
                                <div id="today_hot_distribution1" style="width:30%;height:400px;"></div>


                                <!--<div>{{this.freq_words2_list}}</div>-->
                            </div>
                        </el-tab-pane>
                        <el-tab-pane label="近七日" name="third">
                            <div class="wrap" v-if="isChildUpdate3" style="display: flex; justify-content: space-around">
                                <div id = "hot_key_words3" style="width:30%;min-height:400px;" ></div>
                                <div id = "hot_freq_words3" style="width:30%;min-height:400px;" ></div>
                                <div id="today_hot_distribution3" style="width:30%;height:400px;"></div>
                                <!--<div>{{this.key_words2_list}}</div>-->
                            </div>
                        </el-tab-pane>
                    </el-tabs>

                </el-card>
            <!--</el-main>-->
            <!--<el-main style="text-align: center; margin-top: 10px; ">-->
                <!--<el-card class="box-card" style="min-height: 400px;margin-top: 20px;text-align: center">-->
                <!--<el-card class="noBorderInput" :body-style="{padding: '0px'}" style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">-->
                    <!--<div slot="header" class="clearfix" style="font-size: 18px">-->
                        <!--<span>新闻主题分布图</span>-->
                    <!--</div>-->
                    <!--<div id="today_hot_distribution" style="width:100%;height:600px;"></div>-->
                    <!--<div id="week_hot_distribution" style="width:100%;height:600px;">近七日</div>-->
                  <!--&lt;!&ndash;{{this.recent_half_hour_increase_news}}&ndash;&gt;-->
                  <!--&lt;!&ndash;{{this.nearly_one_week_news_dis}}&ndash;&gt;-->
                  <!--&lt;!&ndash;{{this.nearly_three_days_news_dis}}&ndash;&gt;-->
                  <!--&lt;!&ndash;{{this.today_news_dis}}&ndash;&gt;-->
                <!--</el-card>-->
                <!--<el-card class="box-card" style="min-height: 50px; margin-top: 20px">-->
                <el-card class="noBorderInput" :body-style="{padding: '0px'}" style="text-align: center;margin-top: 30px;min-height: 200px;border: 0px;border-radius: 0;background-color: #fff;box-shadow: 0 0px 0px 0 rgba(0,0,0,.1);">
                    <div slot="header" class="clearfix" style="font-size: 18px">
                        <span>近7日各主题新闻的每天增长数</span>
                    </div>
                    <!--折线图-->
                  <div class="wrap">
                    <div id="hot_trend_test" style="width:50%;min-height: 600px;"></div>
                    <div id="hot_trend" style="width:50%;min-height: 600px;"></div>
                  </div>

                    <!--<div>{{this.hot_statistics}}</div>-->
                </el-card>
            </el-main>

        </el-container>
    </div>
</template>
<script>
import echarts from 'echarts'
import { fetchData } from '../../api/index';
// import resize from "./mixins/resize";
import "echarts-wordcloud/dist/echarts-wordcloud";
import "echarts-wordcloud/dist/echarts-wordcloud.min";
const hotspoturl = "http://49.234.217.110:5000/api/hotspot";

export default {
    name: 'basetable',
    data() {
      return {
        hotspotRes: {},
        items: [],
        // 柱状图
        charts: "",
        view_number: "",
        hot_event: [],
        hot_topic: [],
        freq_words: [],
        freq_words_list: [],
        freq_words1_list: [],
        freq_words2_list: [],
        freq_words3_list: [],
        key_words: [],
        key_words_list: [],
        key_words1_list: [],
        key_words2_list: [],
        entData: [],
        activeName: 'third',
        isChildUpdate1: false,
        isChildUpdate2: false,
        isChildUpdate3: true,
        recent_half_hour_increase_news: [],
        test: {"name": "Liza", "password": "123"},
        hot_statistics: {},
        today_news_distribution: {},
        today_news_dis: [],
        nearly_three_days_news_distribution: {},
        nearly_three_days_news_dis: [],
        nearly_one_week_news_distribution: {},
        nearly_one_week_news_dis: [],

        one_week_time: [],
        news_info: [],
        dataTrend:{},
// <<<<<<< Updated upstream
        name: ["国内", "世界", "体育", "社会", "历史", "娱乐",
          "军事", "政府", "教育", "经济", "评论", "其他"],
        source: [['topic', '今日', '近七日'], ['评论'], ['国内'], ['教育'], ['娱乐'], ['经济'], ['政府'],
          ['历史'], ['军事'], ['其他'], ['社会'], ['体育'], ['世界']],

        //高频词的热力图数据
        heatmap_x_axis: [],
        today_freq_heat_data: [],
        one_week_freq_heat_data: [],
        heatmap: '',
        image1: "data:image/png;base64,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",

// =======
//             name:["Domestic国内","World世界","Sports体育","Society社会","History历史","Entertainment娱乐",
//                         "Military军事","Government政府","Education教育","Finance经济","Comment评论","Other其他"],
//             source:[['topic','今日','近七日'],['Comment评论'],['Domestic国内'], ['Education教育'], ['Entertainment娱乐'], ['Finance经济'],['Government政府'],
//               ['History历史'], ['Military军事'], ['Other其他'], ['Society社会'], ['Sports体育'], ['World世界']],
        image2:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAMy0lEQVR4Xu2deZAU1R3HP697jh1AJVxRjC6lohHvmMOgKY0aUQNCjMZjjUdU4kU4hN2d1ZiKlezschSgUaMoKgJlCRTGECNRPFIaSzSSKChGq8SLCN4Cy+zMdL9UL0tclj26Z97rnZ15+++89/393vf32dfdr7tfCymljfkrWweEAaBsa98ycANAedffAFDm9TcAGADMSWBZM2DOAcq6/OYksMzLbwAwAJh1gPJmwJwDlHf9zWVgmdffAGAAMOsAZc2AOQfoBeVPzGBkJsepXqpOkptVpmwAUOmmIq2BszhkS5aTcy4/lHASMGCntBAsve5oLrrlDHIqwhkAVLioSKPfbEY0pZknJd/rSlLAn360H1Urf0660NAGgEIdVNR/2ByGvNPEE8AIP5JC8OhR+1C15lK2+GnfWRsDQCHuKewbTTExJ5kVRFLA4wfuQdWbE/g0SL+2bQ0A+TqnuJ+V4nkp+U5QWSF4av+BVG0Yz+agfb32BoB8XFPcJ97AuIzL0nxlBTy7d1+qNk7kg6AaBoCgjmlob6V4UErOKURawAuDo1RtmsaGIDoGgCBuaWjbdzrHNOV4UYW0EPxzYB+qPprIW371DAB+ndLUzk4x05VMUiUv4JW+Maq2TOV1P5oGAD8uaWoz/FYGvLUlv5O3blJ6LyqYaQvWtm1nxfhs2xRe6RVXARXTOTnrcIKXrOrlT031DCwbbWBSzmVm4I4FdBDw8lF9OGXNpB3rB0U1A8QbOCsH41yXs4D+O8cZtflVpobbCxh3UXYVKTYg+UbYyVVYnLK9lmd6HIAT5tNn9SbG5SRjJYwC+nVkhhC86iY5JmyjdMaLN3BOxuVBnTE60+5RALwlz41pxuYko6RsKXrCjwlDK9j/gyls9NO2N7Sx6nlWwnGh5ypYL5McvjNuKIeAITM44HOHUW2KHg068HiUMelp/DVov2JtL+rV3M0LOr6oxZRMLbeEAoA3zWVdLmmd3q2gybZtH7G4MVtLQyEaxdTXqme1hG+FndOYI+n7yGiatQOQaODEtMsqVQMUsMSt4wJVej2tc/g97PX6Zm51JReGlYtlcZ9TyxVt42k7BNgp5rmSyxQO7k1Zx6EK9YpCykqxVErGhZFMIsbIpqmsDgUAUc864BCVAxucYPjmybytUrOntewUN7mSm3TnIQRr3OTudxu1zAB9Z3F0UzMvqR5UVDAxk+Q21bo9qRcWAJbg5o4W1LQAEEtxbVYyV4Ox7/WJcPa2atZo0A5Vcuhc9t3URLUruTaMwKECYKdY5ErO0zSwdFQwPpNksSZ97bKxRsZnHaqBYdqDtQbwloDdOr7bPp6WGUDUtxyn99M5OMsi5dTya50xVGsnGjm+2aFawo9Va/vRi9mMa65hhdaTwNh0Ls7mmO8noULbCMHDQ/sx4f0J/LdQLZ39D72N/v/5smW69/7re+zPEix2klysDIBRD1Dx0mYqt7kMc10qHZcRruR04KAQR/lGPMKEdDVPhhjTd6hYI1U5l2opOcx3J00NLcEdTpIJgQDYbzZ7f5Kh0oFhrqTSdRkmoVLuOH5VAhWa8g0kW2x3DL0roXSm5b/+Z4EGoq/xa30TnL91Mq/5AuDrs6n8ON1yjXqJvpzUKltw+8Ujuf7ek8iqVfavdtnTRBe+QHVux0leX/89tbbssPhexE5PAsO6PlU9bCF4MhFnavsnX1TH6UjPe7o360337H62HUb8TmJ0WvwuAbDqWSXhxB5MvJDQm6I2qT0jrPz4et4sRMhP30HTOfgzh2mKl779hO6uTZfFL2UA/m+MEPzNhpV7xXhUBwzRFJNzO87uB3dXjZB/77b4ZQHALic8gidtwWNfi7O80HsKFY2cltlxdu+9vVtsf76KX3YA7AIDPGMLHh0YZcmHU3nXbwXDXsL1m1ebdr6L391J4G2u5Jd5JNDrunivVtmC5UPiLOnqsbOeWMINaGag4ncJQLyR0RmHhwMm0OubC3guInhoaIIlGybteGa/p5dwEXwYEcyJwIsZyRmuZGoHRgcufpcAeD9aKR6WktG9vqp5DkDAM1JQiQzvpk37VAWs7GNTs7Xmq5c8Wmeito/J51X8bgGoaOTMZodH8vTPdCvQAcui0anlho5kvHsuuRxjbIsX43FWtF/h8xu627uB5T4L+DVScbsvYxZXNdfykGLd3eS6BaDPDI7bnuVZ3YkY/a8c6BPn29uu519heNItAC3nAvUskzA2jITKPYYluMdJhnf15QuAQXM4+JOmXe8ilXuhdI1fCB5zk+GdePsCoHUW6M33BnTVS4tuzOL85tr8t4wJkpQBIIhbIbYNCwIDQIhFDRoqDAgMAEGrEnJ73RAYAEIuaB7hNsk69s2jn68uBgBfNvVso74Jjsx3pa+7zA0A3TnUw7939kKHqrQMAKqc1KQTtbg6U8s8TfL+N4nq5c8I6vJPt+6nso4hOoOYGUCnuwVqC1jt1jGyQJkuu/sGwE5xT296R0CnaWFqnzScPZ46l+26YvoGQPWWL7oGVGq6ut948g2AZ2xFI6c2O9wL7FNqRhfreDrb2UNVvoEA8IL2m8lhTVnuk7K0Nm5UZagOnT5Rjt02jX/r0A4MgJfEAXMZtKGJ+VJypo6kjOauDliCPzhJdTuKt1XPC4CdAnY9d7nwC1Mw7Q5slXVf7Z2sMlpBAHiJ2A381nU7fnBRZaLlrhWzuaC5hiWqfSgYAC+hWANXZ11uVZ2c0fvKAe8dRzep/pCrBAAvzXgDZ2fclq1hOtzx2xSzcAeG9mf/D65Ru2G2MgC84SVmcXy6mbuB4YUP1yi0dyAi+E02ye9VOqMUAC+xQbMY/mkzd0n4gcpEjVaLA2/LOrX/XMoB8LI88g72XPsZd0o41xROrQMVEU7dXs3TqlS1APD/y8QUc1zJdaqSNTpgCRY5SXX7NmkFwCtYtIG6nKv2m/flDsKlI0mo2ghLOwCtl4mXZ13uLPfCqRp/1OaaTA13qdALBQAv0cFzOeiLNKc7LgO6S9x7Jb0nvqbRXV7F8nuvBCCoedEGbsxJbkAS+PtCQWP1tvZxm9PTNTyhIu/QZoB8kk008v1mhxtbvzmUj0TJ9RHwZ7eOn6gaWFEDsHOQ0Qam5FxuBPZsN/AvhGCtkKyzbdbaknUOfDPrltZHJdqOOW4zOl3DY2UFgDdYb+/dbJZjpaS/bbFuQD/WbryW9zsywm5glusyUZVJxaIjYLlbp3ZtpVfMAEELUKqPr8WjnJGexuNB/eiqvQFApZsatYRgqZvkfNUhDACqHdWkF49wmo5vIhgANBVMpawleNBJcpFKzZ1aBgAdrirWrIhw8vZq/q5YtkWuJAFo3cF7hg7DwtZUffOnff4lCYBVz19KZfGowubE7TU8pwu8kgOgopHTm51dP42myzzdupbgfifJ5TrjlBwA8emMzeRYptO0sLQTFRzfNIUXdMYrOQC8b/St/6LFtAN1Gqdb24L5Th3jdccpOQA8w+LTGZPJsVy3eTr1EzGOa5qq/gPcZXES6A0y2kBtzuV3OoukS7urXcJVxyzJGWCnSXaKBa7kQtWmadTbYlkscmrDe46ypAFoeTr5c56SkqM0Fq1wacH6iMWiATEWb5rMO4UL+lcoaQA8G7yHStIuT/p+skiy2bL4o/dZXCk5Quejad5HLiM2C686gsW3nEHOf9nUtSx5ADyrYo1ckXVaitrpn4BVUZu727+AGWvgypzLlSpBsGBhNMoD6WmsUlfK/JTKAgDPGjvFbFfu+uVs4D1LsCwR4f6t03i1KwsVgJCxBHP6V7Dgk8msz69c6nuVDQCtEHifwjtPwPMRwbKrjmZh0Km39Vs91/meEQQbojD7sH1YsOZStvgtofdQy/ZanvHbPt92ZQVAviZ11C/eyE+zDjWdgSDgH9EIs5urg61HxBqpyjlM9HQtwTwnydUq826vZQAo0F3v3kPGoVbCCZ6UgCUVNnOaaoIt4XZ2iBmS4ECdVwYGgAIBUNG9q2cYLcFMJ0mtijgdaRgAdDkbQNe7f/HGl6zqaL3C+3ilW8cpAeQCNTUABLJLX+N+sxnRnGaMkGxBsFVYbBOwLRLjXV1bxbccsqSUtr5hGeVid8AAkEeF7BQ3te9WEWPFtut5OQ+5Hu1iAAhov1d8V+4OgO5jdcA0fTc3APi2akfDTgD4MmqRzNT2vj0QDAAFAODt3RcRLNl3T1a8fQ0fBZQqiuYGgDzK4M0Cg/qxYNMENuTRvai6GACKqhzhJ2MACN/zoopoACiqcoSfjAEgfM+LKqIBoKjKEX4yBoDwPS+qiAaAoipH+MkYAML3vKgiGgCKqhzhJ2MACN/zoopoACiqcoSfjAEgfM+LKqIBoKjKEX4yBoDwPS+qiP8DVtEozCptLdcAAAAASUVORK5CYII=",
        image3:"data:image/png;base64,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",
        image4:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABU0lEQVQ4T6WTsUsCYRjGf9/daXfnFu1N1RoFESQJLf0DBU39Bw5KChY0OHgStdTQ1iAELo2NDhYZtBXhEm0RlNGUnEl3X5yinJJ60jd9vB/83ud93ucTUkqVfxwxLmD5nMjjO9NfCape37EBSo47CQt6iFU7RaUHED5g23FYUVVummkK/ZMZeWINl1KnLqDcBfgfFUHWyZDtB5iHLNlNKp16WGNT6JZc+3Y5kjALmH66oZOoJ3mInmHevrHjSvZ90GrEYKulQOT4GbKIDwEvEuZbpkHZNIh7d8/IFkDJUZIQC7pNuYvWVeoBJvJsNF2KQQFmiMV6ivueNY4DUQTHTobkwByoVtusPtO6AhXBqZNp+zAwSEMU1aZ0orUkzyOTqFgUBbxKyZyEdQEXYY1CI81lj4mjzAtZ7Gkq13aaK288f8gC/YWZEyaf4nz+1SgQYJjCXzBWkv34rjyaAAAAAElFTkSuQmCC",
      }
    },
    created() {
    },
    mounted() {
        // this.WordCloud('hot_freq_words');
        this.drawTest('hot_trend_test');
        this.ResultofHospot();
        this.init()
    },
    methods: {

        handleClick(tab) {
              if(tab.name == "first") {
                  this.isChildUpdate1 = true;
                  this.getHotTopic("today_hot_distribution1",this.today_news_distribution,'今日新闻主题分类')
                  this.getKeyWords("hot_key_words1",this.key_words.today,'今日新闻高影响力词分布词云');
                  this.getFreqWords("hot_freq_words1",this.freq_words.today,'今日新闻高频词分布');
                  // this.isChildUpdate2 = false;
                  this.isChildUpdate3 = false;
              } else if(tab.name == "third") {
                  this.isChildUpdate1 = false;
                  // this.isChildUpdate2 = false;
                  this.isChildUpdate3 = true;
                  this.getHotTopic("today_hot_distribution3",this.nearly_one_week_news_distribution,'近七日新闻主题分类')
                  this.getKeyWords("hot_key_words3",this.key_words.nearly_one_week,'近七日新闻高影响力词分布词云');
                  this.getFreqWords("hot_freq_words3",this.freq_words.nearly_one_week,'近七日新闻高频词分布');
              }
          },
          // 获取高频词列表
        getFreqWords(id,freq_words,title){
              for(let i = 0; i < 100; i++){
                  let obj = {};
                  obj.name = freq_words[i].word;
                  obj.value = freq_words[i].frequency;
                  this.freq_words_list[i] = obj;
              }
              this.$nextTick(() => {
                  this.drawRose(id,this.freq_words_list,title);

              })

          },
          // 获取关键词列表
        getKeyWords(id,key_words,title){
              for(let i = 0; i < 100; i++){
                  let obj = {};
                  obj.name = key_words[i].word;
                  obj.value = key_words[i].influence;
                  this.key_words_list[i] = obj;
              }
              this.$nextTick(() => {
                  this.WordCloud(id,this.key_words_list,title);
              })

          },
        getHotTopic(id,today_news_distribution,title){
          this.$nextTick(() => {
            this.drawDistribution(id,today_news_distribution,title);
          })
        },
        //玫瑰图
        drawRose(id,data,title){
            data = data.slice(0,20);
          // 基于准备好的dom，初始化echarts实例
          this.chart = echarts.init(document.getElementById(id));
          // 指定图表的配置项和数据
          var option = {
            title: {
              text: title,
              x: "center",
              top:'1%',//各个方向的内边距，默认是5，可以自行设置
              textStyle:{//标题内容的样式
                fontStyle:'normal',//主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
                fontWeight:"normal",//可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
                fontSize:15//主题文字字体大小，默认为18px

              },
              left: 'center'
            },
            tooltip: {
              trigger: 'item',
              formatter: '{a} <br/>{b} : {c} ({d}%)'
            },

            series: [

              {
                name: '面积模式',
                type: 'pie',
                radius: [30, 110],
                roseType: 'area',
                data: data,
              }
            ]
          }
          this.chart.setOption(option);
          // window.addEventListener("resize", function() {
          //   this.chart.resize()
          // })
          // setTimeout(function () {
          //     var width = $('#aside').width();
          //     if(width=='100'|| width=='60'){ //一定要加定时器，然后判断宽度是展开或者收起的时候再去调用echarts提供的resize()方法
          //         this.chart.resize();
          //     }
          //  },200);
          // window.addEventListener("resize", function() {
          //   this.chart.resize();
          // });
        },
         //词云
        WordCloud(id,words,title) {
            this.chart = echarts.init(document.getElementById(id));
            var maskImage = new Image();
            maskImage.src = this.image2;
            var option = {
                colorArr:['#fda67e', '#81cacc', '#cca8ba', "#88cc81", "#82a0c5", '#fddb7e', '#735BA1', '#bda29a', '#6e7074', '#546570', '#c4ccd3'],
                title: {
                    text: title,
                    x: "center",
                    padding:9,
                    top:'0%',//各个方向的内边距，默认是5，可以自行设置
                    textStyle:{//标题内容的样式
                        fontStyle:'normal',//主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
                        fontWeight:"normal",//可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
                        fontSize:15//主题文字字体大小，默认为18px
                      },

                },
                tooltip: {
                    trigger: 'item',
                },
                backgroundColor: "#fff",
                grid:{
                    left:'',
                    right:'0%',
                    bottom:'5%',
                    top:'19%',
                    containLabel:true
                },

                series: [{
                    type: "wordCloud",
                    //用来调整词之间的距离
                    gridSize: 0,
                    //用来调整字的大小范围
                    // Text size range which the value in data will be mapped to.
                    // Default to have minimum 12px and maximum 60px size.
                    sizeRange: [9, 30],
                    // Text rotation range and step in degree. Text will be rotated randomly in range [-90,                                                                             90] by rotationStep 45
                    //用来调整词的旋转方向，，[0,0]--代表着没有角度，也就是词为水平方向，需要设置角度参考注释内容
                    rotationRange: [-40, 0, 45, 90],
                    // rotationRange: [ 0,90],
                    // rotationRange: [0, 0],
                    //随机生成字体颜色
                    maskImage: maskImage,
                    textStyle: {
                      normal: {
                        color: function() {
                            var colorArr = ['#7db5e2', '#81cacc', '#cca8ba', "#7EBF50", "#82a0c5", '#fddb7e', '#bda29a', '#d2a59a', '#909399', '#c4ccd3','#67C23A'];
                            var flag = parseInt(Math.random() * 10);
                            return (colorArr[flag]);
                        }
                      }
                    },
                    //位置相关设置
                    // Folllowing left/top/width/height/right/bottom are used for positioning the word cloud
                    // Default to be put in the center and has 75% x 80% size.
                    left: "center",
                    top: "center",
                    right: null,
                    bottom: null,
                    width: "90%",
                    height: "90%",
                    //数据
                    // data: words.slice(0,words.length-40),
                    data:words
                  }
                ]
            };
            this.chart.setOption(option);
            // window.addEventListener("resize", function() {
            //   this.chart.resize()
            // })

        },
        // 获取热点挖掘的数据
        ResultofHospot(){
            fetch(hotspoturl, {
                method: "POST",
                body: JSON.stringify({
                  // docs: [{
                  //       "id":0,
                  //       "doc":this.summaryText,
                  // }]
                }),
                headers: {
                  "Content-Type": "application/json",
                },
            })
            .then((res) => res.json())
            .catch((error) => console.error("Error:", error))
            .then((response) => {
                this.hotspotRes = response.results;
                // console.log("success")
                // this.hot_event = hotspotRes.hot_event;
                // this.hot_topic = hotspotRes.hot_topic;
                // this.hot_freq_words = hotspotRes.hot_freq_words;
                // this.hot_key_words = hotspotRes.hot_key_words;
                // this.hot_statistics = hotspotRes.hot_statistics;
                this.recent_half_hour_increase_news = this.hotspotRes.hot_statistics.recent_half_hour_increase_news;

                this.today_news_distribution = this.hotspotRes.hot_statistics.today_news_distribution;
                console.log("success3")
                this.today_news_dis = Object.values(this.today_news_distribution);
                console.log("success5")
                this.nearly_one_week_news_distribution = this.hotspotRes.hot_statistics.nearly_one_week_news_distribution;
                this.nearly_one_week_news_dis = Object.values(this.nearly_one_week_news_distribution);

                /****Part 2****/
                //词云
                this.key_words = this.hotspotRes.hot_key_words;
                // var key_words1 = this.key_words.today;
                // var key_words2 = this.key_words.nearly_three_days;
                var key_words3 = this.key_words.nearly_one_week;
                // this.getKeyWords("hot_key_words1",key_words1,'今日新闻高影响力词分布词云');
                // this.getKeyWords("hot_key_words2",key_words2,'近三日新闻高影响力词分布词云');
                // setTimeout(()=>{
                //     this.getKeyWords("hot_key_words3",this.key_words.nearly_one_week,'近七日新闻高影响力词分布词云');
                //     // this.drawDistribution("today_hot_distribution",this.nearly_one_week_news_dis,'近七日');
                // })
                console.log("success draw ciyun")
                this.getKeyWords("hot_key_words3",key_words3,'近七日新闻高影响力词分布词云');
                //玫瑰图
                this.freq_words = this.hotspotRes.hot_freq_words;
                // var freq_words1 = this.freq_words.today;
                // var freq_words2 = this.freq_words.nearly_three_days;
                var freq_words3 = this.freq_words.nearly_one_week;
                // this.getFreqWords("hot_freq_words1",freq_words1,'今日新闻高频词分布词云');
                // this.getFreqWords("hot_freq_words2",freq_words2,'近三日新闻高频词分布词云');
                this.getFreqWords("hot_freq_words3",freq_words3,'近七日新闻高频词分布');
                //近七天的话题柱状图
                this.getHotTopic("today_hot_distribution3",this.nearly_one_week_news_distribution,'近七日新闻主题分类')
                // //获取高频词热力图所需要的数据
                // var today_freq_heat = this.hotspotRes.hot_freq_words.today;
                // //测试接受数据是否正确
                // for(let i=0;i<10;i++){
                //   this.today_freq_heat_data.push({
                //     'name':today_freq_heat[i].word,
                //     'value':today_freq_heat[i].frequency
                //   });
                // }
                //柱状图
                var i = 1

                for(i;i < 13;i++){
                     this.source[i].push(this.today_news_dis[i-1]);
                       // .push(this.nearly_three_days_news_dis[i-1]).push(this.nearly_one_week_news_dis[i-1])
                     this.source[i].push(this.nearly_one_week_news_dis[i-1]);
                     console.log(i)
                     // this.source = a.concat(b);
                }
                // setTimeout(()=>{
                //     this.drawDistribution("today_hot_distribution",this.today_news_distribution,'今日');
                //     // this.drawDistribution("today_hot_distribution",this.nearly_one_week_news_dis,'近七日');
                // })
                console.log("success")
                //折线图
                this.hot_statistics = this.hotspotRes.hot_statistics;
                this.news_info[0] = {
                    name: '国内',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.domestic_trend
                },
                this.news_info[1] = {
                    name: '世界',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.world_trend
                },
                this.news_info[2] = {
                    name: '体育',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    // data: this.hot_statistics.sports_trend.map((item, index, arr)=> item * -1 )
                    data: this.hot_statistics.sports_trend
                },
                this.news_info[3] = {
                    name: '社会',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.society_trend
                },
                this.news_info[4] = {
                    name: '历史',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    // data: this.hot_statistics.history_trend.map((item, index, arr)=> item * -1 )
                    data: this.hot_statistics.history_trend
                },
                this.news_info[5] = {
                    name: '娱乐',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    // data: this.hot_statistics.entertainment_trend.map((item, index, arr)=> item * -1 )
                    data: this.hot_statistics.entertainment_trend
                },
                this.news_info[6] = {
                    name: '军事',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    // data: this.hot_statistics.military_trend.map((item, index, arr)=> item * -1 )
                    data: this.hot_statistics.military_trend
                },
                this.news_info[7] = {
                    name: '政府',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    // data: this.hot_statistics.government_trend.map((item, index, arr)=> item * -1 )
                    data: this.hot_statistics.government_trend
                },
                this.news_info[8] = {
                    name: '教育',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    // data: this.hot_statistics.education_trend.map((item, index, arr)=> item * -1 )
                    data: this.hot_statistics.education_trend
                },
                this.news_info[9] = {
                    name: '经济',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.finance_trend
                },
                this.news_info[10] = {
                    name: '评论',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    // data: this.hot_statistics.comment_trend.map((item, index, arr)=> item * -1 )
                    data: this.hot_statistics.comment_trend
                },
                this.news_info[11] = {
                    name: '其他',
                    type: 'bar',
                    stack: '总量',
                    // label: {
                    //     show: true,
                    //     position: 'right'
                    // },
                    data: this.hot_statistics.other_trend
                },

                this.getDay();
                for(let i=0;i<7;i++)
                {
                  let key = this.one_week_time[i];
                  this.dataTrend[key]=[this.hot_statistics.domestic_trend[i],this.hot_statistics.world_trend[i],
                                      this.hot_statistics.sports_trend[i],this.hot_statistics.society_trend[i],
                                      this.hot_statistics.history_trend[i],this.hot_statistics.entertainment_trend[i],
                                      this.hot_statistics.military_trend[i],this.hot_statistics.government_trend[i],
                                      this.hot_statistics.education_trend[i],this.hot_statistics.finance_trend[i],
                                      this.hot_statistics.comment_trend[i],this.hot_statistics.other_trend[i]];
                }
                // console.log("data formatter suc:",this.dataTrend)
                this.drawTest('hot_trend_test',this.one_week_time.reverse(),this.news_info);
                this.drawDTrend("hot_trend",this.one_week_time,this.news_info);
            })
        },

        //场景分布柱状图
        drawDistribution(id,data1,date) {
            // 基于准备好的dom，初始化echarts实例
            this.chart = echarts.init(document.getElementById(id));
            // 指定图表的配置项和数据
            var option1 = {
              title: {
                text: date,
                x: "center",
                padding:9,
                top:'0%',//各个方向的内边距，默认是5，可以自行设置
                textStyle:{//标题内容的样式
                  fontStyle:'normal',//主标题文字字体风格，默认normal，有italic(斜体),oblique(斜体)
                  fontWeight:"normal",//可选normal(正常)，bold(加粗)，bolder(加粗)，lighter(变细)，100|200|300|400|500...
                  fontSize:15//主题文字字体大小，默认为18px
                },

              },
              color: ['#3398DB'],
              tooltip: {
                trigger: 'axis',
                axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                  type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                }
              },
              dataset: {
                source: this.source
              },
              grid: {
                left: '3%',
                right: '4%',
                bottom: '10%',
                containLabel: true
              },
              xAxis: [
                {
                  type: 'value',
                }

              ],
              yAxis: [
                {
                  type: 'category',
                  name: '主题',
                  nameTextStyle:{
                    fontSize:'10',
                  },
                  axisLabel: {
                    interval:0,
                    fontSize:'10',
                    fontFamily:'微软雅黑',
                  },
                  data:['评论', '国内', '教育', '娱乐', '经济','政府', '历史', '军事', '其他', '社会', '体育', '世界'],

                  axisTick: {
                    alignWithLabel: true
                  }
                }
              ],
              series: [
                {
                  name: date,
                  type: "bar",
                  data: Object.values(data1),
                  // name: '直接访问',
                  // type: 'bar',
                  barWidth: '60%',
                  // data: [10, 52, 200, 334, 390, 330, 220]
                }
              ]
            }
            var option = {
                // color:['#E47470','#7EBF50','#589EF8'],
                // color:['rgb(210,100,93)','rgb(228,116,79)','rgb(242,176,110)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'],
                color:['rgb(227,158,156)','rgb(224,108,146)','rgb(197,151,212)','rgb(175,159,215)','rgb(160,169,214)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,144,173)','rgb(126,180,225)'].reverse(),
                // tooltip: {
                //     trigger: 'axis',
                //     axisPointer: {
                //         type: 'shadow'
                //     }
                // },
                title: {
                    text: '今日主题分布图',
                    textAlign: "center",
                    left:'50%',//各个方向的内边距，默认是5，可以自行设置
                },
                dataset: {
                    source: this.source
                },
                // grid:{
                //     top:'10%',
                //     // left:'5%',
                //     right:'0%',
                //     bottom:'10%',
                //     // containLabel:true
                // },
                legend: {
                  data:this.source[0],
                    // data: [
                    //     {
                    //         name: '今日',
                    //         icon: '',
                    //         textStyle: {
                    //           fontSize:15,
                    //           // color: 'red',  // 单独设置某一个图列的颜色
                    //           // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
                    //         }
                    //     },
                    //     {
                    //         name: '近三日',
                    //         icon: '',
                    //         textStyle: {
                    //           fontSize:15,
                    //           // color: 'red',  // 单独设置某一个图列的颜色
                    //           // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
                    //         }
                    //     },
                    //     {
                    //         name: '近七日',
                    //         icon: '',
                    //         textStyle: {
                    //           fontSize:15,
                    //           // color: 'red',  // 单独设置某一个图列的颜色
                    //           // backgroundColor: '#fff' // 单独设置某一个图列的字体背景色
                    //         }
                    //     },
                    // ],
                    // textStyle: {
                    //
                    //     fontSize:15
                    // },
                    // right: 100,
                },

                yAxis: {
                    type: 'category',
                    name: '主题',
                    nameTextStyle:{
                        fontSize:'10',
                    },
                    axisLabel: {
                        interval:0,
                        fontSize:'10',
                        fontFamily:'微软雅黑',
                    },
                    data:['评论', '国内', '教育', '娱乐', '经济','政府', '历史', '军事', '其他', '社会', '体育', '世界']
                },
                xAxis: {
                    type: 'value',
                    name: '数量',
                    nameTextStyle:{
                        fontSize:'10',
                    },
                    axisLabel: {
                        fontSize:'10',
                        fontFamily:'微软雅黑',
                        marginTop:'35px',
                        show:true,
                    },
                },
                series: [
                    {
                        name: date,
                        type: "bar",
                        data: Object.values(data1),
                    },
                ]
            };
            // this.chart.on('updateAxisPointer', function (event) {
            //     var xAxisInfo = event.axesInfo[0];
            //     if (xAxisInfo) {
            //         var dimension = xAxisInfo.value + 1;
            //         this.chart.setOption({
            //             series: {
            //                 id: 'pie',
            //                 label: {
            //                     formatter: '{b}: {@[' + dimension + ']} ({d}%)'
            //                 },
            //                 encode: {
            //                     value: dimension,
            //                     tooltip: dimension
            //                 }
            //             }
            //         });
            //     }
            // });
            this.chart.setOption(option1);
            // window.addEventListener("resize", function() {
            //   this.chart.resize()
            // })
            // setTimeout(function () {
            //     var width = $('#aside').width();
            //     if(width=='100'|| width=='60'){ //一定要加定时器，然后判断宽度是展开或者收起的时候再去调用echarts提供的resize()方法
            //         this.chart.resize();
            //     }
            //  },200);
             window.addEventListener("resize", function() {
                this.chart.resize();
            });
        },
        //获取近七日日期 step_1
        getBeforeDate(n) {
            var n = n;
            var d = new Date();
            var year = d.getFullYear();
            var mon = d.getMonth() + 1;
            var day = d.getDate();
            if(day >= n) {
                if(mon > 1) {
                    mon = mon - 1;
                } else {
                    year = year - 1;
                    mon = 12;
                }
            }
            d.setDate(d.getDate() + n); //很重要，+n取得是前一天的时间
            year = d.getFullYear();
            mon = d.getMonth() + 1;
            day = d.getDate();
            var s = (mon < 10 ? ('0' + mon) : mon) + "-" + (day < 10 ? ('0' + day) : day);
            return s;
        },
        //获取近七日日期 step_2
        getDay(){
            for(var i = 0; i > -7; i--){
                this.one_week_time.push(this.getBeforeDate(i));
            }
        },
        //近七日主题新闻每日增长数
        drawTrend(id,date_arr,news_info){
            // 基于准备好的dom，初始化echarts实例
            this.chart = echarts.init(document.getElementById(id));
            // 指定图表的配置项和数据
            var option = {
                // color : ['#7db5e2', '#81cacc', '#cca8ba', "#7EBF50", "#82a0c5", '#fddb7e', '#bda29a', '#d2a59a', '#7f9979', '#c4ccd3','#5F9EA0','#a498d6'],
                color:['rgb(210,100,93)','rgb(228,116,79)','rgb(242,176,110)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'].reverse(),
                // color:['rgb(215,121,118)','rgb(224,108,146)','rgb(175,110,195)','rgb(249,224,150)','rgb(255,254,198)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,134,183)','rgb(125,169,185)'].reverse(),
                // color:['rgb(227,158,156)','rgb(224,108,146)','rgb(197,151,212)','rgb(175,159,215)','rgb(160,169,214)','rgb(233,244,163)','rgb(181,219,169)','rgb(156,218,174)','rgb(125,191,166)','rgb(93,178,155)','rgb(74,144,173)','rgb(126,180,225)'].reverse(),
                // color:['#DC143C','#FFB6C1','#BA55D3','#483D8B','#1E90FF','#5F9EA0','#90EE90','#556B2F','#808000','#FFD700','#FFA500','#8B4513'],
                //标题
                tooltip: {
                      trigger: 'item',
                      axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                        type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                      },
                      formatter: function (params, ticket, callback) {
                          var res = params.name+'</br>'+params.marker+params.seriesName+' : '+Math.abs(params.value)
                          return res;
                         // console.log(params)
                         // var res = params[0].name ;
                         //
                         // for (var i = 0, l = params.length; i < l; i++) {
                         //     res += '<br/>' + params[i].marker+params[i].seriesName + ' : ' + Math.abs(params[i].value) ;
                         //
                         // }
                         // setTimeout(function () {
                         //     // 仅为了模拟异步回调
                         //     callback(ticket, res);
                         // }, 10)
                         // return res;
                      },

                },
                grid: {
                    top:'10%',
                    left: '3%',
                    right: '12%',
                    bottom: '3%',
                    containLabel: true
                },
                //工具箱
                //保存图片
                toolbox:{
                    show:true,
                    feature:{
                        saveAsImage:{
                            show:true
                        }
                    }
                },
                //图例-每一条数据的名字叫销量
                legend:{
                    data:this.name,
                    textStyle: {
                      //legend字体颜色
                    },
                    orient: 'vertical',
                    right: '-0%',
                    top: '8%',
                    bottom: 20,
                },
                //x轴没有显式设置，根据值自动生成x轴
                xAxis:{
                    type: 'value',
                    name: '增长数量',
                    nameTextStyle:{
                        fontSize:'15',
                        padding:10
                    },
                    axisLabel: {
                        formatter:function(value)
                        {
                            return Math.abs(value)
                        },
                        fontSize: '15',
                        fontFamily: '微软雅黑',
                        marginTop: '35px',
                        show: true,
                    },
                },
                //y轴
                yAxis:{
                    type: 'category',
                    name: '日期',
                    nameTextStyle:{
                        fontSize:'15',
                    },
                    data: date_arr,
                    axisLabel: {

                        fontSize:'15',
                        fontFamily:'微软雅黑',
                        marginTop:'35px',
                        show:true,
                    },
                },

                //数据-data是最终要显示的数据

                /*  [+] Here I need Initial the series arr */
                series: news_info
            };
            this.chart.setOption(option);
            // window.addEventListener("resize", () => {
            //     this.chart.resize();
            // });
            window.onresize = () => {
                this.chart.resize();
                // this.percentCharts.resize();
            }
        },
        //动态柱状图
        drawDyTrend(id,date_arr,new_info){
          // 基于准备好的dom，初始化echarts实例
            this.chart = echarts.init(document.getElementById(id));

            var dataMap = {};
            function dataFormatter(obj) {
                  var pList = this.name;
                  var temp;
                  for (var day = date_arr[0]; day <= 2011; year++) {
                      var max = 0;
                      var sum = 0;
                      temp = obj[year];
                      for (var i = 0, l = temp.length; i < l; i++) {
                          max = Math.max(max, temp[i]);
                          sum += temp[i];
                          obj[year][i] = {
                              name: pList[i],
                              value: temp[i]
                          };
                      }
                      obj[year + 'max'] = Math.floor(max / 100) * 100;
                      obj[year + 'sum'] = sum;
                  }
                  return obj;
              }

            dataMap.dataGDP = dataFormatter({
    //max : 60000,
    2011:[16251.93,11307.28,24515.76,11237.55,14359.88,22226.7,10568.83,12582,19195.69,49110.27,32318.85,15300.65,17560.18,11702.82,45361.85,26931.03,19632.26,19669.56,53210.28,11720.87,2522.66,10011.37,21026.68,5701.84,8893.12,605.83,12512.3,5020.37,1670.44,2102.21,6610.05],
    2010:[14113.58,9224.46,20394.26,9200.86,11672,18457.27,8667.58,10368.6,17165.98,41425.48,27722.31,12359.33,14737.12,9451.26,39169.92,23092.36,15967.61,16037.96,46013.06,9569.85,2064.5,7925.58,17185.48,4602.16,7224.18,507.46,10123.48,4120.75,1350.43,1689.65,5437.47],
    2009:[12153.03,7521.85,17235.48,7358.31,9740.25,15212.49,7278.75,8587,15046.45,34457.3,22990.35,10062.82,12236.53,7655.18,33896.65,19480.46,12961.1,13059.69,39482.56,7759.16,1654.21,6530.01,14151.28,3912.68,6169.75,441.36,8169.8,3387.56,1081.27,1353.31,4277.05],
    2008:[11115,6719.01,16011.97,7315.4,8496.2,13668.58,6426.1,8314.37,14069.87,30981.98,21462.69,8851.66,10823.01,6971.05,30933.28,18018.53,11328.92,11555,36796.71,7021,1503.06,5793.66,12601.23,3561.56,5692.12,394.85,7314.58,3166.82,1018.62,1203.92,4183.21],
    2007:[9846.81,5252.76,13607.32,6024.45,6423.18,11164.3,5284.69,7104,12494.01,26018.48,18753.73,7360.92,9248.53,5800.25,25776.91,15012.46,9333.4,9439.6,31777.01,5823.41,1254.17,4676.13,10562.39,2884.11,4772.52,341.43,5757.29,2703.98,797.35,919.11,3523.16],
    2006:[8117.78,4462.74,11467.6,4878.61,4944.25,9304.52,4275.12,6211.8,10572.24,21742.05,15718.47,6112.5,7583.85,4820.53,21900.19,12362.79,7617.47,7688.67,26587.76,4746.16,1065.67,3907.23,8690.24,2338.98,3988.14,290.76,4743.61,2277.35,648.5,725.9,3045.26],
    2005:[6969.52,3905.64,10012.11,4230.53,3905.03,8047.26,3620.27,5513.7,9247.66,18598.69,13417.68,5350.17,6554.69,4056.76,18366.87,10587.42,6590.19,6596.1,22557.37,3984.1,918.75,3467.72,7385.1,2005.42,3462.73,248.8,3933.72,1933.98,543.32,612.61,2604.19],
    2004:[6033.21,3110.97,8477.63,3571.37,3041.07,6672,3122.01,4750.6,8072.83,15003.6,11648.7,4759.3,5763.35,3456.7,15021.84,8553.79,5633.24,5641.94,18864.62,3433.5,819.66,3034.58,6379.63,1677.8,3081.91,220.34,3175.58,1688.49,466.1,537.11,2209.09],
    2003:[5007.21,2578.03,6921.29,2855.23,2388.38,6002.54,2662.08,4057.4,6694.23,12442.87,9705.02,3923.11,4983.67,2807.41,12078.15,6867.7,4757.45,4659.99,15844.64,2821.11,713.96,2555.72,5333.09,1426.34,2556.02,185.09,2587.72,1399.83,390.2,445.36,1886.35],
    2002:[4315,2150.76,6018.28,2324.8,1940.94,5458.22,2348.54,3637.2,5741.03,10606.85,8003.67,3519.72,4467.55,2450.48,10275.5,6035.48,4212.82,4151.54,13502.42,2523.73,642.73,2232.86,4725.01,1243.43,2312.82,162.04,2253.39,1232.03,340.65,377.16,1612.6]
});
            var option = {
                  baseOption: {
                      timeline: {
                          axisType: 'category',
                          // realtime: false,
                          // loop: false,
                          autoPlay: true,
                          // currentIndex: 2,
                          playInterval: 1000,
                          // controlStyle: {
                          //     position: 'left'
                          // },
                          data:date_arr,
                          label: [],
                      },
                      title: {
                          subtext: '数据更新于：'+date_arr[-1],
                      },
                      tooltip: {

                      },
                      legend: {
                        // left: 'right',
                        // orient: 'vertical',
                        // data: this.name,
                        // selected: {
                        //   'GDP': false, '金融': false, '房地产': false
                        // }
                      },
                      calculable : true,
                      grid: {
                          top: 80,
                          bottom: 100,
                          tooltip: {
                              trigger: 'axis',
                              axisPointer: {
                                  type: 'shadow',
                                  label: {
                                      show: true,
                                      formatter: function (params) {
                                          return params.value.replace('\n', '');
                                      }
                                  }
                              }
                          }
                      },
                      xAxis: [
                          {
                              'type':'category',
                              'axisLabel':{'interval':0},
                              // 'data':[
                              //     '北京','\n天津','河北','\n山西','内蒙古','\n辽宁','吉林','\n黑龙江',
                              //     '上海','\n江苏','浙江','\n安徽','福建','\n江西','山东','\n河南',
                              //     '湖北','\n湖南','广东','\n广西','海南','\n重庆','四川','\n贵州',
                              //     '云南','\n西藏','陕西','\n甘肃','青海','\n宁夏','新疆'
                              // ],
                              'data':this.name,
                              splitLine: {show: false}
                          }
                      ],
                      yAxis: [
                          {
                              type: 'value',
                              name: '增长数量（条）'
                          }
                      ],
                      series: news_info
                      //   [
                      //     {name: 'GDP', type: 'bar'},
                      //     {name: '金融', type: 'bar'},
                      //     {name: '房地产', type: 'bar'},
                      //     {name: '第一产业', type: 'bar'},
                      //     {name: '第二产业', type: 'bar'},
                      //     {name: '第三产业', type: 'bar'},
                      //     {
                      //         name: 'GDP占比',
                      //         type: 'pie',
                      //         center: ['75%', '35%'],
                      //         radius: '28%',
                      //         z: 100
                      //     }
                      // ]
                  },
                  options: [
                  {
                      title: {text: date_arr[0]+'各个主题增长'},
                      series: [
                          {data: dataMap.dataGDP[date_arr[0]]},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2002sum']},
                              {name: '第二产业', value: dataMap.dataSI['2002sum']},
                              {name: '第三产业', value: dataMap.dataTI['2002sum']}
                          ]}
                      ]
                  },
                  {
                      title : {text: '2003全国宏观经济指标'},
                      series : [
                          {data: dataMap.dataGDP['2003']},
                          {data: dataMap.dataFinancial['2003']},
                          {data: dataMap.dataEstate['2003']},
                          {data: dataMap.dataPI['2003']},
                          {data: dataMap.dataSI['2003']},
                          {data: dataMap.dataTI['2003']},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2003sum']},
                              {name: '第二产业', value: dataMap.dataSI['2003sum']},
                              {name: '第三产业', value: dataMap.dataTI['2003sum']}
                          ]}
                      ]
                  },
                  {
                      title : {text: '2004全国宏观经济指标'},
                      series : [
                          {data: dataMap.dataGDP['2004']},
                          {data: dataMap.dataFinancial['2004']},
                          {data: dataMap.dataEstate['2004']},
                          {data: dataMap.dataPI['2004']},
                          {data: dataMap.dataSI['2004']},
                          {data: dataMap.dataTI['2004']},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2004sum']},
                              {name: '第二产业', value: dataMap.dataSI['2004sum']},
                              {name: '第三产业', value: dataMap.dataTI['2004sum']}
                          ]}
                      ]
                  },
                  {
                      title : {text: '2005全国宏观经济指标'},
                      series : [
                          {data: dataMap.dataGDP['2005']},
                          {data: dataMap.dataFinancial['2005']},
                          {data: dataMap.dataEstate['2005']},
                          {data: dataMap.dataPI['2005']},
                          {data: dataMap.dataSI['2005']},
                          {data: dataMap.dataTI['2005']},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2005sum']},
                              {name: '第二产业', value: dataMap.dataSI['2005sum']},
                              {name: '第三产业', value: dataMap.dataTI['2005sum']}
                          ]}
                      ]
                  },
                  {
                      title : {text: '2006全国宏观经济指标'},
                      series : [
                          {data: dataMap.dataGDP['2006']},
                          {data: dataMap.dataFinancial['2006']},
                          {data: dataMap.dataEstate['2006']},
                          {data: dataMap.dataPI['2006']},
                          {data: dataMap.dataSI['2006']},
                          {data: dataMap.dataTI['2006']},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2006sum']},
                              {name: '第二产业', value: dataMap.dataSI['2006sum']},
                              {name: '第三产业', value: dataMap.dataTI['2006sum']}
                          ]}
                      ]
                  },
                  {
                      title : {text: '2007全国宏观经济指标'},
                      series : [
                          {data: dataMap.dataGDP['2007']},
                          {data: dataMap.dataFinancial['2007']},
                          {data: dataMap.dataEstate['2007']},
                          {data: dataMap.dataPI['2007']},
                          {data: dataMap.dataSI['2007']},
                          {data: dataMap.dataTI['2007']},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2007sum']},
                              {name: '第二产业', value: dataMap.dataSI['2007sum']},
                              {name: '第三产业', value: dataMap.dataTI['2007sum']}
                          ]}
                      ]
                  },
                  {
                      title : {text: '2008全国宏观经济指标'},
                      series : [
                          {data: dataMap.dataGDP['2008']},
                          {data: dataMap.dataFinancial['2008']},
                          {data: dataMap.dataEstate['2008']},
                          {data: dataMap.dataPI['2008']},
                          {data: dataMap.dataSI['2008']},
                          {data: dataMap.dataTI['2008']},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2008sum']},
                              {name: '第二产业', value: dataMap.dataSI['2008sum']},
                              {name: '第三产业', value: dataMap.dataTI['2008sum']}
                          ]}
                      ]
                  },
                  {
                      title : {text: '2009全国宏观经济指标'},
                      series : [
                          {data: dataMap.dataGDP['2009']},
                          {data: dataMap.dataFinancial['2009']},
                          {data: dataMap.dataEstate['2009']},
                          {data: dataMap.dataPI['2009']},
                          {data: dataMap.dataSI['2009']},
                          {data: dataMap.dataTI['2009']},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2009sum']},
                              {name: '第二产业', value: dataMap.dataSI['2009sum']},
                              {name: '第三产业', value: dataMap.dataTI['2009sum']}
                          ]}
                      ]
                  },
                  {
                      title : {text: '2010全国宏观经济指标'},
                      series : [
                          {data: dataMap.dataGDP['2010']},
                          {data: dataMap.dataFinancial['2010']},
                          {data: dataMap.dataEstate['2010']},
                          {data: dataMap.dataPI['2010']},
                          {data: dataMap.dataSI['2010']},
                          {data: dataMap.dataTI['2010']},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2010sum']},
                              {name: '第二产业', value: dataMap.dataSI['2010sum']},
                              {name: '第三产业', value: dataMap.dataTI['2010sum']}
                          ]}
                      ]
                  },
                  {
                      title : {text: '2011全国宏观经济指标'},
                      series : [
                          {data: dataMap.dataGDP['2011']},
                          {data: dataMap.dataFinancial['2011']},
                          {data: dataMap.dataEstate['2011']},
                          {data: dataMap.dataPI['2011']},
                          {data: dataMap.dataSI['2011']},
                          {data: dataMap.dataTI['2011']},
                          {data: [
                              {name: '第一产业', value: dataMap.dataPI['2011sum']},
                              {name: '第二产业', value: dataMap.dataSI['2011sum']},
                              {name: '第三产业', value: dataMap.dataTI['2011sum']}
                          ]}
                      ]
                  }
              ]
            };

            this.chart.setOption(option);
            // window.addEventListener("resize", () => {
            //     this.chart.resize();
            // });
            window.onresize = () => {
                this.chart.resize();
                // this.percentCharts.resize();
            }
        },
        drawDTrend(id,date_arr,news_info){
            this.chart = echarts.init(document.getElementById(id));

            var dataMap = {};
              function dataFormatter(obj) {
                  var pList = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆'];
                  var temp;
                  for (var year = 2002; year <= 2011; year++) {
                      var max = 0;
                      var sum = 0;
                      temp = obj[year];
                      for (var i = 0, l = temp.length; i < l; i++) {
                          max = Math.max(max, temp[i]);
                          sum += temp[i];
                          obj[year][i] = {
                              name: pList[i],
                              value: temp[i]
                          };
                      }
                      obj[year + 'max'] = Math.floor(max / 100) * 100;
                      obj[year + 'sum'] = sum;
                  }
                  return obj;
              };
              function dataFormat(obj) {
                  var pList = this.name;
                  console.log("pList:",pList)
                  var day = this.one_week_time;
                  let temp;
                  for (var i = 0; i <= 6; i++) {
                      var index = day[i];
                      temp = obj[index];
                      for (var j = 0, l = temp.length; j < l; j++)
                          obj[index][j] = {
                              name: pList[j],
                              value: temp[j]
                          };
                      }
                  return obj;
              };
              console.log("data formatter suc11:",this.dataTrend);
              var tempdataTrend = {};
              tempdataTrend = dataFormat(this.dataTrend);
              console.log("data formatter suc22:",tempdataTrend)

              dataMap.dataGDP = dataFormatter({
                  //max : 60000,
                  2011:[16251.93,11307.28,24515.76,11237.55,14359.88,22226.7,10568.83,12582,19195.69,49110.27,32318.85,15300.65,17560.18,11702.82,45361.85,26931.03,19632.26,19669.56,53210.28,11720.87,2522.66,10011.37,21026.68,5701.84,8893.12,605.83,12512.3,5020.37,1670.44,2102.21,6610.05],
                  2010:[14113.58,9224.46,20394.26,9200.86,11672,18457.27,8667.58,10368.6,17165.98,41425.48,27722.31,12359.33,14737.12,9451.26,39169.92,23092.36,15967.61,16037.96,46013.06,9569.85,2064.5,7925.58,17185.48,4602.16,7224.18,507.46,10123.48,4120.75,1350.43,1689.65,5437.47],
                  2009:[12153.03,7521.85,17235.48,7358.31,9740.25,15212.49,7278.75,8587,15046.45,34457.3,22990.35,10062.82,12236.53,7655.18,33896.65,19480.46,12961.1,13059.69,39482.56,7759.16,1654.21,6530.01,14151.28,3912.68,6169.75,441.36,8169.8,3387.56,1081.27,1353.31,4277.05],
                  2008:[11115,6719.01,16011.97,7315.4,8496.2,13668.58,6426.1,8314.37,14069.87,30981.98,21462.69,8851.66,10823.01,6971.05,30933.28,18018.53,11328.92,11555,36796.71,7021,1503.06,5793.66,12601.23,3561.56,5692.12,394.85,7314.58,3166.82,1018.62,1203.92,4183.21],
                  2007:[9846.81,5252.76,13607.32,6024.45,6423.18,11164.3,5284.69,7104,12494.01,26018.48,18753.73,7360.92,9248.53,5800.25,25776.91,15012.46,9333.4,9439.6,31777.01,5823.41,1254.17,4676.13,10562.39,2884.11,4772.52,341.43,5757.29,2703.98,797.35,919.11,3523.16],
                  2006:[8117.78,4462.74,11467.6,4878.61,4944.25,9304.52,4275.12,6211.8,10572.24,21742.05,15718.47,6112.5,7583.85,4820.53,21900.19,12362.79,7617.47,7688.67,26587.76,4746.16,1065.67,3907.23,8690.24,2338.98,3988.14,290.76,4743.61,2277.35,648.5,725.9,3045.26],
                  2005:[6969.52,3905.64,10012.11,4230.53,3905.03,8047.26,3620.27,5513.7,9247.66,18598.69,13417.68,5350.17,6554.69,4056.76,18366.87,10587.42,6590.19,6596.1,22557.37,3984.1,918.75,3467.72,7385.1,2005.42,3462.73,248.8,3933.72,1933.98,543.32,612.61,2604.19],
                  2004:[6033.21,3110.97,8477.63,3571.37,3041.07,6672,3122.01,4750.6,8072.83,15003.6,11648.7,4759.3,5763.35,3456.7,15021.84,8553.79,5633.24,5641.94,18864.62,3433.5,819.66,3034.58,6379.63,1677.8,3081.91,220.34,3175.58,1688.49,466.1,537.11,2209.09],
                  2003:[5007.21,2578.03,6921.29,2855.23,2388.38,6002.54,2662.08,4057.4,6694.23,12442.87,9705.02,3923.11,4983.67,2807.41,12078.15,6867.7,4757.45,4659.99,15844.64,2821.11,713.96,2555.72,5333.09,1426.34,2556.02,185.09,2587.72,1399.83,390.2,445.36,1886.35],
                  2002:[4315,2150.76,6018.28,2324.8,1940.94,5458.22,2348.54,3637.2,5741.03,10606.85,8003.67,3519.72,4467.55,2450.48,10275.5,6035.48,4212.82,4151.54,13502.42,2523.73,642.73,2232.86,4725.01,1243.43,2312.82,162.04,2253.39,1232.03,340.65,377.16,1612.6]
              });
              console.log(this.dataTrend)
                var option = {
                    baseOption: {
                        timeline: {
                            axisType: 'category',
                            // realtime: false,
                            // loop: false,
                            autoPlay: true,
                            // currentIndex: 2,
                            playInterval: 1000,
                            // controlStyle: {
                            //     position: 'left'
                            // },
                            data: date_arr,
                            label: {},
                        },
                        title: {
                            subtext: '数据更新于：'+date_arr[6],
                        },
                        tooltip: {
                        },
                        legend: {
                            left: 'right',
                            data: ['GDP'],
                            // selected: {
                            //     'GDP': true, '金融': false, '房地产': false,'第一产业': false, '第二产业': false, '第三产业': false
                            // }
                        },
                        calculable : true,
                        grid: {
                            top: 80,
                            bottom: 100,
                            tooltip: {
                                trigger: 'axis',
                                axisPointer: {
                                    type: 'shadow',
                                    label: {
                                        show: true,
                                        formatter: function (params) {
                                            return params.value.replace('\n', '');
                                        }
                                    }
                                }
                            }
                        },
                        xAxis: [
                            {
                                'type':'category',
                                'axisLabel':{'interval':0},
                                'data':this.name,
                                  splitLine: {show: true}
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                name: '增长数量（条）'
                            }
                        ],
                        series: [
                            {name: 'GDP', type: 'bar'},
                            // {name: '金融', type: 'bar'},
                            // {name: '房地产', type: 'bar'},
                            // {name: '第一产业', type: 'bar'},
                            // {name: '第二产业', type: 'bar'},
                            // {name: '第三产业', type: 'bar'},
                            {
                                name: 'GDP占比',
                                type: 'pie',
                                center: ['75%', '35%'],
                                radius: '28%',
                                z: 100
                            }
                        ]
                    },
                options: [
                    {
                        title: {text: date_arr[0]+'各个主题增长'},
                        series: [
                            {data: dataMap.dataGDP['2002']},
                            // {data: dataMap.dataFinancial['2002']},
                            // {data: dataMap.dataEstate['2002']},
                            // {data: dataMap.dataPI['2002']},
                            // {data: dataMap.dataSI['2002']},
                            // {data: dataMap.dataTI['2002']},
                            {data:
                                dataMap.dataGDP['2002'],
                                // {name: '第二产业', value: dataMap.dataFinancial['2002sum']},
                                // {name: 'dataEstate', value: dataMap.dataEstate['2002sum']}
                            }
                        ]
                    },
                    {
                        title : {text: date_arr[1]+'各个主题增长'},
                        series : [
                            {data: dataMap.dataGDP['2003']},
                            // {data: dataMap.dataFinancial['2003']},
                            // {data: dataMap.dataEstate['2003']},
                            // {data: dataMap.dataPI['2003']},
                            // {data: dataMap.dataSI['2003']},
                            // {data: dataMap.dataTI['2003']},
                            {data:
                                dataMap.dataGDP['2003'],
                            }
                        ]
                    },
                    {
                        title : {text: date_arr[2]+'各个主题增长'},
                        series : [
                            {data: dataMap.dataGDP['2004']},
                            // {data: dataMap.dataFinancial['2004']},
                            // {data: dataMap.dataEstate['2004']},
                            // {data: dataMap.dataPI['2004']},
                            // {data: dataMap.dataSI['2004']},
                            // {data: dataMap.dataTI['2004']},
                            {data: dataMap.dataGDP['2004'],}
                        ]
                    },
                    {
                        title : {text: date_arr[3]+'各个主题增长'},
                        series : [
                            {data: dataMap.dataGDP['2005']},
                            // {data: dataMap.dataFinancial['2005']},
                            // {data: dataMap.dataEstate['2005']},
                            // {data: dataMap.dataPI['2005']},
                            // {data: dataMap.dataSI['2005']},
                            // {data: dataMap.dataTI['2005']},
                            {data: dataMap.dataGDP['2005'],}
                        ]
                    },
                    {
                        title : {text: date_arr[4]+'各个主题增长'},
                        series : [
                            {data: dataMap.dataGDP['2006']},
                            // {data: dataMap.dataFinancial['2006']},
                            // {data: dataMap.dataEstate['2006']},
                            // {data: dataMap.dataPI['2006']},
                            // {data: dataMap.dataSI['2006']},
                            // {data: dataMap.dataTI['2006']},
                            {data: dataMap.dataGDP['2006'],}
                        ]
                    },
                    {
                        title : {text: date_arr[5]+'各个主题增长'},
                        series : [
                            {data: dataMap.dataGDP['2007']},
                            // {data: dataMap.dataFinancial['2007']},
                            // {data: dataMap.dataEstate['2007']},
                            // {data: dataMap.dataPI['2007']},
                            // {data: dataMap.dataSI['2007']},
                            // {data: dataMap.dataTI['2007']},
                            {data: dataMap.dataGDP['2007'],}
                        ]
                    },
                    {
                        title : {text: date_arr[6]+'各个主题增长'},
                        series : [
                            {data: dataMap.dataGDP['2008']},
                            // {data: dataMap.dataFinancial['2008']},
                            // {data: dataMap.dataEstate['2008']},
                            // {data: dataMap.dataPI['2008']},
                            // {data: dataMap.dataSI['2008']},
                            // {data: dataMap.dataTI['2008']},
                            {data: dataMap.dataGDP['2008'],}
                        ]
                    },

                  ]
              };
            this.chart.setOption(option);
            // window.addEventListener("resize", () => {
            //     this.chart.resize();
            // });
            window.onresize = () => {
                this.chart.resize();
                // this.percentCharts.resize();
            }
        },
        drawTest(id,date_arr,news_info){
            this.chart = echarts.init(document.getElementById(id));

         var dataMap = {};
function dataFormatter(obj) {
    var pList = ['北京','天津','河北','山西','内蒙古','辽宁','吉林','黑龙江','上海','江苏','浙江','安徽','福建','江西','山东','河南','湖北','湖南','广东','广西','海南','重庆','四川','贵州','云南','西藏','陕西','甘肃','青海','宁夏','新疆'];
    var temp;
    for (var year = 2002; year <= 2011; year++) {
        var max = 0;
        var sum = 0;
        temp = obj[year];
        for (var i = 0, l = temp.length; i < l; i++) {
            max = Math.max(max, temp[i]);
            sum += temp[i];
            obj[year][i] = {
                name: pList[i],
                value: temp[i]
            };
        }
        obj[year + 'max'] = Math.floor(max / 100) * 100;
        obj[year + 'sum'] = sum;
    }
    return obj;
};
console.log("data formatter suc")


dataMap.dataGDP = dataFormatter({
    //max : 60000,
    2011:[16251.93,11307.28,24515.76,11237.55,14359.88,22226.7,10568.83,12582,19195.69,49110.27,32318.85,15300.65,17560.18,11702.82,45361.85,26931.03,19632.26,19669.56,53210.28,11720.87,2522.66,10011.37,21026.68,5701.84,8893.12,605.83,12512.3,5020.37,1670.44,2102.21,6610.05],
    2010:[14113.58,9224.46,20394.26,9200.86,11672,18457.27,8667.58,10368.6,17165.98,41425.48,27722.31,12359.33,14737.12,9451.26,39169.92,23092.36,15967.61,16037.96,46013.06,9569.85,2064.5,7925.58,17185.48,4602.16,7224.18,507.46,10123.48,4120.75,1350.43,1689.65,5437.47],
    2009:[12153.03,7521.85,17235.48,7358.31,9740.25,15212.49,7278.75,8587,15046.45,34457.3,22990.35,10062.82,12236.53,7655.18,33896.65,19480.46,12961.1,13059.69,39482.56,7759.16,1654.21,6530.01,14151.28,3912.68,6169.75,441.36,8169.8,3387.56,1081.27,1353.31,4277.05],
    2008:[11115,6719.01,16011.97,7315.4,8496.2,13668.58,6426.1,8314.37,14069.87,30981.98,21462.69,8851.66,10823.01,6971.05,30933.28,18018.53,11328.92,11555,36796.71,7021,1503.06,5793.66,12601.23,3561.56,5692.12,394.85,7314.58,3166.82,1018.62,1203.92,4183.21],
    2007:[9846.81,5252.76,13607.32,6024.45,6423.18,11164.3,5284.69,7104,12494.01,26018.48,18753.73,7360.92,9248.53,5800.25,25776.91,15012.46,9333.4,9439.6,31777.01,5823.41,1254.17,4676.13,10562.39,2884.11,4772.52,341.43,5757.29,2703.98,797.35,919.11,3523.16],
    2006:[8117.78,4462.74,11467.6,4878.61,4944.25,9304.52,4275.12,6211.8,10572.24,21742.05,15718.47,6112.5,7583.85,4820.53,21900.19,12362.79,7617.47,7688.67,26587.76,4746.16,1065.67,3907.23,8690.24,2338.98,3988.14,290.76,4743.61,2277.35,648.5,725.9,3045.26],
    2005:[6969.52,3905.64,10012.11,4230.53,3905.03,8047.26,3620.27,5513.7,9247.66,18598.69,13417.68,5350.17,6554.69,4056.76,18366.87,10587.42,6590.19,6596.1,22557.37,3984.1,918.75,3467.72,7385.1,2005.42,3462.73,248.8,3933.72,1933.98,543.32,612.61,2604.19],
    2004:[6033.21,3110.97,8477.63,3571.37,3041.07,6672,3122.01,4750.6,8072.83,15003.6,11648.7,4759.3,5763.35,3456.7,15021.84,8553.79,5633.24,5641.94,18864.62,3433.5,819.66,3034.58,6379.63,1677.8,3081.91,220.34,3175.58,1688.49,466.1,537.11,2209.09],
    2003:[5007.21,2578.03,6921.29,2855.23,2388.38,6002.54,2662.08,4057.4,6694.23,12442.87,9705.02,3923.11,4983.67,2807.41,12078.15,6867.7,4757.45,4659.99,15844.64,2821.11,713.96,2555.72,5333.09,1426.34,2556.02,185.09,2587.72,1399.83,390.2,445.36,1886.35],
    2002:[4315,2150.76,6018.28,2324.8,1940.94,5458.22,2348.54,3637.2,5741.03,10606.85,8003.67,3519.72,4467.55,2450.48,10275.5,6035.48,4212.82,4151.54,13502.42,2523.73,642.73,2232.86,4725.01,1243.43,2312.82,162.04,2253.39,1232.03,340.65,377.16,1612.6]
});
console.log("data formatter suc2")
dataMap.dataPI = dataFormatter({
    //max : 4000,
    2011:[136.27,159.72,2905.73,641.42,1306.3,1915.57,1277.44,1701.5,124.94,3064.78,1583.04,2015.31,1612.24,1391.07,3973.85,3512.24,2569.3,2768.03,2665.2,2047.23,659.23,844.52,2983.51,726.22,1411.01,74.47,1220.9,678.75,155.08,184.14,1139.03],
    2010:[124.36,145.58,2562.81,554.48,1095.28,1631.08,1050.15,1302.9,114.15,2540.1,1360.56,1729.02,1363.67,1206.98,3588.28,3258.09,2147,2325.5,2286.98,1675.06,539.83,685.38,2482.89,625.03,1108.38,68.72,988.45,599.28,134.92,159.29,1078.63],
    2009:[118.29,128.85,2207.34,477.59,929.6,1414.9,980.57,1154.33,113.82,2261.86,1163.08,1495.45,1182.74,1098.66,3226.64,2769.05,1795.9,1969.69,2010.27,1458.49,462.19,606.8,2240.61,550.27,1067.6,63.88,789.64,497.05,107.4,127.25,759.74],
    2008:[112.83,122.58,2034.59,313.58,907.95,1302.02,916.72,1088.94,111.8,2100.11,1095.96,1418.09,1158.17,1060.38,3002.65,2658.78,1780,1892.4,1973.05,1453.75,436.04,575.4,2216.15,539.19,1020.56,60.62,753.72,462.27,105.57,118.94,691.07],
    2007:[101.26,110.19,1804.72,311.97,762.1,1133.42,783.8,915.38,101.84,1816.31,986.02,1200.18,1002.11,905.77,2509.14,2217.66,1378,1626.48,1695.57,1241.35,361.07,482.39,2032,446.38,837.35,54.89,592.63,387.55,83.41,97.89,628.72],
    2006:[88.8,103.35,1461.81,276.77,634.94,939.43,672.76,750.14,93.81,1545.05,925.1,1011.03,865.98,786.14,2138.9,1916.74,1140.41,1272.2,1532.17,1032.47,323.48,386.38,1595.48,382.06,724.4,50.9,484.81,334,67.55,79.54,527.8],
    2005:[88.68,112.38,1400,262.42,589.56,882.41,625.61,684.6,90.26,1461.51,892.83,966.5,827.36,727.37,1963.51,1892.01,1082.13,1100.65,1428.27,912.5,300.75,463.4,1481.14,368.94,661.69,48.04,435.77,308.06,65.34,72.07,509.99],
    2004:[87.36,105.28,1370.43,276.3,522.8,798.43,568.69,605.79,83.45,1367.58,814.1,950.5,786.84,664.5,1778.45,1649.29,1020.09,1022.45,1248.59,817.88,278.76,428.05,1379.93,334.5,607.75,44.3,387.88,286.78,60.7,65.33,461.26],
    2003:[84.11,89.91,1064.05,215.19,420.1,615.8,488.23,504.8,81.02,1162.45,717.85,749.4,692.94,560,1480.67,1198.7,798.35,886.47,1072.91,658.78,244.29,339.06,1128.61,298.69,494.6,40.7,302.66,237.91,48.47,55.63,412.9],
    2002:[82.44,84.21,956.84,197.8,374.69,590.2,446.17,474.2,79.68,1110.44,685.2,783.66,664.78,535.98,1390,1288.36,707,847.25,1015.08,601.99,222.89,317.87,1047.95,281.1,463.44,39.75,282.21,215.51,47.31,52.95,305]
});

dataMap.dataSI = dataFormatter({
    //max : 26600,
    2011:[3752.48,5928.32,13126.86,6635.26,8037.69,12152.15,5611.48,5962.41,7927.89,25203.28,16555.58,8309.38,9069.2,6390.55,24017.11,15427.08,9815.94,9361.99,26447.38,5675.32,714.5,5543.04,11029.13,2194.33,3780.32,208.79,6935.59,2377.83,975.18,1056.15,3225.9],
    2010:[3388.38,4840.23,10707.68,5234,6367.69,9976.82,4506.31,5025.15,7218.32,21753.93,14297.93,6436.62,7522.83,5122.88,21238.49,13226.38,7767.24,7343.19,23014.53,4511.68,571,4359.12,8672.18,1800.06,3223.49,163.92,5446.1,1984.97,744.63,827.91,2592.15],
    2009:[2855.55,3987.84,8959.83,3993.8,5114,7906.34,3541.92,4060.72,6001.78,18566.37,11908.49,4905.22,6005.3,3919.45,18901.83,11010.5,6038.08,5687.19,19419.7,3381.54,443.43,3448.77,6711.87,1476.62,2582.53,136.63,4236.42,1527.24,575.33,662.32,1929.59],
    2008:[2626.41,3709.78,8701.34,4242.36,4376.19,7158.84,3097.12,4319.75,6085.84,16993.34,11567.42,4198.93,5318.44,3554.81,17571.98,10259.99,5082.07,5028.93,18502.2,3037.74,423.55,3057.78,5823.39,1370.03,2452.75,115.56,3861.12,1470.34,557.12,609.98,2070.76],
    2007:[2509.4,2892.53,7201.88,3454.49,3193.67,5544.14,2475.45,3695.58,5571.06,14471.26,10154.25,3370.96,4476.42,2975.53,14647.53,8282.83,4143.06,3977.72,16004.61,2425.29,364.26,2368.53,4648.79,1124.79,2038.39,98.48,2986.46,1279.32,419.03,455.04,1647.55],
    2006:[2191.43,2457.08,6110.43,2755.66,2374.96,4566.83,1915.29,3365.31,4969.95,12282.89,8511.51,2711.18,3695.04,2419.74,12574.03,6724.61,3365.08,3187.05,13469.77,1878.56,308.62,1871.65,3775.14,967.54,1705.83,80.1,2452.44,1043.19,331.91,351.58,1459.3],
    2005:[2026.51,2135.07,5271.57,2357.04,1773.21,3869.4,1580.83,2971.68,4381.2,10524.96,7164.75,2245.9,3175.92,1917.47,10478.62,5514.14,2852.12,2612.57,11356.6,1510.68,240.83,1564,3067.23,821.16,1426.42,63.52,1951.36,838.56,264.61,281.05,1164.79],
    2004:[1853.58,1685.93,4301.73,1919.4,1248.27,3061.62,1329.68,2487.04,3892.12,8437.99,6250.38,1844.9,2770.49,1566.4,8478.69,4182.1,2320.6,2190.54,9280.73,1253.7,205.6,1376.91,2489.4,681.5,1281.63,52.74,1553.1,713.3,211.7,244.05,914.47],
    2003:[1487.15,1337.31,3417.56,1463.38,967.49,2898.89,1098.37,2084.7,3209.02,6787.11,5096.38,1535.29,2340.82,1204.33,6485.05,3310.14,1956.02,1777.74,7592.78,984.08,175.82,1135.31,2014.8,569.37,1047.66,47.64,1221.17,572.02,171.92,194.27,719.54],
    2002:[1249.99,1069.08,2911.69,1134.31,754.78,2609.85,943.49,1843.6,2622.45,5604.49,4090.48,1337.04,2036.97,941.77,5184.98,2768.75,1709.89,1523.5,6143.4,846.89,148.88,958.87,1733.38,481.96,934.88,32.72,1007.56,501.69,144.51,153.06,603.15]
});

dataMap.dataTI = dataFormatter({
    //max : 25000,
    2011:[12363.18,5219.24,8483.17,3960.87,5015.89,8158.98,3679.91,4918.09,11142.86,20842.21,14180.23,4975.96,6878.74,3921.2,17370.89,7991.72,7247.02,7539.54,24097.7,3998.33,1148.93,3623.81,7014.04,2781.29,3701.79,322.57,4355.81,1963.79,540.18,861.92,2245.12],
    2010:[10600.84,4238.65,7123.77,3412.38,4209.03,6849.37,3111.12,4040.55,9833.51,17131.45,12063.82,4193.69,5850.62,3121.4,14343.14,6607.89,6053.37,6369.27,20711.55,3383.11,953.67,2881.08,6030.41,2177.07,2892.31,274.82,3688.93,1536.5,470.88,702.45,1766.69],
    2009:[9179.19,3405.16,6068.31,2886.92,3696.65,5891.25,2756.26,3371.95,8930.85,13629.07,9918.78,3662.15,5048.49,2637.07,11768.18,5700.91,5127.12,5402.81,18052.59,2919.13,748.59,2474.44,5198.8,1885.79,2519.62,240.85,3143.74,1363.27,398.54,563.74,1587.72],
    2008:[8375.76,2886.65,5276.04,2759.46,3212.06,5207.72,2412.26,2905.68,7872.23,11888.53,8799.31,3234.64,4346.4,2355.86,10358.64,5099.76,4466.85,4633.67,16321.46,2529.51,643.47,2160.48,4561.69,1652.34,2218.81,218.67,2699.74,1234.21,355.93,475,1421.38],
    2007:[7236.15,2250.04,4600.72,2257.99,2467.41,4486.74,2025.44,2493.04,6821.11,9730.91,7613.46,2789.78,3770,1918.95,8620.24,4511.97,3812.34,3835.4,14076.83,2156.76,528.84,1825.21,3881.6,1312.94,1896.78,188.06,2178.2,1037.11,294.91,366.18,1246.89],
    2006:[5837.55,1902.31,3895.36,1846.18,1934.35,3798.26,1687.07,2096.35,5508.48,7914.11,6281.86,2390.29,3022.83,1614.65,7187.26,3721.44,3111.98,3229.42,11585.82,1835.12,433.57,1649.2,3319.62,989.38,1557.91,159.76,1806.36,900.16,249.04,294.78,1058.16],
    2005:[4854.33,1658.19,3340.54,1611.07,1542.26,3295.45,1413.83,1857.42,4776.2,6612.22,5360.1,2137.77,2551.41,1411.92,5924.74,3181.27,2655.94,2882.88,9772.5,1560.92,377.17,1440.32,2836.73,815.32,1374.62,137.24,1546.59,787.36,213.37,259.49,929.41],
    2004:[4092.27,1319.76,2805.47,1375.67,1270,2811.95,1223.64,1657.77,4097.26,5198.03,4584.22,1963.9,2206.02,1225.8,4764.7,2722.4,2292.55,2428.95,8335.3,1361.92,335.3,1229.62,2510.3,661.8,1192.53,123.3,1234.6,688.41,193.7,227.73,833.36],
    2003:[3435.95,1150.81,2439.68,1176.65,1000.79,2487.85,1075.48,1467.9,3404.19,4493.31,3890.79,1638.42,1949.91,1043.08,4112.43,2358.86,2003.08,1995.78,7178.94,1178.25,293.85,1081.35,2189.68,558.28,1013.76,96.76,1063.89,589.91,169.81,195.46,753.91],
    2002:[2982.57,997.47,2149.75,992.69,811.47,2258.17,958.88,1319.4,3038.9,3891.92,3227.99,1399.02,1765.8,972.73,3700.52,1978.37,1795.93,1780.79,6343.94,1074.85,270.96,956.12,1943.68,480.37,914.5,89.56,963.62,514.83,148.83,171.14,704.5]
});

dataMap.dataEstate = dataFormatter({
    //max : 3600,
    2011:[1074.93,411.46,918.02,224.91,384.76,876.12,238.61,492.1,1019.68,2747.89,1677.13,634.92,911.16,402.51,1838.14,987,634.67,518.04,3321.31,465.68,208.71,396.28,620.62,160.3,222.31,17.44,398.03,134.25,29.05,79.01,176.22],
    2010:[1006.52,377.59,697.79,192,309.25,733.37,212.32,391.89,1002.5,2600.95,1618.17,532.17,679.03,340.56,1622.15,773.23,564.41,464.21,2813.95,405.79,188.33,266.38,558.56,139.64,223.45,14.54,315.95,110.02,25.41,60.53,143.44],
    2009:[1062.47,308.73,612.4,173.31,286.65,605.27,200.14,301.18,1237.56,2025.39,1316.84,497.94,656.61,305.9,1329.59,622.98,546.11,400.11,2470.63,348.98,121.76,229.09,548.14,136.15,205.14,13.28,239.92,101.37,23.05,47.56,115.23],
    2008:[844.59,227.88,513.81,166.04,273.3,500.81,182.7,244.47,939.34,1626.13,1052.03,431.27,506.98,281.96,1104.95,512.42,526.88,340.07,2057.45,282.96,95.6,191.21,453.63,104.81,195.48,15.08,193.27,93.8,19.96,38.85,89.79],
    2007:[821.5,183.44,467.97,134.12,191.01,410.43,153.03,225.81,958.06,1365.71,981.42,366.57,511.5,225.96,953.69,447.44,409.65,301.8,2029.77,239.45,67.19,196.06,376.84,93.19,193.59,13.24,153.98,83.52,16.98,29.49,91.28],
    2006:[658.3,156.64,397.14,117.01,136.5,318.54,131.01,194.7,773.61,1017.91,794.41,281.98,435.22,184.67,786.51,348.7,294.73,254.81,1722.07,192.2,44.45,158.2,336.2,80.24,165.92,11.92,125.2,73.21,15.17,25.53,68.9],
    2005:[493.73,122.67,330.87,106,98.75,256.77,112.29,163.34,715.97,799.73,688.86,231.66,331.8,171.88,664.9,298.19,217.17,215.63,1430.37,165.05,38.2,143.88,286.23,76.38,148.69,10.02,108.62,63.78,14.1,22.97,55.79],
    2004:[436.11,106.14,231.08,95.1,73.81,203.1,97.93,137.74,666.3,534.17,587.83,188.28,248.44,167.2,473.27,236.44,204.8,191.5,1103.75,122.52,30.64,129.12,264.3,68.3,116.54,5.8,95.9,56.84,13,20.78,53.55],
    2003:[341.88,92.31,185.19,78.73,61.05,188.49,91.99,127.2,487.82,447.47,473.16,162.63,215.84,138.02,418.21,217.58,176.8,186.49,955.66,100.93,25.14,113.69,231.72,59.86,103.79,4.35,83.9,48.09,11.41,16.85,47.84],
    2002:[298.02,73.04,140.89,65.83,51.48,130.94,76.11,118.7,384.86,371.09,360.63,139.18,188.09,125.27,371.13,199.31,145.17,165.29,808.16,82.83,21.45,90.48,210.82,53.49,95.68,3.42,77.68,41.52,9.74,13.46,43.04]
});

dataMap.dataFinancial = dataFormatter({
    //max : 3200,
    2011:[2215.41,756.5,746.01,519.32,447.46,755.57,207.65,370.78,2277.4,2600.11,2730.29,503.85,862.41,357.44,1640.41,868.2,674.57,501.09,2916.13,445.37,105.24,704.66,868.15,297.27,456.23,31.7,432.11,145.05,62.56,134.18,288.77],
    2010:[1863.61,572.99,615.42,448.3,346.44,639.27,190.12,304.59,1950.96,2105.92,2326.58,396.17,767.58,241.49,1361.45,697.68,561.27,463.16,2658.76,384.53,78.12,496.56,654.7,231.51,375.08,27.08,384.75,100.54,54.53,97.87,225.2],
    2009:[1603.63,461.2,525.67,361.64,291.1,560.2,180.83,227.54,1804.28,1596.98,1899.33,359.6,612.2,165.1,1044.9,499.92,479.11,402.57,2283.29,336.82,65.73,389.97,524.63,194.44,351.74,23.17,336.21,88.27,45.63,75.54,198.87],
    2008:[1519.19,368.1,420.74,290.91,219.09,455.07,147.24,177.43,1414.21,1298.48,1653.45,313.81,497.65,130.57,880.28,413.83,393.05,334.32,1972.4,249.01,47.33,303.01,411.14,151.55,277.66,22.42,287.16,72.49,36.54,64.8,171.97],
    2007:[1302.77,288.17,347.65,218.73,148.3,386.34,126.03,155.48,1209.08,1054.25,1251.43,223.85,385.84,101.34,734.9,302.31,337.27,260.14,1705.08,190.73,34.43,247.46,359.11,122.25,168.55,11.51,231.03,61.6,27.67,51.05,149.22],
    2006:[982.37,186.87,284.04,169.63,108.21,303.41,100.75,74.17,825.2,653.25,906.37,166.01,243.9,79.75,524.94,219.72,174.99,204.72,899.91,129.14,16.37,213.7,299.5,89.43,143.62,6.44,152.25,50.51,23.69,36.99,99.25],
    2005:[840.2,147.4,213.47,135.07,72.52,232.85,83.63,35.03,675.12,492.4,686.32,127.05,186.12,69.55,448.36,181.74,127.32,162.37,661.81,91.93,13.16,185.18,262.26,73.67,130.5,7.57,127.58,44.73,20.36,32.25,80.34],
    2004:[713.79,136.97,209.1,110.29,55.89,188.04,77.17,32.2,612.45,440.5,523.49,94.1,171,65.1,343.37,170.82,118.85,118.64,602.68,74,11.56,162.38,236.5,60.3,118.4,5.4,90.1,42.99,19,27.92,70.3],
    2003:[635.56,112.79,199.87,118.48,55.89,145.38,73.15,32.2,517.97,392.11,451.54,87.45,150.09,64.31,329.71,165.11,107.31,99.35,534.28,61.59,10.68,147.04,206.24,48.01,105.48,4.74,77.87,42.31,17.98,24.8,64.92],
    2002:[561.91,76.86,179.6,124.1,48.39,137.18,75.45,31.6,485.25,368.86,347.53,81.85,138.28,76.51,310.07,158.77,96.95,92.43,454.65,35.86,10.08,134.52,183.13,41.45,102.39,2.81,67.3,42.08,16.75,21.45,52.18]
});


var option = {
    baseOption: {
        timeline: {
            axisType: 'category',
            // realtime: false,
            // loop: false,
            autoPlay: true,
            // currentIndex: 2,
            playInterval: 1000,
            // controlStyle: {
            //     position: 'left'
            // },
            data: [
                '2002-01-01','2003-01-01','2004-01-01',
                {
                    value: '2005-01-01',
                    tooltip: {
                        formatter: '{b} GDP达到一个高度'
                    },
                    symbol: 'diamond',
                    symbolSize: 16
                },
                '2006-01-01', '2007-01-01','2008-01-01','2009-01-01','2010-01-01',
                {
                    value: '2011-01-01',
                    tooltip: {
                        formatter: function (params) {
                            return params.name + 'GDP达到又一个高度';
                        }
                    },
                    symbol: 'diamond',
                    symbolSize: 18
                },
            ],
            label: {
                formatter : function(s) {
                    return (new Date(s)).getFullYear();
                }
            }
        },
        title: {
            subtext: '数据来自国家统计局'
        },
        tooltip: {
        },
        legend: {
            left: 'right',
            data: ['第一产业', '第二产业', '第三产业', 'GDP', '金融', '房地产'],
            selected: {
                'GDP': true, '金融': false, '房地产': false,'第一产业': false, '第二产业': false, '第三产业': false
            }
        },
        calculable : true,
        grid: {
            top: 80,
            bottom: 100,
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow',
                    label: {
                        show: true,
                        formatter: function (params) {
                            return params.value.replace('\n', '');
                        }
                    }
                }
            }
        },
        xAxis: [
            {
                'type':'category',
                'axisLabel':{'interval':0},
                'data':[
                    '北京','\n天津','河北','\n山西','内蒙古','\n辽宁','吉林','\n黑龙江',
                    '上海','\n江苏','浙江','\n安徽','福建','\n江西','山东','\n河南',
                    '湖北','\n湖南','广东','\n广西','海南','\n重庆','四川','\n贵州',
                    '云南','\n西藏','陕西','\n甘肃','青海','\n宁夏','新疆'
                ],
                splitLine: {show: false}
            }
        ],
        yAxis: [
            {
                type: 'value',
                name: 'GDP（亿元）'
            }
        ],
        series: [
            {name: 'GDP', type: 'bar'},
            {name: '金融', type: 'bar'},
            {name: '房地产', type: 'bar'},
            {name: '第一产业', type: 'bar'},
            {name: '第二产业', type: 'bar'},
            {name: '第三产业', type: 'bar'},
            {
                name: 'GDP占比',
                type: 'pie',
                center: ['75%', '35%'],
                radius: '28%',
                z: 100
            }
        ]
    },
    options: [
        {
            title: {text: '2002全国宏观经济指标'},
            series: [
                {data: dataMap.dataGDP['2002']},
                {data: dataMap.dataFinancial['2002']},
                {data: dataMap.dataEstate['2002']},
                {data: dataMap.dataPI['2002']},
                {data: dataMap.dataSI['2002']},
                {data: dataMap.dataTI['2002']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2002sum']},
                    {name: '第二产业', value: dataMap.dataSI['2002sum']},
                    {name: '第三产业', value: dataMap.dataTI['2002sum']}
                ]}
            ]
        },
        {
            title : {text: '2003全国宏观经济指标'},
            series : [
                {data: dataMap.dataGDP['2003']},
                {data: dataMap.dataFinancial['2003']},
                {data: dataMap.dataEstate['2003']},
                {data: dataMap.dataPI['2003']},
                {data: dataMap.dataSI['2003']},
                {data: dataMap.dataTI['2003']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2003sum']},
                    {name: '第二产业', value: dataMap.dataSI['2003sum']},
                    {name: '第三产业', value: dataMap.dataTI['2003sum']}
                ]}
            ]
        },
        {
            title : {text: '2004全国宏观经济指标'},
            series : [
                {data: dataMap.dataGDP['2004']},
                {data: dataMap.dataFinancial['2004']},
                {data: dataMap.dataEstate['2004']},
                {data: dataMap.dataPI['2004']},
                {data: dataMap.dataSI['2004']},
                {data: dataMap.dataTI['2004']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2004sum']},
                    {name: '第二产业', value: dataMap.dataSI['2004sum']},
                    {name: '第三产业', value: dataMap.dataTI['2004sum']}
                ]}
            ]
        },
        {
            title : {text: '2005全国宏观经济指标'},
            series : [
                {data: dataMap.dataGDP['2005']},
                {data: dataMap.dataFinancial['2005']},
                {data: dataMap.dataEstate['2005']},
                {data: dataMap.dataPI['2005']},
                {data: dataMap.dataSI['2005']},
                {data: dataMap.dataTI['2005']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2005sum']},
                    {name: '第二产业', value: dataMap.dataSI['2005sum']},
                    {name: '第三产业', value: dataMap.dataTI['2005sum']}
                ]}
            ]
        },
        {
            title : {text: '2006全国宏观经济指标'},
            series : [
                {data: dataMap.dataGDP['2006']},
                {data: dataMap.dataFinancial['2006']},
                {data: dataMap.dataEstate['2006']},
                {data: dataMap.dataPI['2006']},
                {data: dataMap.dataSI['2006']},
                {data: dataMap.dataTI['2006']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2006sum']},
                    {name: '第二产业', value: dataMap.dataSI['2006sum']},
                    {name: '第三产业', value: dataMap.dataTI['2006sum']}
                ]}
            ]
        },
        {
            title : {text: '2007全国宏观经济指标'},
            series : [
                {data: dataMap.dataGDP['2007']},
                {data: dataMap.dataFinancial['2007']},
                {data: dataMap.dataEstate['2007']},
                {data: dataMap.dataPI['2007']},
                {data: dataMap.dataSI['2007']},
                {data: dataMap.dataTI['2007']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2007sum']},
                    {name: '第二产业', value: dataMap.dataSI['2007sum']},
                    {name: '第三产业', value: dataMap.dataTI['2007sum']}
                ]}
            ]
        },
        {
            title : {text: '2008全国宏观经济指标'},
            series : [
                {data: dataMap.dataGDP['2008']},
                {data: dataMap.dataFinancial['2008']},
                {data: dataMap.dataEstate['2008']},
                {data: dataMap.dataPI['2008']},
                {data: dataMap.dataSI['2008']},
                {data: dataMap.dataTI['2008']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2008sum']},
                    {name: '第二产业', value: dataMap.dataSI['2008sum']},
                    {name: '第三产业', value: dataMap.dataTI['2008sum']}
                ]}
            ]
        },
        {
            title : {text: '2009全国宏观经济指标'},
            series : [
                {data: dataMap.dataGDP['2009']},
                {data: dataMap.dataFinancial['2009']},
                {data: dataMap.dataEstate['2009']},
                {data: dataMap.dataPI['2009']},
                {data: dataMap.dataSI['2009']},
                {data: dataMap.dataTI['2009']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2009sum']},
                    {name: '第二产业', value: dataMap.dataSI['2009sum']},
                    {name: '第三产业', value: dataMap.dataTI['2009sum']}
                ]}
            ]
        },
        {
            title : {text: '2010全国宏观经济指标'},
            series : [
                {data: dataMap.dataGDP['2010']},
                {data: dataMap.dataFinancial['2010']},
                {data: dataMap.dataEstate['2010']},
                {data: dataMap.dataPI['2010']},
                {data: dataMap.dataSI['2010']},
                {data: dataMap.dataTI['2010']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2010sum']},
                    {name: '第二产业', value: dataMap.dataSI['2010sum']},
                    {name: '第三产业', value: dataMap.dataTI['2010sum']}
                ]}
            ]
        },
        {
            title : {text: '2011全国宏观经济指标'},
            series : [
                {data: dataMap.dataGDP['2011']},
                {data: dataMap.dataFinancial['2011']},
                {data: dataMap.dataEstate['2011']},
                {data: dataMap.dataPI['2011']},
                {data: dataMap.dataSI['2011']},
                {data: dataMap.dataTI['2011']},
                {data: [
                    {name: '第一产业', value: dataMap.dataPI['2011sum']},
                    {name: '第二产业', value: dataMap.dataSI['2011sum']},
                    {name: '第三产业', value: dataMap.dataTI['2011sum']}
                ]}
            ]
        }
    ]
};
this.chart.setOption(option);
            // window.addEventListener("resize", () => {
            //     this.chart.resize();
            // });
            window.onresize = () => {
                this.chart.resize();
                // this.percentCharts.resize();
            }
        },

        //画出热力图
        init() {
           const self = this;//因为箭头函数会改变this指向，指向windows。所以先把this保存
           setTimeout(() => {
              window.addEventListener('resize', function() {
                  self.chart = self.$echarts.init(self.$refs.Echart);
                  self.chart.resize();
              })
           },10)
         },
    }
}
        // tableRowClassName({row, rowIndex}) {
        //     if (rowIndex === 0) {
        //       return 'warning-row';
        //     } else if (rowIndex === 1) {
        //       return 'warning-row';
        //     }else if (rowIndex === 2) {
        //       return 'warning-row';
        //     }
        //     return '';
        // }
</script>

<style scoped type="text/css">
    @import url("//unpkg.com/element-ui@2.13.2/lib/theme-chalk/index.css");
    @import '../../assets/css/icon.css';

    .el-header, .el-footer {
        font-size: 20px;
        color: black;
        text-align: center;
        line-height: 60px;
    }
    .res-textarea/deep/ {
        color: black; margin-top: 30px;box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04)
    }
    .el-card/deep/ {
        box-shadow: 0 8px 12px 0 rgba(0,0,0,.1);
    }
    .el-table/deep/.tableStyle/deep/{
        background-color: #1989fa!important;
        color:#fff;
        font-weight:300;
    }
    .buttonText{
        color: #303133;
        text-align:left;
    }
    /*.clearfix{*/
        /*display: flex;*/
        /*justify-content: center;*/
        /*align:middle;*/
    /*}*/
    .wrap{
        display: flex;
        height: 100%;
        justify-content: center;
        align:middle;
    }
    a:link {color:#000000;}      /* 未访问链接*/
    a:visited {color:#000000;}  /* 已访问链接 */
    a:hover {color: #589ef8;}  /* 鼠标移动到链接上 */
    a:active {color: #589ef8;}  /* 鼠标点击时 */
    .chartsClass {
      padding-left: 1.2rem;
    }
</style>
