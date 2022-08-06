import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class conic:

    def __init__(self):
        mpl.rcParams['axes.prop_cycle'] = mpl.cycler('color', ['k'])
        x_axis_x = [-40, 40]
        x_axis_y = [0, 0]

        y_axis_y = [-40, 40]
        y_axis_x = [0, 0]

        plt.plot(x_axis_x, x_axis_y, color = 'k')
        plt.plot(y_axis_x, y_axis_y, color = 'k')

        plt.grid(True)
        plt.title("shat")

    def show(self):
        plt.show()

    def axes(self):
        plt.axhline(0, alpha=.1)
        plt.axvline(0, alpha=.1)
    
    def right_parabola(self, a, h, k):
        #a=5.0
        x = np.linspace(-40, 40, 400)
        y = np.linspace(-40, 40, 400)
        x, y = np.meshgrid(x, y)
        self.axes()
        plt.contour(x+h, y+k, (y**2 - 4*a*x), [0], colors = 'k')

    def left_parabola(self, a, h, k):
        #a=5.0
        x = np.linspace(-40, 40, 400)
        y = np.linspace(-40, 40, 400)
        x, y = np.meshgrid(x, y)
        self.axes()
        plt.contour(x+h, y+k, (y**2 + 4*a*x), [0], colors = 'k')

    def up_parabola(self, a, h, k):
        #a=5.0
        x = np.linspace(-40, 40, 400)
        y = np.linspace(-40, 40, 400)
        x, y = np.meshgrid(x, y)
        self.axes()
        plt.contour(x+h, y+k, (x**2 - 4*a*y), [0], colors = 'k')

    def down_parabola(self, a, h, k):
        #a=5.0
        x = np.linspace(-40, 40, 400)
        y = np.linspace(-40, 40, 400)
        x, y = np.meshgrid(x, y)
        self.axes()
        plt.contour(x+h, y+k, (x**2 + 4*a*y), [0], colors = 'k')

    def ellipse_circle(self, a, b, h, k):
        x = np.linspace(-40, 40, 400)
        y = np.linspace(-40, 40, 400)
        x, y = np.meshgrid(x, y)
        self.axes()
        plt.contour(x+h, y+k,(x**2/a**2 + y**2/b**2), [1], colors='k')

    def hyperbola(self, a, b, h, k):
        x = np.linspace(-40, 40, 400)
        y = np.linspace(-40, 40, 400)
        x, y = np.meshgrid(x, y)
        self.axes()
        plt.contour(x+h, y+k,(x**2/a**2 - y**2/b**2), [1], colors='k')




#a = conic()
#a.hyperbola(8., 4., 10, 10)
#a.show()
