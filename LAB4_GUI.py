#!/usr/bin/env python
# coding: utf-8

# # GUI

# In[52]:


import tkinter as tk
from tkinter import font
import subprocess

def modify_resolution(input_file, output_file, new_width, new_height):
    try:
        # Construct the ffmpeg command to change resolution
        cmd = [
            'ffmpeg',
            '-i', input_file,  # Input video file
            '-vf', f'scale={new_width}:{new_height}',  # Set new resolution
            output_file
        ]

        # Run the ffmpeg command
        subprocess.run(cmd, check=True)

        print(f"Resolution modification successful. Output video saved as {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def new_window():
    ventana = tk.Tk()
    ventana.title("Comparación de dos videos")
    ventana.configure(bg="#D2B4DE")
    
    def export_video_comparison(video1, video2, output_path, width, height):
        # Obtener la duración del video más largo
        duracion_video1 = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries',
                                                         'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',
                                                         video1]).decode('utf-8').strip())

        duracion_video2 = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries',
                                                         'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',
                                                         video2]).decode('utf-8').strip())

        duracion_total = max(duracion_video1, duracion_video2)

        # Ejecutar ffmpeg para comparar los videos
        subprocess.run([
            'ffmpeg',
            '-i', video1,
            '-i', video2,
            '-filter_complex', f'[0:v]scale={width}:{height}[v0];[1:v]scale={width}:{height}[v1];[v0][v1]hstack=inputs=2[v]',
            '-map', '[v]',
            '-t', str(duracion_total),
            output_path
        ])
        
        print(f"Comparation successful")
        
    # Crear un botones
    boton1_1 = tk.Button(ventana, text="Comparar 1280x720 con 854x480", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\1280x720_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\854x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_1280x720_VS_854x480_BBB_9sec.mp4", 1280, 720))
    boton1_2 = tk.Button(ventana, text="Comparar 1280x720 con 640x480", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\1280x720_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\640x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_1280x720_VS_640x480_BBB_9sec.mp4", 1280, 720))
    boton1_3 = tk.Button(ventana, text="Comparar 1280x720 con 360x240", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\1280x720_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\360x240_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_1280x720_VS_360x240_BBB_9sec.mp4", 1280, 720))

    boton2_1 = tk.Button(ventana, text="Comparar 854x480 con 1280x720", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\854x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\1280x720_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_854x480_VS_1280x720_BBB_9sec.mp4", 1280, 720))
    boton2_2 = tk.Button(ventana, text="Comparar 854x480 con 640x480", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\854x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\640x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_854x480_VS_640x480_BBB_9sec.mp4", 854, 480))
    boton2_3 = tk.Button(ventana, text="Comparar 854x480 con 360x240", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\854x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\360x240_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_854x480_VS_360x240_BBB_9sec.mp4", 854, 480))

    boton3_1 = tk.Button(ventana, text="Comparar 640x480 con 1280x720", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\640x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\1280x720_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_640x480_VS_1280x720_BBB_9sec.mp4", 1280, 720))
    boton3_2 = tk.Button(ventana, text="Comparar 640x480 con 854x480", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\640x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\854x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_640x480_VS_854x480_BBB_9sec.mp4", 854, 480))
    boton3_3 = tk.Button(ventana, text="Comparar 640x480 con 360x240", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\640x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\360x240_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_640x480_VS_360x240_BBB_9sec.mp4", 640, 480))

    boton4_1 = tk.Button(ventana, text="Comparar 360x240 con 1280x720", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\360x240_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\1280x720_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_360x240_VS_1280x720_BBB_9sec.mp4", 1280, 720))
    boton4_2 = tk.Button(ventana, text="Comparar 360x240 con 854x480", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\360x240_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\854x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_360x240_VS_854x480_BBB_9sec.mp4", 854, 480))
    boton4_3 = tk.Button(ventana, text="Comparar 360x240 con 640x480", command=lambda: export_video_comparison(r"C:\Users\MARIA\Downloads\360x240_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\640x480_BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\Comparacion_360x240_VS_640x480_BBB_9sec.mp4", 640, 480))

     # Crear una etiqueta para mostrar el mensaje
    etiqueta1_1 = tk.Label(ventana, text="¿Qué videos quieres comparar?", font=fuente_grande, bg="#D2B4DE")
                         
    # Colocar los botones y la etiqueta en la ventana
    etiqueta1_1.pack(pady=10)
    
    boton1_1.pack(pady=10)
    boton1_2.pack(pady=10)
    boton1_3.pack(pady=10)
    
    boton2_1.pack(pady=10)
    boton2_2.pack(pady=10)
    boton2_3.pack(pady=10)
    
    boton3_1.pack(pady=10)
    boton3_2.pack(pady=10)
    boton3_3.pack(pady=10)
    
    boton4_1.pack(pady=10)
    boton4_2.pack(pady=10)
    boton4_3.pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Modificar la resolución")

# Cambiar el color de fondo de la ventana
ventana.configure(bg="#D4E6F1")

# Declaración de fuentes
fuente_grande = tk.font.Font(size=16)
fuente_mediana = tk.font.Font(size=12)

# Crear los botones
boton1 = tk.Button(ventana, text="1280x720", font=fuente_mediana, command=lambda: modify_resolution(r"C:\Users\MARIA\Downloads\BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\1280x720_BBB_9sec.mp4",1280, 720))
boton2 = tk.Button(ventana, text="854x480", font=fuente_mediana, command=lambda: modify_resolution(r"C:\Users\MARIA\Downloads\BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\854x480_BBB_9sec.mp4",854, 480))
boton3 = tk.Button(ventana, text="640x480", font=fuente_mediana, command=lambda: modify_resolution(r"C:\Users\MARIA\Downloads\BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\640x480_BBB_9sec.mp4",640, 480))
boton4 = tk.Button(ventana, text="360x240", font=fuente_mediana, command=lambda: modify_resolution(r"C:\Users\MARIA\Downloads\BBB_9sec.mp4", r"C:\Users\MARIA\Downloads\360x240_BBB_9sec.mp4",360, 240))
boton5 = tk.Button(ventana, text="Claro!", font=fuente_mediana, command=lambda: new_window())


# Crear etiquetas para mostrar mensajes
etiqueta1 = tk.Label(ventana, text="¿A qué resolución quieres pasar el video?", font=fuente_grande, bg="#D4E6F1")
etiqueta2 = tk.Label(ventana, text="¿Quieres comparar dos videos?", font=fuente_grande, bg="#D4E6F1")

# Colocar los botones y las etiquetas en la ventana
etiqueta1.pack(pady=10)
boton1.pack(pady=10)
boton2.pack(pady=10)
boton3.pack(pady=10)
boton4.pack(pady=10)
etiqueta2.pack(pady=10)
boton5.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()


# In[ ]:





# In[ ]:




