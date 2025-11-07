# gpt1

1、创建一个conda环境

`conda create -n gpt1 python=3.10`

2、激活conda环境

`conda activate gpt1`

3、安装 tensorflow

第一种情况：如果你的显卡不是50系的直接运行下面的命令

`pip install tensorflow[and-cuda]`

第二种情况：如果你的显卡是50系，请手动安装，依次运行下面的命令

whl文件可以通过下面的链接下载：
https://drive.google.com/file/d/1HEQDH1LiGCvZ7RIGIqEunIqSAkIVIPaj/view?usp=drive_link

`pip install tf_nightly-2.20.0.dev0+selfbuilt-cp310-cp310-linux_x86_64.whl -i https://mirrors.aliyun.com/pypi/simple/`

`ln -sf /usr/lib/x86_64-linux-gnu/libstdc++.so.6 /home/你的地址/anaconda3/envs/gpt1/bin/../lib/libstdc++.so.6`

4、安装需要的库

```
pip install tqdm -i https://mirrors.aliyun.com/pypi/simple/
pip install joblib -i https://mirrors.aliyun.com/pypi/simple/
pip install scikit-learn -i https://mirrors.aliyun.com/pypi/simple/
pip install pandas -i https://mirrors.aliyun.com/pypi/simple/
pip install ftfy -i https://mirrors.aliyun.com/pypi/simple/
pip install spacy -i https://mirrors.aliyun.com/pypi/simple/
python -m spacy download en_core_web_sm
```

5、运行代码

`python train.py --dataset rocstories --desc rocstories --submit --analysis`
