import math
import numpy as np

def main (a, b, maxiter, tol):

    m = 1
    x = np.linspace(a, b, m+1)
    y = f(x)
    approx = np.trapz(y,x)

    print("  m       integral approximation")

    print(m, end="")
    print(" "*12, end="")
    print('%.10f' % approx)

    i = 1
    n = 1

    while (i < maxiter):

        m = 2 ** n
        n = n + 1

        oldapprox = approx

        x = np.linspace (a, b, m+1)
        y = f(x)
        approx = np.trapz(y,x)
        print(m, end="")
        print(" "*12, end="")
        print('%.10f' % approx)

        if (np.abs((approx - oldapprox)/approx) < tol):
            return

        i = i + 1

    print("Did not converge in",end="")
    print(maxiter, end="")
    print("iterations")

def f(i):

    ans = []

    for x in i:
        y = ((math.log((1/x)))**0.5)
        ans.append(y)

    return ans

if __name__ == '__main__':
	main(0.02, 1, 20, 0.000001)
