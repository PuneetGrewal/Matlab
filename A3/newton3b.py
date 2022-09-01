import math


def main(x,e,imax):

    i = 1
    print("iteration" + "   " + "approximation")

    while (i <= imax):
        root = x - (f(x)/fp(x))
        print(i, end="")
        print(" "*12, end="")
        print('%.6f' % root)

        if ((abs(1 - x/root)) < e):
            return root

        i = i+1
        x = root

    print("failed to converge in" + imax + "iterations")

def f (i):
    ans = (math.cos(i + (2 ** 0.5)) + (i**2)/2 + (2 ** 0.5)*i)
    return ans

def fp (i):
    ans = (-(math.sin(i + 2**0.5)) + i + 2**0.5)
    return ans

if __name__ == '__main__':
	main(1,0.000001,50)
