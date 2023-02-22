#Romina_mendoza_&_Francisco_Gorrin
#serie de fibonacci
# dado un numero N entero ingresario por el usuario imprima los numeros de la serie de fibonacci menos a N

n= int(input("introduzca el numero : "))
a=0
b=1
s = 0 

listafibo= [0]
listapares = []
listaimpares = [-1]
suma1 =0
suma2 =0

for x in range(n):
    print( s,end= " ") 
    s=a+b
    b=a
    a=s
    listafibo.append(s)
    


    # suma de los numeros pares e impares
    if s % 2== 0 :
        listapares.append(s)
    else :
        listaimpares.append(s)



for x in listapares:
    suma1 = suma1 + x

for x in listaimpares:
    suma2 = suma2 + x

# suma de de la serie fibonacci
for x in range(n):
    c=a+b
    b=a

m=c-b-1

print("la suma de la cadena es: ", m,"\n"
"la suma de los numeros pares es : ", suma1 ,"\n"
"la suma de los numeros impares es : ", suma2,)

