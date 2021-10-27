'''
str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/',1)[0])
print(str1.rsplit('-',1)[0])

s=input('enter the string')
if len(s)%4==0:
    print(''.join(reversed(s)))
else:
    print(s)

def revese(str):
    if len(str)%4==0:
        return ''.join(reversed(str))
    return str
print(revese('jube'))

str=input('enter your string')
print('1.upper,2.lower,3.swapcase,4.title')
n= int(input('select the operation'))
if     n==1:
    print(str.upper())
elif   n==2:
    print(str.lower())
elif n==3:
    print(str.swapcase())
elif      n==4:
    print(str.title())
else:
    print('enter correct number')

def upper_string(str):
    new_str=0
    for i in str[:4]:
        if i.upper()==i:
            new_str+=1
    if new_str>=2:
        return str.upper()
    return str
print(upper_string('juermulla'))

#loxicography
s='w3resource'
jm=sorted(sorted(s),key=str.upper)
print(''.join(jm))

#to remove new line use strip function
str1='Python Exercises\n'
print(str1.strip())

string = "w3resource.com"
print(string.startswith('w3r'))

import textwrap
s

#print(textwrap.fill(sample_text,width=50))

import textwrap
sample_text =

s='hello python how are you'
str1='pythonj'
if (s.find(str1) ==-1):
    print('no substring')
else:
    print('substring is present')

str1 = 'The quick brown fox jumps over the lazy dog.'
print(str1.count('brown'))

s='The quick brown fox jumps over the lazy dog.'
for i in reversed(s.split()):
    print(i,end=' ')

s='jubermulla'
print(s[::-1][3])

s='juber mulla'
k='a,e,i,o,u,'
l=[]
for i in s:
    for j in k:
        if j!=k:
            l.append([i])
            print(i,end='')

import re
s='juber nasaruddin mulla'
k=re.sub('[aeiouAEIOU]','',s)
print(k)

s='juber nasaruddin mulla'
v=('a','e','i','o','u','A','E','I','O','U')
output=''
for i in s:
    if i in v:
        s=s.replace(i,'')
print(s)

string=input('enter your string:')
v=['a','e','i','o','u']
s=''
for i in string:
    if i.lower() not in v:
        s+=i
print(s)

str=input('enter your string:')
string_new=str.lower()
v=['a','e','i','o','u']
d={}
for i in string_new:
    if i in v:
        d[i]=d.get(i,0)+1
print(d)

str=input('enter your string:')
string_new=str.lower()
v=['a','e','i','o','u']
count=0
for i in string_new:
    if i in v:
        count+=1
print('thw total number of vowels in given string is ',count)

s='jubermulla'
l=[]
for i in s:
    if i not in l:
        l.append(i)
for i in l:
    print('{} occures {} times'.format(i,s.count(i)) )

s= 'jjjubbhwducwucbvjwu'
output=''
for i in s:
    if i not in output:
       output=output+i
        jutput=output.split()
print('{} occures {} times'.format(jutput,s.count(output)))

s = "asldaksldkalskdla"
dict = {}
for i in s:
    dict[i]=dict.get(i,0)+1
print(dict)

s = "asldaksldkalskdla"
dict = {}
for i in s:
    if i not in dict.keys():
        dict[i]=1
    else:
        dict[i]+=1
print(dict)

s='w3resource'
print(list(enumerate(s,start=0)))

s='w3resource'
for i,x in enumerate(s):
    print('character',x,'present at index',i)

s=input('enter the string:')
if s.isalpha()==True:
        print('yes alphbets present in string')
else:
    print('string is not contain all alphabets')


S='JUBERMULLA'
J=S[:4].lower() + S[4:]
print(J)

str=input('enter the string')
n=int(input('enter a number'))
def lower_string(str,n):
    return str[:4].lower()+str[4:]
J=lower_string(str,n)
print(J)
j='32.054,23'
k=j.replace('.',',').replace(',','.').replace('.',',')
print(k)

j='32.054,23'
juber=j.maketrans
jm=j.translate(juber('.,',',.'))
print(jm)

j='jubermulla'
jm=j.maketrans
juber=j.translate(jm('jl','ky'))
print(juber)

s='JUBermulla'
j=s.swapcase()
print(s)

str1 = 'w,3,r,e,s,o,u,r,c,e'
jm=str1.rsplit(',',5)
print(jm)

#prime number factorail number,prime number,number divisible by 5,palindrom
txt = "Hello Sam!"

mytable = txt.maketrans

print(txt.translate(mytable('s','p')))

class juber:
    def __init__(self):
        self.a=100
        self.b=100
        self.c=500
h=juber()
print(h.__dict__)

a=10
b=a
c=a+2
print(id(a)==id(b))

l1=[10,20,30,40]
l2=[50,60,70,80]
print(l1*3)

d={1:100,2:200,3:400}
s={7:100,8:500,9:500}

#students_maths = ['raj', 'sai', 'sudha']
# students_english = ['chitti', 'ajith', 'Dean']
#students_history = ['vijay', 'Mike']
# #Output:- PRINT raj sai sudha
s=['raj', 'sai', 'sudha']
k=['chitti', 'ajith', 'Dean']
j=['vijay', 'Mike']
jm=s+k+j
print(' '.join(jm))
for i in jm:
    print(i,end=' ')

print(list(range(1,16)))

j=list(range(1,16))
print( j[15 : 0 : -3])

a=[1,2,3,4,8,6,7,8,9, 10 ,11]
print(a[::2])

print(3+10*2)

print((3+10)*2)
'''
