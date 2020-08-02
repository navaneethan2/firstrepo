"String Literals - By single or double quotes"
print ("Hello")
print ('Hello')
"Assign String to a Variable"
y = 'abc'
z = "abc"
print y,
print z
"Multiline Strings"
a = """afghjkl,
    bnm,
    ghjkghj"""

print a
"Strings are Arrays - No char data set, "
a = "Hello ,World"
print(a[1])
"Slicing"
b = "Hello, World"
print (b[2:7])
"Negative Slicing"
print(b[-5:-2])
"String Length use len() module"
a = "Hello ,World"
print(len(a))


"String Methods- Python has set of inbuilt methods"
"strip() - removes whitespace from beginning / end"
a = " Hello , World "
print(a.strip())
"lower() - return string in lower case"
print (a.lower())
"upper() - return string in upper case"
print (a.upper())
"replace() - replace a string with another string"
print (a.replace("H","J"))
"split()- split method splits the string into substrings"
print (a.split(","))

"Check string"
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print x
y = "ain" not in txt
print y

"String Concatenation - to concatinate two string using + operator"
a = "naveen"
b = "Hari"
c = a + b
print c
d = a + " "+b
print d

"String Format format()- takes passed arugument and placed in {}"

txt = "my age is"
age = 30
#bio = txt + age
#print bio
print txt+format(age)

myorder = "i want a {} piece of item {} for {} dollars"
quantity = 3
itemno = 567
price = 49.95

print (myorder.format(quantity,itemno,price))



