Peso=float(input("ingrese el Peso DE La Persona"))
Estatura=float(input("ingrese La Estatura De La Persona"))
imc=(Peso/(Estatura*Estatura))
print("El INDICE DE LA MASA COROPRAL IMC DE LA PERSONA ES: "+str(imc))

if (imc>18 and imc<25):
    print ("Saludable: ")

    if (imc<18):
        print ("Desnutricion:")

    if (imc>25 and imc<29):
        print ("Sobrepeso: ")

    if (imc>30):
        print ("Obesidad: ")

   