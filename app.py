import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Função para analisar a imagem
def analyze_image():
    image_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png *.jpg *.jpeg *.gif")])
    if image_path:
        # cv2.imread: Carrega a imagem selecionada no OpenCV.
        image = cv2.imread(image_path)

        # cv2.cvtColor: Converte a imagem de cor (BGR) para escala de cinza
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # cv2.GaussianBlur: Aplica um filtro gaussiano para suavizar a imagem, reduzindo ruídos.
        blurred = cv2.GaussianBlur(gray, (5, 5), 0) # Tamanho do kernel e indicação de calculo automatico do desvio padrão gaussiano

        # cv2.Canny: Detecta bordas na imagem com limites inferior e superior de 50 e 150.
        edges = cv2.Canny(blurred, 50, 150)

        # cv2.findContours: Encontra os contornos detectados nas bordas da imagem.
        # edges.copy(): Cria uma cópia da imagem de bordas para preservar a original.
        # cv2.RETR_EXTERNAL: Captura apenas os contornos externos.
        # cv2.CHAIN_APPROX_SIMPLE: Simplifica os pontos do contorno, reduzindo o número de vértices.
        contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # cv2.drawContours: Desenha os contornos detectados sobre a imagem original.
        # image: A imagem na qual os contornos serão desenhados.
        # contours: Lista de contornos a serem desenhados.
        # -1: Desenha todos os contornos.
        # (0, 255, 0): Cor verde (formato BGR).
        # 2: Espessura da linha.
        cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
        
        # Verificar se há anomalia
        if len(contours) > 0:
            ask_for_spraying()

        # Converter a imagem do OpenCV para o formato do tkinter
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Converte a imagem do formato OpenCV para um objeto compatível com tkinter
        img_tk = ImageTk.PhotoImage(Image.fromarray(image_rgb))
        
        # Atualizar a label com a imagem analisada
        result_label.config(image=img_tk)
        result_label.image = img_tk

# Função para perguntar sobre a pulverização
def ask_for_spraying():
    response = messagebox.askyesno("Detecção de Anomalia", "Uma anomalia foi detectada. Deseja ativar o mecanismo de pulverização?", icon="warning")
    if response:
        start_spraying()

# Função para iniciar a pulverização
def start_spraying():
    # Coloque aqui a lógica para ativar o mecanismo de pulverização
    messagebox.showinfo("Pulverização Ativada", "O mecanismo de pulverização foi ativado!", icon="info")

# Criar a janela principal
root = tk.Tk()
root.title("AgroApp - Detecção e Pulverização")

# Configurar cores do agro
bg_color = "#f0f7d4"  # Cor de fundo
button_color = "#a3c34a"  # Cor dos botões

# Aplicar cor de fundo
root.configure(bg=bg_color)

# Botão para fazer upload da imagem
upload_button = tk.Button(root, text="Fazer Upload da Imagem", command=analyze_image, bg=button_color)
upload_button.pack(pady=10)

# Label para exibir a imagem analisada
result_label = tk.Label(root, bg=bg_color)
result_label.pack()

# Iniciar o loop principal da interface
root.mainloop()
