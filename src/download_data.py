import os
import zipfile

# Função para baixar e descompactar o dataset
def download_and_extract_kaggle_dataset():
    # Comando para baixar o dataset do Kaggle (substitua o dataset pelo que você deseja)
    os.system('kaggle datasets download -d ex0ticone/house-prices-of-sao-paulo-city')

    # Nome do arquivo baixado
    zip_file = 'house-prices-of-sao-paulo-city.zip'

    # Verifica se o arquivo foi baixado
    if os.path.exists(zip_file):
        print("Dataset baixado com sucesso!")

        # Descompacta o arquivo zip
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall('../data/raw')
        print("Dataset extraído para o diretório 'data/raw'.")
    else:
        print("Erro ao baixar o dataset.")

if __name__ == "__main__":
    # Executa a função de download e extração
    download_and_extract_kaggle_dataset()
