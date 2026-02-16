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
        
    .___.__                          ___.        ___.         .__          __                
  __| _/|__| ______ ____  ___   _____\_ |__   ___\_ |__  __ __|  | _____ _/  |_  ___________ 
 / __ | |  |/  ___// ___\/ _ \ /     \| __ \ / _ \| __ \|  |  \  | \__  \\   __\/  _ \_  __ \
/ /_/ | |  |\___ \\  \__( <_> )  Y Y  \ \_\ ( <_> ) \_\ \  |  /  |__/ __ \|  | (  <_> )  | \/
\____ | |__/____  >\___  >___/|__|_|  /___  /\___/|___  /____/|____(____  /__|  \____/|__|   
     \/         \/     \/           \/    \/          \/                \/                   
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

📂 Anatomía del Proyecto (Modo Arquitecto)

Si vas a modificar el código o ejecutarlo desde la fuente, este es el propósito de cada módulo:

    launcher.py: El punto de entrada. Gestiona la interfaz TUI, la secuencia de arranque y la inyección de variables de entorno.

    extract.py: El corazón del tanque. Contiene la lógica de los 4 niveles de supervivencia y el flujo principal de trabajo.

    analyzer.py: El especialista en discos. Escanea las ISOs y detecta los títulos mediante makemkvcon.

    metadata_provider.py: El "Sabueso". Gestiona las peticiones a la API de TMDB y el filtrado de nombres.

    persistence.py: El libro de bitácora. Evita procesar archivos duplicados y guarda el estado de la misión en /states.

    mediainfo.py: El perito técnico. Analiza los flujos de audio y vídeo usando ffprobe.
    
🔧 Gestión de Binarios (Munición)

El sistema necesita "motores" externos para procesar el vídeo. Tienes dos formas de configurarlos:

    Uso de carpeta /bin (Recomendado para Portables): Descarga los ejecutables y colócalos dentro de la carpeta /bin del proyecto. El script los detectará automáticamente.

    Instalación en Sistema: Si prefieres no usar la carpeta /bin, asegúrate de que los comandos ffmpeg y makemkvcon respondan en tu terminal (añadidos al PATH).

¿Dónde conseguirlos?

    FFmpeg/FFprobe: Descargar aquí. Necesitas las Static Builds (un solo .exe o binario).

    MakeMKV (makemkvcon): [https://ffmpeg.org/download.html]. En Linux, instala el paquete makemkv-bin. En Windows, busca el makemkvcon.exe en la carpeta de instalación.

🚀 Guía de Uso "Para Dummies"

Si te has bajado la Versión Release (Portable), sigue estos pasos:

    Prepara los binarios: Revisa los archivos de ffmpeg y makemkvcon en la carpeta /bin. Sin esto, el tanque no arranca.

    Lanzamiento: * Windows: Ejecuta MKVerything.bat.

        Linux: Ejecuta MKVerything.sh.

    Configuración inicial: La primera vez que inicies, el sistema te pedirá los datos mínimos para empezar la purificación.

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

    Contexto de Instalación: He incluido menciones a la instalación de librerías como requests.
