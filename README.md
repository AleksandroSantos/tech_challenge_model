# Previsão de Preços de Imóveis em São Paulo

Este projeto visa prever os preços de imóveis na cidade de São Paulo utilizando técnicas de machine learning. A aplicação foi desenvolvida com base em um conjunto de dados coletados do Kaggle e inclui um modelo preditivo implementado em uma interface simples utilizando Streamlit.

## Objetivo do Projeto

O objetivo é criar um modelo que permita prever o preço de venda de imóveis com base em suas características, ajudando compradores e vendedores a tomar decisões informadas no mercado imobiliário.

## Coleta de Dados

Os dados foram coletados do Kaggle e contêm informações sobre imóveis, incluindo características como área útil, número de banheiros, suítes e tipo de imóvel.

## Estrutura do Projeto

- `data/`: Contém o dataset original e os dados processados.
- `models/`: Armazena o modelo treinado em formato `.pkl`.
- `notebooks/`: Jupyter Notebooks com análise exploratória e desenvolvimento do modelo.
- `src/`:
  - `app.py`: Aplicação Streamlit que permite a previsão de preços de imóveis.
  - `download_data.py`: Script que utiliza a API do Kaggle para realizar o download do dataset.
  
- `README.md`: Este arquivo, que fornece uma visão geral do projeto.

## Pré-requisitos

Para executar o script, é necessário:

1. **Conta no Kaggle**: Crie uma conta em [kaggle.com](https://www.kaggle.com/).
2. **Instalar a biblioteca Kaggle**: Execute o seguinte comando no terminal para instalar a biblioteca:
    ```bash
    pip install kaggle
    ```

3. **Configurar a API do Kaggle**:
    - Acesse [My Account](https://www.kaggle.com/account) e crie um token de API para baixar o arquivo `kaggle.json`.
    - Mova o arquivo `kaggle.json` para o diretório:
        - **Linux/Mac**: `~/.kaggle/kaggle.json`
        - **Windows**: `C:\Users\<SeuUsuário>\.kaggle\kaggle.json`
    - Verifique as permissões (Linux/Mac: `chmod 600 ~/.kaggle/kaggle.json`).

## Instalação

Para executar este projeto localmente, siga as etapas abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/AleksandroSantos/tech_challenge_model.git
   cd tech_challenge_model
   ```

2. Instale as dependências:
   ```bash
    pip install -r requirements.txt
   ```

3. Execute o script para baixar os dados:
   ```bash
    python src/download_data.py
   ```

4. Treino e salvar modelo:
   ```bash
    notebooks/eda-tc-fase3.ipynd
   ```

5. Execute a Aplicação Streamlit:
   ```bash
    streamlit run src/app.py
   ```