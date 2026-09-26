import matplotlib.pyplot as plt

x = [x for x in range(9)]
squares = [1,4,9,16,25,36,49,64,81]
plt.plot(x,squares,linewidth=5)
plt.grid()
plt.show()