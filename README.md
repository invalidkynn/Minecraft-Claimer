⛏️ Minecraft Username Claimer
A lightweight Python script that monitors a specific Minecraft username and automatically claims it the moment it becomes available.

🚀 Features
Automated Monitoring: Checks availability via the Public Mojang API.

Instant Claiming: Swaps your username via the Minecraft Services API immediately upon detection.

Rate-Limit Safe: Uses a 15-second delay to stay under the 600 req/10 min limit.

Input Popup: Prompts for the target username via a UI window so you don't have to edit the code for every new name.

🛠️ How to Get Your Bearer Token
To claim a name, the script needs to "act" as your account. You provide this permission via a Bearer Token.

Go to Minecraft.net and log in to your profile.

Press F12 (or Right-Click > Inspect) to open the Developer Tools.

Navigate to the Network tab.

Refresh the page.

In the "Filter" or "Search" box, type profile.

Look for a request named profile (it should be a GET request).

Click on it and look at the Request Headers section.

Find the line that says authorization: Bearer ....

Copy the long string of random characters after the word "Bearer".

💻 Setup & Usage
1. Requirements
Ensure you have Python installed and the requests library:
'pip install requests'

2. Configuration
Open the script file and paste your token into the configuration variable:

'BEARER_TOKEN = "PASTE_YOUR_TOKEN_HERE"'
3. Execution
Run the script from your terminal:

python main.py
A popup will appear asking for the Target Username. Enter the name you want, and the script will handle the rest.

📝 Technical Notes
Token Lifespan: Bearer tokens typically expire every 24 hours. If the script returns a "Token Error," simply grab a fresh one from your browser.

30-Day Rule: Your account must be eligible for a name change (i.e., you haven't changed your name in the last 30 days).

Monitoring Speed: The script checks every 15 seconds. This is the "Safe Zone" to ensure your IP doesn't get temporarily blocked by Mojang's API.
