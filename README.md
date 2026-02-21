# 🦇 MKVerything: V2.beta "The Purge"
> **"Las ISOs son sagradas, los AVIs son el enemigo."**

![Status](https://img.shields.io/badge/Status-Battle--Ready-green)
![OS](https://img.shields.io/badge/OS-Linux%20%7C%20Windows-blue)
![Flavor](https://img.shields.io/badge/Edition-Spanglish--V2--beta-orange)
![Python](https://img.shields.io/badge/Python-3.6+-blue)

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

---

## 📋 Table of Contents
1. [🎯 La Misión](#-la-misión)
2. [🚀 Quick Start (Release)](#-quick-start-release)
3. [💡 Casos de Uso](#-casos-de-uso)
4. [🎮 5 Modos de Operación](#-5-modos-de-operación)
5. [🔥 God Mode Explicado](#-god-mode-explicado)
6. [🛠️ Lógica de Supervivencia](#️-lógica-de-supervivencia)
7. [🐶 Sabueso TMDB](#-sabueso-tmdb)
8. [⚡ Mejoras V2 vs V1.1](#-mejoras-v2-vs-v11)
9. [📊 Performance & Rendimiento](#-performance--rendimiento)
10. [🐛 Troubleshooting](#-troubleshooting)
11. [⚖️ Filosofía y Advertencias](#️-filosofía-y-advertencias)
12. [⚙️ Configuración (DEV)](#️-configuración-dev)
13. [📦 Instalación para Desarrolladores](#-instalación-para-desarrolladores)
14. [📂 Arquitectura Técnica](#-arquitectura-técnica)

---

## 🎯 La Misión

Un **"tanque de guerra"** diseñado para la purificación automatizada de bibliotecas multimedia. Su objetivo es rescatar contenido atrapado en formatos obsoletos o imágenes de disco pesadas y unificarlo en contenedores MKV modernos **sin intervención humana constante**.

**MKVerything no es solo un conversor; es el eslabón perdido en tu cadena de automatización multimedia.**

---

## 🚀 Quick Start (Release)

### **Instalación Portable (Recomendado para Todos)**

Descarga y Extrae el archivo .zip

Verifica los Órganos: Asegúrate de que la carpeta /bin contiene los ejecutables necesarios (ffmpeg, makemkvcon, mkvmerge, etc.)

🐧 En Linux:
```bash
chmod +x MKVerything.sh
./MKVerything.sh
```

🪟 En Windows:
Ejecuta el archivo MKVerything.bat.

    Nota: Si Windows Defender bloquea la ejecución, haz clic en "Más información" y luego en "Ejecutar de todas formas". Es el peaje por usar herramientas de rescate sin firmar.

Eso es todo. El menú TUI te guiará desde ahí.


**Para Desarrolladores que quieran usar el código fuente:** Ver sección [📦 Instalación para Desarrolladores](#-instalación-para-desarrolladores) al final.

---

## 🎮 5 Modos de Operación

Cada modo está diseñado para un escenario específico:

### **[1] 📦 Extraer ISOs (MakeMKV)**
**Uso:** Convierte imágenes de disco a archivos MKV individuales.

```bash
# Interfaz TUI te pedirá:
# → Carpeta o ISO origen
# → Carpeta destino (puede ser la misma)

# El proceso:
# 1. Lee la ISO con makemkvcon
# 2. Extrae todos los títulos a carpeta temporal
# 3. Selecciona el archivo principal (el más grande)
# 4. Verifica integridad (pistas de audio/subs)
# 5. Mueve a destino final
# 6. Limpia temporales
```

**Salida esperada:**
```
/destino/
└── nombre_iso.mkv  (± 80% del tamaño del original al ser un remux)
```

---

### **[2] 🚑 Rescatar MKVs Rotos (Modo Estricto)**
**Uso:** Solo procesa archivos MKV que estén **dañados**.

```bash
# Proporciona:
# → Una carpeta (busca MKVs recursivos)
# → Un archivo individual .mkv
# → Un archivo .txt con lista de rutas

# El proceso:
# 1. Ejecuta check_health() en cada MKV
# 2. Si FALLA: ejecuta transcoding (rescate)
# 3. Si PASA: lo deja intacto (evita re-procesamiento innecesario)
# 4. Genera log de estadísticas
```

**Resultado:** Original reemplazado por versión reparada.

---

### **[3] ⚖️ AUDITORÍA DE CAMPO (Recursivo + Informe)**
**Uso:** Escanea una biblioteca completa y reporta archivos rotos.

```bash
# Proporciona:
# → Carpeta o punto de montaje a auditar

# El proceso:
# 1. Encuentra todos los videos (.mkv, .avi, .mp4, .mov, .wmv)
# 2. Ejecuta health check en cada uno
# 3. Clasifica en: ✅ Sanos | ❌ Rotos | 🏷️ Spam
# 4. Genera informe: videos-rotos-DD-MM-YY.txt
# 5. Crea estadísticas finales

# Ejemplo de salida en logs/videos-rotos-20-02-26.txt:
# /mnt/media/series/archivo_corrupto.mkv
# /mnt/media/peliculas/otro_roto.avi
# ... (lista completa)
```

---

### **[4] 🎞️ Convertir Legacy (AVI/MP4 → MKV)**
**Uso:** Migra archivos antiguos a estándar moderno.

```bash
# Proporciona:
# → Carpeta a escanear (busca recursivo)

# Formatos soportados:
# .avi, .mp4, .m4v, .divx, .wmv, .mov → .mkv

# El proceso POR ARCHIVO:
# 1. Lee metadatos y verifica salud
# 2. Selecciona level de rescate (1-4)
# 3. Ejecuta conversión
# 4. Verifica MKV resultante
# 5. SI OK: Borra original, mantiene MKV
#    SI FALLA: Preserva original, reporta error
```

**Estadísticas generadas:**
```
✅ Procesados: 157
💾 Bytes recuperados: 45.2 GB
❌ Fallos: 2
⏭️  Saltados: 3
```

---

### **[5] ⚡ GOD MODE (Full Pipeline Desatendido)**
**Uso:** Automatización total sin intervención. **ZONA PELIGROSA.**

```bash
# El tanque ejecuta TODA la cadena:
# 1. Detecta y extrae ISOs
# 2. Convierte legacy (AVI/MP4 → MKV)
# 3. Rescata MKVs rotos existentes
# 4. Audita salud de toda la biblioteca
# 5. Limpia archivos temporales
# 6. Genera reporte final: GOD_MODE_log.txt

# Puede ejecutarse desatendido SEMANAS sin tocar el terminal
```

---

## 🔥 God Mode Explicado

### **¿Qué hace exactamente?**

God Mode es una **tubería orquestada** que ejecuta 4 subprocesos en secuencia:

```
┌─────────────────────────────────────────────────┐
│                  GOD MODE PIPELINE              │
├─────────────────────────────────────────────────┤
│ 1. ISO EXTRACTION                               │
│    └─ Detecta .iso en carpeta origen            │
│    └─ Ejecuta modo [1] para cada una            │
│    └─ Reporta: X ISOs procesadas, Y MB          │
├─────────────────────────────────────────────────┤
│ 2. LEGACY CONVERSION                            │
│    └─ Detecta .avi, .mp4, .wmv, etc             │
│    └─ Ejecuta modo [4] para cada una            │
│    └─ Reporta: X archivos convertidos, Y MB     │
├─────────────────────────────────────────────────┤
│ 3. MKV RESCUE (Broken Files)                    │
│    └─ Detecta .mkv rotos                        │
│    └─ Ejecuta modo [2] para cada uno            │
│    └─ Reporta: X rescatados, Y fallos           │
├─────────────────────────────────────────────────┤
│ 4. HEALTH AUDIT & CLEANUP                       │
│    └─ Audita toda la biblioteca (modo [3])      │
│    └─ Limpia archivos temporales                │
│    └─ Genera estadísticas finales               │
└─────────────────────────────────────────────────┘
```

### **Características de Resistencia:**

- **Atomic Execution:** Si falla en paso 2, registra el error en `GOD_MODE_log.txt` y continúa con paso 3
- **Cleanup Automático:** Si un archivo temporal queda tirado de 30GB, lo limpia antes de continuar
- **Resume Capabilty:** El estado se guarda en `/states/` para evitar reprocessar
- **Unattended Mode:** Puede correr 24/7 sin intervención. Solo necesita suficiente espacio en disco

### **Parámetros de Entrada:**

```bash
# El TUI te pedirá:
# 1. Carpeta origen (ISOs + videos legacy)
# 2. Carpeta destino para extracciones
# 3. Confirmar: ¿Borrar archivos originales tras éxito? (S/N)
```

### **Salida Esperada:**

```
logs/GOD_MODE_log.txt
─────────────────────
[2026-02-20 14:32:10] ⚡ GOD MODE INICIADO
[2026-02-20 14:32:10] 📦 Fase 1: Extrayendo 5 ISOs...
[2026-02-20 14:45:30]    ✅ ISO 01 OK (8.2 GB)
[2026-02-20 15:02:15] 🎞️  Fase 2: Convirtiendo 157 legacy...
[2026-02-20 18:30:45]    ✅ Procesados 157, Fallos: 2, Recuperados: 45.2 GB
[2026-02-20 18:31:10] 🚑 Fase 3: Rescatando 23 MKVs rotos...
[2026-02-20 19:15:22]    ✅ Rescatados: 21, Fallos: 2
[2026-02-20 19:15:45] ⚖️  Fase 4: Auditoría final
[2026-02-20 19:45:20]    ✅ Sanos: 8432, Rotos: 3, Spam: 12
[2026-02-20 19:45:30] 🎯 GOD MODE COMPLETADO - 62.4 GB recuperados
```

---

## 🛠️ Lógica de Supervivencia (4-Level Core)

A diferencia de convertidores estándar, MKVerything emplea una **agresividad escalonada** para asegurar que ningún archivo se quede atrás:

```
┌──────────────────────────────────────────────┐
│        4-LEVEL RESCUE ESCALATION             │
├──────────────────────────────────────────────┤
│ Archivo de Entrada → ¿Es válido FFmpeg?      │
│                                              │
│ ❌ No → NIVEL 1                              │
│ └─ Direct Remux: Copia bit a bit             │
│    └─ Intenta mover flujos SIN re-codificar  │
│    └─ Si funciona: ✅ 1:1 lossless           │
│    └─ Si falla: Continúa NIVEL 2             │
│                                              │
│ ❌ → NIVEL 2                                 │
│ └─ Clean Stream: Purga fuentes conflictivas  │
│    └─ Elimina pistas de subs dañadas         │
│    └─ Elimina flujos corruptos               │
│    └─ Re-encapsula en MKV limpio             │
│    └─ Si funciona: ✅ Guardado               │
│    └─ Si falla: Continúa NIVEL 3             │
│                                              │
│ ❌ → NIVEL 3                                 │
│ └─ Audio Transcoding: Recodifica audio       │
│    └─ Mantiene vídeo intacto (copia)         │
│    └─ Re-codifica audio a AAC (estándar TV)  │
│    └─ Si funciona: ✅ Guardado               │
│    └─ Si falla: Continúa NIVEL 4             │
│                                              │
│ ❌ → NIVEL 4                                 │
│ └─ Total Resurrection: Re-encodifica TODO    │
│    └─ Vídeo: libx264 (H.264, calidad media)  │
│    └─ Audio: AAC                             │
│    └─ Subs: Copia si es posible              │
│    └─ ✅ Última oportunidad - casi siempre OK│
└──────────────────────────────────────────────┘
```

### **¿Cuándo se usa cada nivel?**

| Escenario | Nivel | Resultado |
|-----------|-------|-----------|
| Video H.264 con audio limpio | 1 | 1:1 Bit-identical (< 1 min) |
| Video OK, audio corrupto | 2-3 | Audio limpio (20-60 min) |
| Timestamps destruidos | 4 | Re-encod completo (4-8 horas) |
| DivX/MPEG4 legacy | 4 | Conversión moderna (4-8 horas) |

---

## 🐶 Sabueso TMDB (Metadata Engine)

El motor de metadatos automatiza la identificación de archivos:

```
Archivo Original: AVATAR.2009.1080p.BluRay.x264.ac3-evo.mkv
                    ↓
           [LIMPIEZA DE NOMBRES]
                    ↓
         Nombre limpio: AVATAR
         Año extraído: 2009
                    ↓
        [CONSULTA TMDB API]
                    ↓
    ✅ Match encontrado:
      - Título real: Avatar
      - Año: 2009
      - Tipo: Movie
      - ID TMDB: 19995
                    ↓
      [RENOMBRAMIENTO FINAL]
                    ↓
     Resultado: Avatar (2009).mkv
```

### **Características:**

1. **Limpieza:** Elimina etiquetas técnicas (rarbg, yify, BluRay, x264, etc.)
2. **Extracción:** Detecta año de producción automáticamente
3. **Consulta Inteligente:** Cruza nombre + año para evitar falsos positivos (ej: "Vibes" vs "Avatar")
4. **Organización:** Crea estructura de carpetas: `/Titulo (Año)/archivo.mkv`

### **Palabras Clave Detectadas (Spam Filter):**
```
rarbg, yify, ettv, www., .com, torrent, axxo, brrip, web-dl, 
bluray, rip, x264, x265, ac3-evo, evo, bypixel, spam, wolfmax
```

---

## 📂 Arquitectura Técnica

### **Estructura Modular:**

```python
launcher.py                    # Punto de entrada TUI
│
├── modules/
│   ├── extract.py            # IsoExtractor - Extracción de ISOs
│   │   └─ Usa: makemkvcon
│   │   └─ Salida: archivo.mkv
│   │
│   ├── universal_rescuer.py   # UniversalRescuer - Conversión/Rescate
│   │   └─ Usa: ffmpeg
│   │   └─ Niveles 1-4 de re-codificación
│   │
│   ├── verifier.py           # Verifier - Health checks
│   │   └─ Usa: mkvmerge, ffprobe, ffmpeg
│   │   └─ Detecta: corrupción, timestamps rotos, integridad
│   │
│   ├── analyzer.py           # DiscScanner - Análisis de ISOs
│   │   └─ Usa: makemkvcon
│   │   └─ Extrae: lista de títulos, duraciones
│   │
│   ├── metadata_provider.py   # MetadataProvider - TMDB queries
│   │   └─ Usa: API REST de TMDB
│   │   └─ Función: limpieza de nombres + identificación
│   │
│   ├── persistence.py        # StateManager - Estado persistente
│   │   └─ Almacena: qué archivos ya se procesaron
│   │   └─ Previene: reprocessamiento innecesario
│   │
│   └─ mediainfo.py          # (Future expansion)
│
└── Configuration
    ├── .env                 # API keys (NO incluido en Git)
    ├── example.env          # Plantilla de configuración
    └── requirements.txt     # Dependencias Python
```

### **Flujo de Datos V2 (Monitorización en Tiempo Real):**

```
Archivo Input → FFmpeg stderr stream
                  ↓
        [Palabra clave detectada?]
         corrupt | invalid | mismatch
                  ↓
           ✅ Error encontrado
                  ↓
      Deep Scan + Full Health Check
                  ↓
      Decidir nivel de rescate (1-4)
                  ↓
          Salida: archivo.mkv
```

**Diferencia V1.1 → V2.beta:**
- V1.1: "¿Salió OK FFmpeg?" (exit code 0 = todo bien)
- V2: "¿Qué dice FFmpeg mientras trabaja?" (stderr parsing en tiempo real)

---

---

## 💡 Casos de Uso

### **Caso 1: Pre-Procesador para Tdarr (The Space Saver)**

**Problema:** Tdarr ahorra 50-60% espacio pero es "delicado". Falla con archivos legacy o indexados corruptamente.

**Solución:**
```bash
# Step 1: Ejecuta MKVerything modo [4]
# → Convierte toda la biblioteca a MKV limpio

# Step 2: Ejecuta MKVerything modo [3]
# → Audita salud de toda la biblioteca

# Step 3: Apunta Tdarr a la carpeta limpia
# → Tdarr comprime a H.265 sin pestañear
```

**Resultado:** 50% de ahorro original + 0 errores.

---

### **Caso 2: Preparación de Subidas (The Uploader's Wingman)**

**Problema:** EMUploadrr/Uploadrr no soportan .avi. Trackers antiguos con contenido legacy.

**Solución:**
```bash
# Step 1: Usa MKVerything modo [4]
# → Convierte .avi antiguos a .mkv

# Step 2: Ejecuta Uploadrr en dry-run
# → Genera NFOs, capturas, mediainfo automáticamente

# Resultado: Contenido profesional listo para subir
```

---

### **Caso 3: Estandarización de Contenedores (The MKV Supremacy)**

**Problema:** AVI no soporta metadatos modernos, múltiples audios con etiquetas, subs PGS.

**Solución:**
```bash
# Migra TODO a MKV con MKVerything modo [4]
# Ahora puedes:
# - Inyectar carátulas (covers)
# - Agregar metadatos avanzados
# - Insertar capítulos
# - Embebed subtítulos PGS/ASS
```

---

### **Caso 4: Arqueología Digital (The Legacy Rescuer)**

**Problema:** Carpetas olvidadas con .divx, .mpg, .m4v que ya no reproducen. Smart TV rechaza archivos corruptos.

**Solución:**
```bash
# God Mode (modo [5])
# 1. Detecta todos los viejos formatos
# 2. Identifica con TMDB (pone nombres reales)
# 3. Convierte a MKV moderno
# 4. Resultado: Compatibilidad 100% con cualquier dispositivo siglo XXI
```

---

## ⚡ Mejoras V2 vs V1.1

| Aspecto | V1.1 (GitHub) | V2.beta "The Purge" |
|---------|---|---|
| **Monitorización FFmpeg** | Ciega (exit code) | ✅ stderr parsing en tiempo real |
| **Detección de Corrupción** | Solo al final | ✅ Durante codificación (palabras clave) |
| **Verificación Híbrida** | Básica (exist + duration) | ✅ Fast Path + Deep Scan |
| **Orquestación** | Procesos estancos | ✅ Pipeline automática (God Mode) |
| **Robustez** | Puede dejar temporales | ✅ Limpieza atómica + resume capability |
| **UI/UX** | Terminal estándar | ✅ Typewriter effects + troll mode |
| **Troll Mode** | No existe | ✅ 210+ líneas de frases aleatorias |
| **Battle Report** | Manual | ✅ Auto-generado con estadísticas |
| **Estado Persistente** | Archivos .txt | ✅ JSON con validación |
| **API Integration** | No | ✅ TMDB para auto-identificación |

---

## 📊 Performance & Rendimiento

### **Benchmarks Típicos (Máquina media: i7 + NVMe):**

| Operación | Tiempo | Notas |
|-----------|--------|-------|
| Extracción ISO (8GB) | 15-25 min | Depende velocidad disco |
| Nivel 1 (Direct Remux) | < 1 min | Copia bit a bit |
| Nivel 2 (Clean Stream) | 20-60 min | Re-encapsula |
| Nivel 3 (Audio Transcode) | 30-90 min | Vídeo intacto |
| Nivel 4 (Full Re-encode) | 4-8 horas | Depende resolución |
| Auditoría (1000 archivos) | 30-60 min | Escaneo de integridad |
| God Mode (100 ISOs + 1000 legacy) | 2-3 semanas | Desatendido |

### **Requisitos de Espacio (Por Archivo - No Acumulativo)**

A diferencia de otros convertidores, MKVerything **procesa archivo por archivo**, así que NO necesitas 2x el tamaño total de la biblioteca:

```
Espacio recomendado = 2x el ARCHIVO MÁS GRANDE que vayas a procesar + margen

Ejemplo: Si tu archivo más grande es 15GB
└─ Necesitas: ~35GB libre (15GB original + 15GB temporal + 5GB margen)

Legacy → MKV: El archivo original se BORRA tras éxito,
              así que recuperas espacio inmediatamente.
```

**Para Extracción de ISOs (especial):**
- Si usas **mismo disco:** Necesitas ~2x el tamaño de la ISO
- Si usas **disco diferente (RECOMENDADO):** Mejor velocidad (SSD/NVMe ideal)
  ```bash
  # Ejemplo: ISO en /datos/isos/ (HDD lento)
  #         Extrae a /nvme/temp/ (SSD rápido)
  # Resultado: 3-5x más rápido que extraer en mismo disco
  ```

### **Consumo de CPU:**

```
Direct Remux (Nivel 1):      5% CPU (lectura/escritura)
Audio Transcode (Nivel 3):   40-60% CPU
Full Re-encode (Nivel 4):    80-95% CPU (recomendado a 23 CRF)
God Mode (pipeline):         Variable (cambia entre fases)
```

### **Optimizaciones Aplicadas:**

1. **Fast Path:** Si FFmpeg no reporta errores, solo verifica metadatos (10x más rápido)
2. **Atomic Operations:** No crea garbage si falla a mitad del proceso
3. **Resume Capability:** `states/` permite reanudar sin reprocesar
4. **Parallel Scanning:** Auditoría usa lectura secuencial optimizada

---

## 🐛 Troubleshooting

### **Problema: "makemkvcon not found"**

```bash
# Solución 1: Verifica que esté en /bin
ls -la bin/makemkvcon

# Solución 2: Instala manualmente
# Linux: sudo apt-get install makemkv-bin
# Windows: Descarga desde https://www.makemkv.com/download/
# macOS: brew install makemkv

# Solución 3: Añade al PATH
export PATH="/ruta/a/makemkvcon:$PATH"
```

---

### **Problema: "Error de TMDB API"**

```bash
# Verifica credenciales en .env
cat .env

# Si falta API key:
TMDB_API_KEY=""  # ← Esto está vacío

# Soluciona:
# 1. Regístrate en https://www.themoviedb.org/settings/api
# 2. Copia tu API Key v3
# 3. Actualiza .env
TMDB_API_KEY="tu_clave_real_aqui"

# 4. Relanza
python launcher.py
```

---

### **Problema: "FFmpeg falla con audio corrupto"**

```bash
# MKVerything automáticamente escala a Nivel 3
# Pero si quieres verificar manualmente:

ffprobe -v error -select_streams a -show_entries stream=codec -of default=noprint_wrappers=1 archivo.mkv
# Si sale algo raro → Nivel 3+ es necesario
```

---

### **Problema: "Stuck en conversión (parece colgado)"**

```bash
# Comprueba uso de disco
df -h

# Si está 100% lleno:
# → God Mode se pausará para no perder datos
# → Libera espacio y continúa (resume automático)

# Mira logs en tiempo real:
tail -f logs/rescue_process.log
```

---

### **Problema: "Original NO fue borrado pero debería"**

```bash
# Verifica que .mkv pasó check_health:
# Abre archivo log:
cat logs/rescue_process.log | grep "archivo_sospechoso.mkv"

# Si dice ❌ FAILED: El original se preserva (seguridad)
# Si dice ✅ OK pero NO se borró:
# → Permisos incorrectos. Soluciona:

chmod 755 directorio/
# Y reintenta
```

---

## ⚖️ Filosofía y Advertencias

### **ISOs Intocables**
- El script **jamás borra el archivo ISO original**.
- Solo extrae el contenido.
- Los "masters" se respetan siempre.
- Destino de extracción puede ser diferente del origen.

```
/almacenamiento/originales/        (ISOs seguros)
/plex/peliculas/                   (Archivos MKV extraídos)
```

---

### **Exterminio de Codecs Obsoletos**
- Los archivos **legacy (.avi, .mp4, .wmv) SÍ se borran** tras éxito.
- Solo si pasaron `check_health()` correctamente.
- Si conversión falla: original se preserva (máxima seguridad).

```bash
# Antes:
archivo_viejo.avi  (2.4 GB) ← SERÁ ELIMINADO

# Después (si OK):
archivo_viejo.mkv  (1.8 GB) ← Nuevo archivo
# Original .avi → Borrado → Recuperados: 0.6 GB
```

---

### **Robustez y Seguridad**
- **100% tasa de éxito en pruebas reales** (15.000+ archivos).
- Únicos fallos: archivos tan corruptos que ni VLC los lee.
- Si VLC puede abrirlo (**aunque timeline esté roto**), MKVerything lo rescatará.

---

### **Pruebas Recomendadas**
⚠️ **Antes de lanzar contra toda la biblioteca:**

```bash
# Crea carpeta de prueba
mkdir test_folder
cp 5-10_archivos_variados test_folder/

# Ejecuta modo [4] en test_folder
python launcher.py
# Selecciona: [4] Convertir Legacy
# Proporciona: test_folder

# Verifica resultados:
ls -lh test_folder/
# ¿Los MKVs se crearon? ¿Originales están intactos/borrados correctamente?

# Solo después: Ejecuta contra biblioteca completa
```

---

### **Spanglish Edition**
Interfaz diseñada **por y para la comunidad hispana**.
- Menús en español
- Mensajes de error claros
- Documentación en español
- Si usuario angloparlante tiene dudas... que espabile 😏

---

## ⚙️ Configuración (DEV)

### **1. Configurar API Keys (TMDB/TVDB)**

La primera vez que lances `launcher.py`, el sistema te pedirá los API keys. También puedes configurar manualmente:

```bash
# Archivo .env (SEGURO - Se ignora en Git)
cp example.env .env
nano .env  # O abre con tu editor preferido
```

**Contenido de .env:**
```dotenv
# TMDB (The Movie Database) - Para Cine y Series generales
TMDB_API_KEY="tu_clave_aqui"

# TVDB (The TV Database) - Para Anime y orden de episodios
TVDB_API_KEY="tu_clave_aqui"
```

**¿Cómo obtener las claves?**

1. **TMDB API Key:**
   - Regístrate en [tmdb.org](https://www.themoviedb.org/settings/api)
   - Solicita Developer Access
   - Copia tu API Key v3 (no token)

2. **TVDB API Key:**
   - Regístrate en [thetvdb.com](https://www.thetvdb.com/api-information)
   - Genera una API Key de desarrollo

### **2. Estructura de Directorios**

El sistema crea automáticamente:
```
MKVerything_PROJECT-V2/
├── logs/
│   ├── extraction_process.log      # Logs de extracción de ISOs
│   ├── rescue_process.log          # Logs de rescate
│   ├── security_audit.log          # Auditoría de salud
│   └── videos-rotos-DD-MM-YY.txt   # Informe de archivos corruptos
├── states/
│   └── proyecto_name.json          # Estado persistente (qué ya se procesó)
└── TEMP_WORK_AREA/
    └── [archivos temporales durante conversión]
```

---

## 📦 Instalación para Desarrolladores

### **Dependencias Python**
```bash
pip install -r requirements.txt
# Solo requiere: requests>=2.28.0
```

### **Binarios Externos (Munición del Tanque)**

MKVerything necesita 5 herramientas externas. Tienes dos opciones:

#### **Opción 1: Carpeta /bin (Portable - Recomendado)**
Descarga los ejecutables compilados y colócalos en `/bin`:
```
bin/
├── ffmpeg          (o ffmpeg.exe en Windows)
├── ffprobe         (o ffprobe.exe)
├── makemkvcon      (o makemkvcon.exe)
├── mediainfo       (o mediainfo.exe)
└── mkvmerge        (o mkvmerge.exe)
```

**Dónde conseguirlos:**

| Herramienta | Link | Notas |
|-------------|------|-------|
| **FFmpeg** | [ffmpeg.org/download](https://ffmpeg.org/download.html) | Descarga Static Builds (un solo .exe o binario) |
| **MakeMKV** | [makemkv.com/download](https://www.makemkv.com/download/) | Windows: busca `makemkvcon.exe` en carpeta instalación. Linux: `sudo apt-get install makemkv-bin` |
| **MKVToolNix** | [mkvtoolnix.download](https://mkvtoolnix.download/) | Incluye `mkvmerge` y `mediainfo`. Linux: `sudo apt-get install mkvtoolnix mediainfo` |
| **MediaInfo** | [mediainfo.sourceforge.io](https://mediainfo.sourceforge.io/en) | Herramienta independiente de análisis |

#### **Opción 2: Instalación en Sistema**
Si prefieres no usar `/bin`, asegúrate de que los comandos respondan en tu terminal:
```bash
# Verifica disponibilidad
which ffmpeg && which makemkvcon && which mkvmerge

# En Windows, añade al PATH las carpetas de instalación manualmente
```

### **Lanzamiento desde Código Fuente**

```bash
# 1. Clona el repo
git clone https://github.com/RawSmokeTerribilus/MKVerything.git
cd MKVerything

# 2. Instala dependencias Python
pip install -r requirements.txt

# 3. Instala binarios externos (ver sección anterior)

# 4. Lanza el TUI
python launcher.py
```

---

## 📄 Licencia

Ver archivo LICENSE en el repositorio.

---

## 🤝 Contribuciones

Reporta bugs o sugiere mejoras en GitHub Issues:
https://github.com/RawSmokeTerribilus/MKVerything/issues

---

**Última actualización:** 20 de febrero de 2026 (V2.beta "The Purge")
**Estado:** Battle-Ready ⚔️
