import csv
import numpy as np


'''
指定した病名の含まれている行を抽出して新規リストとして出力するスクリプト
病名毎に別のファイルに保存される
'''

#ここに病名をリスト形式で入力
DiseaseList = ['斜視']

data = np.loadtxt("DiseaseInfo_all_connected.csv",       # 読み込みたいファイルのパス
                  delimiter=",", dtype="unicode")  # ファイルの区切り文字

#病名ごとに出力
b=[]
for i in range(len(DiseaseList)):
    a = data[np.any(data== DiseaseList[int(i)], axis=1)]
    np.savetxt('DiseaseInfo_extracted_' + str(DiseaseList[i]) + '.csv', a, delimiter=',', fmt='%s')


#DiseaseInfo_extracted.csvに出力
#np.savetxt('DiseaseInfo_extracted_'+i+'.csv', a, delimiter=',', fmt='%s')