#!/bin/bash

# 获取当前脚本所在目录并进入该目录
DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$DIR"

echo "=========================================================="
echo "     🚀 开始批量生成所有课程的教务材料 (DOCX + PDF) 🚀"
echo "=========================================================="
echo ""

COURSE_DIR="/Users/yamlam/Downloads/2025-2026-2 课程"
PYTHON_BIN="/opt/anaconda3/envs/mybase/bin/python"

if [ ! -d "$COURSE_DIR" ]; then
    echo "❌ 找不到课程总目录: $COURSE_DIR"
    read -p "按回车键退出..."
    exit 1
fi

# 遍历所有包含 course.yaml 的课程目录
for d in "$COURSE_DIR"/*/; do
    if [ -f "${d}course.yaml" ]; then
        COURSE_NAME=$(basename "$d")
        echo "▶️ 正在处理课程: 【$COURSE_NAME】..."
        "$PYTHON_BIN" scripts/generate.py --course "$COURSE_NAME"
        echo "----------------------------------------------------------"
    fi
done

echo "=========================================================="
echo "           🎉 所有教务材料生成与导出已完成！ 🎉"
echo "=========================================================="
echo ""

# 让终端停留在屏幕上供查看日志
read -p "按回车键关闭窗口..."
