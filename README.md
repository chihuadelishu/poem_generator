0、注意中文字符的处理：
1、路径和读取的文件名称中不能有中文
2、全部使用utf-8编码，代码前面加：
# -*- coding: utf-8 -*-
# coding: utf-8
import sys
#重新加载sys模块
reload(sys)
#重新设置字符集
sys.setdefaultencoding("utf-8")
3、注意异常的处理，比如数学计算和关键字取不到的情况
4、如何满足诗句字数的要求
5、注意line的切分和正则表达式的使用

python preprocess.py
python get_collocations.py
python get_topic.py
python get_start_words.py


In `./data` folder, there is a corpus file "唐诗语料库.txt", and some data files will be generated here.
