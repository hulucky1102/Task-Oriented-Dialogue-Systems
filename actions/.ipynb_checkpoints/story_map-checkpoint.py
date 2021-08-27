import json

with open('../stories/stories_map.json', mode='r', encoding='utf-8') as f:
    stories = json.load(f)

def story2action():
    