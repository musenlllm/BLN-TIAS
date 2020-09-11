// var utils = require('utils')
const path = require("path");
function resolve(dir) {
  return path.join(__dirname,'.', dir);
}

module.exports = {
  publicPath: './',
  productionSourceMap: false,
  lintOnSave: false,

  // chainWebpack: config => {
  //   config.module
  //     .rule('svg')
  //     .test(/\.(png|jpe?g|gif|svg)(\?.*)?$/)
  //     .exclude.add(resolve('src/assets/icon'))
  //     .end()
  //     .use('url-loader')
  //     .loader('url-loader')
  //     .options({
  //       limit: 10000,
  //       name: utils.assetsPath('img/[name].[hash:7].[ext]')
  //     })
  //
  //   config.module
  //     .rule('icons')
  //     .test(/\.svg$/)
  //     .include.add(resolve('src/assets/icon'))
  //     .end()
  //     .use('svg-sprite-loader')
  //     .loader('svg-sprite-loader')
  //     .options({
  //       symbolId: 'icon-[name]'
  //     })
  //     // .end();
  // }
  // "lintOnSave": false,
  // "transpileDependencies": [
  //   "vuetify"
  // ],
  // chainWebpack: config => {
  //   const svgRule = config.module.rule('svg')
  //   // 清除已有的所有 loader。
  //   // 如果你不这样做，接下来的 loader 会附加在该规则现有的 loader 之后。
  //   svgRule.uses.clear()
  //   svgRule
  //       .test(/\.svg$/)
  //       .include.add(path.resolve(__dirname, 'src/assets/icon'))
  //       .end()
  //       .use('svg-sprite-loader')
  //       .loader('svg-sprite-loader')
  //       .options({
  //         symbolId: 'icon-[name]'
  //       })
  //   const fileRule = config.module.rule('file')
  //   fileRule.uses.clear()
  //   fileRule
  //       .test(/\.svg$/)
  //       .exclude.add(path.resolve(__dirname, 'src/assets/icon'))
  //       .end()
  //       .use('file-loader')
  //       .loader('file-loader')
  // }



}
