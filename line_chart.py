import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft YaHei')


"""
(1,2), (2,4), (3,6), (4,8)
"""
# plt.plot([1, 2, 3, 4], [2, 4, 6, 8])
# plt.show()


"""
(1,2), (2,4), (3,6), (4,8)
(1,3), (2,5), (3,7), (4,9)
"""
# plt.plot([1, 2, 3, 4], [[2, 3], [4, 5], [6, 7], [8, 9]], label=['line 1', 'line 2'])
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()


# include csv file
import csv
file=open('line_chart_data.csv', encoding='utf-8')
csvreader = csv.reader(file)

header = next(csvreader)
print(header)

x=[]
y=[]
for row in csvreader:
    print(row)
    x.append(int(row[0]))
    y.append([int(row[1]), int(row[2])])

plt.plot(x, y, label=header[1:3])
plt.legend()
plt.xlabel('year')
plt.ylabel('salary')
plt.show()