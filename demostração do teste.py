import getpass
import json
import os
import urllib.error
import urllib.request


API_URL = "https://api.openai.com/v1/chat/completions"
MODELO = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")
INSTRUCAO = (
    "Você é um assistente amigável que conversa em português claro. "
    "Responda de forma natural, útil e adequada para a idade de quem conversa."
)
MAX_MENSAGENS = 20


def consultar_openai(chave, historico):
    dados = json.dumps(
        {
            "model": MODELO,
            "messages": [{"role": "system", "content": INSTRUCAO}, *historico],
        }
    ).encode("utf-8")
    requisicao = urllib.request.Request(
        API_URL,
        data=dados,
        headers={
            "Authorization": f"Bearer {chave}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(requisicao, timeout=45) as resposta:
            resultado = json.loads(resposta.read().decode("utf-8"))
    except urllib.error.HTTPError as erro:
        if erro.code == 401:
            raise RuntimeError(
                "A chave da API foi recusada. Verifique se OPENAI_API_KEY contém "
                "sua chave da OpenAI, e não o caminho do arquivo Python."
            ) from None
        try:
            corpo = json.loads(erro.read().decode("utf-8"))
            detalhe = corpo.get("error", {}).get("message", "erro sem detalhes")
        except (json.JSONDecodeError, UnicodeDecodeError):
            detalhe = "a API retornou uma resposta de erro inválida"
        raise RuntimeError(f"A API recusou a solicitação ({erro.code}): {detalhe}") from None
    except urllib.error.URLError:
        raise RuntimeError(
            "Não foi possível conectar à API. Verifique sua internet e tente novamente."
        ) from None
    except TimeoutError:
        raise RuntimeError("A API demorou demais para responder. Tente novamente.") from None
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise RuntimeError("A API retornou uma resposta que não consegui entender.") from None

    try:
        texto = resultado["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        raise RuntimeError("A resposta da API veio sem uma mensagem válida.") from None

    if not isinstance(texto, str) or not texto.strip():
        raise RuntimeError("A API retornou uma resposta vazia.")
    return texto.strip()


def main():
    chave = os.environ.get("OPENAI_API_KEY", "").strip()
    if not chave:
        try:
            chave = getpass.getpass(
                "Cole sua chave da API (a digitação ficará oculta): "
            ).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEntrada da chave cancelada.")
            return
        if not chave:
            print("Nenhuma chave foi informada. O chatbot não pode iniciar.")
            return

    historico = []
    print("=== BATE-PAPO COM IA ===")
    print("Conversa conectada à OpenAI. Digite 'sair' para terminar.")

    while True:
        try:
            mensagem = input("Você: ").strip()
        except EOFError:
            print("\nBot: Até mais!")
            break

        if mensagem.lower() in {"sair", "quit", "exit"}:
            print("Bot: Até mais!")
            break
        if not mensagem:
            continue

        historico.append({"role": "user", "content": mensagem})
        try:
            resposta = consultar_openai(chave, historico)
        except RuntimeError as erro:
            historico.pop()
            print(f"Bot: {erro}")
            continue

        historico.append({"role": "assistant", "content": resposta})
        historico = historico[-MAX_MENSAGENS:]
        print(f"Bot: {resposta}")


if __name__ == "__main__":
    main()
