#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class HexoLatexFix(object):
    """用于修复hexo中的latex问题

    主要加上两行,如下
        {% raw %}
        $$ 由一个$或两个$$包括起来的数学公式 $$
        {% endraw %}

    参数
    ------
    fix_file : str
        要修复文件名
    """

    def __init__(self, fix_file):
        super(HexoLatexFix, self).__init__()
        self.fix_file = fix_file

    def load_file(self):
        '''读取要修复的md文件

        返回值
        ------
        _fix_file_str : str
            修复的文件内容全部读取出来的str
        '''
        _fix_file_str = ''
        with open(self.fix_file) as f:
            for eachline in f:
                _fix_file_str += eachline
        return _fix_file_str

    def write_file(self, new_file_str):
        '''将修复的字符串写入新的文件中

        参数
        ------
        new_file_str : str
            已经修复的字符串
        '''
        with open(self.fix_file, 'w') as f:
            f.write(new_file_str)

    def find_next_dollar_pair(self, fix_file_str):
        '''寻找$-$对或者$$-$$对
        '''
        if len(fix_file_str) == 0:
            return False, None
        head = -1
        end = -1

        for inx in range(len(fix_file_str)):
            if fix_file_str[inx] == u'$' and head == -1:
                head = inx
                break

        if head == -1:
            return False, None
        # 跳过连续的$
        jump_head = head + 1
        for inx in range(head + 1, len(fix_file_str)):
            if fix_file_str[inx] == u'$':
                jump_head += 1
            else:
                break
        # 判断寻找下一个有效$结尾
        for inx in range(jump_head, len(fix_file_str)):
            if fix_file_str[inx] == u'$' and end == -1:
                end = inx
                break
        real_end = end + 1
        for inx in range(end + 1, len(fix_file_str)):
            if fix_file_str[inx] == u'$':
                real_end += 1
            else:
                break
        return True, (head, real_end)

    def fix(self):
        '''修复逻辑'''
        u_post_str = self.load_file()
        new_post_str = ''
        ret = True
        while ret == True:
            ret, pos_pair = self.find_next_dollar_pair(u_post_str)
            if ret == True:
                start = pos_pair[0]
                end = pos_pair[1]
                new_post_str += u_post_str[:start] + u"{% raw %}"
                new_post_str += u_post_str[start:end] + u"{% endraw %}"
                u_post_str = u_post_str[end:]
            else:
                new_post_str += u_post_str
        self.write_file(new_post_str)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('用法: python3 %s fix_file' % sys.argv[0])
        sys.exit(-1)
    fix_file = sys.argv[1]

    hexo_fix = HexoLatexFix(fix_file)
    hexo_fix.fix()
    print('Done')
