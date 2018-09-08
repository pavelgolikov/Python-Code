
def Fibbonacci(n):
    num1 = 0
    num2 = 1
    flag = 2
    total = 1
    while flag < n:
        flag += 1
        total = num1 + num2
        num1 = num2
        num2 = total
        print(num1, num2)
    return total
    

print(Fibbonacci(5))