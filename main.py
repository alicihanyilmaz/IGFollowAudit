from instagrapi import Client
import requests
import time
from datetime import datetime

# --- SETTINGS ---
TELEGRAM_TOKEN = "8835306685:AAExps6cw5NLfCTBV2BTvkIjWqcy79Xrjmk"
CHAT_ID = "Telegram_chat_id"
TARGET_ACCOUNT = "Target_account"

# THE LONG SESSIONID (TOKEN) VALUE COPIED FROM YOUR BROWSER
INSTA_SESSION_ID = "INSTA_SESSION_ID"
# ---------------

def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": CHAT_ID, "text": message})
    except:
        pass

def main():
    # STAGE 1: Setting up the initial client to fetch the starting list
    cl_initial = Client()
    
    try:
        print("Connecting to Instagram in the background using SessionID...")
        cl_initial.login_by_sessionid(INSTA_SESSION_ID)
        print("Login successful! Security bypassed.")
    except Exception as e:
        print(f"Login error: {e}")
        return

    try:
        print(f"Fetching the initial follower list for {TARGET_ACCOUNT}...")
        target_id = cl_initial.user_id_from_username(TARGET_ACCOUNT)
        followers = cl_initial.user_followers(target_id)
        
        old_followers = set()
        for user_id, user_info in followers.items():
            old_followers.add(user_info.username)
        
        current_time = datetime.now().strftime('%H:%M:%S')
        print(f"[{current_time}] Initial list ready. Total: {len(old_followers)} followers.")
        send_telegram_notification(f" Bot started running.\nFetched an initial list of {len(old_followers)} followers for {TARGET_ACCOUNT}.")
        
    except Exception as e:
        print(f"Error occurred while fetching the initial list: {e}")
        return

    # We are done with the initial client after getting the starting list
    del cl_initial 

    # STAGE 2: Continuous monitoring loop
    while True:
        # You can change 1800 (30 mins) to 60 (1 min) here for testing
        time.sleep(60) 
        
        try:
            current_time = datetime.now().strftime('%H:%M:%S')
            print(f"[{current_time}] Memory cleared. Forcing a fresh list pull from Instagram...")
            
            # --- THE SOLUTION IS HERE ---
            # We create a BRAND NEW client with empty memory at the start of each loop iteration
            cl_current = Client()
            cl_current.login_by_sessionid(INSTA_SESSION_ID)
            # --------------------------
            
            # The brand new client is forced to connect to Instagram and fetch the latest data
            current_followers = cl_current.user_followers(target_id)
            
            new_followers = set()
            for user_id, user_info in current_followers.items():
                new_followers.add(user_info.username)

            gained_followers = new_followers - old_followers
            lost_followers = old_followers - new_followers

            if gained_followers:
                names = "\n".join([f" {k}" for k in gained_followers])
                message = f" {TARGET_ACCOUNT} GAINED NEW FOLLOWERS:\n{names}"
                print(message)
                send_telegram_notification(message)
            
            if lost_followers:
                names = "\n".join([f" {k}" for k in lost_followers])
                message = f" {TARGET_ACCOUNT} LOST FOLLOWERS:\n{names}"
                print(message)
                send_telegram_notification(message)

            if not gained_followers and not lost_followers:
                print("No changes in the follower list.")
                
            old_followers = new_followers
            
            # Destroying the current client so it forgets everything for the next iteration
            del cl_current
            
        except Exception as e:
            print(f"Error during the monitoring cycle: {e}")

if __name__ == "__main__":
    main()