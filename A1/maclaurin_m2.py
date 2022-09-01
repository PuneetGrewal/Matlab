import math

def main():
    i = 0

    for j in range(7):
        x = 0
        temp = 0
        value = 0
        x = j + 1
        print ("Using",x,"Terms", end=" ")
        for i in range(x):
            temp = (2.75**i)/math.factorial(i)
            value = value + temp
        value = 1/value
        print ("Approximation=",value, end=" ")
        error = 0.06392786 - value
        abserror = abs(error)
        relative_error = (abserror/0.06392786)
        print ("Relative Error=",relative_error)

main()
