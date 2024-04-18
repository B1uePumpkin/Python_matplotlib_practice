import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft YaHei')

"""
    一組資料點
    (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)
"""

# plt.scatter([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], c='red', s=100)
# plt.show()

"""
兩組資料點
    (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6)
"""

# plt.scatter([1, 2, 3, 4, 5], [1, 4, 9, 16, 25], c='red', s=100, label='red')
# plt.scatter([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], c='blue', s=100, label='blue')
# plt.legend()
# plt.show()

"""
csv檔案
"""

import csv
file=open('scatter_chart_data.csv', encoding='utf-8')
reader=csv.reader(file)
next(reader)

data={
    "男":{'x':[], 'y':[]},
    "女":{'x':[], 'y':[]}
}
for row in reader:
    gender=row[0]
    data[gender]['x'].append(int(row[1]))
    data[gender]['y'].append(int(row[2]))
print(data)

plt.scatter(data['男']['x'], data['男']['y'], c='blue', s=100, label='男')
plt.scatter(data['女']['x'], data['女']['y'], c='red', s=100, label='女')
plt.legend()
plt.show()