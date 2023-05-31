
def caracterfun(caracter):
  ascii = ord(caracter)
  binario = format(ascii, 'b')
  return(binario,ascii)

def palabrafun(palabra):
  palabracompleta = []
  palabra = list(palabra)
  for x in palabra:
    ascii = ord(x)
    binario = format(ascii, 'b')
    palabracompleta.append(binario)
  return palabracompleta,palabra