import os
import sys
import time
import random

# --- CARGADOR MANUAL DE .ENV ---
# Esto permite que el binario lea tu clave sin instalar 'python-dotenv'
if os.path.exists(".env"):
    try:
        with open(".env", "r") as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key.strip()] = value.strip()
    except Exception:
        pass

# --- PALETA CROMÁTICA DE TUBO CATÓDICO ---
CYAN = "\033[96m"; GREEN = "\033[92m"; YELLOW = "\033[93m"; RED = "\033[91m"; BOLD = "\033[1m"; RESET = "\033[0m"

def draw_box(text, color=CYAN):
    lines = text.split('\n')
    width = max(len(l) for l in lines) + 6
    print(color + "╔" + "═" * (width - 2) + "╗")
    for line in lines:
        print(f"║   {line.ljust(width - 6)}   ║")
    print("╚" + "═" * (width - 2) + "╝" + RESET)

def typewriter(text, delay=0.015):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_boot_sequence():
    os.system('cls' if os.name == 'nt' else 'clear')
    boot_msgs = [
        "Initializing MKV-CORE [v1.1]...",
        "Detecting legacy file signatures (AVI/MP4/DIVX)...",
        "Calibrating neural remuxing engine...",
        "Checking drive health for sector integrity...",
        "Warning: Detected remnants of 20th century codecs.",
        "Establishing TMDB metadata uplink...",
        "Purging non-essential sub-routines...",
        "System ready. Awaiting Architect command."
    ]
    for msg in boot_msgs:
        prefix = f"{GREEN}[ OK ]{RESET}" if random.random() > 0.1 else f"{YELLOW}[WARN]{RESET}"
        print(f"{prefix} {msg}")
        time.sleep(random.uniform(0.1, 0.4))
    time.sleep(0.5)

def get_input(prompt, flair=">>"):
    print(f"\n{YELLOW}{BOLD}{flair} {prompt}{RESET}")
    return input(f"{GREEN}   CMD_PROMPT_   ").strip()

def tui_launcher():
    fake_boot_sequence()
    
    logo = """
    ███╗   ███╗██╗  ██╗██╗   ██╗███████╗██████╗ ████████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
    ████╗ ████║██║ ██╔╝██║   ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝ 
    ██╔████╔██║█████╔╝ ██║   ██║█████╗  ██████╔╝   ██║   ███████║██║██╔██╗ ██║██║  ███╗
    ██║╚██╔╝██║██╔═██╗ ╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══██║██║██║╚██╗██║██║   ██║
    ██║ ╚═╝ ██║██║  ██╗ ╚████╔╝ ███████╗██║  ██║   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
    ╚═╝     ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    """
    print(CYAN + logo + RESET)
    draw_box("MKVERITHING - INTERACTIVE INTERFACE V1.1\nARCHITECT: GEMINI | OS: RHEL/POSIX HYBRID\nMISSION: FAREWELL TO THE LEGACY", CYAN)
    
    # STEP 1: SOURCE
    typewriter(f"\n{BOLD}OBJETIVO: LOCALIZAR LOS DATOS RESISTENTES...{RESET}")
    source = get_input("Ruta de la ISO o carpeta contenedora:")
    while not source or not os.path.exists(source):
        print(f"{RED}   ERROR: Sector no encontrado. Verifique la ruta.{RESET}")
        source = get_input("Ruta de Origen:")

    # STEP 2: DESTINATION
    typewriter(f"\n{BOLD}DESTINO: DONDE LAS ISOs SE CONVIERTEN EN LEYENDA...{RESET}")
    output = get_input("Ruta de salida (Presione ENTER para local):")
    if not output: 
        output = os.path.dirname(source) if os.path.isfile(source) else source

    # STEP 3: PROJECT
    typewriter(f"\n{BOLD}METADATOS: IDENTIFICANDO LA PIEZA DE CULTURA...{RESET}")
    print(f"{CYAN}   (Dejar en blanco para escaneo automático de patrones){RESET}")
    project = get_input("Nombre del proyecto (TMDB):")

    # FINAL BRIEFING
    os.system('cls' if os.name == 'nt' else 'clear')
    summary = f"SOURCE: {source}\nDEST  : {output}\nTARGET: {project if project else 'AUTO-SCANNER'}"
    draw_box(f"MISSION PARAMETERS LOCKED:\n--------------------------\n{summary}", GREEN)
    
    farewell_msgs = [
        "Despidiéndose de los bits de 1995...",
        "Diciéndole adiós al DivX por última vez...",
        "Preparando el funeral de los artefactos de compresión...",
        "Haciendo justicia a la alta definición..."
    ]
    typewriter(f"{YELLOW}{random.choice(farewell_msgs)}{RESET}")
    
    confirm = get_input("¿INICIAR SECUENCIA DE LANZAMIENTO? (S/N)", flair="[CONFIRM]")
    
    if confirm.lower() == 's':
        print(f"\n{CYAN}{BOLD}INYECTANDO BINARIOS EN EL KERNEL...{RESET}")
        time.sleep(1.2)
        
        # --- PREPARACIÓN PARA EL FREEZE (LLAMADA DIRECTA) ---
        import extract
        sys.argv = ["extract.py", source, output]
        if project: 
            sys.argv.extend(["--project", project])
        
        # Saltamos al núcleo del programa
        extract.main()
    else:
        print(f"\n{RED}OPERACIÓN CANCELADA POR EL ARQUITECTO. REGRESANDO A LAS SOMBRAS.{RESET}")
        time.sleep(1)

if __name__ == "__main__":
    try:
        tui_launcher()
    except KeyboardInterrupt:
        print(f"\n{RED}INTERRUPCIÓN FORZADA. ABORTANDO MISIÓN.{RESET}")
        sys.exit(0)
