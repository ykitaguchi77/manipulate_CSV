import csv
import numpy as np
import os
import os.path
import sys
import glob
import pandas as pd
import codecs

'''
IDMap（匿名連結リスト）と匿名化されたリストを参照し、
匿名化されたリストのD列にIDを記入するスクリプト
'''


anonymus_path = 'C:\\Users\\ykita\\PycharmProjects\\FacePhoto\\DiseaseInfo_modified1.1.csv'
connection_path = 'C:\\Users\\ykita\\PycharmProjects\\FacePhoto\\20190910143919_IDMap.csv'
output_path = 'C:\\Users\\ykita\\PycharmProjects\\FacePhoto\\DiseaseInfo_modified1.1_connected.csv'

#各ファイルを開く　※codec errorを回避
with codecs.open(anonymus_path, "r", "Shift-JIS", "ignore") as file:
    data_anonymus = pd.read_csv(file, delimiter=",", header=None)

with codecs.open(connection_path, "r", "Shift-JIS", "ignore") as file:
    data_connection = pd.read_csv(file, delimiter=",", header=None)

#ファイルの前5列を表示させることにより一応確認
#print(data_anonymus.head())
#print(data_connection.head())

#2つのファイルを連結する
data_merge = pd.merge( data_connection, data_anonymus, how="inner" ,on=data_anonymus.index[1])

#csvを出力
data_merge.to_csv(output_path, encoding='utf_8_sig', index = False, header=False)



