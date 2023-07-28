from matplotlib import pyplot as plt
from mpl_toolkits import basemap

x_werte = (1, 2, 3, 4, 5, 6)
y_werte = (2, 2, 3, 3, 4, 5)

plt.xkcd()

plt.plot(x_werte, y_werte)
# plt.scatter(x_werte, y_werte)
# plt.bar(x_werte, y_werte, 0.5)

plt.title('Ein erster Test')
plt.xlabel('X-Werte')
plt.ylabel('Y-Werte')

plt.show()
