# cefpython浏览器

#### 介绍
用pythoninstall cefpython打包exe，制作自己的浏览器，

#### 软件架构
 PyInstaller: 3.4
 Python: 3.5.4
 Platform: Windows-10-10.0.17763-SP0


#### 打包操作

1. 运行pythoninstaller.py

#### 可能会报错的地方

1. Microsoft visual c++ 14.0 is required问题
解决办法：解压目录下的Microsoft Visual C++ 14.0.rar，并安装（csdn花积分下载的，请叫我雷锋）

### 配置自己的窗口标题和默认打开页面
 **这里注意打包完成后，把目录中的config.ini复制到build中，否则启动报错** 

config.ini里面就是自定义口标题和默认打开页面的url

## 截图
![输入图片说明](https://images.gitee.com/uploads/images/2019/0519/150218_c1c02506_24891.png "微信截图_20190519150151.png")

#### 参与贡献

1. https://github.com/cztomczak/cefpython/blob/master/examples/pyinstaller/README-pyinstaller.md



#### 青苗科技

1. 更多资料请访问www.qingmiaokeji.cn
2. 有问题请加微信qingmiaogu