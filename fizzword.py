num =1;
while (num<=100):
    if(num%3==0) and (num%5==0):
        print(str(num) + ":Fizzbuzz!")
    elif(num%3==0):
        print(str(num) + ":Fizz")
    elif(num%5==0):
        print(str(num) + ":Buzz")
    print(num)
    num +=1