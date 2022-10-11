num = [2,4,10,3,5,6,7,8,9,45,56,11,0]
def is_prime(n):
    list1 = []
    for item in range(1,n+1):
        if n % item == 0:
            list1.append(item)
        else:
            continue
    return len(list1)

for i in num:
    if is_prime(i) ==2:
        print(f'{i} is a prime number')
    else:
        print(f'{i} is not prime number')