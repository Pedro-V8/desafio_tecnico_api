# Use a base image with Python pre-installed
FROM python:3.8

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o código da aplicação para o contêiner
COPY . /app

# Expõe a porta em que a aplicação Flask vai rodar
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "run.py"]