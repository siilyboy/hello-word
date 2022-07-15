# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :hex_utf.py
# @Time      :2022/7/13 16:57
# @Author    :kang


import codecs
hex_chinese = 'E59FBAE7AB99E5908DE7A7B0'
result_str = codecs.decode(hex_chinese.encode('utf-8'),"hex").decode('utf-8')
print(result_str)

chinese = '中国人不骗中国人'
# 字符串生成十六进制
hex_chinese = chinese.encode('utf-8')
print(f'==>中文转成十六进制的结果为：{hex_chinese}')
hex_chinese = hex_chinese.hex()
print(f'==>中文转成十六进制的结果为：{hex_chinese}')