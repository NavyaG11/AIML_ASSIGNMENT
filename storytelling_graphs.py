import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 30]

plt.bar(labels, values)
plt.title("Bar Chart Example")
plt.show()

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()

plt.hist(values)
plt.title("Histogram Example")
plt.show()