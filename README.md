# QuadTree Image Compression

Este projeto implementa um algoritmo de compressão de imagens utilizando a estrutura de dados **QuadTree**. O objetivo é representar imagens de forma hierárquica e compactada, dividindo a imagem em regiões homogêneas e reduzindo a quantidade de dados necessária para armazená-la.

## 📖 O que é uma QuadTree?

Uma **QuadTree** é uma estrutura de árvore em que cada nó possui, no máximo, quatro filhos. Ela é amplamente utilizada em computação gráfica, compressão de imagens e processamento espacial. No contexto deste projeto, a **QuadTree** é usada para dividir uma imagem em quadrantes até que cada região seja suficientemente homogênea.

## 🏗️ Estrutura do Projeto

O projeto contém dois arquivos principais:

1. **`compactacao_imagens.py`** → Implementa a classe `QuadTree` e os métodos para construção e manipulação da árvore.
2. **`teste_quadtree.py`** → Carrega uma imagem, aplica a compressão utilizando QuadTree e exibe os resultados.

---

## 📜 Explicação do Código

### 📂 `compactacao_imagens.py`

Este arquivo contém a implementação da **QuadTree** e suas funções auxiliares.

### 🔹 Classe `QuadTree`

A classe `QuadTree` é responsável por armazenar e processar os dados da imagem de forma hierárquica.

#### 🔑 **Atributos:**
- `NO`, `NE`, `SE`, `SO` → Representam os filhos da árvore (nós superiores e inferiores).
- `_altura` → Nível atual da árvore.
- `max_altura` → Profundidade máxima permitida para a árvore.
- `imagem_com_cores_mesclados` → Representação da cor média da região.
- `folha` → Define se o nó é uma folha (sem filhos).

#### 🛠️ **Métodos:**
- `inserir_vertices(img)`: Insere uma imagem na árvore QuadTree, dividindo-a em regiões menores.
- `obter_vertices(altura)`: Retorna a imagem reconstruída até uma determinada altura.

### 🔹 Funções Auxiliares

- **`obter_img_com_cores_mesclados(img)`**: Calcula a cor média de uma região da imagem.
- **`dividir_em_4(img)`**: Divide a imagem em quatro quadrantes (NO, NE, SO, SE).
- **`imagens_diferentes(imagens)`**: Determina se uma subdivisão da imagem é necessária, com base na diferença de cores.
- **`concatenar(NO, NE, SO, SE)`**: Junta os quadrantes para reconstruir a imagem.

---

### 📂 `teste_quadtree.py`

Este arquivo carrega uma imagem, aplica a compressão usando a **QuadTree** e exibe os resultados.

#### 🛠️ **Passo a passo:**
1. **Carregar a imagem:**
   ```python
   img = cv2.imread('sua_imagem.png')
   ```
2. **Criar a árvore QuadTree e inserir a imagem:**
   ```python
   quadtree = QuadTree()
   quadtree.inserir_vertices(img)
   ```
3. **Obter a reconstrução da imagem:**
   ```python
   img_reconstruida = quadtree.obter_vertices(2)
   ```
4. **Converter para escala de cinza e exibir:**
   ```python
   img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   img_reconstruida_gray = cv2.cvtColor(img_reconstruida, cv2.COLOR_BGR2GRAY)
   cv2.imshow('Imagem Original', img_gray)
   cv2.imshow('Imagem Reconstruída', img_reconstruida_gray)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   ```

---

## 🎯 Aplicações

- Compressão de imagens.
- Representação hierárquica de imagens.
- Processamento espacial e segmentação.

## 🎓 Aprendizado

Este projeto foi desenvolvido como parte do curso de **Ciência de Dados**, na disciplina de **Estrutura de Dados**, na **Faculdade Ampli**.

## 🔗 Contato

🔗 **LinkedIn**: [Isaque Almeida](https://www.linkedin.com/in/isaque-f-s-almeida/)  
🐙 **GitHub**: [IsaqueAlmeida](https://github.com/IsaqueAlmeida)

