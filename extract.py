import argparse
import logging
import os
import subprocess
import json
import sys
import time
import random
import threading
import itertools
import shutil
import re # Necesario para el Sabueso
from persistence import StateManager
from analyzer import DiscScanner
from metadata_provider import MetadataProvider

# --- CONFIGURACIÓN DE LOGS ---
logging.basicConfig(
    filename='mkverithing_debug.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

# --- CLAVES API ---
EMBEDDED_TMDB_KEY = os.getenv("TMDB_API_KEY", "")

# --- EFECTOS VISUALES ---
CYAN = "\033[96m"; GREEN = "\033[92m"; YELLOW = "\033[93m"; RED = "\033[91m"; BOLD = "\033[1m"; RESET = "\033[0m"

def typewriter_effect(text, delay=0.005):
    for char in text:
        sys.stdout.write(char); sys.stdout.flush(); time.sleep(delay)
    print()

def print_credits():
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = """
   _____   ____  __.____   ____                     __  .__    .__                
  /     \\ |    |/ _|\\   \\ /   /___________ ___.__._/  |_|  |__ |__| ____    ____  
 /  \\ /  \\|      <   \\   Y   // __ \\_  __ <   |  |\\   __\\  |  \\|  |/    \\  / ___\\ 
/    Y    \\    |  \\   \\     /\\  ___/|  | \\/\\___  | |  | |   Y  \\  |   |  \\/ /_/  >
\\____|__  /____|__ \\   \\___/  \\___  >__|   / ____| |__| |___|  /__|___|  /\\___  / 
        \\/        \\/              \\/       \\/                \\/        \\//_____/  
    """
    print(CYAN + logo + RESET)
    print("\033[90m" + "-" * 65 + RESET)
    typewriter_effect(" SYSTEM ONLINE... INITIALIZING CORE MODULES...", 0.02)
    typewriter_effect(" 🤖 ARCHITECT AI: GEMINI [GOOGLE DEEP MIND]", 0.01)
    print("\033[90m" + "-" * 65 + RESET + "\n")

# --- CLASE ANIMACIÓN (DRESSED UP) ---
class FakeProgress(threading.Thread):
    def __init__(self, phrase_list=None):
        super().__init__()
        self._stop_event = threading.Event()
        # LA LISTA DE LA GLORIA: Más de 70 frases para el disfrute del usuario
        self.troll_phrases = [
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

    def run(self):
        width = 20
        idx_seq = itertools.cycle(list(range(width)) + list(range(width-1, 0, -1)))
        last_phrase_time = 0
        phrase = random.choice(self.troll_phrases)
        while not self._stop_event.is_set():
            i = next(idx_seq)
            bar = [' '] * width; bar[i] = '█'
            if i > 0: bar[i-1] = '▒'
            if i < width-1: bar[i+1] = '▒'
            if time.time() - last_phrase_time > 4:
                phrase = random.choice(self.troll_phrases); last_phrase_time = time.time()
            sys.stdout.write(f"\r{CYAN} PROCESSING: {GREEN}[{''.join(bar)}] {RESET}{phrase}\033[K")
            sys.stdout.flush(); time.sleep(0.1)

    def stop(self):
        self._stop_event.set(); print()

# --- TECNICISMOS ---
def check_dependencies():
    base_path = sys._MEIPASS if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    local_bin = os.path.join(base_path, "bin")
    if os.path.exists(local_bin): os.environ["PATH"] = local_bin + os.pathsep + os.environ["PATH"]
    missing = []
    if not shutil.which("ffmpeg"): missing.append("FFmpeg")
    if not shutil.which("makemkvcon"): missing.append("MakeMKV Console")
    if missing:
        print(f"{RED}❌ MISSING: {', '.join(missing)}{RESET}"); sys.exit(1)

def get_technical_tags(file_path):
    cmd = ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", "-show_format", file_path]
    try:
        data = json.loads(subprocess.run(cmd, capture_output=True, text=True, timeout=30).stdout)
        v = next(s for s in data['streams'] if s['codec_type'] == 'video')
        a = next(s for s in data['streams'] if s['codec_type'] == 'audio')
        return {"v_codec": "x265" if v['codec_name'] == 'hevc' else "x264", "v_res": f"{v['height']}p", 
                "a_codec": a['codec_name'].upper(), "a_chan": f"{a['channels']}.1" if a['channels'] > 2 else "2.0"}
    except: return {"v_codec": "x264", "v_res": "1080p", "a_codec": "AC3", "a_chan": "2.0"}

# --- LÓGICA DE SUPERVIVENCIA (PUNTO 3 REVISADO) ---
def library_eater(source_dir, dry_run=False):
    print(f"\n{BOLD} 🧹 INITIATING LIBRARY CLEANUP (DEFCON 4){RESET}")
    exts = ('.avi', '.mp4', '.m4v', '.divx', '.mpg', '.mpeg', '.flv', '.wmv', '.ogm', '.mov')
    files = [os.path.join(r, f) for r, d, fs in os.walk(source_dir) for f in fs if f.lower().endswith(exts)]
    if not files: return
    for f_in in files:
        f_out = os.path.splitext(f_in)[0] + ".mkv"
        if os.path.exists(f_out) or dry_run: continue
        anim = FakeProgress(); anim.start()
        success = False
        try:
            # Nivel 1: Copy Full
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f_in, "-map", "0", "-c", "copy", f_out], check=True)
            success = True
        except:
            try: # Nivel 2: No Subs
                subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f_in, "-map", "0:v", "-map", "0:a", "-c", "copy", "-sn", "-dn", f_out], check=True)
                success = True
            except:
                try: # Nivel 3: Audio AAC
                    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", f_in, "-map", "0:v", "-map", "0:a", "-c:v", "copy", "-c:a", "aac", "-sn", "-dn", f_out], check=True)
                    success = True
                except:
                    try: # Nivel 4: Re-encode (Timestamps rotos)
                        subprocess.run(["ffmpeg", "-y", "-v", "error", "-fflags", "+genpts", "-i", f_in, "-c:v", "libx264", "-crf", "23", "-c:a", "aac", "-sn", "-dn", f_out], check=True)
                        success = True
                    except: pass
        anim.stop(); anim.join()
        if success: os.remove(f_in); print(f"    ✅ CONVERTED: {os.path.basename(f_in)}")

# --- MAIN ---
def main():
    check_dependencies(); print_credits()
    parser = argparse.ArgumentParser()
    parser.add_argument("source"); parser.add_argument("output", nargs='?')
    parser.add_argument("--project", "-p", default=""); parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    # Detectar ISOs
    iso_files = []
    if os.path.isfile(args.source) and args.source.lower().endswith(".iso"):
        iso_files = [os.path.basename(args.source)]; src_dir = os.path.dirname(args.source)
    elif os.path.isdir(args.source):
        src_dir = args.source; iso_files = sorted([f for f in os.listdir(src_dir) if f.lower().endswith(".iso")])

    if iso_files and args.output:
        for iso_name in iso_files:
            # --- MEJORA DE SABUESO (GIT-STYLE IMPROVEMENT) ---
            # Ahora detectamos el año para que el match en TMDB sea quirúrgico
            raw_name = iso_name.lower().replace(".iso", "")
            
            # Buscamos un año entre paréntesis o suelto (ej: 1985 o (1985))
            year_match = re.search(r'\(?(\d{4})\)?', raw_name)
            p_year = year_match.group(1) if year_match else None
            
            # Limpiamos el nombre: todo lo que esté antes del año o etiquetas de calidad
            p_name = raw_name
            if year_match:
                p_name = raw_name[:year_match.start()]
            
            # Limpieza extra de etiquetas basura (Custom, Remux, UHD...)
            for tag in ["2160p", "1080p", "hevc", "hdr10", "dts-hd", "custom", "remux", "bluray"]:
                p_name = p_name.split(tag)[0]
            
            p_name = p_name.replace(".", " ").replace("_", " ").strip()
            # --------------------------------------------------

            state = StateManager(p_name)
            provider = MetadataProvider()
            if not os.getenv("TMDB_API_KEY"): os.environ["TMDB_API_KEY"] = EMBEDDED_TMDB_KEY
            
            # Pasamos el año detectado para que el match sea perfecto
            meta = state.data.get("metadata") or provider.get_best_match(p_name, year=p_year)
            
            if not meta:
                print(f" ⚠️  No se encontró match para '{p_name}'. Saltando ISO...")
                continue
            
            state.data["metadata"] = meta; state.save()

            print(f"🎬 {BOLD}PROCESANDO:{RESET} {meta['clean_name']} ({meta['year']})")
            titles = DiscScanner().scan_iso(os.path.join(src_dir, iso_name))
            for t in titles:
                if state.is_title_processed(iso_name, t['id']): continue
                num = state.get_next_number()
                anim = FakeProgress(); anim.start()
                try:
                    subprocess.run(["makemkvcon", "mkv", f"iso:{os.path.join(src_dir, iso_name)}", t['id'], args.output], capture_output=True, check=True)
                    mkv = max([os.path.join(args.output, f) for f in os.listdir(args.output) if f.endswith(".mkv")], key=os.path.getctime)
                    tech = get_technical_tags(mkv)
                    
                    # Naming Logic (Respetando el purismo de la ISO)
                    f_name = f"{meta['clean_name']} ({meta['year']}) Remux-{tech['v_res']} {tech['a_codec']} {tech['v_codec']}.mkv"
                    f_dir = os.path.join(args.output, f"{meta['clean_name']} ({meta['year']}) Spanish")
                    os.makedirs(f_dir, exist_ok=True)
                    os.replace(mkv, os.path.join(f_dir, f_name))
                    state.register_extraction(iso_name, t['id'], f_name)
                    anim.stop(); anim.join(); print(f"    ✅ LISTO: {f_name}")
                except Exception as e: anim.stop(); anim.join(); print(f"    ❌ ERROR: {e}")

    # LA ISO NO SE BORRA. Es un bien intrínseco.
    library_eater(args.source if os.path.isdir(args.source) else os.path.dirname(args.source), args.dry_run)

if __name__ == "__main__":
    main()
