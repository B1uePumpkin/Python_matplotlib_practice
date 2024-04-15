import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft YaHei')

# 繪製一組資料點的圓餅圖，加上適當的百分比標籤

# x=[1, 2, 3, 4]
# total=sum(x)
# lables={str(100 * data/total) + '%' for data in x}
# plt.pie(
#     x,
#     labels=lables,
#     labeldistance=0.5
# )
# plt.legend()
# plt.show()

###########################################################################################

import csv
file = open("pie_chart_data.csv", "r", encoding="utf-8")
reader = csv.reader(file)
next(reader)
# for row in reader:
#     print(row)

x=[]
lables=[]
for row in reader:
    x.append(float(row[1]))
    lables.append(row[0])

print(x)
print(lables)

plt.pie(
    x,
    labels=lables,
    autopct='%1.1f%%',
    labeldistance=1.1,
    startangle=90,
    counterclock=False,
    explode=(0, 0.1, 0.1, 0.1, 0.1, 0.1)
)
plt.legend()
plt.title("個瀏覽器市占率")
plt.show()