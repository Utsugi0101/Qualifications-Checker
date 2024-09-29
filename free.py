import pandas as pd

# CSVファイルを読み込み（エンコーディングを指定）
data = pd.read_csv('./imformation exercises.csv', encoding='ISO-8859-1')  # または 'shift_jis' に変更

# 1行目を表示して確認
first_column_list = data.iloc[:, 0].tolist()
first_column_str = ','.join(f'"{str(item)}"' for item in first_column_list)

print(first_column_str)
