Markdown


# 🦇 MKVerything: Spanglish Edition (v1.1)
> **"Las ISOs son sagradas, los AVIs son el enemigo."**

![Status](https://img.shields.io/badge/Status-Battle--Ready-green)
![OS](https://img.shields.io/badge/OS-Linux%20%7C%20Windows-blue)
![Flavor](https://img.shields.io/badge/Edition-Spanglish--Edition-orange)

```text
   _____   ____  __.____   ____                     __  .__    .__                
  /     \ |    |/ _|\   \ /   /___________ ___.__._/  |_|  |__ |__| ____    ____  
 /  \ /  \|      <   \   Y   // __ \_  __ <   |  |\   __\  |  \\|  |/    \  / ___\\ 
/    Y    \    |  \   \     /\  ___/|  | \/\___  | |  | |   Y  \\|  |   |  \/ /_/  >
\____|__  /____|__ \   \___/  \___  >__|   / ____| |__| |___|  /__|___|  /\___  / 
        \/        \/              \/       \/                \/        \//_____/  


MKVerything es un tanque de guerra diseñado para la purificación de bibliotecas multimedia. Automatiza el remux de imágenes ISO y la conversión de formatos "Legacy" (AVI, MP4, DIVX) a contenedores MKV modernos, empleando una lógica de supervivencia de 4 niveles para que ningún archivo se quede atrás.
🛠️ Lógica de Supervivencia (4-Level Core)
A diferencia de otros scripts que simplemente "fallan", MKVerything escala su agresividad técnica para salvar el archivo:
Nivel 1 (Direct Remux): Copia bit a bit. Si los flujos son compatibles, no se toca nada. Calidad 1:1.
Nivel 2 (Clean Stream): Si el remux falla, purga subtítulos conflictivos e ítems corruptos que suelen bloquear los motores de renderizado.
Nivel 3 (Audio Transcoding): Si el contenedor original tiene audios incompatibles con reproductores modernos, transcodifica el audio a AAC manteniendo el vídeo intacto.
Nivel 4 (Total Resurrection): Para archivos con "timestamps" destruidos o codecs de la era de los dinosaurios, realiza un re-encodificado total con libx264 para asegurar la supervivencia.
🐶 El Sabueso (Metadata Engine)
Olvídate de renombrar archivos a mano. El motor interno de MKVerything:
Limpia el nombre del archivo eliminando etiquetas de calidad y basura de trackers.
Extrae el año de producción automáticamente.
Consulta la API de TMDB (The Movie Database) cruzando nombre y año para evitar falsos positivos.
Organiza el resultado final en carpetas por título y año.
📂 Instalación
Opción A: Binario (Ready to Launch)
Descarga la versión compilada para tu sistema desde la sección de Releases.
Coloca los binarios de ffmpeg y makemkvcon en la carpeta /bin.
Crea tu archivo .env con tu clave de API (ver example.env).
Ejecuta MKVerything.sh (Linux) o MKVerything.exe (Windows).
Opción B: Código Fuente (Modo Arquitecto)

Bash


git clone [https://github.com/tu-usuario/MKVerything.git](https://github.com/tu-usuario/MKVerything.git)
pip install -r requirements.txt
python launcher.py


⚖️ Filosofía del Proyecto
Las ISOs no se tocan: Una imagen de disco es un bien intrínseco. El script extrae el contenido pero jamás borra el "master".
Spanglish Edition: Interfaz en español para el disfrute de la comunidad hispana. Los gringos que espabilen.
Developed with grit by the Rubber Duck & the Architect.



---

