def calcular_media(*args: int) -> float:
    if args == 0:
        return 0.0
    else: return sum(args)/len(args)
print(calcular_media(1,2,3,4))

def estilizar_nome_por_posicao(nome: str) -> str:
    novaString = []
    for i, caractere in enumerate(nome):
        if i % 2 == 0:
            novaString.append(str.upper(caractere))
        else: 
            novaString.append(str.lower(caractere))
    return ''.join(novaString)
print(estilizar_nome_por_posicao('Eduardo'))

from typing import List

def comparar_nomes_simples(nome1: str, nome2: str) -> List[str]:
    resultados: List[str] = []
    for i, (c1, c2) in enumerate(zip(nome1, nome2)):
        if c1 == c2:
            resultados.append(f"Posição {i}: {c1} == {c2}")
        else:
            resultados.append(f"Posição {i}: {c1} != {c2}")
    return resultados
print(comparar_nomes_simples('Eduardo','Edu'))