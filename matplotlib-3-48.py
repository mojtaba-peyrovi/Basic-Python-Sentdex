from matplotlib import pyplot as plt
from matplotlib import style
#style.use('ggplot') # referencing the file matplotlib/style folder.
x = [2,4,6,7,8]
y = [3,3,6,3,6]

plt.plot(x,y,'g',linewidth=5) # [x],[y] (some inline styles)
plt.title('Moji\'s first chart')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.show()
