// var utils = require('utils')


module.exports = {
  publicPath: './',
  productionSourceMap: false,
  lintOnSave: false,


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
  //   chainWebpack: config => {
  //
  //     config.module.rules.delete("svg"); //重点:删除默认配置中处理svg,
      // 将 icons 目录排除在 svg 默认规则之外
      // config.module.rule('svg').exclude.add(resolve('src/assets/icon')).end();
      // const svgRule = config.module.rule('svg')
      // svgRule.uses.clear()
      //   const dir = path.resolve(__dirname, 'src/assets/icon');
      //   config.module
      //     .rule('svg-sprite-loader')
      //     .test(/\.svg$/)
      //     .include
      //     .add(resolve(dir) //处理svg目录
      //     .end()
      //     .use('svg-sprite-loader')
      //     .loader('svg-sprite-loader')
      //     .options({
      //       symbolId: 'icon-[name]'
      //     })
      //     .end()
      //     .use('svgo-loader') // 添加 svgo-loader
      //     .loader('svgo-loader')
      //     .tap(options => ({...options, plugins: [{removeAttrs: {attrs: 'fill'}}]})).end()
      //   config.plugin('svg-sprite').use(require('svg-sprite-loader/plugin'), [{plainSprite: true}])
      //   config.module.rule('svg').exclude.add(dir)
      //
      // },
      // const dir = path.resolve(__dirname, 'src/assets/icon');

    //   config.module
    //     .rule('svg-sprite')
    //     .test(/\.svg$/)
    //     .include.add(dir).end() // 包含 icons 目录
    //     .use('svg-sprite-loader').loader('svg-sprite-loader').options({extract: false}).end()
    //     .use('svgo-loader').loader('svgo-loader')
    //     .tap(options => ({...options, plugins: [{removeAttrs: {attrs: 'fill'}}]})).end()
    //   config.plugin('svg-sprite').use(require('svg-sprite-loader/plugin'), [{plainSprite: true}])
    //   config.module.rule('svg').exclude.add(dir) // 其他 svg loader 排除 icons 目录
    //
    // }



}
