import math

def main(x, e, imax):
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
    return ans

def fp (i):
    return ans

if __name__ == '__main__':
	main()
