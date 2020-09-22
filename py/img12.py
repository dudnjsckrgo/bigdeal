# -*- coding: utf-8 -*-
import random

import os 

from PIL import Image



# 각 이미지 사이즈 45 x 45

# 새로만들 이미지 사이즈.  -> 가로로 세장 붙이기. 135 x 45

result_width = 135

result_height = 45



# input 파일 path 

input_path_1 = 'C:\Users\yyw\.spyder-py3'

input_path_2 = r'E:\deep_learning\handwrittenmathsymbols\data\test\2'

oper_path = r'E:\deep_learning\handwrittenmathsymbols\data\test\+'



# path 폴더 안의 파일 리스트 가져오기.

file_list_input_1 = os.listdir(input_path_1)

file_list_input_2 = os.listdir(input_path_2)

file_list_oper = os.listdir(oper_path)



# 파일 폴더별 파일 개수 저장.

random_input_1 = len(file_list_input_1)

random_input_2 = len(file_list_input_2)

random_input_oper = len(file_list_oper)



#파일_리네임_변수

idx = 0



# 랜덤으로 파일 100개 생성.

for i in range(100):

    idx += 1



    # 1 ~ 파일 개수 사이의 랜덤 넘버 생성. 

    random_num_input_1 =  random.randrange(0,random_input_1)

    random_num_input_2 =  random.randrange(0,random_input_2)

    random_num_input_oper =  random.randrange(0,random_input_oper)



    # 각 파일의 이미지 불러오기.

    input_img_1 = Image.open(r'E:\deep_learning\handwrittenmathsymbols\data\test\1\1_{0}.jpg'.format(random_num_input_1))

    inpit_oper_img = Image.open(r'E:\deep_learning\handwrittenmathsymbols\data\test\+\+_{0}.jpg'.format(random_num_input_2))

    input_img_2 = Image.open(r'E:\deep_learning\handwrittenmathsymbols\data\test\2\2_{0}.jpg'.format(random_num_input_oper))



    # 흑백이미지 생성 및 이미지 가로로 붙이기.

    result = Image.new("L",(result_width, result_height))

    result.paste(im=input_img_1, box=(0, 0))

    result.paste(im=inpit_oper_img, box=(45, 0))

    result.paste(im=input_img_2, box=(90, 0))



    # 이미지 저장.

    result.save(r'E:\deep_learning\handwrittenmathsymbols\data\new_img\1_2_+\1_2_+_{0}.jpg'.format(idx))