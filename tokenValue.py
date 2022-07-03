import random

charac = ['+','-','*','/','?','@','#','&','%','!','^']
alphabets = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']

tok = []

for i in range(1,10):
    if i <= 3:
        tok.append(random.randint(1,9))
    elif i <= 6:
        tok.append(random.choice(charac))
    else:
        tok.append(random.choice(alphabets))

random.shuffle(tok)
token = ""
for i in tok:
    token+=str(i)

print(token)