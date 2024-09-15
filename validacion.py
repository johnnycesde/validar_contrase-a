# Función para validar una contraseña según los criterios especificados
def validar_contraseña(contraseña):
    # Variables para verificar cada criterio
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False
    
    # Caracteres especiales permitidos
    caracteres_especiales = "!@#$%^&*"
    
    # Verificar la longitud de la contraseña
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    
    # Iterar sobre cada carácter de la contraseña
    for caracter in contraseña:
        if caracter.isupper():  # Verificar si es mayúscula
            tiene_mayuscula = True
        elif caracter.islower():  # Verificar si es minúscula
            tiene_minuscula = True
        elif caracter.isdigit():  # Verificar si es número
            tiene_numero = True
        elif caracter in caracteres_especiales:  # Verificar si es carácter especial
            tiene_especial = True
    
    # Verificar que cumpla con todos los criterios
    if not tiene_mayuscula:
        print("La contraseña debe tener al menos una letra mayúscula.")
    if not tiene_minuscula:
        print("La contraseña debe tener al menos una letra minúscula.")
    if not tiene_numero:
        print("La contraseña debe tener al menos un número.")
    if not tiene_especial:
        print("La contraseña debe tener al menos un carácter especial (!@#$%^&*).")
    
    # Si cumple todos los criterios, retornar True
    if tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial:
        return True
    else:
        return False

# Solicitar la contraseña al usuario y validar
def main():
    contraseña = input("Introduce una contraseña para validar: ")
    if validar_contraseña(contraseña):
        print("La contraseña es válida.")
    else:
        print("La contraseña no es válida.")

# Llamar a la función principal
if __name__ == "__main__":
    main()
