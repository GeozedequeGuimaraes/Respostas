def inverter_string(string):
    resultado = ""
    
    for i in range(len(string) - 1, -1, -1):
    
        resultado += string[i]
    
    return resultado

string_original = input("Digite uma string: ")  # Solicita ao usuário que insira uma string
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
