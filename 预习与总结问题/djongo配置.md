# mvc

## 高内聚，低耦合

模块内代码精密联系，模块之间关联度低。



## 虚拟环境

pip install -i https://pypi.douban.com/simple django==2.2.5

windows 稍微有一点区别, 就是把 pip install virtualenvwrapper 命令改为 pip install virtualenvwrapper-win



## setting



### BASE_DIR

根据setting.py位置变化而变化：

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

作用#Build paths inside the project like this: os.path.join(BASE_DIR, ...)

