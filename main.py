import os
import shutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_ORIGEM = os.path.join(BASE_DIR, "pasta_teste")


CATEGORIAS = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "pdfs": [".pdf"],
    "documentos": [".doc", ".docx", ".txt"],
    "planilhas": [".xls", ".xlsx", ".csv"],
    "audios": [".mp3", ".wav"],
    "videos": [".mp4", ".mkv", ".avi"],
    "compactados": [".zip", ".rar", ".7z"],
}


def criar_pasta_se_nao_existir(caminho_pasta):
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)


def descobrir_categoria(extensao):
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return "outros"


def organizar_arquivos():
    if not os.path.exists(PASTA_ORIGEM):
        print("A pasta_teste não foi encontrada.")
        return

    arquivos = os.listdir(PASTA_ORIGEM)

    if not arquivos:
        print("A pasta_teste está vazia.")
        return

    for nome_arquivo in arquivos:
        caminho_arquivo = os.path.join(PASTA_ORIGEM, nome_arquivo)

        if os.path.isdir(caminho_arquivo):
            continue

        nome, extensao = os.path.splitext(nome_arquivo)
        extensao = extensao.lower()

        categoria = descobrir_categoria(extensao)
        pasta_destino = os.path.join(PASTA_ORIGEM, categoria)

        criar_pasta_se_nao_existir(pasta_destino)

        novo_caminho = os.path.join(pasta_destino, nome_arquivo)
        shutil.move(caminho_arquivo, novo_caminho)

        print(f"Arquivo '{nome_arquivo}' movido para a pasta '{categoria}'.")

    print("\nOrganização concluída com sucesso.")


if __name__ == "__main__":
    organizar_arquivos()
