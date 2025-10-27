# Exemplo de Uso da API Gemini - Geração e Edição de Imagens

Exemplo de como usar a API do Google Gemini para gerar e editar imagens de carros com placas personalizadas.

### Requisitos

- Python 3.7 ou superior
- Chave da API do Google Gemini
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/viniciusorsilveira/exemplo_api_gemini.git
cd gemini-api-exemplo
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure sua chave da API do Gemini:
   - Crie um arquivo `.env` na raiz do projeto, conforme o arquivo `.env.example`
   - Adicione sua chave da API:
```env
GEMINI_API_KEY=sua_chave_api_aqui
MODELO=gemini-2.0-flash-preview-image-generation
```

## Executando o Projeto

Execute o script principal:
```bash
python3 gemini.py
```
### Modalidades de Resposta

O modelo usado requer que ambas as modalidades `TEXT` e `IMAGE` sejam especificadas na configuração:
```python
config={"response_modalities": ["TEXT", "IMAGE"]}
```
### Dependências

- `google-genai`: SDK oficial do Google para a API Gemini
- `Pillow`: Manipulação de imagens
- `python-dotenv`: Carregamento de variáveis de ambiente

### Formato de Placas

O projeto está configurado para trabalhar com placas no padrão Mercosul (formato brasileiro), mas pode ser adaptado para outros padrões.

## Como gerar uma chave de API

1. Crie um projeto no Google Cloud (https://console.cloud.google.com/) e **não** ative o Billing (Faturamento)
2. Navegue até o AI Studio do Google para gerar sua chave de API (https://aistudio.google.com/api-keys)
3. Clique em criar chave de API, confira se a cota está no nível gratuito e sem faturamento configurado para evitar gastos.
4. Salve a chave de API e adicione ao arquivo `.env`
