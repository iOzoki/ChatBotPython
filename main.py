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

def responder(pergunta: str, BancoDeDados: dict) -> str | None:
    for i in BancoDeDados["questions"]:
        if i ["question"] == pergunta:
            return i["answer"]
        
def chatbot():
    BD: dict = Carregar_BD("BandoDeDados.json")

    while True:
        user_input: str = input("You : ")

        if user_input.lower() == "sair":
            break

        best_response: str | None = Encontrar_melhor_resposta(user_input, [i["question"]for i in BD["questions"]])

        if best_response:
            answer: str = responder(best_response, BD)
            print(f"Bot: {answer}")
        
        else:
            new_answer_input: str = input("""Bot: Eu não sei responder isso, você poderia me ensinar?\n Digite a resposta para sua pergunta, ou se preferir "pular":""")

            if user_input.lower() == "sair":
                break

            if(new_answer_input != "pular"):
                BD["questions"].append({"question": user_input, "answer": new_answer_input})
                Salvar_BD("BancoDeDados.json", BD)

                print("Obrigado por me ensinar!!")