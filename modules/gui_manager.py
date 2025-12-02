import tkinter as tk
from modules.audio_manager import escuchar
from modules.command_processor import procesar_comando


def crear_ventana():
    """Crea la interfaz gráfica principal y devuelve la ventana."""

    ventana = tk.Tk()
    ventana.title("Control por voz - Versión modular")  # 🎙️
    ventana.geometry("500x350")
    ventana.config(bg="#1e1e1e")

    titulo = tk.Label(
        ventana,
        text="CONTROL POR VOZ (VOSK)",
        font=("Arial", 16, "bold"),
        bg="#1e1e1e",
        fg="#00ffcc"
    )
    titulo.pack(pady=10)

    texto_label = tk.Label(
        ventana,
        text="Haz clic en Escuchar y da un comando...",
        font=("Arial", 12),
        bg="#1e1e1e",
        fg="white"
    )
    texto_label.pack(pady=5)

    resultado_label = tk.Label(
        ventana,
        text="...",
        font=("Arial", 14, "bold"),
        bg="#1e1e1e",
        fg="#00ffcc"
    )
    resultado_label.pack(pady=10)

    estado_motor = tk.Label(
        ventana,
        text="Motor: OFF",
        font=("Arial", 16, "bold"),
        bg="#333",
        fg="white",
        width=15,
        height=2
    )
    estado_motor.pack(pady=20)

    def ejecutar_reconocimiento():
        texto_label.config(text=" Escuchando... Habla ahora")  # 🎧
        ventana.update()

        text = escuchar()

        texto_label.config(text="Procesando reconocimiento...")
        ventana.update()

        procesar_comando(text, estado_motor, resultado_label, ventana)

    boton = tk.Button(
        ventana,
        text=" Escuchar",  # 🎤
        command=ejecutar_reconocimiento,
        font=("Arial", 14),
        bg="#00ffcc",
        fg="black",
        width=15,
        height=2
    )
    boton.pack(pady=20)

    return ventana
