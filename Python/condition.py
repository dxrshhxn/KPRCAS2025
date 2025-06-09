a=10
b=20
c=30
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("C is greater")

for i in range(0,5,2):
    print(i)

def add():
    print(10+20)
add()

l=[1,2,3,4,5]  #list mutable
for i in l:
    print(i)

t=(6,7,8,9,10)  #tuple immutable
for i in t:
    print(i)

dic={"name":"Darshan","password":"123456"}  #dictionary
print(dic["name"])
print(type(dic))
for key in dic:
    print(dic[key])