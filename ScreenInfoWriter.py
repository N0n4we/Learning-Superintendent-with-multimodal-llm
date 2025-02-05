from screenshot import Screenshot, DescribeScreen
from datetime import datetime
import os

def Shot():
    path, now = Screenshot()
    info, is_entertaining = DescribeScreen(path)
    description = f"\n\n时间：{now.hour}:{now.minute}, 屏幕信息：{info}"
    record_path = os.path.join("record", f'{now.month}-{now.day}.txt')
    if not os.path.exists(os.path.dirname(record_path)):
        os.makedirs(os.path.dirname(record_path))
    with open(record_path, 'a', encoding='utf-8') as file:
        file.write(description)
    return now, is_entertaining