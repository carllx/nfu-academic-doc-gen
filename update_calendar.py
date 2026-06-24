from ruamel.yaml import YAML

yaml = YAML()
yaml.preserve_quotes = True

with open('/Users/yamlam/Downloads/2025-2026-2 课程/交互产品开发/course_calendar.yaml', 'r', encoding='utf-8') as f:
    data = yaml.load(f)

for item in data['calendar']:
    week = item['week']
    lessons = item.get('lessons', [])
    if week == 1:
        lessons[0]['steps'][0]['minutes'] = 20
        lessons[1]['steps'][0]['minutes'] = 25
        lessons[2]['steps'][0]['minutes'] = 20
    elif week == 5:
        lessons[0]['steps'][0]['minutes'] = 5
        lessons[0]['steps'][1]['minutes'] = 10
        lessons[0]['steps'][2]['minutes'] = 5
        lessons[0]['steps'][3]['minutes'] = 5
        
        lessons[1]['steps'][0]['minutes'] = 5
        lessons[1]['steps'][1]['minutes'] = 15
        lessons[1]['steps'][2]['minutes'] = 5
        
        lessons[2]['steps'][0]['minutes'] = 10
        lessons[2]['steps'][1]['minutes'] = 5
        lessons[2]['steps'][2]['minutes'] = 5
        
        lessons[3]['steps'][0]['minutes'] = 10
        lessons[3]['steps'][1]['minutes'] = 5
        lessons[3]['steps'][2]['minutes'] = 5
    elif week == 6:
        lessons[2]['steps'][0]['minutes'] = 70
    elif week == 7:
        lessons[2]['steps'][0]['minutes'] = 70
    elif week == 11:
        lessons[0]['steps'][1]['minutes'] = 25
        lessons[2]['steps'][2]['minutes'] = 40
    elif week == 14:
        lessons[0]['steps'][2]['minutes'] = 100

with open('/Users/yamlam/Downloads/2025-2026-2 课程/交互产品开发/course_calendar.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(data, f)
