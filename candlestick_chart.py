import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

'''
範例資料:
    日期, 開盤, 收盤, 最高, 最低
    11/01, 100, 105, 110, 98
    11/02, 105, 110, 120, 100
    11/03, 110, 112, 115, 105
'''

# plt.bar("11/01", 5, bottom=100, color='red', width=0.5)
# plt.bar("11/01", 12, bottom=98, color='red', width=0.1)

# plt.bar("11/02", 5, bottom=105, color='red', width=0.5)
# plt.bar("11/02", 20, bottom=100, color='red', width=0.1)

# plt.bar("11/03", 2, bottom=110, color='red', width=0.5)
# plt.bar("11/03", 10, bottom=105, color='red', width=0.1)
# plt.show()

# csv 數據讀取

import csv
f = open('candlestick_chart_data.csv', encoding='utf-8')
data = csv.reader(f)
header = next(data)
print(header)
for row in data:
    date = row[0]
    open = int(row[1])
    close = int(row[2])
    high = int(row[3])
    low = int(row[4])
    if open > close:
        color = "red"
    else:
        color = "green"
    plt.bar(date,
            abs(close - open),
            bottom=min(close, open),
            color=color,
            width=0.5)
    plt.bar(date,
            high - low,
            bottom=low,
            color=color,
            width=0.1)        
plt.xlabel(header[0])
plt.ylabel(header[1])
plt.show()