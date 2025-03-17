class SegmentTree:
    def __init__(self, vetor):
        self.n = len(vetor)
        self.vetor = vetor.copy() 
        self.arvore = [ (0, float('inf'), float('-inf')) ] * (4 * self.n)
        self.atualizacao_preguicosa = [None] * (4 * self.n)
        self.construir(0, 0, self.n - 1)

    def construir(self, no, inicio, fim):
        if inicio == fim:
            self.arvore[no] = (self.vetor[inicio], self.vetor[inicio], self.vetor[inicio])
        else:
            meio = (inicio + fim) // 2
            filho_esquerda = 2 * no + 1
            filho_direita = 2 * no + 2
            self.construir(filho_esquerda, inicio, meio)
            self.construir(filho_direita, meio + 1, fim)
            soma = self.arvore[filho_esquerda][0] + self.arvore[filho_direita][0]
            minimo = min(self.arvore[filho_esquerda][1], self.arvore[filho_direita][1])
            maximo = max(self.arvore[filho_esquerda][2], self.arvore[filho_direita][2])
            self.arvore[no] = (soma, minimo, maximo)

    def propagar_preguica(self, no, inicio, fim):
        if self.atualizacao_preguicosa[no] is not None:
            valor = self.atualizacao_preguicosa[no]
            self.arvore[no] = (valor * (fim - inicio + 1), valor, valor)
            if inicio != fim:
                esq = 2 * no + 1
                dir = 2 * no + 2
                self.atualizacao_preguicosa[esq] = valor
                self.atualizacao_preguicosa[dir] = valor
            self.atualizacao_preguicosa[no] = None

    def atualizar(self, indice, valor):
        self._atualizar(indice, valor, 0, 0, self.n - 1)

    def _atualizar(self, indice, valor, no, inicio, fim):
        self.propagar_preguica(no, inicio, fim)
        if inicio == fim:
            self.arvore[no] = (valor, valor, valor)
        else:
            meio = (inicio + fim) // 2
            esq = 2 * no + 1
            dir = 2 * no + 2
            if indice <= meio:
                self._atualizar(indice, valor, esq, inicio, meio)
            else:
                self._atualizar(indice, valor, dir, meio + 1, fim)
            soma = self.arvore[esq][0] + self.arvore[dir][0]
            minimo = min(self.arvore[esq][1], self.arvore[dir][1])
            maximo = max(self.arvore[esq][2], self.arvore[dir][2])
            self.arvore[no] = (soma, minimo, maximo)

    def consulta(self, l, r):
        return self._consulta(l, r, 0, 0, self.n - 1)

    def _consulta(self, l, r, no, inicio, fim):
        self.propagar_preguica(no, inicio, fim)
        if r < inicio or l > fim:
            return (0, float('inf'), float('-inf'))
        if l <= inicio and fim <= r:
            return self.arvore[no]
        meio = (inicio + fim) // 2
        esq = self._consulta(l, r, 2 * no + 1, inicio, meio)
        dir = self._consulta(l, r, 2 * no + 2, meio + 1, fim)
        return (esq[0] + dir[0], min(esq[1], dir[1]), max(esq[2], dir[2]))

    def atualizacao_intervalo(self, l, r, valor):
        self._atualizacao_intervalo(l, r, valor, 0, 0, self.n - 1)

    def _atualizacao_intervalo(self, l, r, valor, no, inicio, fim):
        self.propagar_preguica(no, inicio, fim)
        if r < inicio or l > fim:
            return
        if l <= inicio and fim <= r:
            self.arvore[no] = (valor * (fim - inicio + 1), valor, valor)
            if inicio != fim:
                esq = 2 * no + 1
                dir = 2 * no + 2
                self.atualizacao_preguicosa[esq] = valor
                self.atualizacao_preguicosa[dir] = valor
            return
        meio = (inicio + fim) // 2
        self._atualizacao_intervalo(l, r, valor, 2 * no + 1, inicio, meio)
        self._atualizacao_intervalo(l, r, valor, 2 * no + 2, meio + 1, fim)
        esq_val = self.arvore[2 * no + 1]
        dir_val = self.arvore[2 * no + 2]
        soma = esq_val[0] + dir_val[0]
        minimo = min(esq_val[1], dir_val[1])
        maximo = max(esq_val[2], dir_val[2])
        self.arvore[no] = (soma, minimo, maximo)


if __name__ == '__main__':
    vetor = [1, 3, 5, 7, 9, 11]
    arvore_seg = SegmentTree(vetor)

    print("Vetor original:", vetor)
    
    resultado = arvore_seg.consulta(1, 3)
    print("Consulta intervalo [1, 3] -> Soma: {}, Mínimo: {}, Máximo: {}".format(*resultado))
    
    arvore_seg.atualizar(1, 10)
    resultado = arvore_seg.consulta(1, 3)
    print("Após atualizar índice 1 para 10, consulta [1, 3] -> Soma: {}, Mínimo: {}, Máximo: {}".format(*resultado))
    
    arvore_seg.atualizacao_intervalo(0, 2, 5)
    resultado = arvore_seg.consulta(0, 5)
    print("Após atualizar intervalo [0, 2] para 5, consulta [0, 5] -> Soma: {}, Mínimo: {}, Máximo: {}".format(*resultado))

    resultado = arvore_seg.consulta(3, 5)
    print("Consulta intervalo [3, 5] -> Soma: {}, Mínimo: {}, Máximo: {}".format(*resultado))