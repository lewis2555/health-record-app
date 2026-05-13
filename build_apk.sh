#!/bin/bash
set -e
echo "=========================================="
echo "🚀 开始打包健康记录 APP"
echo "=========================================="
# 更新系统
echo "[1/7] 更新系统..."
sudo apt update && sudo apt upgrade -y
# 安装依赖
echo "[2/7] 安装基础依赖..."
sudo apt install -y python3 python3-pip python3-venv     git curl wget unzip openjdk-17-jdk autoconf libtool     libncurses5 libncurses5-dev zlib1g zlib1g-dev     libssl-dev libffi-dev libbz2-dev liblzma-dev     build-essential libsqlite3-dev
# 设置 Java 环境
echo "[3/7] 配置 Java 环境..."
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
export PATH=$JAVA_HOME/bin:$PATH
# 安装 Buildozer
echo "[4/7] 安装 Buildozer..."
pip3 install --upgrade pip
pip3 install buildozer cython
# 初始化 Buildozer
echo "[5/7] 初始化 Buildozer 环境..."
buildozer init
# 下载 Android SDK 和 NDK
echo "[6/7] 下载 Android SDK 和 NDK (这可能需要 10-20 分钟)..."
buildozer android debug
# 正式打包
echo "[7/7] 开始编译 APK..."
buildozer -v android debug
echo "=========================================="
echo "✅ 打包完成！"
echo "=========================================="
# 显示生成的 APK
if [ -d "bin" ]; then
    echo "📱 APK 文件位置:"
    ls -lh bin/*.apk
else
    echo "⚠️ 未找到 bin 目录"
fi
