发现自己总是刷b站
于是做的**AI督学脚本**

运行MessageBox.py启动每20分钟一次的屏幕检查
发现摸鱼则弹窗提示

memory用来存人物设定，prompt用来存任务设定，可以随意制定

注：本仓库用的是openrouter，apikey自备，在screenshot.py中填写

关于为什么使用command-r-plus作为判别模型————因为只有command-r-plus能按照提示词中规定的格式输出，直接用claude-3.5-sonnet的话说不定会输出除了"是"或"否"以外的字符，无法识别
