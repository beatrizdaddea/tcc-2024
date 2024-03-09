# Use a imagem base Python
FROM python:3.9

# Crie e defina o diretório de trabalho
WORKDIR /tcc-2024

# Copie o código-fonte para o contêiner
COPY . /tcc-2024

# Crie e ative o ambiente virtual
RUN python -m venv landslide_detection
RUN /bin/bash -c "source landslide_detection/bin/activate"

# Instale as dependências
RUN pip install --upgrade pip
RUN pip install ultralytics yolov8 roboflow

# Exponha a porta do Jupyter Notebook
EXPOSE 8888

# Comando para iniciar o Jupyter Notebook
CMD ["bash", "-c", "source landslide_detection/bin/activate && jupyter-notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"]

