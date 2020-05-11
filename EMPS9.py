import math as maths
import numpy as np
from matplotlib import pyplot as plt

def multiple_formatter(denominator=2, number=np.pi, latex='\pi'):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    def _multiple_formatter(x, pos):
        den = denominator
        num = np.int(np.rint(den*x/number))
        com = gcd(num,den)
        (num,den) = (int(num/com),int(den/com))
        if den==1:
            if num==0:
                return r'$0$'
            if num==1:
                return r'$%s$'%latex
            elif num==-1:
                return r'$-%s$'%latex
            else:
                return r'$%s%s$'%(num,latex)
        else:
            if num==1:
                return r'$\frac{%s}{%s}$'%(latex,den)
            elif num==-1:
                return r'$\frac{-%s}{%s}$'%(latex,den)
            else:
                return r'$\frac{%s%s}{%s}$'%(num,latex,den)
    return _multiple_formatter


def find_variables(theta_i):
    theta_t=maths.asin(maths.sin(theta_i)/2)
    a=maths.cos(theta_t)/maths.cos(theta_i)
    b=2
    E_t=2/(a+b)
    E_r=(a-b)/(a+b)
    return(E_t,E_r)

theta_is = np.linspace(0,maths.pi/2, 1000, False)
E_ts = np.zeros(len(theta_is))
E_rs = np.zeros(len(theta_is))
for i in range(len(theta_is)):
    E_ts[i],E_rs[i]=find_variables(theta_is[i])

theta_b=maths.atan(2)
print(theta_b)
E_t_b,E_r_b=find_variables(theta_b)

xs=[0,maths.pi/2]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
ax = plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
ax.yaxis.set_major_locator(plt.MultipleLocator(1 / 3))
ax.yaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter(denominator=3, number=1, latex='E_I')))
ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter(denominator=2)))
plt.grid(color='g', linestyle='--')
plt.plot(theta_is,E_rs,label=r'$E_r$')
plt.plot(theta_is,E_ts,label=r'$E_t$')
plt.scatter(theta_b,E_r_b)
plt.scatter(theta_b,E_t_b)
plt.plot([theta_b,theta_b],[-1/3,1],color='r', linestyle='--',label=r'$\theta_{b}$')
plt.title("Reflectedand and transmitted amplitudes in terms of incident ones against angle")
plt.ylabel("Amplitude")
plt.xlabel("Incident angle")
plt.legend()
plt.show()

