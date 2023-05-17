# Un registro es un dispositivo para contener datos que pueden tener diferente tipo. Los
# registros normalmente están asociados a dispositivos externos de almacenamiento como
# discos. Algunos lenguajes de programación tienen un tipo especial de datos para
# representar registros.
# Python no dispone en su librería estándar este tipo de datos, sin embargo, se puede usar
# una variable de tipo lista como un recipiente natural para almacenar un registro puesto
# que las listas en Python pueden contener componentes de diferente tipo y además pueden
# modificarse.
#Esto se queda temporalmente

#Primer
#datos=[]
# reg=[1,2,3,4,5]
# datos=datos+[reg]
# print(datos)
# reg2=["Juan","Pedro","Erika"]
# datos+=[reg2]
# print(datos)
# reg3=[]
# nom=input("Dame tu nombre: ")
# reg3.append(nom)
# datos+=[reg3]
#print(datos)

#Ejercicio Uno
registros=[]
bandera=True
while bandera==True:
    print("########################")
    print("1.- Ingresar un Artículo")
    print("2.- Consultar un Artículo")
    print("3.- Comprar")
    print("4.- Vender")
    print("5.- Eliminar Articulo ")
    print("6.- Salir")
    opc=int(input("Selecciona una Opcion: "))
    if opc > 0 and opc < 7:
        if opc==1:
            cod=int(input('Ingrese código: '))
            cant=int(input('Ingrese cantidad: '))
            pre=float(input('Ingrese precio: '))
            nom=input('Ingrese nombre: ')
            reg=[cod,cant,pre,nom]
            registros+=[reg]
            print("Registros Exitoso")
        elif opc==2:
            c=int(input("Ingresa el Código a Buscar: "))
            p=-1
            for i in range(len(registros)):
                if  c==registros[i][0]:
                    p=i  #Registro encontrado
                    break;
            if p < 0:
                print("##### Resultado de Busqueda #########\n")
                print('#######   Artículo no existe #######\n')
                print("##### Resultado de Busqueda: #########\n")
            else:
                print("\n####### Se encontro el siguiente Producto #####\n")
                print(f"Cantidad= {registros[p][1]}")
                print(f"Precio= {registros[p][2]}")
                print(f"Nombre= {registros[p][3]}")
                print("####### Se encontro el siguiente Producto #####")
        elif opc==3:
            c=int(input("Ingresa el Código a Buscar: "))
            p=-1
            for i in range(len(registros)):
                if  c==registros[i][0]:
                    p=i  #Registro encontrado
                    break;
            if p < 0:
                print("##### Resultado de Busqueda #########\n")
                print('#######   Artículo no existe #######\n')
                print("##### Resultado de Busqueda: #########\n")
            else:
                cantidad=int(input("Ingresa la cantidad Comprada: "))
                registros[p][1]=registros[p][1]+cantidad
                print("##### Se agrego la cantidad #########\n")
                print('#######   CON EXITO #######\n')
                print("##### Se agrego la cantidad #########\n")
        elif opc==4:
            c=int(input("Ingresa el Código a Buscar: "))
            p=-1
            for i in range(len(registros)):
                if  c==registros[i][0]:
                    p=i  #Registro encontrado
                    break;
            if p < 0:
                print("##### Resultado de Busqueda #########\n")
                print('#######   Artículo no existe #######\n')
                print("##### Resultado de Busqueda: #########\n")
            else:
                cantidad=int(input("Ingresa la cantidad a Vender: "))
                registros[p][1]=registros[p][1]-cantidad
                print("##### Se agrego la cantidad #########\n")
                print('#######   CON EXITO #######\n')
                print("##### Se agrego la cantidad #########\n")
                
        elif opc==5:
            c=int(input("Ingresa el Código a Buscar: "))
            p=-1
            for i in range(len(registros)):
                if  c==registros[i][0]:
                    p=i  #Registro encontrado
                    break;
            if p < 0:
                print("##### Resultado de Busqueda #########\n")
                print('#######   Artículo no existe #######\n')
                print("##### Resultado de Busqueda: #########\n")
            else:
                del registros[p]
                print("##### Eliminar Registro #########\n")
                print('#######   Se Elimino Exitosamente #######\n')
                print("##### Eliminar Registro #########\n")
        else:
            print("Hasta la Proxima")
            bandera=False
            #break
            
        
    else:
        print("########## OPCIÓN NO VALIDA ########")
        print("Selecciona una opción del 1-6")