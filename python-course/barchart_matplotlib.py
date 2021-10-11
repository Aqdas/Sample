import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [1500,1200,1100,1800]
#plt.plot(x,y)
legend = ["January", "February", "March", "April"]
plt.xticks(x, legend)
plt.bar(x,y)
plt.title("Monthly Sales")
plt.ylabel("This chart is for sales")
plt.show()