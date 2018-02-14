from matplotlib import pyplot as plt
from matplotlib import style
#style.use('ggplot') # referencing the file matplotlib/style folder.
x = [2,4,6,7,8]
y = [3,3,6,3,6]

x2= [6,4,2,1,0]
y2= [8,6,3,1,0]
plt.bar(x,y, label='first values') # we can switch between plot, scatter or bar to see different types of charts
plt.bar(x2,y2, label='second values')
plt.title('Moji\'s first chart')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.legend()
plt.grid(True, color='k')
plt.show()
