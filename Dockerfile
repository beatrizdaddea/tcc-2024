# Use uma imagem Debian mais antiga
FROM debian:buster

# Instale as dependências necessárias
RUN apt-get update && \
    apt-get install -y wget build-essential libssl-dev libffi-dev libsqlite3-dev libreadline-dev libbz2-dev zlib1g-dev

# Download e instalação do Python 3.9
RUN wget https://www.python.org/ftp/python/3.9.7/Python-3.9.7.tgz && \
    tar -xzf Python-3.9.7.tgz && \
    cd Python-3.9.7 && \
    ./configure --enable-optimizations && \
    make && \
    make install && \
    cd .. && \
    rm -rf Python-3.9.7*

# Crie e defina o diretório de trabalho
WORKDIR /tcc-2024

# Copie o código-fonte para o contêiner
COPY . /tcc-2024

# Crie e ative o ambiente virtual
RUN python3.9 -m venv landslide_detection
ENV PATH="/tcc-2024/landslide_detection/bin:$PATH"

# Instale as dependências
RUN pip install --upgrade pip
RUN pip install ultralytics yolov8 roboflow

# Exponha a porta do Jupyter Notebook
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook
CMD ["jupyter-notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
