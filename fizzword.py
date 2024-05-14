num =1
fizzcount=0
buzzcount=0
fizzbuzzcount=0
while (num<=100000):
    if(num%3==0) and (num%5==0):
        print(str(num) + ":Fizzbuzz!")
        fizzbuzzcount+=1
    elif(num%3==0):
        print(str(num) + ":Fizz")
        fizzcount+=1
    elif(num%5==0):
        print(str(num) + ":Buzz")
        buzzcount+=1
    else:
        print(str(num) + '.')
   
    num +=1
print("________________________________")
print("fizz\tBuzz\tFizzbuzz")
print(str("{:,}".format(fizzcount)) + "\t" + str("{:,}".format(buzzcount)) +"\t" +str("{:,}".format(fizzbuzzcount)))