# 老虎web应用文档

### 概述：

本文档描述了一个简单的Web应用程序，

其功能是从用户输入的句子中提取前三个字符，

并在前端页面上显示这些字符。应用分为前端和后端两部分

### 技术栈：

前端：HTML，JavaScript，CSS

后端：Python，Flask，flask_cors

### 前端：

前端页面由HTML构建，使用javaScript处理用户输入和后端的通信
，CSS用于页面的样式设计。

>Words.html:用户界面，包含输入框，提交按钮和结果

### 后端

后端使用Flask框架建立一个简单的服务来处理前端

### 预装库

flask,轻量级web

> pip install flask


flask_cors

> pip install flask_cors

### 可能会遇到的问题

在IDEA中启动app.py后，出现错误

>  * Restarting with stat
     D:\python\python.exe: can't open file 'D:\\python\\PyCharm': [Errno 2] No such file or directory

导致前端发送不了请求，解决办法是在安装文件夹的界面上方地址栏输入cmd，进入终端输入

> python app.py

即可解决问题
