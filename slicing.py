
#Reverse Integer
#Slicing
#txt = "-123"

def solution(x):
     txt = str(x)
     if txt[0] == "-":
          return int("-" +txt[:0:-1])
     else:
          return int(txt[::-1])

#print(solution(123))
#print(solution(-1234))


#Return a Given integer

n = int(input("Enter the No: "))
rev = 0
while (n > 0 ):
     rem = n % 10
     rev = rev * 10  + rem
     n = n / 10
print("The reverse of the given integer is :", rev)