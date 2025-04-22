# 文档分析工具 (DocAnalyzer)

一个基于Vue.js和Flask的文档分析工具，能够上传文档、提取文本、生成AI总结并创建相关图片。本项目使用vivo GPT API进行文本总结和AI绘画生成。

## 功能特点

- 支持上传PDF、Word和TXT文档
- 自动提取文档文本内容
- 使用vivo GPT API生成文本总结
- 使用vivo AI绘画API生成与总结相关的图片
- 文件上传历史记录
- 下载总结和生成的图片

## 项目架构

### 系统架构

```
┌─────────────┐      HTTP      ┌─────────────┐      HTTP      ┌─────────────┐
│   前端      │ ─────────────> │    后端     │ ─────────────> │  vivo API   │
│  (Vue.js)   │ <───────────── │   (Flask)   │ <───────────── │  (GPT/画图) │
└─────────────┘                └─────────────┘                └─────────────┘
      │                              │
      │                              │
      ▼                              ▼
┌─────────────┐            ┌─────────────────┐
│  用户浏览器  │            │ 文件存储/历史记录 │
└─────────────┘            └─────────────────┘
```

### 模块关系

- **前端(Vue.js)**: 负责用户界面，通过API与后端交互
- **后端(Flask)**: 处理文件上传、文本提取、API调用和数据存储
- **vivo API**: 提供AI文本总结和图像生成能力
- **文件存储**: 在后端服务器保存上传文件和生成历史

### 技术栈

- **前端**: Vue.js 3, Vue Router, Vuex, Element Plus, Axios
- **后端**: Flask, PyPDF2, python-docx, Flask-CORS
- **API**: vivo GPT API, vivo AI绘画API
- **开发工具**: Git, NPM, Pip

## 项目结构

```
DocAnalyzer/
├── backend/                # Flask后端
│   ├── uploads/            # 上传文件存储
│   │   └── history.json    # 历史记录文件
│   ├── app.py              # 主应用文件
│   ├── auth_util.py        # API认证工具
│   ├── test_upload.py      # 文件上传测试脚本
│   └── requirements.txt    # Python依赖
│
└── frontend/               # Vue.js前端
    ├── src/
    │   ├── assets/         # 静态资源
    │   ├── components/     # 组件
    │   ├── views/          # 页面
    │   ├── router/         # 路由
    │   ├── store/          # 状态管理
    │   ├── App.vue         # 根组件
    │   └── main.js         # 入口文件
    ├── public/             # 公共文件
    └── package.json        # 前端依赖
```

## 安装步骤

### 后端

1. 安装Python依赖
```bash
cd DocAnalyzer/backend
pip install -r requirements.txt
```

如果没有依赖文件，请安装以下包：
```bash
pip install flask flask-cors PyPDF2 python-docx requests
```

2. 运行Flask应用（注意使用端口5001，避免与Mac系统服务冲突）
```bash
python app.py
```

服务器将在 http://localhost:5001 上运行

### 前端

1. 安装依赖
```bash
cd DocAnalyzer/frontend
npm install
```

2. 运行开发服务器
```bash
npm run serve
```

3. 构建生产版本
```bash
npm run build
```

## 使用说明

1. 打开浏览器访问http://localhost:8080（前端）
2. 上传文档（支持PDF、Word和TXT）
3. 上传完成后选择是否立即分析
4. 在分析页面查看文档总结
5. 点击"生成图片"按钮创建AI绘画
6. 下载总结或图片

## API接口

- `POST /upload` - 上传文件
- `GET /history` - 获取上传历史
- `GET /analyze/<file_id>` - 分析文件
- `POST /generate-image` - 生成图片
- `GET /task-status/<task_id>` - 查询任务状态

## 测试

项目包含测试脚本以验证后端API功能：

```bash
cd DocAnalyzer/backend
python test_upload.py
```

测试脚本会：
1. 创建一个测试文本文件
2. 上传到后端服务
3. 获取上传历史
4. 测试文件分析接口
5. 清理测试文件

测试成功会显示详细的请求和响应信息。

## 故障排除

- **端口冲突**: 默认情况下，Flask使用端口5001（避免与Mac系统AirTunes冲突）。如果端口已被占用，请修改`app.py`中的端口号。
- **连接拒绝**: 确保Flask服务器正在运行。
- **依赖错误**: 确保所有依赖已正确安装，可能需要使用`pip3`而不是`pip`。
- **API错误**: 检查vivo API配置是否正确（APP_ID和APP_KEY）。

## 注意事项

- 文件大小限制为16MB
- 仅支持PDF、Word和TXT文件格式
- 需要有效的vivo GPT API密钥和AI绘画API密钥 