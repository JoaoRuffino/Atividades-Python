resp = "Não"
while (resp == "Não" or resp == "não"):
    dia = input("Informe seu dia de nascimento: ")
    mes = input("Informe o mes de nascimento: ")
    ano = input("Informe o ano de nascimento: ")
    
    print("Você nasceu no dia", dia, "de", mes, "de", ano, ". Correto?")
    resp = input()