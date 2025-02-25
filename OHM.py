valor_predeterminado_potencia = 300

print("""

      ¿Que vas a buscar? / What are you going to find?
      
      1) Voltaje (Voltios)
      2) Corriente (Amperios)
      3) Resistencia (Ohmios)
      
      """)

Opcion1 = int(input(" Selecciona un numero / Select a number: "))

if Opcion1 > 3:
    print("No Opcion.")

if Opcion1 == 1:
    print("Seleccionaste la opcion: ", Opcion1)
    Corriente = int(input("Introduce el valor de los amperios: "))
    Resistencia = int(input("Introduce un valor para la potencia / coloca 0 para el valor predeterminado: "))
    if Resistencia == 0:
        Resistencia = 300
    resultado = print("El resultado del voltaje en voltios es: ", Corriente*Resistencia)

if Opcion1 == 2:
    print("Seleccionaste la opcion: ", Opcion1)
    Voltaje = int(input("Introduce el valor de los Voltios: "))
    Resistencia = int(input("Introduce un valor para la potencia / coloca 0 para el valor predeterminado: "))
    if Resistencia == 0:
        Resistencia = 300
    resultado = print("El resultado del Corriente en Amperios es: ", Voltaje*Resistencia)

if Opcion1 == 3:
    print("Seleccionaste la opcion: ", Opcion1)
    Voltaje = int(input("Introduce el valor de los Voltios: "))
    Corriente = int(input("Introduce el valor de los Amperios: "))
    resultado = print("El resultado de la Resistencia en Ohmios es: ", Voltaje*Corriente)
