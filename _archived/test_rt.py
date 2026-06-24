from docxtpl import RichText
rt = RichText()
rt.add("测试", font="SimSun", size=24)
print(rt.xml)
