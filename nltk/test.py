from pylab import *
# encoding=utf-8
x = arange(-2, 2, 0.001)
y = 3*x*log(x)-1.0/36*exp(-(36.0*x-36.0/exp(1))**4)
plt.plot(x, y)
plt.title(u'beautiful Math')
plt.xlabel(u'x')
plt.ylabel(u'y')
plt.axis([-0.05, 1.2, -1.5, 0.2])
text(0.0, 0.05, r'$f(x)=3x{log}(x)-\frac{1}{36}e^{-(36x-\frac{36}{e})^4}', fontsize=10)
plt.grid(True)
plt.show()