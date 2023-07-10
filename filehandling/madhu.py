'''with open('madhu.txt','w+') as fo:
    fo.write('madhu is a good boy')
    x=fo.read()
    print(x)
    print(fo.tell())

with open('madhu.txt','a+') as fo:
    x=fo.read()


with open('madhu.txt','r+') as fo:
    fo.write('xxsdfghjkl;x')
    x=fo.read()
    print(x)'''
    
fo=open('madhu.txt','r+')
fo.write('madhu is a g')
x=fo.read()
print(x)
