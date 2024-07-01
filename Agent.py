from screenshot import request, packMessages
from ScreenInfoWriter import Shot
import os

def checkScreen():
    now, is_entertaining = Shot()
    if is_entertaining == False:
        return None

    screenshot_path = os.path.join("screenshot", f"{now.month}-{now.day}", f"{now.hour}-{now.minute}.png")
    record_path = os.path.join("record", f'{now.month}-{now.day}.txt')

    with open(os.path.join("memory", 'AgentCharacter.txt'), 'r', encoding='utf-8') as file:
        AgentCharacter = file.read()
    with open(os.path.join("memory", 'UserPersonality.txt'), 'r', encoding='utf-8') as file:
        UserPersonality = file.read()
    with open(os.path.join("memory", 'Matters.txt'), 'r', encoding='utf-8') as file:
        Matters = file.read()
    with open(os.path.join("memory", 'Thoughts.txt'), 'r', encoding='utf-8') as file:
        Thoughts = file.read()
    with open(record_path, 'r', encoding='utf-8') as file:
        record = file.read()
    with open(os.path.join('prompt', 'replyPrompt.txt'), 'r', encoding='utf-8') as file:
        replyPrompt = file.read()

    replyPrompt = replyPrompt.format(**locals())

    messages = packMessages(replyPrompt, screenshot_path)
    reply = request(messages)
    return reply
