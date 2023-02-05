#HACER UN PROGRAMA QUE LEA NOMBRE,CANTIDAD Y PRECIO DE 5 PRODUCTOS
#MOSTRARA AL FINAL LA CANTIDAD A PAGAR DE ESOS PRODUCTOS
#LOS DATOS DEBEN ESTAR VALIDADOS Y SI SE INTRODUZCA UN ERROR SE VOLVERA A PEDIR

from metodos import Validaciones
validar = Validaciones

def muestra():
    con=0
    c1=0
    c2=0
    c3=0
    t=0.0
    while con<5:
        while c1<5:
            a=input("Nombre: ")
            if validar.validarLetras(a):
                c1 += 1
            else:
                print("Error, Ingresa los datos correctos")     
        while c2<5:
            b=input("Cantidad: ")
            if validar.validarNumeros(b):
                c2 += 1
            else:
                print("Error, No es una cantidad") 
        while c3<5:
            c=input("Precio: ")
            if validar.validarPrecios(c):
                c3 +=1
                prr = c.split("$")
                flo=float(prr[1])
                t=float(b)*flo
                total=+t
                
            else:
                print("Error, No es un precio")  
        
        
        print("Total a pagar: ",total)

        #print("Nombre: ",a,"Cantidad: ",b,"Precio: ",c,"Total: $",t," pesos")
        break
        
muestra()

#append y meter de uno en uno
#imprimir los productos en un for 

