#question1
print(3/5)

#question2
x = [0,1,2]
x.insert(0,1)
print(x)
del x[1]
print(x)
print(sum(x))

#question3
x = input()
y = input()
print(x+y)

#question4
d = {}
d[1] = 1
d['1'] = 2
d[1] += 1
sum = 0
for k in d:
    sum += d[k]
print("sum: ", sum)

#question5
def qn5Fun():
    i = 4
    while i > 0:
        i -= 2
        print('*')
        if(i == 2):
            break
    else:
        print('*')

qn5Fun()

#question6
dict1 = {'one':'two','three':'one','two':'three'}
v = dict1['one']
for k in range(len(dict1)):
    v = dict1[v]
print(v)

#question7
a = [ 1,2,3,4,5,6,7,8,9]
print(a[::2])

#question8
x = 2
y = 1
x *= y + 1
print(x)

#question9
x1 = '\''
print(len(x1))

#question10
num = 1
def func():
    global num
    num = num + 3
    print(num)
func()
print(num)

#question11
def func1(x):
    return 1 if x % 2 != 0 else 2
print(func1(1))
print(func1(func1(1)))

#question12
def func2(x,y,z):
    return x + 2 * y + 3 * z
print(func2(0,z=1,y=3))

#question13
print(list('hello'))

#question14
def func3(num):
    res = '*'
    for _ in range(num):
        res += res
    return res

for x in func3(2):
    print(x,end='')

#question15
x = 1
y = 2
z = x
x = y
y = z
print(x,y)

#question16
nums = [1,2,3,4,5,6,7,8]
vals = nums
del vals[1:4]
print(nums)
print(vals)

#question17
nums.pop(1)
print(nums)

#question18
x = 28
y = 8
print(x/y)
print(x//y)
print(x%y)

#question19
x1 = bool(23)
print(x1)
x2 = bool('')
print(x2)
x3 = bool(' ')
print(x3)
x4 = bool([False])
print(x4)

#question20
def func4(a,b,c=0):
    print(a+b+c)
func4(b=1,a=2)
func4(1,2,3)
#The below will throw an error as one argument is missing
#func4(b=1)

#question21
i1 = 0
while i1 <= 3:
    i1 += 2
    print('*')

#question22
i2 = 1
if i2 > 0 or i2 < 1:
    print('1')
if i2 > 1:
    print('2')
elif i2 >= 1:
    print('3')
else:
    print('4')

#question23
list1 = [1,3]
list2 = list1
list1[0] = 4
print(list2)

#question24
sum = count = done = 0
average = 0.0
while done != -1:
    rating = float(input('Enter the next rating (1-5). -1 fr done'))
    if rating == -1:
        break
    sum += rating
    count += 1
average = float(sum/count)
print('The average star rating for the new coffee is: ' + format(average, '.2f'))

#question25
def func5(p1,p2):
    p1 = 4
    p2[0] = 45
x = 3
y = [1,2,3]
func5(x,y)
print(x , y[0])

#question26
list3 = [False,True,"2",3,4,5]
b = 0 not in list3
print(b)
b = 0 in list3
print(b)

#question27
def func6(x=1,y=2):
    x = x + y
    y += 1
    print(x,y)
func6(2,1)

#question28
for i in range(1,6):
    print(str(i)*5)
    print(i,i,i,i,i)

#question29
dct = {}
dct['1'] = (1,2)
dct['2'] = (2,1)
for x in dct.keys():
    print(dct[x][1],end='')

#question30
def func7():
    return True
x = func7(False)
print(x)