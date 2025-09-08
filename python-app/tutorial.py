print("hello")

print(type(1.2))

print(1>3)

print (True and False)

n=3 
while (1<n):
    print(n)
    n-=1

def printOne():
    print("1")

def printNumber(number):
    print(number)

printOne()

printNumber(4)

i=0
string = "programming"
strlen = len(string)
while (i<strlen):
    if(string[i]== 'a' or string[i]==  'e' or string[i]== 'i' or string[i]== 'o' or string[i]== 'u' ):
        print(string[i])
    i+=1

text = "Python"
print(list(reversed(text)))  # ['n', 'o', 'h', 't', 'y', 'P']
reversed =text.join(reversed(text))  # "nohtyP"
print(reversed) 

