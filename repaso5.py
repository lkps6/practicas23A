#HACER UN PROGRAMA QUE LEA NOMBRE,CANTIDAD Y PRECIO DE 5 PRODUCTOS
#MOSTRARA AL FINAL LA CANTIDAD A PAGAR DE ESOS PRODUCTOS
#LOS DATOS DEBEN ESTAR VALIDADOS Y SI SE INTRODUZCA UN ERROR SE VOLVERA A PEDIR
#MUESTRE LOS ARTICULOS EN UNA LISTA
#append y meter de uno en uno
#imprimir los productos en un for 

from metodos import Validaciones
validar = Validaciones


def prueba():
    contador=0
    total = 0.0
    totalf = 0.0
    lista2 = []
    while (True):
        con1=True
        con2=True
        con3=True
        lista1 = []
        while con1==True:
            nom = input("Escribe nombre \n")
            if validar.validarLetras(nom)==True:
            
                con1=False
                while con2==True:
                    can = input("Escribe cantidad \n")
                    if validar.validarNumeros(can)==True:
                        
                        con2=False
                        while con3==True:
                            a = input("Escribe precio \n")
                            if validar.validarPrecios(a)==True:
                                con3=False
                                c=''
                                b = 0.0
                                for i in a:
                                    if i != "$":
                                        c +=i
                                b = float(c)
                                total = b * float(can)
                                totalf +=total
                                lista1.append(nom)
                                lista1.append(can)
                                lista1.append(b)
                                lista1.append(total)
                                lista2 += lista1
                                contador +=1
                            else:
                               print("Precio no válido")  
                    else:
                        print("Cantidad no válida")          
            else:
                print("Nombre no válido")
        if contador>1:
            break
    for i in range(len(lista2)):
        print(lista2[i])
        
    #print("Datos del producto: ",lista2)
    print("Total a pagar: ",totalf)
prueba()    



