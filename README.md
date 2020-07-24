

## 安装步骤

cd BLN-TIAS    // 进入模板目录
npm install         // 安装项目依赖，等待安装完成之后，安装失败可用 cnpm 或 yarn

// 开启服务器，浏览器访问 http://localhost:8080
npm run serve

// 执行构建命令，生成的dist文件夹放在服务器下即可访问
npm run build

## 更改
### 7.23
避免URL“#” src/router/index.js 添加mode
