import tkinter as tk
import matplotlib.pyplot as plt

def actualizar_grafica(temperatura):
    # Establecer el rango de la barra o termómetro
    min_valor = 0
    max_valor = 255

    # Normalizar el valor de la temperatura dentro del rango de 0 a 1
    valor_normalizado = (temperatura - min_valor) / (max_valor - min_valor)

    # Actualizar la barra o termómetro en la ventana
    canvas.coords(barra, 10, 10, 10 + valor_normalizado * 400, 40)

    # Actualizar la etiqueta de temperatura en la ventana
    etiqueta_temperatura.config(text=f'Temperatura: {temperatura} / 255')

# Crear la ventana
ventana = tk.Tk()
ventana.title('Termómetro')
ventana.geometry('500x100')

# Crear el lienzo para la barra o termómetro
canvas = tk.Canvas(ventana, width=420, height=50, bg='white')
canvas.pack()

# Dibujar la barra inicial en el lienzo
barra = canvas.create_rectangle(10, 10, 10, 40, fill='blue')

# Crear la etiqueta "Temperatura"
etiqueta_texto = tk.Label(ventana, text='Temperatura')
etiqueta_texto.pack()

# Crear la etiqueta de temperatura
etiqueta_temperatura = tk.Label(ventana, text='0 / 255')
etiqueta_temperatura.pack()

# Valores de prueba
valores_prueba = [50, 100, 150, 200, 250, 220, 190, 180, 170, 200, 150, 120, 95]

# Mostrar los valores de prueba en forma gráfica
for valor in valores_prueba:
    actualizar_grafica(valor)
    ventana.update()
    plt.pause(1)  # Pausa de 1 segundo para simular la actualización en tiempo real

ventana.mainloop()
