import json
from difflib import get_close_matches

def Carregar_BD(file_path: str) -> dict:

    with open(file_path, "r") as file:
        data: dict = json.load(file)
        return data
    
def Salvar_BD(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2) 

def Encontrar_melhor_resposta(mensagem_usuario: str, respostas: list[str]) -> str | None:
    m_resposta: list = get_close_matches(mensagem_usuario, respostas, n=1, cutoff=0.6)
    return m_resposta[0] if m_resposta else None