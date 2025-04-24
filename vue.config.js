const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false // 关闭保存时的lint检查，避免开发时的干扰
}) 