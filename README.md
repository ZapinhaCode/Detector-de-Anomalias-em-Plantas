# Detector de Anomalias e Pulverização Automatizada em Plantas

## Descrição do trabalho

- Esta aplicação desenvolvida em Python que utiliza técnicas de processamento de imagens para identificar anomalias em imagens agrícolas. Com uma interface gráfica amigável, o sistema permite que o usuário carregue uma imagem, detecte problemas visuais e ative um mecanismo de pulverização automatizado (simulado).

## Funcionalidades

- **Upload de imagens:** Carregue imagens diretamente na aplicação.
- **Processamento de imagens:**
    - Conversão para escala de cinza.
    - Suavização com filtro gaussiano.
    - Detecção de bordas e contornos.
- **Detecção de anomalias:** Identifica possíveis problemas com base nos contornos detectados.
- **Interface gráfica:** Desenvolvida com Tkinter, possui botões e caixas de diálogo intuitivos.
- **Simulação de pulverização:** O sistema pergunta ao usuário se deseja ativar o mecanismo de pulverização ao detectar problemas.

## Tecnologias Utilizadas

- **Python 3.9+**

- **Bibliotecas:**
    - OpenCV - Processamento de imagens.
    - Pillow - Manipulação de imagens para integração com Tkinter.
    - Tkinter - Interface gráfica.

## Instalação

### Clone este repositório:

```bash
    git clone https://github.com/seu-usuario/agroapp.git
    cd agroapp
```
### Crie um ambiente virtual

```bash
    python -m venv venv
    source venv/bin/activate # Linux e MacOS
    venv\Scripts\activate # Windows
```

### Instale as dependências:

```bash
    pip install -r requirements.txt
```

## Executar o aplicativo
```bash
    python app.py
```
__________________________________________________________________________________
Fim da Documentação