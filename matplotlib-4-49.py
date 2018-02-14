from matplotlib import pyplot as plt
from matplotlib import style
#style.use('ggplot') # referencing the file matplotlib/style folder.
x = [2,4,6,7,8]
y = [3,3,6,3,6]

x2= [6,4,2,1,0]
y2= [8,6,3,1,0]
plt.plot(x,y,'g',linewidth=5, label='first values') # [x],[y] (some inline styles)
plt.plot(x2,y2,'b', linewidth=2, label='second values')
plt.title('Moji\'s first chart')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.legend()
plt.grid(True, color='k')
plt.show()
