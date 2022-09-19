pesokg: float; pesogr: int; racaodiaria: float; resto: float
pesokg = float(input('Informe quantos quilogramas tem o saco de ração comprado: '))
racaodiaria = float(input('Informe quantas gramas de ração os seus gatos comem por dia: '))
pesogr = pesokg* 1000
resto = pesogr - racaodiaria * 2 * 5
print('após 5 dias restará: ',resto,'gramas')
