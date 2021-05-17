import csv
import numpy as np
import os
import os.path
import sys
import glob

'''
指定したフォルダにあるファイル(写真）番号に対応したリストをDiseaseInfo_modified1.1
から抽出して新しいCSVファイルを作成するスクリプト
'''

path = 'C:\\Users\\ykita\\OneDrive\\デスクトップ\\甲状腺眼症'
output_path = 'C:\\Users\\ykita\\PycharmProjects\\FacePhoto\\甲状腺眼症_new.csv'


#まずはpathのファイル内のファイル名を抜き出す
list = os.listdir(path)
namelist = []

#namelistに症例番号を追加
for i in list:
    l = i.split('.')[0]
    namelist.append(str(l))

outlist = []
with open("DiseaseInfo_modified1.1.csv", 'r', newline='') as f:
    r = csv.reader(f)

    for l in r:
        if l[0] in namelist:
            #print(l)
            outlist.append(l)


#csvfileに出力
with open(output_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(outlist)

