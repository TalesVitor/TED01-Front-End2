maior_alt = 0
menor_alt = float('inf')
soma_alt_masc = 0
quant_masc = 0
quant_fem = 0

for i in range(1, 16):
    print(f"Pessoa {i}:")

    while True:
        try:
            altura = float(input("Digite a altura em metros: "))
            if altura <= 0:
                print("A altura deve ser positiva.")
                continue
            break
        except ValueError:
            print("Digite um número válido.")

    while True:
        genero = input("Digite o genêro: M para Masculino / F para Feminino. ")
        if genero in ['M', 'F']:
            break
        else:
            print("Inválido, digite apenas M ou F.")

    if altura>maior_alt:
        maior_alt = altura
    if altura<menor_alt:
        menor_alt = altura


    if genero == 'M':
        soma_alt_masc += altura
        quant_masc += 1
    elif genero == 'F':
        quant_fem += 1


    if quant_masc > 0:
        media_masc = soma_alt_masc / quant_masc
    else:
        media_masc = 0

    print("Resultados")
    print(f"Maior altura do grupo: {maior_alt:.2f}")
    print(f"Menor altura do grupo: {menor_alt:.2f}")
    if quant_masc > 0:
        print(f"Média de altura dos homens: {media_masc:.2f}")
    else:
        print("Não há homens no grupo para calcular média de altura.")
    print(f"Número de mulheres: {quant_fem}")




