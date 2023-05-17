 #Problema. Diseñar una aplicación interactiva para administrar los registros de estudiantes
# en un seminario mediante un menú con las siguientes opciones:
# 1) Agregar registro
# 2) Eliminar registro
# 3) Consultar registro
# 4) Cupo actual
# 5) Salir
# Solución
# El programa presentará el menú para que el usuario elija alguna opción.
# Cada opción será instrumentada como una función.
# El programa llamará a cada función para realizar la acción solicitada.
# El programa y las funciones se almacenarán en un solo módulo.

#Crear las funciones
#Agregar



def Agregar(e):
    try:
        mat=int(input("Ingrea la Matrícula: "))
        if mat not in e:
            e=e+[mat]
            print("Registro Exitoso")
        else:
            print("Ya estas Matículado")
        return  e 
    except:
        print("No se Pudo Registrar")
        
def Eliminar(e):
    try:
        mat=int(input("Ingrea la Matrícula: "))
        if mat in e:
            e.remove(mat)
            print("Se Elimino la Matrícula")
        else:
            print("No estas Inscrito")    
    except:
        print("No Existe el Registro")
        
def Consultar(e):
    try:
        mat=int(input("Ingrea la Matrícula: "))
        if mat in e:           
            print(f"Estas Inscrito con la Matrícula {mat}")
        else:
            print("No estas Inscrito")    
    except:
        print("No se pudo Consultar")
        
def Cupo(e):
    try:
        num=len(e)                
        print(f"Cantidad de Inscritos {num}")   
    except:
        print("No hay Inscritos")
        
e=[]
bandera=True
while bandera==True:
    print('1) Agregar registro')
    print('2) Eliminar registro')
    print('3) Consultar registro')
    print('4) Cupo actual')
    print('5) Salir')
    opc=int(input("Elija una Opción: "))
    if opc > 0  and  opc < 6:
        if opc==1:
            e=Agregar(e)
        elif opc==2:
            e=Eliminar(e)
        elif opc==3:
            Consultar(e)
        elif opc==4:
            Cupo(e)
        else:
            #break
            print("Hasta Pronto")
            bandera=False
    else:
        print("opción no valida selecciona una del 1-6")
    
    