
## 安装步骤

cd BLN-TIAS    // 进入模板目录
npm install         // 安装项目依赖，等待安装完成之后，安装失败可用 cnpm 或 yarn

// 开启服务器，浏览器访问 http://localhost:8080
npm run serve

// 执行构建命令，生成的dist文件夹放在服务器下即可访问
npm run build
```

## 7.20
刘如日完成登陆前的界面，路由是/entry
## 7.23
刘如日修复路由权限，不需要实现登陆即可访问介绍页，且退出登陆或者没有权限一律跳转到介绍首页
## 7.23
刘如日增加deploy.sh，开发者修改之后可以直接运行该发布脚本
该脚本可以自动build且push在github page上然后可以在
 https://kingsunfather.github.io/tias-dev/线上预览变化
## 7.24
后台管理侧边栏目录更改
## 9.3
连接后端获取数据
