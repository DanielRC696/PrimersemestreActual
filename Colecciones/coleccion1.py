numero = 123
resultado = str(numero)
print(resultado)

texto = "hello"
resultado = texto.upper()
print(resultado)

texto = "HelLo"
resultado2 = texto.lower()
print(resultado2)

texto = "HelLo"
resultado3 = texto.capitalize()
print(resultado3)

texto = "helLo moresco y piña"
resultado4 = texto.title()
print(resultado4)

texto = "Hola, mundo"
indice = texto.find("mundo")
print(indice)

texto = "mundo"
nuevo_texto = texto.replace("mundo", "Python")
print(nuevo_texto)  # Output: 'Hola, Python'


texto = "hello"
resultado = texto.startswith("he")
print(resultado)


texto = "manzana,banana,pera, perro, porro"
resultado = texto.split(',')
print(resultado)  # devuelve una lista ['manzana', 'banana', 'pera']

nombres = ['Juan', 'María', 'Carlos', 'Lucía']
resultado = " " .join(nombres)
print(resultado)  # 'Juan,María,Carlos,Lucía'



texto = "   hola   "
resultado = texto.strip()
print(resultado)  # Output: 'hola'

