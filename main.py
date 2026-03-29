import requests
import time
import tkinter as tk
from tkinter import messagebox, simpledialog

# Paste your token here
BEARER_TOKEN = "BEARER_TOKEN_HERE"

def verify_token(token):
    url = "https://api.minecraftservices.com/minecraft/profile"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except:
        return False

def claim_name(name, token):
    # Updated 2026 Endpoint Check
    url = f"https://api.minecraftservices.com/minecraft/profile/name/{name}"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.put(url, headers=headers)
    
    if response.status_code == 200:
        messagebox.showinfo("SUCCESS", f"Claimed {name}!")
        return True
    elif response.status_code == 404:
        print(f"Error 404: The name '{name}' is invalid or the API path has changed.")
    else:
        print(f"Claim failed: {response.status_code}")
    return False

def run_claimer():
    if not verify_token(BEARER_TOKEN):
        messagebox.showerror("Token Error", "Invalid Bearer Token.")
        return

    root = tk.Tk()
    root.withdraw()
    target = simpledialog.askstring("Minecraft Claimer", "Enter Username:")
    if not target: return

    print(f"Monitoring: {target}")
    # Using the public API for monitoring
    check_url = f"https://api.mojang.com/users/profiles/minecraft/{target}"
    
    while True:
        try:
            res = requests.get(check_url)
            if res.status_code == 204: # 204 means Available
                if claim_name(target, BEARER_TOKEN):
                    break
            elif res.status_code == 404:
                # If the MONITORING api returns 404, it's the same as 204 (Available) 
                # for some newer Microsoft-linked names.
                if claim_name(target, BEARER_TOKEN):
                    break
            else:
                print(f"[{time.strftime('%H:%M:%S')}] {target} is taken.")
        except:
            print("Network glitch, retrying...")
            
        time.sleep(7)

if __name__ == "__main__":
    run_claimer()
