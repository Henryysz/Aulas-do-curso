def calculo_valor_hora(salario: float, dias: int, horas: int = 8) -> float:
    return round(salario / (dias * horas))

salario:float = float(input('Digite o salário: '))
dias: int = int(input('Digite o número de dias: '))
horas: str = input('Digite o número de horas trabalhadas[Padrão 8h]: ')


if horas == 8:
    print(f'Valor/hora R${calculo_valor_hora(salario, dias)}')
else:
    print(f'Valor/hora R${calculo_valor_hora(salario, dias, int(horas))}')
