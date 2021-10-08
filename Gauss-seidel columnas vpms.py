# -- coding: utf-8 --
"""
Created on Mon Oct 4 15:25:48 2021
@author: José Manuel Ramírez Olivera.
         Viviana Paloma Muñoz Sánchez.
         
Gauss Seidel con Pivoteo(Columnas)
De ejemplo se va a resolver
6x + 2y + z = 22   
-x + 8y + 2z = 30
x - y + 6z = 23  
'''
"""

#Librerías utilizadas:
import numpy as np
import sys

#Para leer datos del archivo:
def Read_inputs(text_basis):
#A=incógnitas y b=constantes.
    a_temp, b_temp = text_basis.strip().split("=")
    #"Elimina" los "=" para dividirlo en dos matrices.
    b_temp = eval(b_temp.strip(" "))
    a_temp = a_temp[:-1]
    #Para quitar espacios.
    a_temp = [eval(i) for i in a_temp.split()]

    return a_temp, b_temp

def Read_file(path):
    A= []
    b= []
    with open(path,"r") as f:
        flag=0
        for line in f:
#Empieza a usar los valores a partir de la X en el archivo:
            if line.strip() != "X":
                pass
            else:
                flag=1
                continue
#Termina la lectura del archivo en "Y":
            if line.strip() == "Y":
                flag=0
                break
            if flag==1:
                aux_1, aux_2 = Read_inputs(line)
                A.append(aux_1)
                b.append(aux_2)
    return A, b

#Exportar matriz al código.
ruta = 'matriz JMRO.txt'
A, b = Read_file(ruta)
#Para imprimir las matrices:
print("A = ",A)
print("b = ",b)

def Matriz_cuadrada(M):
    if len(M) != len(M[0]):
        print("La matriz no es cuadrada.")
        #Si la matriz no es cuadrada sale del programa.
        sys.exit
    else:
        print("La matriz es cuadrada.")

Matriz_cuadrada(A)
#Se definen los elementos como numpy del archivo de texto:
A_np = np.array(A)

b_np = np.array(b)

#Pivoteo parcial por columnas.
def Pivoteo_C(M, v):
    t = np.shape(M)
    n = t[0]
    for i in range(0,n-1,1):
        filaM = abs(M[i:,i])
#Valor máximo por columnas recorriendo filas:
        maxM = np.argmax(filaM)
#Método para intercambiar columnas de mayor a menor, el cambio es con base en el máximo de cada fila: 
        if(maxM != 0):
            aux = np.copy(M[:,i])
            M[:,i] = M[:,maxM+i]
            M[:,maxM+i] = aux
            print("A =", M)
            auxv = np.copy(v[i])
            v[i] = v[maxM+i]
            v[maxM+i] = auxv
            print("b =", v)
        return M, v
print("Matriz después del pivoteo: ")    
Pivoteo_C(A_np, b_np)  
    
def GS(M_np, v_np, iter_max, umbral):
    #Auxiliares para el cálculo:
    x_np = np.zeros(len(M_np)) 
    aux_np = np.ones(len(M_np))

    for ite in range(iter_max):
        for i in range(len(M_np)):
            aux_np[i] = 0.0
            x_np[i] = (v_np[i] - np.sum(x_np*aux_np*M_np[i,:]))/M_np[i][i]
            aux_np[i] = 1.0
            
        current_v = np.dot(M_np,x_np)
        error_np = np.sum(np.abs(current_v-v_np))
        
        if error_np < umbral:
            #print(x_np)
            return x_np
        
#Imprimir valores:
print("Soluciones cambiando columnas: ", GS(A_np, b_np, 100000, 0.00001))