import json
from collections import Counter

with open('/home/ai/hgm/Smart_Home/stories/stories_map.json', mode='r', encoding='utf-8') as f:
    stories = json.load(f)

def story2action(story, stories):

    flag = 0
    action = []
    for val in stories:
        if Counter(val['storys'][1]) == Counter(story[1]) and Counter(val['storys'][0]) == Counter(story[0]):
            flag += 1
            return val['action'], flag
        elif Counter(val['storys'][1]) == Counter(story[1]) and Counter(val['storys'][0][-1]) == Counter(story[0]):
            flag += 1
            return val['action'], flag
            pass

    return action, flag