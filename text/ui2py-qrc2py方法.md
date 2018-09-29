#### 1、导入.ui格式
首先，代开cmd到.ui文件的位置，然后使用一下命令把.ui 格式转换成 .py 格式
```
pyuic5 -x MyWidget.ui -o MyWidget.py1
```

2、导入 .qrc格式

同理，类似。
只是代码是：
```
Pyrcc5 input_file.qrc -o Out_file.py
```