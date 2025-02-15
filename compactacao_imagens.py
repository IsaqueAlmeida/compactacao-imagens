import numpy as np


class QuadTree:
    # instanciando os atributos NO, NE, SE, SO, _altura com os valores padrão
    def __init__(self, altura=0):
        self.NO = None
        self.NE = None
        self.SE = None
        self.SO = None
        self._altura = altura
        self.imagem_com_cores_mesclados = None
        self.folha = True

    # obtendo um código da imagem com as cores mescladas
    # fazendo a imagem em quatro quadrantes
    def inserir_vertices(self, img):
        self.imagem_com_cores_mesclados = obter_img_com_cores_mesclados(img)

        imagem_dividida = dividir_em_4(img)

        # fazendo a divisão em 4 quadrantes
        if imagens_diferentes(imagem_dividida):
            """ se as imagens tiverem cores diferentes, é criado um filho para
            compor os atributos NO, NE, SE, SO"""
            self.folha = False
            h = self._altura + 1

            self.NO = QuadTree(h)
            self.NE = QuadTree(h)
            self.SE = QuadTree(h)
            self.SO = QuadTree(h)

            self.NO.inserir_vertices(imagem_dividida[0])
            self.NE.inserir_vertices(imagem_dividida[1])
            self.SE.inserir_vertices(imagem_dividida[2])
            self.SO.inserir_vertices(imagem_dividida[3])
        return self

    # criando uma nova função para obter vértices
    """
        retornando a imagem formada pelos quadrantes de uma dada altura ou de
        um vértice
    """
    def obter_vertices(self, altura):
        if self.folha or self._altura == altura:
            return self.imagem_com_cores_mesclados
        return concatenar(
            self.NO.obter_vertices(altura),
            self.NE.obter_vertices(altura),
            self.SE.obter_vertices(altura),
            self.SO.obter_vertices(altura)
          )


def obter_img_com_cores_mesclados(img):
    """ Calculando a cor média da imagem"""
    if img.size == 0:  # Se a imagem estiver vazia, retorne preto
        return np.array([0, 0, 0], dtype=np.uint8)

    # Calcula a média dos valores dos pixels: assumindo RGB
    media_cor = np.mean(img, axis=(0, 1))

    # retornando um array representando a cor média: convertendo para uint8
    return np.array(media_cor, dtype=np.uint8)


def dividir_em_4(img):
    """ Divide a imagem em quatro quadrantes (NO, NE, SE, SO)"""
    altura, largura, _ = img.shape  # obtém dimensões da imagem
    meio_h, meio_w = altura // 2, largura // 2  # calcula os pontos médios

    # Retornando os quatros quadrantes da img
    return [
        img[:meio_h, :meio_w],  # NO - Canto superior esquerdo
        img[:meio_h, meio_w:],  # NE - Canto superior direito
        img[meio_h:, :meio_w],  # SO - Canto inferior esquerdo
        img[meio_h:, meio_w:]   # SE - Canto inferior direito
    ]


def imagens_diferentes(imagens):
    # verifica se os quadrantes são diferentes o suficente para subdividir
    """obtém cores médias"""
    cores = [obter_img_com_cores_mesclados(img) for img in imagens]

    # Calcula a diferença máxima entre os quadrantes
    diferenca_max = np.max(np.abs(np.diff(cores, axis=0)))

    # Se a diferença for grande, continua dividindo
    return diferenca_max > 30  # 30 já é um limiar ajustável


def concatenar(NO, NE, SO, SE):
    # Junta os quadrantes para reconstruir a imagem
    """ Une os quadrantes superiores"""
    linha_superior = np.hstack((NO, NE))
    """Une os quadrantes inferiores"""
    linha_inferior = np.hstack((SO, SE))

    return np.vstack((linha_superior, linha_inferior))  # Junta as linhas
