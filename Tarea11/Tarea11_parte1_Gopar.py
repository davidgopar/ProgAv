import pickle
f=open("tarea11_parte1.txt","wb")
dct=['Progra','Avanzada','Cinvestav']
dct.append(1)
pickle.dump(dct,f)
f.close()

#Para leer
f=open("tarea11_parte1.txt","rb")
d=pickle.load(f)
print (d)
f.close()