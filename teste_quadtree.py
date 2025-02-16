import cv2
from compactacao_imagens import QuadTree


# carregando uma imagem
img = cv2.imread('nauhanne.jpeg')

# criando uma árvore QuadTree e inserir a imagem
quadtree = QuadTree()
quadtree.inserir_vertices(img)

# obter uma reconstrução da imagem na altura 2
img_reconstruida = quadtree.obter_vertices(quadtree.max_altura)

# convertendo para uma escala de cinza
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_reconstruida_gray = cv2.cvtColor(img_reconstruida, cv2.COLOR_BGR2GRAY)

# Exibir a imagem original e a reconstruída para comparação
cv2.imshow('Imagem Original', img_gray)
cv2.imshow('Imagem Reconstruida', img_reconstruida_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
