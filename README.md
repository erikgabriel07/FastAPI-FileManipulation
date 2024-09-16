# FastAPI-FileManipulation

Desenvolvimento de um serviço monolítico em linguagem Python utilizando o Framework FastAPI com Upload e Manipulação de Arquivos

## Descrição

**Fastapi-File** é um serviço monolítico desenvolvido em Python utilizando o framework FastAPI. Este projeto permite o upload e a manipulação de arquivos, proporcionando uma interface simples e eficiente para gerenciar arquivos em uma aplicação web.

## Funcionalidades

- **Upload de arquivos**: Suporte para o envio de múltiplos tipos de arquivos.
- **Manipulação de arquivos**: Processamento e gestão de arquivos enviados.
- **API RESTful**: Exposição de endpoints para interação com o serviço de forma programática.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para o desenvolvimento do serviço.
- **FastAPI**: Framework web utilizado para construir a API do serviço.
- **Uvicorn**: Servidor ASGI usado para rodar a aplicação FastAPI.
- **Pydantic**: Utilizado para a validação dos dados das requisições.
- **Docker**: Para containerização da aplicação.

## Pré-requisitos

- **Python 3.x**
- **Pip** para instalação de dependências
- **Docker** (opcional) para execução em contêiner.

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/erikgabriel07/FastAPI-FileManipulation
    cd FastAPI-FileManipulation
    ```

2. Crie um ambiente virtual:

    - Para Linux/Mac:
      ```bash
      python -m venv venv
      source venv/bin/activate
      ```
    - Para Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

1. Inicie o servidor:

    ```bash
    uvicorn main:app --reload
    ```

2. Acesse a documentação interativa da API em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

3. Use os endpoints disponíveis para fazer upload e manipular arquivos.

## Docker

1. Build a imagem Docker:

    ```bash
    docker build -t fastapi-file .
    ```

2. Execute o contêiner:

    ```bash
    docker run -d -p 8000:8000 fastapi-file
    ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [https://github.com/erikgabriel07/FastAPI-FileManipulation/blob/main/LICENSE](LICENSE) para obter mais informações.
