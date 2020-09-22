# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 19:00:51 2019

@author: yyw
"""
from googletrans import Translator
translator = Translator()
print(translator.translate('hi',dest='ko').text)
