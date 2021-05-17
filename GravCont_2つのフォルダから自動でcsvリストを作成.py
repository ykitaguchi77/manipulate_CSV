import pandas as pd
import os
import glob

grav_dir = "C:\\Users\\ykita\\OneDrive\\デスクトップ\\甲状腺眼症_photo_中等症以上のみ"
cont_dir = "C:\\Users\\ykita\\OneDrive\\デスクトップ\\Control_photo_random"
grav = os.listdir(grav_dir)
cont = os.listdir(cont_dir)
print("grav: "+str(len(grav)))
print("cont: "+str(len(cont)))

columns1 = ["image_name", "Label", "Inoue", "kohzaki", "morimoto", "kitaguchi", "kawasaki"]
index1 = list(range(len(grav)+len(cont)))
df = pd.DataFrame(index=index1, columns=columns1)
df.iloc[0:len(grav),0] = os.listdir(grav_dir)
df.iloc[len(grav):len(grav)+len(cont),0] = os.listdir(cont_dir)
df.iloc[0:len(grav),1] = "grav"
df.iloc[len(grav):len(grav)+len(cont),1] = "cont"

for i in range(len(grav+cont)): #拡張子を削除する
    name = df.iloc[i,0]
    df.iloc[i,0] = int(os.path.splitext(name)[0])

pd.set_option('display.max_rows', 800) #省略なしで表示
df = df.sort_values("image_name", ascending=True) #画像番号順に並び替え
df = df.reset_index(drop=True) #indexがばらばらになったので振りなおす
print(df)

#CSVとして出力
df.to_csv("C:\\Users\\ykita\\OneDrive\\デスクトップ\\Hum_eval.csv", encoding="shift_jis")
