class Validaciones:
    def validarPrecios(a):
         for i in a:
            if i!=" ":
                if a[0]=="$":
                    prr = a.split("$")
                    if len(prr)>2:
                        return False
                    else:
                        objeto.validarDecimales(prr[1])
                        return True
                else:
                    return False
            else:
                return False
       
    
    
    def validarCorreos(a):
        arr = a.split("@")
        if len(arr)==2:
            if arr[1]=="gmail.com" or arr[1]=="hotmail.com":
                space = arr[0].split(" ")
                if len(space) !=1:
                    return False
                else:
                    return True  
            else:
                return False
        else:
            return False
        
        
    def validarNumeros(a):
        if a.isnumeric():
            return True
        else:
            return False

    def validarLetras(a):
        x = 0
        for i in a:
            if i==' ':
                b = a.split(" ")
                #print(len(b))
                for y in b:
                    if y.isalpha():
                        x += 1   
                if x == len(b):
                    return True
                    break

                else:
                    return False
                    break
        if a.isalpha():
            return True
        else:
            return False

    def validarDecimales(a):
        x = 0
        for i in a:
            if i=='.':
                b = a.split(".")
                if len(b)>2:
                    return False
                    break
                else:
                    for y in b:
                        if y.isnumeric():
                            x += 1
                    if x==len(b):
                        return True
                        break
                    else:
                        return False
                        break

objeto = Validaciones 
