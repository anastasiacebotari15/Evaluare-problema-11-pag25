n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
# if n<10:
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
print(a)

print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(a[0:5])
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
for i in range(len(a), 0 , -1):
    v=a[i-1]
    print(v)
print('c)  sortează componentele tabloului în ordine descrescătoare;')
b=sorted(a)
b.sort(reverse=True)
print(b)
print('d)  afişează pe ecran doar componentele pare;')
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        c.extend([y])
print(c)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')
print(sum(c)/len(c))
print('f)  afişează pe ecran doar componentele impare;')
d=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        d.extend([y])
print(d)
print('g)  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt divizibile cu y (valorile x şi y se citesc de la tastatură);')
x1=int(input('Valoarea lui x:'))
y1=int(input('Valoarea lui y:'))
e=[]
for i in range(0,len(a)):
    if ((a[i]>x1) and (a[i]%y1!=0)):
        f=a[i]
        e.extend([f])
print(e)
print('h)  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici decât y (valorile x şi y se citesc de la tastatură);')
x2=int(input('Valoarea lui x:'))
y2=int(input('Valoarea lui y:'))
g=[]
for i in range(0,len(a)):
    if ((a[i]>x2) and (a[i]<y2)):
        t=a[i]
        g.extend([t])
print(g)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
for i in a:
    if i<0 and i%2==1:
        print(a.index(i))
print('j)  afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative;')
for i in a:
    if (i<100 and i>9) or (i>-100 and i<-9):
        print(a.index(i))
print('k)  înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv;')
k=a
randomvar=a[0]
ind=a.index(min(a))
k[0:1]=[min(k)]
print(k)
print('l)  înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia;')
k[ind]=randomvar
print(k)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
m =[]
for i in a:
    if i%2==0:
        m.append(i)
print(m)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
n=[]
for i in a:
    if i%3==0:
        n.append(i)
print(n)

print('o)  creează un tablou nou, format doar din acele componente ale tabloului in-trodus de la tastatură care au cel mult patru divizori.')
o=[]
for i in a:
    counter=0
    for w in range(1,i):
        if i%w==0:
            counter+=1
    if counter <5:
        o.append(i)
print(o)