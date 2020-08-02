
#Reverse Integer
#Slicing
#txt = "-123"

def solution(x):
     txt = str(x)
     if txt[0] == "-":
          return int("-" +txt[:0:-1])
     else:
          return int(txt[::-1])

print(solution(123))
print(solution(-1234))


