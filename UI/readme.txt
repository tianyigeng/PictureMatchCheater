需要安装以下几个python库：
pywin32：http://sourceforge.net/projects/pywin32/files/?source=navbar
pymouse：https://github.com/SavinaRoja/PyUserInput/wiki/Installation
pil：http://www.pythonware.com/products/pil/


运行UI.py前，先运行cmd，执行：【pip install PyUserInput】，安装pymouse

每块连连看的大小和总个数初始已定义

getOrigin()
得到左上角那块连连看的左上角和右下角那块的右下角在屏幕上的位置

getPic()
抓取连连看区域的图片

pause()
暂停，考虑到搜索解答时可能较耗费时间，可以在抓取图片后先暂停游戏；待找到解答后，再次pause()即可继续

click(pos)
输入目标连连看的坐标（左上(0,0)，右下(13,9)）,点击目标块

test部分用于测试，可保存抓取的图片
