import csv
import numpy as np
import os


'''
ダウンロードした画像ファイルのidが長すぎるので、
対応した番号(1, 2, 3...)にフォルダ名を振りなおすscript
'''

#Diseaseinfo_modified.csvから、Bの列の情報を抜き出す


data = np.loadtxt("DiseaseInfo_modified1.1.csv",       # 読み込みたいファイルのパス
                  delimiter=",", dtype="unicode")  # ファイルの区切り文字


#目的パスにあるフォルダの名前を書き換える
for i in range(0, data.shape[0]):
    #print('E:\\眼位写真\\Files\\' + str(data[i, 1]))
    #print(os.path.exists('E:\\眼位写真\\Files\\' + str(data[i,1])))

    try:
        os.rename('E:\\眼位写真\\Files\\' + str(data[i,1]), 'E:\\眼位写真\\Files\\' + str(data[i,0]))
    except FileNotFoundError:
        print(str(data[i,1]) + 'のフォルダが見つかりませんでした')



