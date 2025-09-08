text = "Python"
print(text[::-1])  
# start = nothing (means whole string)
# stop = nothing (means till the end)
# step = -1 (reverse order)
# → "nohtyP"

text = "Python"
count = len(text)
i = count-1
while (i >= 0):
    print(text[i],end="")
    i-=1
print()

text = "Python"
print(list(reversed(text)))  # ['n', 'o', 'h', 't', 'y', 'P']
reversedText ="".join(reversed("Python"))  # "nohtyP"
print(reversedText) 


for i in range(len(text) - 1, -1, -1):
    print(text[i], end="")
