import pyautogui
from datetime import datetime
import os
import requests
import json
import base64


OPENROUTER_API_KEY = "your_api_key"
describePrompt = """屏幕上有什么？使用者（请称呼“主人”）正在干什么？（请简短回复）"""

# 捕获整个屏幕
def Screenshot():
	screenshot = pyautogui.screenshot()
	now = datetime.now()
	save_path = os.path.join("screenshot", f"{now.year}_{now.month}-{now.day}_{now.hour}-{now.minute}.png")
	screenshot.save(save_path)
	return save_path, now


def request(messages, model_name="anthropic/claude-3.5-sonnet"):
	response = requests.post(
		url="https://openrouter.ai/api/v1/chat/completions",
		headers={
			"Authorization": f"Bearer {OPENROUTER_API_KEY}",
		},
		data=json.dumps({
			"model": model_name,
			"messages": messages
		})
	)
	reply = response.json()['choices'][0]['message']['content']
	return reply

def packMessages(prompt, screenshot_path=None, messages=[]):
	if screenshot_path is None:
		messages.append({
			"role": "user",
			"content": [
				{
					"type": "text",
					"text": prompt
				}
			]
		})
	else:
		with open(screenshot_path, "rb") as image_file:
			encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
		messages.append({
			"role": "user",
			"content": [
				{
					"type": "text",
					"text": prompt
				},
				{
					"type": "image_url",
					"image_url": {"url": f"data:image/png;base64,{encoded_image}"}
				}
			]
		})
	return messages


def DescribeScreen(screenshot_path):
	messages = packMessages(describePrompt, screenshot_path)
	reply = request(messages)
	messages = packMessages(f"描述如下\n\"{reply}\"\n根据描述判断，主人有没有在进行娱乐活动。只回答“是”或“否”")
	is_entertaining = "是"
	retries = 0
	while isinstance(is_entertaining, str):
		if retries == 5:
			is_entertaining = True
			break
		else:
			retries += 1
		is_entertaining = request(messages, model_name="cohere/command-r-plus")
		if is_entertaining == "是":
			is_entertaining = True
		elif is_entertaining == "否":
			is_entertaining = False
	return reply, is_entertaining
