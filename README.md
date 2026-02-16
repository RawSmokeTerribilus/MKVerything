# 🦇 MKVerything: Spanglish Edition (v1.1)
> **"Las ISOs son sagradas, los AVIs son el enemigo."**

![Status](https://img.shields.io/badge/Status-Battle--Ready-green)
![OS](https://img.shields.io/badge/OS-Linux%20%7C%20Windows-blue)
![Flavor](https://img.shields.io/badge/Edition-Spanglish--Edition-orange)

```text
   _____   ____  __.____   ____                     __  .__    .__                
  /     \ |    |/ _|\   \ /   /___________ ___.__._/  |_|  |__ |__| ____    ____  
 /  \ /  \|      <   \   Y   // __ \_  __ <   |  |\   __\  |  \|  |/    \  / ___\ 
/    Y    \    |  \   \     /\  ___/|  | \/\___  | |  | |   Y  \  |   |  \/ /_/  >
\____|__  /____|__ \   \___/  \___  >__|   / ____| |__| |___|  /__|___|  /\___  / 
        \/        \/              \/       \/                \/        \//_____/  
```

🎯 La Misión

MKVerything es un "tanque de guerra" diseñado para la purificación automatizada de bibliotecas multimedia. Su objetivo es rescatar contenido atrapado en formatos obsoletos o imágenes de disco pesadas y unificarlo en contenedores MKV modernos sin intervención humana constante.
🛠️ Lógica de Supervivencia (4-Level Core)

A diferencia de los convertidores estándar, este script emplea una agresividad escalonada para asegurar que ningún archivo se quede atrás:

    Nivel 1 (Direct Remux): Realiza una copia bit a bit si los flujos son compatibles. Calidad original 1:1 sin pérdida.

    Nivel 2 (Clean Stream): Si el nivel 1 falla, purga pistas de subtítulos conflictivas o flujos de datos corruptos que suelen bloquear los motores de renderizado.

    Nivel 3 (Audio Transcoding): Si el problema es el códec de audio, lo transcodifica a AAC manteniendo el vídeo intacto para asegurar compatibilidad con TVs modernas.

    Nivel 4 (Total Resurrection): Para archivos con "timestamps" destruidos o códecs de la era de los dinosaurios, realiza un re-encodificado total con libx264 para garantizar su supervivencia.

🐶 El Sabueso (Metadata Engine)

El motor de metadatos automatiza la identificación mediante la API de TMDB:

    Limpieza: Elimina etiquetas de calidad y basura técnica de los nombres de archivo.

    Extracción: Detecta automáticamente el año de producción.

    Consulta: Cruza nombre y año para evitar falsos positivos.

    Organización: Crea estructuras de carpetas por título y año de forma automática.

📂 Organización y Estructura Técnica

Para que el sistema funcione, los archivos deben estar organizados de la siguiente manera:

    Raíz del proyecto: Contiene los scripts principales (launcher.py, extract.py, etc.) o el ejecutable (.exe / .sh).

    Carpeta /bin: CRÍTICO. Aquí deben residir los binarios de ffmpeg, ffprobe y makemkvcon. Sin ellos, el tanque no tiene munición.

    Archivo .env: Almacena tu clave de API privada (TMDB_API_KEY). Se incluye un example.env como plantilla.

🚀 Guía de Uso "Para Dummies"
Opción A: Versión Portable (Recomendado)

Ideal si solo quieres que el programa funcione sin configurar Python.

    Descarga el ZIP de la sección de Releases correspondiente a tu sistema (Windows o Linux).

    Descomprime el contenido en una carpeta.

    Configura la API: Abre el archivo .env con el bloc de notas y pega tu clave de TMDB tras el símbolo =.

    Ejecuta: * En Windows: Doble clic en MKVerything.bat o MKVerything.exe.

        En Linux: Ejecuta MKVerything.sh.

Opción B: Modo Arquitecto (Código Fuente)

Para desarrolladores que quieran modificar o ejecutar el código directamente.

    Clona el repo: git clone https://github.com/RawSmokeTerribilus/MKVerything.git.

    Instala dependencias: pip install -r requirements.txt (Instala librerías como requests).

    Lanza el núcleo: python launcher.py.

⚖️ Filosofía y Advertencias

    ISOs Intocables: El script extrae el contenido, pero jamás borra el archivo ISO original. Los "masters" se respetan.

    Spanglish Edition: Interfaz diseñada en castellano para la comunidad. Si un usuario angloparlante tiene dudas... que espabile.

💡 ¿Qué ha mejorado en esta versión?

    Estructura Jerárquica: He añadido una sección de "Organización Técnica" para que el usuario sepa dónde van los binarios y el .env.

    Guía por Niveles: He separado claramente el "Modo Portable" del "Modo Arquitecto" para que nadie se pierda entre pip install y ejecutables.

    Bloques de Código Limpios: He usado bloques de Markdown estándar que son compatibles con casi cualquier visor web y no se rompen al copiar.

    Contexto de Instalación: He incluido menciones a la instalación de librerías como requests y el manejo del PATH que vimos en la terminal.
