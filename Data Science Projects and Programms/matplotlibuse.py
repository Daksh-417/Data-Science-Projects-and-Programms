import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# xpoints = np.array([1, 2, 6, 8])
# ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

# ypoints = np.array([3, 8, 1, 10, 5, 7])

# plt.plot(ypoints)
# plt.show()

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, marker = 'o')
# plt.show()

# plt.plot(ypoints, marker = '*')
# plt.show()

# plt.plot(ypoints, 'o:r')
# plt.show()

# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()

# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()

# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
# plt.show()

# plt.plot(ypoints, linestyle = "-.")
# plt.show()

# plt.plot(ypoints, color = 'r')
# plt.show()

# plt.plot(ypoints, linewidth = '5')
# plt.show()

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()

# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("Sports Watch Data", fontdict = font1)
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.plot(x, y)
# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data", loc = 'left')
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)
# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# plt.grid()

# plt.show()

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

# plt.show()

#plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)

# plt.show()

#plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 1, 1)
# plt.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 1, 2)
# plt.plot(x,y)

# plt.show()

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 2)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 3)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 4)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 5)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 6)
# plt.plot(x,y)

# plt.show()

# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(1, 2, 1)
# plt.plot(x,y)
# plt.title("SALES")

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(1, 2, 2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.suptitle("MY SHOP")
# plt.show()

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# plt.scatter(x, y)
# plt.show()

# #day one, the age and speed of 13 cars:
# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y)

# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y)

# plt.show()

# x = np.random.randint(100, size=(100))
# y = np.random.randint(100, size=(100))
# colors = np.random.randint(100, size=(100))
# sizes = 10 * np.random.randint(100, size=(100))

# plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')

# plt.colorbar()

# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x,y)
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.barh(x, y)
# plt.show()

# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])

# plt.bar(x, y, width = 0.1)
# plt.show()


# x = np.random.normal(170, 10, 250)

# print(x)

# x = np.random.normal(170, 10, 250)

# plt.hist(x)
# plt.show()

# y = np.array([35, 25, 25, 15])

# plt.pie(y)
# plt.show() 

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels)
# plt.show() 

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels, startangle = 90)
# plt.show() 

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]

# plt.pie(y, labels = mylabels, explode = myexplode)
# plt.show() 

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
# myexplode = [0.2, 0, 0, 0]

# plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
# plt.show() 

# y = np.array([35, 25, 25, 15])
# mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

# plt.pie(y, labels = mylabels)
# plt.legend()
# plt.show() 