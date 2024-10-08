from flask import Flask, request, render_template, jsonify
import pandas as pd
import io

def check(data):
    f = [0] * 9

    f1, f2, f3, f4, f5, f6, f7, f8, f9 = f

    field1 = ["GE60201"]
    field2 = ["GE20701", "GE20401"]
    field3 = ["GE20901", "GE22601"]
    field4_1 = ["6101101","6102101","6104101","6105101","6107101","6109101","6110101","6112101","6115101","6116101","6117101","6117201","6118101","6120101","6120201","6120301","6120401","6121101","6123101","6124101","6125101","6126101","6127101","6127201","6127301","6127401","6127501","6127601","6127701","6128011","GA14201"]
    field4_2 =["GE21201","GE70301"]
    field5 = ["GE60113","GE60123","GE70113","GE70123","GE80113","GE80123"]
    field6_1 = ["1420014"]
    field6_2 = ["GE11112","GE11122","GE71001"]
    field7_1 = ["6401102","6401202","6402102","6402202","6404102","6404202","6405102","6406102","6407102","6408102","6409102","6410102","6410202","6411102","6412102","6413102","6414102","6415102","6415202","6416102","6416202","6417102","6417202","6417302","6418102","6419102","6420102","6420202","6420302","6420402","6420502","6420602","6421102","6421202","6422102","6423102","6423202","6424102","6425102","6426102","6427102","6427202","6427302","6427402","6427502","6427602","6427702","6427802","6427902","6427912","6428012","FH60214",
            "GE12112","GE12122","GE12132","GE12142"]
    field7_3 =["GE51118","GE51128","GE51218","GE51228"]
    field8 = ["GE50712","GE50722","GE50732","GE50812","GE50822","GE50832"]
    field9 = ["GA10201","GE81401","GA10101","GE81301","GE40703"]

    for index, row in data.iterrows():
        if row['科目番号'] in field1:
            f1 +=2
        if row['科目番号'] in field2:
            f2 +=2
        if row['科目番号'] in field3:
            f3 +=2
        if row['科目番号'] in field4_1:
            f4 +=1
        if row['科目番号'] in field4_2:
            f4 +=2
        if row['科目番号'] in field5:
            f5 +=2
        if row['科目番号'] in field6_1:
            f6 +=1
        if row['科目番号'] in field6_2:
            f6 +=2
        if row['科目番号'] in field7_1:
            f7 +=2
        if row['科目番号'] in field7_3:
            f7 +=3
        if row['科目番号'] in field8:
            f8 +=1
        if row['科目番号'] in field9:
            f9 +=2

    result1 = (f'TC基礎は{f1}/2<br>'
               f'情報収集と分析は{f2}/2<br>'
               f'企画設計は{f3}/2<br>'
               f'情報アーキテクチャは{f4}/2<br>'
               f'制作管理・ディレクションは{f5}/2<br>'
               f'デザイン・表現設計は{f6}/2<br>'
               f'ライティングは{f7}/2<br>'
               f'英文ライティングは{f8}/2<br>'
               f'周辺分野は{f9}/2')

    return result1

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "ファイルがアップロードされていません", 400

    file = request.files['file']
    if file.filename == '':
        return "ファイル名が空です", 400

    try:
        df = pd.read_csv(file)

        result = check(df)
        return result

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
