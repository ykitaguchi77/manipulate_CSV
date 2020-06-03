import numpy as np
import matplotlib.pyplot as plt
import time
import os
import copy
import pandas as pd
import csv
from random import randint
from time import sleep
import math

import glob
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import cv2
import codecs

'''
患者リストのうち、測定リストに含まれているものを抜き出すスクリプト
'''


#患者リスト
patient_list = 'C:\\Users\\ykita\\OneDrive\\デスクトップ\\201904_2.csv'

#測定リスト
measurement_list = 'C:\\Users\\ykita\\OneDrive\\デスクトップ\\exams200601.CSV'


with codecs.open(patient_list, "r", "Shift-JIS", "ignore") as file:
    df_patient = pd.read_csv(file, index_col=None, header=0)
    print(df_patient)

with codecs.open(measurement_list, "r", "Shift-JIS", "ignore") as file:
    df_measurement = pd.read_csv(file, index_col=None, header=None)
    #print(df_patient)

measurement = df_measurement.iloc[:,2].values.tolist() #pandasをリストにする
measurement = (list(dict.fromkeys(measurement))[1:]) #重複を削除

patient = df_patient.iloc[:,0].values.tolist()

print(patient)
print(measurement)

#両リストに共通するものを、commonID_listに格納する
commonID_list = []
for i in patient:
    if str(i) in measurement:
        commonID_list.append(i)
print(commonID_list)
print(len(commonID_list))
print(commonID_list[0])

#Patient_listから、commonID_listにIDが含まれているものを抜き出す
row = df_patient[df_patient['id'] == commonID_list[0]]
k=0
for i in commonID_list:
    row = pd.concat([row, df_patient[df_patient['id'] == commonID_list[k]]])
    k+=1
print(row)
row2 = row.drop_duplicates(subset='id') #重複を削除
print(row2)
row3 = row2.iloc[:,0:4] #必要な項目のみ抜き出し

#CSV形式で保存
save_path = 'C:\\Users\\ykita\\OneDrive\\デスクトップ\\corvis_list.csv'
row3.to_csv(save_path, encoding='utf_8_sig')


