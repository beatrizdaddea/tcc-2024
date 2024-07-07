# Detecção de Cicatrizes de Terra

Este projeto tem como objetivo detectar cicatrizes de terra em imagens de satélite.

## Instalação

Siga os passos abaixo para instalar e configurar o projeto em seu ambiente local:

1. Clone o repositório:

  ```shell
  git clone https://github.com/seu-usuario/nome-do-repositorio.git
  ```

2. Acesse o diretório do projeto:

  ```shell
  cd nome-do-repositorio
  ```

3. Intalação:
  - No terminal instalar o Flask

    ```shell
    pip install Flask
    ```

    - Instalar Ultralytics/Yolo 

    ```shell
    pip install pip install ultralytics
    ```

    - Instalar CV2 

    ```shell
    pip install opencv-python
    ```

4. No terminal rodar aplicação (root):
    ```shell
    flask --app yolo_app.py run --host=0.0.0.0
    ```

## Contribuição

Se você deseja contribuir para este projeto, siga as etapas abaixo:

1. Faça um fork do repositório.

2. Crie uma nova branch:

  ```shell
  git checkout -b minha-nova-feature
  ```

3. Faça as alterações desejadas.

4. Faça o commit das suas alterações:

  ```shell
  git commit -m "Adiciona nova feature"
  ```

5. Faça o push para o repositório remoto:

  ```shell
  git push origin minha-nova-feature
  ```

6. Abra um pull request no repositório original.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).