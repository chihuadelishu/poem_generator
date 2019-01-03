# -*- coding: utf-8 -*-
# coding: utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import os
import re
import time
import codecs
import argparse

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
BASE_FOLDER = os.path.abspath(os.path.dirname(__file__))
DATA_FOLDER = os.path.join(BASE_FOLDER, 'data')
DEFAULT_FIN = os.path.join(DATA_FOLDER, 'tang.txt')
DEFAULT_FOUT = os.path.join(DATA_FOLDER, 'poem.txt')
reg_noisy = re.compile('[^\u3000-\uffee]')
reg_note = re.compile('(（.*）)') # Cannot deal with （） in seperate lines
# 中文及全角标点符号(字符)是\u3000-\u301e\ufe10-\ufe19\ufe30-\ufe44\ufe50-\ufe6b\uff01-\uffee

def set_arguments():
    parser = argparse.ArgumentParser(description='Pre process')
    parser.add_argument('--fin', type=str, default=DEFAULT_FIN,
                        help='Input file path, default is {}'.format(DEFAULT_FIN))
    parser.add_argument('--fout', type=str, default=DEFAULT_FOUT,
                        help='Output file path, default is {}'.format(DEFAULT_FOUT))
    return parser


if __name__ == '__main__':
    parser = set_arguments()
    cmd_args = parser.parse_args()

    print('{} START'.format(time.strftime(TIME_FORMAT)))

    fd = codecs.open(cmd_args.fin, 'r', 'utf-8')
    fw = codecs.open(cmd_args.fout, 'w', 'utf-8')
    #reg = re.compile('〖(.*)〗')\u3016
    #reg = re.compile('(?<=\\〖)[^\\〗]+')
    text = "〖(.+)〗"
    start_flag = False
    for line in fd:
        line = line.strip()
        if not line or '《全唐诗》' in line or '<http'  in line or '□' in line or line=='\n':
            continue
        elif '〖' in line and '〗' in line:
            if start_flag:
                fw.write('\n')
            start_flag = True
            line = line.decode("utf-8")
            text = text.decode("utf-8")
            #fw.write(line)
            #fw.write('\n')
            g = re.search(text,line)
            if g:
                fw.write(g.group(1))
                fw.write('\n')
            #else:
                # noisy data
                #print(line)
                #continue;
        else:#python preprocess.py
            #print(line)
            line = reg_noisy.sub('', line)
            line = reg_note.sub('', line)
            line = line.replace(' .', '')
            fw.write(line)

    fd.close()
    fw.close()

    print('{} STOP'.format(time.strftime(TIME_FORMAT)))
