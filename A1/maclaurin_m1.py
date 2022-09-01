import math

def main():
    i = 1
    j = 1

    for j in range(8):
        value = 0
        temp = 0
        print ("Using",j,"Terms,", end=" ")
        for i in range(j):
            temp = ((-1)**i)*(2.75**i)/math.factorial(i)
            value = value + temp
        print ("Approximation=",value,",", end=" ")
        error = 0.06392786 - value
        abserror = abs(error)
        relative_error = (abserror/0.06392786)
        print ("Relative Error=",relative_error)

main()
