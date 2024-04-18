slovo = str(input())
x = len(slovo)
i = 0
x = x - 1
l = 0
while x - 1 >= i:
    if slovo[x - i] == slovo[i]:
        i +=1
    else:
        l = 1
        break
if l == 1:
    print("Слово не є паліндромом")    
else:
    print("Слово є паліндромом")    