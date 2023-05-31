from operaciones import caracterfun, palabrafun

print("|| MENU ||")
respuesta = str(input("""
  Que desea ver en binario:
  
  1. Un Carácter
  2. Una Palabra

"""))

if respuesta == "1":
  print("")
  caracter = str(input("Escriba el carácter: "))
  print("")
  caracter_binario,caracter_ascii = caracterfun(caracter)
  print(f"El valor ASCII de '{caracter}' es {caracter_ascii}. El caracter '{caracter}' en binario es: {caracter_binario}")
  
elif respuesta == "2":
  print("")
  palabra = str(input("Escriba la palabra: "))
  print("")
  palabra_binario,palabralista = palabrafun(palabra)
  for x in range(len(palabra_binario)):
    print(f"El valor ASCII de '{palabralista[x]}' es {ord(palabralista[x])}. El caracter '{palabralista[x]}' en binario es: {palabra_binario[x]}")
  print("")
  print(f"Y la palabra completa en binario es: {' '.join(map(str,palabra_binario))}")
  
else:
  print("Esa no es una opción disponible")



