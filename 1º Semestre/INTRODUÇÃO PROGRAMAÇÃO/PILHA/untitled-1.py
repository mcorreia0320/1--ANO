def pilha():
    return []

def e_pilha(x):
    return isinstance(x, list)

def pilha_vazia(pilha):
    return pilha == []

def inserir(pilha, elemento):
    if (e_pilha(pilha)):
        return [elemento] + pilha
    
def topo(pilha):
    if not e_pilha(pilha):
        raise TypeError ('Não é uma pilha')
    if pilha_vazia:
        raise ValueError ('A pilha está vazia')
    return pilha[0]

def tira(pilha):
    if not e_pilha(pilha):
        raise TypeError ('Não é uma pilha')
    if pilha_vazia:
        raise ValueError ('A pilha está vazia')    
    return pilha[1:]

def pilhas_iguais(pilha_1, pilha_2):
    return pilha_1 == pilha_2
