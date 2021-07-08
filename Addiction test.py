def notas(* n, sit=True):
    """
    => Analisa desempenho de alunos
    :param n: Recebe os valores dentro do dicionário
    :param sit: Situação final, mostra Boa, razoável ou Ruim
    :return: Retorna os valores para print
    """
    r = dict()
    r ['total'] = len(n)
    r ['maior'] = max(n)
    r ['menor'] = min(n)
    r ['média'] = sum(n) / len(n)
    if sit:
        if r ['média'] > 70:
            r ['situação'] = "Boa"
        elif r ['média'] >= 50:
            r ['situação'] = "Razoável"
        else:
            r['situação'] = "Ruim"
    return r


#Principal
resp = notas(37, 68, 75, 77.4, 95.7)
print(resp)
help(notas)
