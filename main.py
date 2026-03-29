import requests
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

# ==========================================
# CONFIGURATION: PASTE YOUR TOKEN BELOW
# ==========================================
BEARER_TOKEN = "PASTE_YOUR_BEARER_TOKEN_HERE"
# ==========================================

def get_target_name():
    """Opens a popup to ask for the username."""
    root = tk.Tk()
    root.withdraw()  # Hide the main tiny window
    target = simpledialog.askstring("Minecraft Claimer", "Enter Username to Monitor:")
    return target

def verify_token(token):
    """Checks if the hardcoded token is still active."""
    url = "https://api.minecraftservices.com/minecraft/profile"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except:
        return False

def claim_name(name, token):
    """The actual request to change your name."""
    url = f"https://api.minecraftservices.com/minecraft/profile/name/{name}"
    headers = {"Authorization": f"Bearer {token}"}
    
    try:
        response = requests.put(url, headers=headers)
        if response.status_code == 200:
            messagebox.showinfo("SUCCESS", f"Successfully claimed: {name}")
            return True
        else:
            print(f"Claim failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"Connection error during claim: {e}")
        return False

def run_claimer():
    # 1. Verify the token first
    if BEARER_TOKEN == "PASTE_YOUR_BEARER_TOKEN_HERE" or not verify_token(BEARER_TOKEN):
        messagebox.showerror("Token Error", "Your Bearer Token is missing, invalid, or expired!")
        return

    # 2. Get the target name from popup
    target = get_target_name()
    if not target:
        print("No username entered. Exiting.")
        return

    print(f"Starting monitor for: {target}")
    check_url = f"https://api.mojang.com/users/profiles/minecraft/{target}"
    
    while True:
        try:
            # Check availability (Public API - No rate limit risk at 15s)
            response = requests.get(check_url)
            
            if response.status_code == 204:
                print(f"[{time.strftime('%H:%M:%S')}] {target} IS FREE! CLAIMING...")
                if claim_name(target, BEARER_TOKEN):
                    break
            elif response.status_code == 200:
                print(f"[{time.strftime('%H:%M:%S')}] {target} is taken.")
            else:
                print(f"API Error: {response.status_code}")

        except Exception as e:
            print(f"Network error: {e}")

        # Wait 15 seconds (Safe from Mojang's 600 req/10 min limit)
        time.sleep(15)

if __name__ == "__main__":
    run_claimer()
