# 健康记录助手 - Android APP
## 📱 功能
- 用药记录（记录吃药时间和药名）
- 血压测量记录（收缩压/舒张压）
- 血糖测量记录（数值和时间）
- 拍照保存检查结果
## 🚀 如何打包 APK
### 方法一：GitHub Actions（推荐）
1. 将本项目上传到 GitHub 仓库
2. 在仓库页面点击 **Actions** → **Build Android APK** → **Run workflow**
3. 等待 20-30 分钟
4. 下载生成的 APK 文件
### 方法二：本地 WSL 打包
双击运行 `打包APK.bat` 即可
## 📋 技术栈
- Python + Kivy 框架
- Buildozer 打包工具
- 目标平台：Android (API 21+)
