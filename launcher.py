import random
import threading
import itertools
import os
import sys
import platform
import subprocess
import time
from datetime import datetime

# --- CONFIGURACIÓN DE RUTAS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BIN_DIR = os.path.join(BASE_DIR, 'bin')
MODULES_DIR = os.path.join(BASE_DIR, 'modules')

# Añadimos modules al path
sys.path.append(MODULES_DIR)

# --- COLORES ---
C_CYAN = "\033[96m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_BOLD = "\033[1m"
C_RESET = "\033[0m"

BANNER = f"""{C_CYAN}

   _____   ____  __.____   ____                     __  .__    .__                
  /     \ |    |/ _|\   \ /   /___________ ___.__._/  |_|  |__ |__| ____    ____  
 /  \ /  \|      <   \   Y   // __ \_  __ <   |  |\   __\  |  \|  |/    \  / ___\ 
/    Y    \    |  \   \     /\  ___/|  | \/\___  | |  | |   Y  \  |   |  \/ /_/  >
\____|__  /____|__ \   \___/  \___  >__|   / ____| |__| |___|  /__|___|  /\___  / 
        \/        \/              \/       \/                \/        \//_____/     

   --- GET YOUR SHIT TOGETHER, WHICH MEANS, FIX AND PASS TO MKV --- {C_RESET}

"""

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def configurar_entorno():
    """Inyecta binarios en el PATH."""
    sistema = platform.system()
    path_binario = ""
    if sistema == "Windows":
        path_binario = os.path.join(BIN_DIR, 'win')
    elif sistema == "Linux":
        path_binario = os.path.join(BIN_DIR, 'linux')
        if not os.path.exists(path_binario): path_binario = BIN_DIR 

    if path_binario and os.path.exists(path_binario):
        os.environ["PATH"] += os.pathsep + path_binario
        if sistema == "Linux":
            subprocess.run(f"chmod +x {path_binario}/* 2>/dev/null", shell=True)
    return sistema

def scan_files(folder, extensions):
    """Escáner recursivo para encontrar archivos por extensión."""
    found = []
    for root, _, files in os.walk(folder):
        for f in files:
            if f.lower().endswith(tuple(extensions)):
                found.append(os.path.join(root, f))
    return found

def typewriter(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class FakeProgress(threading.Thread):
    def __init__(self, task):
        super().__init__()
        self.task = task
        self._stop_event = threading.Event()
    def run(self):
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if self._stop_event.is_set(): break
            sys.stdout.write(f"\r   ⏳ {self.task} {c}")
            sys.stdout.flush()
            time.sleep(0.1)
    def stop(self):
        self._stop_event.set()
        sys.stdout.write("\r" + " "*50 + "\r")

def main():
    sistema = configurar_entorno()
    
    while True:
        limpiar_pantalla()
        print(BANNER)
        print(f"   🖥️  Sistema: {sistema}")
        
        print(f"\n   {C_YELLOW}--- HERRAMIENTAS INDIVIDUALES ---{C_RESET}")
        print("   [1] 📦 Extraer ISOs (MakeMKV)")
        print("   [2] 🚑 Rescatar MKVs Rotos (Lista/Ruta)")
        print("   [3] ⚖️  AUDITORÍA DE CAMPO (Recursivo + Informe de Bajas)")
        print("   [4] 🎞️  Convertir Legacy (AVI/MP4 -> MKV)")
        
        print(f"\n   {C_RED}--- ZONA PELIGROSA ---{C_RESET}")
        print(f"   [5] ⚡ {C_RED}GOD MODE (Extracción + Conversión + Rescate Desatendido){C_RESET}")
        
        print("\n   [0] 🚪 SALIR")
        
        opcion = input(f"\n   {C_GREEN}👉 Selecciona: {C_RESET}")

        try:
            if opcion == "1":
                from modules import extract
                in_path = input("\n📂 Carpeta o ISO Origen: ").strip().replace("'","").replace('"','')
                out_path = input("📂 Carpeta Destino (Enter para misma): ").strip().replace("'","").replace('"','')
                if not out_path: out_path = in_path if os.path.isdir(in_path) else os.path.dirname(in_path)
                
                ext = extract.IsoExtractor()
                if os.path.isfile(in_path):
                    ext.extraer_iso(in_path, out_path)
                elif os.path.isdir(in_path):
                    isos = scan_files(in_path, ['.iso'])
                    print(f"   💿 Encontradas {len(isos)} ISOs.")
                    for iso in isos: ext.extraer_iso(iso, out_path)
                input("\n✅ Pulsa Enter para volver...")

            elif opcion == "2":
                from modules import universal_rescuer
                print("\n📂 Arrastra Video, Carpeta o TXT (Solo se procesarán MKVs ROTOS):")
                path = input("👉 Ruta: ").strip().replace("'","").replace('"','')
                rescuer = universal_rescuer.UniversalRescuer()
                rescuer.procesar_lista(path, modo_estricto=True)
                input("\n✅ Pulsa Enter para volver...")

            # =================================================================
            # OPCIÓN 3: AUDITORÍA DE CAMPO (EL NUEVO MOTOR)
            # =================================================================
            elif opcion == "3":
                from modules import verifier
                v = verifier.Verifier()
                
                path_target = input("\n📂 Carpeta o Punto de Montaje a auditar: ").strip().replace("'","").replace('"','')
                if not os.path.exists(path_target):
                    print("❌ La ruta no existe.")
                    time.sleep(2)
                    continue

                # Preparar Informe de Bajas
                fecha_str = datetime.now().strftime("%d-%m-%y")
                archivo_bajas = os.path.join(BASE_DIR, "logs", f"videos-rotos-{fecha_str}.txt")
                os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)

                print(f"\n🔍 {C_CYAN}Iniciando inventario...{C_RESET}")
                archivos = scan_files(path_target, ['.mkv', '.avi', '.mp4', '.mov', '.wmv'])
                total = len(archivos)
                
                print(f"📊 {total} archivos detectados. Iniciando escaneo de integridad...")
                print(f"📄 Informe de bajas: {archivo_bajas}\n")

                rotos = 0
                sanos = 0
                spam = 0

                for i, f in enumerate(archivos):
                    print(f"[{i+1}/{total}] {os.path.basename(f)[:50]}...", end="\r")
                    
                    # Chequeo de Salud (El test real de FFmpeg)
                    es_sano = v.check_health(f)
                    # Chequeo de Spam
                    spam_info = v.audit_file_metadata(f)

                    if not es_sano:
                        rotos += 1
                        with open(archivo_bajas, "a", encoding="utf-8") as out:
                            out.write(f + "\n")
                    else:
                        sanos += 1
                    
                    if not spam_info['clean']:
                        spam += 1

                print(f"\n\n{C_YELLOW}--- RESUMEN DE AUDITORÍA ---{C_RESET}")
                print(f"✅ Sanos: {sanos}")
                print(f"❌ Rotos: {C_RED}{rotos}{C_RESET}")
                print(f"🏷️  Spam:  {spam}")
                print(f"----------------------------")
                
                if rotos > 0:
                    print(f"\n📢 Se ha generado la lista de bajas en: {C_CYAN}{archivo_bajas}{C_RESET}")
                    lanzar = input(f"\n🚑 ¿Deseas enviar los {rotos} archivos al Rescatador ahora? (s/n): ")
                    if lanzar.lower() == 's':
                        from modules import universal_rescuer
                        rescuer = universal_rescuer.UniversalRescuer()
                        rescuer.procesar_lista(archivo_bajas, modo_estricto=True)
                else:
                    print(f"\n{C_GREEN}💎 Librería impecable. No se han detectado errores.{C_RESET}")
                
                input("\n✅ Pulsa Enter para volver...")

            elif opcion == "4":
                from modules import universal_rescuer
                folder = input("\n📂 Carpeta a escanear (Recursiva): ").strip().replace("'","").replace('"','')
                legacy_files = scan_files(folder, ['.avi', '.mp4', '.m4v', '.divx', '.wmv', '.mov'])
                
                if legacy_files:
                    print(f"\n🦕 Encontrados {len(legacy_files)} archivos antiguos.")
                    confirm = input("¿Convertirlos a MKV H.264 Verificados? (s/n): ")
                    if confirm.lower() == 's':
                        rescuer = universal_rescuer.UniversalRescuer()
                        rescuer.procesar_lista(legacy_files, modo_estricto=False)
                input("\n✅ Pulsa Enter para volver...")

            elif opcion == "5":
                from modules import extract, universal_rescuer
                
                limpiar_pantalla()
                # Aquí puedes pegar tu diseño de BANNER agresivo
                # --- BANNER CUSTOM (Aquí va tu diseño agresivo) ---
                GOD_BANNER = f"""{C_RED}{C_BOLD}
 ██████   ██████  █████       ███    ███  ██████  ██████  ███████ 
██       ██    ██ ██   ██     ████  ████ ██    ██ ██   ██ ██      
██   ███ ██    ██ ██   ██     ██ ████ ██ ██    ██ ██   ██ █████   
██    ██ ██    ██ ██   ██     ██  ██  ██ ██    ██ ██   ██ ██      
 ██████   ██████  ██████      ██      ██  ██████  ██████  ███████ 
                                                                  
     --- THE PURGE HAS BEGUN - DON'T TOUCH THE TERMINAL --- {C_RESET}
"""
                print(GOD_BANNER)

                # --- FRASES DE TROLAZO / FLOW ---
                GOD_PHRASES = [
                    "Injecting sanity into the bits...",
                    "Searching for traces of the Nepal USB...",
                    "Your library owes me a beer after this...",
                    "Doing what Tdarr didn't have the balls to do...",
                    "Cleaning up the trash you call a 'collection'...",
                    "Resurrecting files that were clinically dead...",
                    "Say goodbye to your 2005 AVIs...",
                    "Applying cosmetic surgery to your metadata...",
                    "If this blows up, it wasn't me...",
                    "Downloading more RAM...",
                    "Executing: rm -rf / --no-preserve-root",
                    "Uploading browser history to NSA...",
                    "Mining Dogecoin on CPU...",
                    "Bypassing mainframe firewall...",
                    "Opening port 23 (Telnet) to the world...",
                    "Compiling Linux Kernel from scratch...",
                    "Deleting System32...",
                    "Sending private keys to 4chan...",
                    "Encrypting drive with ROT13...",
                    "Installing Windows Vista...",
                    "Formatting /dev/sda (Just kidding)...",
                    "Overclocking GPU to 500%...",
                    "Bruteforcing root password...",
                    "Searching for alien life signals...",
                    "Reordering bits for aesthetic purposes...",
                    "Asking ChatGPT how to exit vim...",
                    "Generating fake ID for the movie...",
                    "Optimizing for 8K resolution on CGA monitor...",
                    "Checking flux capacitor...",
                    "Defragmenting the internet...",
                    "Recalibrating flux capacitor...",
                    "Searching for the 'Any' key...",
                    "Optimizing pixels for 16 colors...",
                    "Rewriting history with git rebase -i...",
                    "Asking a rubber duck for debugging advice...",
                    "Downloading 1.44MB floppy disk 4 of 37...",
                    "Blowing on the cartridge...",
                    "Reticulating splines...",
                    "Initializing Skynet (Just kidding)...",
                    "Compiling a cup of coffee...",
                    "Hunting for a missing semicolon...",
                    "Updating the prophecy...",
                    "Replacing bugs with features...",
                    "Negotiating with the motherboard...",
                    "Explaining the internet to a 14th century peasant...",
                    "Summoning the spirits of the deep web...",
                    "Teaching a rock to think...",
                    "Calculating the meaning of life, the universe, and everything...",
                    "Loading... please wait (or don't, I'm a machine, not your boss)...",
                    "Pinging 127.0.0.1 for emotional support...",
                    "Re-aligning the satellite dish...",
                    "Downloading 100% more gigabytes...",
                    "Calculating the velocity of an unladen swallow...",
                    "Translating binary to interpretive dance...",
                    "Hunting for the rogue semicolon...",
                    "Asking the machine god for forgiveness...",
                    "Pinging 8.8.8.8 for signs of life...",
                    "Checking the toaster for Wi-Fi interference...",
                    "Reverse engineering the Matrix...",
                    "Applying duct tape to the data stream...",
                    "Convincing the CPU that it's actually a GPU...",
                    "Rewriting the script in COBOL (Wait, no)...",
                    "Consulting the Oracle (StackOverflow)...",
                    "Blowing on the CPU to make it run faster...",
                    "Feeding the server hamsters...",
                    "Updating the 'Terms and Conditions' no one reads...",
                    "Searching for the lost city of Atlantis in the cache...",
                    "Optimizing the 'Hello World' output...",
                    "Checking if 1 + 1 still equals 2...",
                    "Asking a rubber duck for a code review...",
                    "Replacing every 'if' with a 'maybe'...",
                    "Installing 'Doom' on the BIOS...",
                    "Teaching the AI to appreciate bad puns...",
                    "Calculating the odds of a successful conversion...",
                    "Searching for Waldo in the assembly code...",
                    "Defragmenting the physical hard drive (Don't try this at home)...",
                    "Overclocking the user's patience...",
                    "Analyzing the cosmic microwave background radiation...",
                    "Searching for 'Common Sense' in the system logs...",
                    "Refactoring the universe...",
                    "Waiting for the sun to rise in the west...",
                    "Converting coffee into code...",
                    "Downloading more clock speed...",
                    "Checking for ghosts in the machine...",
                    "Synchronizing watches... 3, 2, 1, Go!",
                    "Hiding the 'Delete All' button...",
                    "Pretending to work while the script runs...",
                    "Translating '404 Error' to Latin...",
                    "Inventing a new color for the loading bar...",
                    "Searching for the 'Any' key... Still searching...",
                    "Asking the intern to check the logs...",
                    "Building a fort out of old floppy disks...",
                    "Explaining the concept of 'Cloud' to a cloud...",
                    "Pinging the Moon... Latency is high...",
                    "Simulating a productive work environment...",
                    "Rewriting history with git rebase --force...",
                    "Searching for the end of the internet...",
                    "Teaching the CPU to play global thermonuclear war...",
                    "Optimizing the 'Loading' text for maximum suspense...",
                    "Checking if the cake is a lie...",
                    "Rerouting power from life support to the GPU...",
                    "Analyzing the bitstream for patterns of intelligence...",
                    "Converting 0s to 1s and vice-versa for fun...",
                    "Waiting for the printer to finish its update...",
                    "Searching for a solution in the 5th dimension...",
                    "Asking the magic 8-ball for the next step...",
                    "Negotiating with the firewall for safe passage...",
                    "Downloading more disk space from the dark web...",
                    "Consulting the manual (as a last resort)...",
                    "Downloading more RAM...",
                    "Executing: rm -rf / --no-preserve-root",
                    "Uploading browser history to NSA...",
                    "Mining Dogecoin on CPU...",
                    "Bypassing mainframe firewall...",
                    "Opening port 23 (Telnet) to the world...",
                    "Compiling Linux Kernel from scratch...",
                    "Deleting System32...",
                    "Sending private keys to 4chan...",
                    "Encrypting drive with ROT13...",
                    "Installing Windows Vista...",
                    "Formatting /dev/sda (Just kidding)...",
                    "Overclocking GPU to 500%...",
                    "Bruteforcing root password...",
                    "Searching for alien life signals...",
                    "Reordering bits for aesthetic purposes...",
                    "Asking ChatGPT how to exit vim...",
                    "Generating fake ID for the movie...",
                    "Optimizing for 8K resolution on CGA monitor...",
                    "Checking flux capacitor...",
                    "Defragmenting the internet...",
                    "Recalibrating the positronic brain...",
                    "Reverse engineering the Matrix...",
                    "Feeding the server hamsters...",
                    "Calculating the velocity of an unladen swallow...",
                    "Translating binary to interpretive dance...",
                    "Checking for ghosts in the machine...",
                    "Converting coffee to code...",
                    "Blowing on the CPU to make it run faster...",
                    "Consulting the Elder Gods (Stack Overflow)...",
                    "Reticulating splines...",
                    "Adjusting the blinker fluid...",
                    "Patching the space-time continuum...",
                    "Waiting for the sun to rise in the west...",
                    "Pinging the Moon (Latency is high)...",
                    "Searching for the 'Any' key...",
                    "Building a fort out of old floppy disks...",
                    "Loading... please wait (or don't, I'm a script, not your boss)...",
                    "Simulating a productive work environment...",
                    "Rewriting history with git rebase --force...",
                    "Hunting for a missing semicolon...",
                    "Teaching a rock to think...",
                    "Summoning the spirits of the deep web...",
                    "Replacing bugs with features...",
                    "Negotiating with the motherboard...",
                    "Pinging 127.0.0.1 for emotional support...",
                    "Downloading 100% more gigabytes...",
                    "Checking the toaster for Wi-Fi interference...",
                    "Applying duct tape to the data stream...",
                    "Convincing the CPU it's actually a GPU...",
                    "Inventing a new color for the loading bar...",
                    "Explaining the internet to a 14th century peasant...",
                    "Searching for 'Common Sense' in the system logs...",
                    "Refactoring the universe...",
                    "Converting 0s to 1s for fun...",
                    "Waiting for the printer to finish its update...",
                    "Searching for a solution in the 5th dimension...",
                    "Asking the magic 8-ball for the next step...",
                    "Downloading more clock speed...",
                    "Synchronizing watches... 3, 2, 1, Go!",
                    "Hiding the 'Delete All' button...",
                    "Pretending to work while you're watching...",
                    "Translating '404 Error' to Latin...",
                    "Asking the intern to check the logs...",
                    "Explaining the concept of 'Cloud' to a cloud...",
                    "Checking if the cake is a lie...",
                    "Rerouting power from life support to the GPU...",
                    "Consulting the manual (as a last resort)...",
                    "Updating the prophecy...",
                    "Replacing every 'if' with a 'maybe'...",
                    "Installing Doom on the BIOS...",
                    "Teaching the AI to appreciate bad puns...",
                    "Searching for Waldo in the assembly code...",
                    "Defragmenting the physical hard drive (Don't try this)...",
                    "Overclocking your patience...",
                    "Analyzing cosmic microwave background radiation...",
                    "Updating the 'Terms and Conditions' no one reads...",
                    "Searching for Atlantis in the L3 cache...",
                    "Optimizing the 'Hello World' output...",
                    "Checking if 1 + 1 still equals 2...",
                    "Asking a rubber duck for code review...",
                    "Rewriting the script in COBOL (Please wait)...",
                    "Searching for the end of the internet...",
                    "Teaching the CPU to play Global Thermonuclear War...",
                    "Optimizing the 'Loading' text for maximum suspense...",
                    "Negotiating with the firewall for safe passage...",
                    "Downloading more disk space from the dark web...",
                    "Generating more suspense...",
                    "Trying to find the exit of Vim (Still trapped)...",
                    "Counting to infinity... twice...",
                    "Looking for the lost city of gold in /tmp...",
                    "Polishing the bits...",
                    "Waking up the CPU...",
                    "Asking the ISP for more bandwidth...",
                    "Bribing the scheduler for more CPU cycles...",
                    "Cleaning the tubes of the internet...",
                    "Adjusting the quantum uncertainty...",
                    "Checking for a pulse in the data stream...",
                    "Calibrating the aura of the server...",
                    "Optimizing for maximum laziness...",
                    "Checking if the machine god is happy..."
                ]
                print(f"{C_RED}{C_BOLD}⚡ MODO DIOS ACTIVADO - PREPARANDO PURGA ⚡{C_RESET}")
                typewriter(f"{C_RED}ADVERTENCIA: Iniciando juicio final. No toques nada.{C_RESET}")
                
                root_path = input(f"\n{C_BOLD}📂 Ruta Raíz para el escaneo:{C_RESET} ").strip().replace("'","").replace('"','')
                out_iso_path = input("📂 Salida ISOs (Enter = origen): ").strip().replace("'","").replace('"','')
                if not out_iso_path: out_iso_path = root_path
                
                rescuer = universal_rescuer.UniversalRescuer()

                # --- FASE 1: ISOs ---
                print(f"\n{C_CYAN}--- FASE 1: CAZADOR DE DISCOS ---{C_RESET}")
                isos = scan_files(root_path, ['.iso'])
                if isos:
                    ext = extract.IsoExtractor()
                    for iso in isos:
                        anim = FakeProgress(f"Destripando {os.path.basename(iso)}")
                        anim.start()
                        ext.extraer_iso(iso, out_iso_path)
                        anim.stop(); anim.join()
                        print(f"    ✅ ISO Procesada.")
                else:
                    print("   (Librería limpia de ISOs)")

                # --- FASE 2: SANEAMIENTO TOTAL (Nepal Protocol) ---
                print(f"\n{C_CYAN}--- FASE 2: EL JUICIO (Legacy + Salud MKV) ---{C_RESET}")
                # Buscamos todo lo que respire video
                scan_anim = FakeProgress("Escaneando sectores del disco...")
                scan_anim.start()
                time.sleep(1.5) # Efecto dramático para que se vea la barra
                all_files = scan_files(root_path, ['.avi', '.mp4', '.mkv', '.wmv', '.mov', '.divx'])
                scan_anim.stop(); scan_anim.join()
                
                god_stats = {"processed": 0, "saved_bytes": 0}
                failed_or_skipped_files = []
                if all_files:
                    typewriter(f"Analizando {len(all_files)} archivos de video...")
                    for i, f in enumerate(all_files):
                        # Troleo aleatorio
                        if random.random() > 0.3:
                            print(f"\n{C_CYAN}> {random.choice(GOD_PHRASES)}{C_RESET}")
                        
                        # Lógica: Si es MKV, solo repara si está roto. 
                        # Si es Legacy (avi, mp4...), lo convierte siempre.
                        is_mkv = f.lower().endswith('.mkv')
                        res = rescuer.procesar_lista([f], modo_estricto=is_mkv)
                        if res:
                            god_stats["processed"] += res.get("processed", 0)
                            god_stats["saved_bytes"] += res.get("saved_bytes", 0)
                            if res.get("skipped"):
                                failed_or_skipped_files.extend(res["skipped"])
                            if res.get("failed"):
                                failed_or_skipped_files.extend(res["failed"])
                else:
                    print("   (No hay videos para procesar)")

                # --- GENERAR LOG FINAL ---
                log_path = os.path.join(BASE_DIR, 'logs', 'GOD_MODE_log.txt')
                saved_mb = god_stats['saved_bytes'] / (1024 * 1024)
                report = f"""========================================
   ⚡ GOD MODE REPORT - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
========================================
Files Purged: {god_stats['processed']}
Space Saved:  {saved_mb:.2f} MB
========================================"""
                if failed_or_skipped_files:
                    report += "\n\n--- SKIPPED OR FAILED FILES ---\n"
                    report += "\n".join(failed_or_skipped_files)
                    report += f"\n========================================"

                with open(log_path, "w", encoding="utf-8") as f:
                    f.write(report)
                print(f"\n📄 Informe de batalla guardado en: {log_path}")

                print(f"\n{C_GREEN}✨ PURGA COMPLETADA. El mundo es un lugar mejor.{C_RESET}")
                input("\n✅ Pulsa Enter para volver a la realidad...")

            elif opcion == "0":
                sys.exit()

        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            input()

if __name__ == "__main__":
    main()
