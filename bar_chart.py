import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

# plt.bar([3, 4, 1], [2, 5, 3])
# plt.title('Bar Chart')
# plt.show()

# plt.bar(["B", "A", "C"], [8,10,16], width=0.5, color='pink', alpha=0.5)
# plt.xlabel('Class')
# plt.ylabel('Score')
# plt.show()

# csv 數據讀取
import csv
f = open('bar-chart-data.csv', encoding='utf-8')
data = csv.reader(f)
header = next(data)
x = []
y = []
for row in data:
    x.append(row[0])
    y.append(int(row[1]))
plt.bar(x, y)
plt.xlabel(header[0])
plt.ylabel(header[1])
plt.show()
f.close()

