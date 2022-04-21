num = int(input("Enter Any Number :"))

if num > 1:
    for i in range(2, num):
        if (num % i)==0:
            print(num, "Its not a prime number...")
            print(i,"times",num//i,"is" ,num)
            break
    else:
        print(num, "Its an prime number...")
else:
    print(num, "Its not a prime number...")




 
