def calcular_promedio(a, b, c) :
  return (a + b + c) / 3

num1 = int(input("Escribe el primer número: "))
num2 = int(input("Escribe el segundo número: "))
num3 = int(input("Escribe el tercer número: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"El promedio es: {promedio}")
