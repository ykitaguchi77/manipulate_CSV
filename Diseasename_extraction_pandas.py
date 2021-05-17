import csv
import numpy as np
import os
import os.path
import sys
import glob
import pandas as pd
import codecs

'''
指定した病名の含まれている行を抽出して新規リストとして出力するスクリプト
'''

data_path = 'C:\\Users\\ykita\\PycharmProjects\\FacePhoto\\DiseaseInfo_all_connected.csv'
keyword = ['眼窩腫瘍', '涙腺腫瘍', 'ミクリッツ']

#正規表現のための前処理
byoumei = keyword[0]
j=1
for i in range(len(keyword)-1):
    byoumei = byoumei + '|' + keyword[j]
    j+=1
print(byoumei)

#ファイル名設定のための前処理
byoumei_filename = keyword[0]
j=1
for i in range(len(keyword)-1):
    byoumei_filename = byoumei_filename + '.' + keyword[j]
    j+=1
print(byoumei_filename)



#ファイルを開く　※codec errorを回避
with codecs.open(data_path, "r", "Shift-JIS", "ignore") as file:
    data = pd.read_csv(file, delimiter=",",  header=None)


print(data)



column=4

#指定した病名が含まれるものを列ごとに抽出
list=pd.DataFrame({})
for i in data:
    try:
        extract = data[data[column].str.contains('('+byoumei+')', na=False)]
        list = list.append(extract)
        column+=1
    except AttributeError:
        break

#重複した行を削除
list = list[~list.duplicated()]
#番号順に並び替え
list = list.sort_values([0])

print(list)

list.to_csv('C:\\Users\\ykita\\PycharmProjects\\FacePhoto\\DiseaseInfo_extracted'+byoumei_filename +'.csv'
, encoding='utf_8_sig', index = False, header=False)




