import re

with open("/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/course_assessment.yaml", "r", encoding="utf-8") as f:
    text = f.read()

# Replace practice_theme
text = re.sub(r"\*\*一、创作主题:\*\*\n\n\s*", "", text)
# Replace 价值意义
text = re.sub(r"\*\*【价值意义】\*\*\n\n\s*", "", text)
# Replace 表现方式与思路
text = re.sub(r"\*\*【表现方式与思路（二选一）】\*\*\n\n\s*", "", text)
# Replace 题目基本要求
text = re.sub(r"\*\*二、题目基本要求:\*\*\n\n\s*", "", text)
# Replace 结果呈现方式
text = re.sub(r"\*\*三、结果呈现方式：\*\*\n\n\s*", "", text)
# Replace 提交时间
text = re.sub(r"\*\*四、提交时间：\*\*\n\n\s*", "", text)
# Replace 提交途径
text = re.sub(r"\*\*五、提交途径：\*\*\n\n\s*", "", text)
# Replace 其他说明
text = re.sub(r"\*\*六、其他说明：\*\*\n\n\s*", "", text)

# There are also some in-line bold text like:
# (a) **完全手绘的方式**：
# (b) **使用数据的方式**：
# We can leave them, the deep_clean will handle them if they don't cause duplicate titles.

with open("/Users/yamlam/Downloads/2025-2026-2 课程/信息可视化/course_assessment.yaml", "w", encoding="utf-8") as f:
    f.write(text)

print("YAML fixed.")
