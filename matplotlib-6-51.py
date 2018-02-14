from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
#style.use('ggplot') # referencing the file matplotlib/style folder.
x,y = np.loadtxt('sampletxt-part-51.txt' , unpack=True , delimiter =',') # instead of txt file we can simply use csv file.

plt.plot(x,y)

plt.title('Moji\'s first chart')
plt.ylabel('Y Axis')
plt.xlabel('X Axis')
plt.legend()
plt.grid(True, color='k')
plt.show()
