#!/bin/bash

# ==============================================================================
# REMUX MASTER - V10 (Gold Edition)
# Author: RawSmokeTerribilus
# Description: Mass convert legacy video containers (AVI, MP4, OGM...) to MKV.
# Features:
#   - Lossless conversion (copy codec) whenever possible.
#   - Auto-fix for common errors (mov_text subtitles, attached cover art).
#   - "Survival Mode": Drops problematic subtitles if conversion fails.
#   - Safe delete: Only removes original file after verified success.
# ==============================================================================

LOG_FILE="remux_master_log.txt"
# Target extensions (Case insensitive)
EXT_FIND_CMD='\( -iname "*.avi" -o -iname "*.ogm" -o -iname "*.divx" -o -iname "*.mpg" -o -iname "*.mpeg" -o -iname "*.mp4" -o -iname "*.flv" -o -iname "*.wmv" \)'

# Header for the log file
echo "" >> "$LOG_FILE"
echo "=== SESSION START: $(date) ===" >> "$LOG_FILE"

echo "=========================================="
echo "      REMUX MASTER V10 - SCANNING         "
echo "=========================================="

# Find files and process loop
eval find . -type f "$EXT_FIND_CMD" -print0 | while IFS= read -r -d '' source_file; do

    # Skip if file is already MKV
    if [[ "${source_file##*.}" == "mkv" ]]; then continue; fi

    mkv_file="${source_file%.*}.mkv"

    # --- EXISTENCE CHECK ---
    # If a valid MKV (>0 bytes) exists, skip silently.
    if [ -s "$mkv_file" ]; then
        continue
    fi
    # If a corrupt/empty MKV exists from previous run, remove it.
    if [ -f "$mkv_file" ]; then rm -f "$mkv_file"; fi

    echo "--------------------------------------------------"
    echo "📄 PROCESSING: $source_file"

    TEMP_OUTPUT=$(mktemp)
    CONVERSION_OK=0
    METHOD=""

    # ==============================================================================
    # ATTEMPT 1: DIRECT COPY (Lossless 1:1)
    # Best quality, keeps all tracks. Fails on incompatible subs/cover art.
    # ==============================================================================
    if ffmpeg -hide_banner -fflags +genpts -i "$source_file" -map 0 -c copy -avoid_negative_ts make_zero "$mkv_file" < /dev/null >"$TEMP_OUTPUT" 2>&1; then
        CONVERSION_OK=1
        METHOD="Direct Copy"
    else
        rm -f "$mkv_file"
        
        # ==============================================================================
        # ATTEMPT 2: FIX SUBTITLES (Convert to SRT)
        # Fixes MP4 'mov_text' incompatibility. Fails if subs are bitmap.
        # ==============================================================================
        echo "   ⚠️  Direct copy failed. Trying Subtitle -> SRT conversion..."
        
        if ffmpeg -hide_banner -fflags +genpts -i "$source_file" -map 0 -c:v copy -c:a copy -c:s srt -avoid_negative_ts make_zero "$mkv_file" < /dev/null >"$TEMP_OUTPUT" 2>&1; then
            CONVERSION_OK=1
            METHOD="Subtitle Re-encode (SRT)"
        else
            rm -f "$mkv_file"

            # ==============================================================================
            # ATTEMPT 3: RESCUE MODE (Drop Subtitles)
            # If subs are bitmap/corrupt, we drop them to save Video/Audio.
            # ==============================================================================
            echo "   ⚠️  Subtitle error. Trying RESCUE MODE (Dropping Subtitles)..."

            if ffmpeg -hide_banner -fflags +genpts -i "$source_file" -map 0 -c copy -sn -avoid_negative_ts make_zero "$mkv_file" < /dev/null >"$TEMP_OUTPUT" 2>&1; then
                CONVERSION_OK=1
                METHOD="Rescue Mode (No Subs)"
            else
                rm -f "$mkv_file"

                # ==============================================================================
                # ATTEMPT 4: STRICT MODE (Video Main + Audio Only)
                # Last resort. Ignores cover art, attachments, menus.
                # ==============================================================================
                echo "   ⚠️  Rescue failed. Trying STRICT MODE (Video+Audio Only)..."

                if ffmpeg -hide_banner -fflags +genpts -i "$source_file" -map 0:v:0 -map 0:a -c copy -sn -avoid_negative_ts make_zero "$mkv_file" < /dev/null >"$TEMP_OUTPUT" 2>&1; then
                    CONVERSION_OK=1
                    METHOD="Strict Mode (V+A Only)"
                fi
            fi
        fi
    fi

    # ==============================================================================
    # FINAL RESULT HANDLER
    # ==============================================================================
    rm -f "$TEMP_OUTPUT"

    if [ $CONVERSION_OK -eq 1 ]; then
        echo "   ✅ SUCCESS ($METHOD)"
        
        # SAFE DELETE ORIGINAL
        rm -f "$source_file"
        if [ ! -f "$source_file" ]; then
            echo "   🗑️  ORIGINAL DELETED"
        else
            echo "   ❌ ERROR DELETING ORIGINAL (Check permissions)"
        fi
    else
        echo "   ❌ FATAL ERROR: Could not convert file."
        echo "      Details logged to $LOG_FILE"
        
        # Log the specific error for debug
        {
            echo "=================================================="
            echo "DATE: $(date)"
            echo "FILE: $source_file"
            echo "FINAL ATTEMPT LOG:"
            echo "--------------------------------------------------"
            # Dry run to capture error
            ffmpeg -v error -i "$source_file" -map 0:v:0 -map 0:a -c copy -sn -f null - < /dev/null
            echo "=================================================="
            echo ""
        } >> "$LOG_FILE"
        
        if [ -f "$mkv_file" ]; then rm -f "$mkv_file"; fi
    fi

done

echo ""
echo "=========================================="
echo "          PROCESS COMPLETED               "
echo "=========================================="
