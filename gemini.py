from google import genai
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
from uuid import uuid4

# Opcional: Defina a variável de ambiente diretamente
# os.environ["GEMINI_API_KEY"] = "sua_chave_api_aqui"
# os.environ["MODELO"] = "gemini-2.5-flash"

# Carrega a variável de ambiente do arquivo .env
load_dotenv()

# Modelo pode ser colocado na variável de ambiente MODELO no arquivo .env
MODELO = os.getenv("MODELO", "gemini-2.0-flash-preview-image-generation")

# O Gemini só possui um modelo de imagem com requisições gratuitas

client = genai.Client()

def gerar_carro_com_placa(modelo_carro, placa):
    prompt = f"Gere um {modelo_carro} com placa {placa}"
    response = client.models.generate_content(
        model=MODELO, 
        contents=prompt,
        config={"response_modalities": ["TEXT", "IMAGE"]}
    )

    nome_arquivo = f"gerada_{uuid4()}_{modelo_carro}_{placa}.png".replace(" ", "_")

    ## É preciso verificar se a resposta veio como texto ou imagem
    ## Às vezes, o modelo alucina e retorna somente texto (sugiro tentar refinar o prompt para evitar isso)
    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = Image.open(BytesIO(part.inline_data.data))
            image.save(nome_arquivo)

def alterar_placa_de_carro_usando_imagem_base(caminho_imagem, placa):
    imagem = Image.open(caminho_imagem)

    prompt = f"""
        Edit the car image by replacing the license plate area with a Mercosul-style plate. Change the license plate to {placa}. 
        Keep the plate size, perspective and reflections matching the original photo. Use the standard Mercosul layout: a thin blue horizontal 
        band at the top with the Mercosul emblem, a white main field with black alphanumeric characters in a bold sans-serif plate font.
    """

    response = client.models.generate_content(
        model=MODELO, 
        contents=[prompt, imagem],
        config={"response_modalities": ["TEXT", "IMAGE"]}
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            imagem = Image.open(BytesIO(part.inline_data.data))
            imagem.save(f"gerada_{caminho_imagem}_{placa}.png")

def descreva_a_placa_do_carro(caminho_imagem):
    imagem = Image.open(caminho_imagem)

    prompt = "Descreva a placa do carro na imagem."

    response = client.models.generate_content(
        model=MODELO, 
        contents=[prompt, imagem],
        config={"response_modalities": ["TEXT", "IMAGE"]}
    )

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            print("Descrição da placa do carro: ")
            print(part.text)

gerar_carro_com_placa("Honda Civic vermelho", "XYZ-1234")
alterar_placa_de_carro_usando_imagem_base("exemplo_carro.png", "ABC-5678")
descreva_a_placa_do_carro("exemplo_carro.png")