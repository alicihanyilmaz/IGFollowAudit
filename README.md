# IGFollowAudit

## Overview

IGFollowAudit is an automated Python script designed to monitor an Instagram account's follower count continuously. It accurately detects when the target account gains new followers or loses existing ones, and instantly sends detailed alert messages via a Telegram bot.

By utilizing a `sessionid` token for authentication and a unique memory-clearing approach (creating a fresh client instance per cycle), this script bypasses common API caching issues and ensures the follower data is always accurate and up-to-date.

## Features

* **Real-Time Telegram Alerts:** Get instant notifications directly to your Telegram chat whenever someone follows or unfollows the target account.
* **SessionID Login:** Bypasses basic Instagram login security and 2FA prompts by using an existing browser session cookie.
* **Anti-Cache Mechanism:** Safely deletes and recreates the Instagram client in every loop to prevent fetching outdated or cached follower lists.
* **Cloud-Ready:** Lightweight architecture allows it to be easily deployed on free Python hosting environments for uninterrupted 24/7 operation.

## Prerequisites

* Python 3.x
* `instagrapi` library
* `requests` library

You can install the required dependencies using pip:

```bash
pip install instagrapi requests

```

## Configuration

Before running the script, open the Python file and update the variables in the `# --- SETTINGS ---` section with your specific details:

* `TELEGRAM_TOKEN`: Your Telegram Bot API token (obtained from @BotFather).
* `CHAT_ID`: Your personal Telegram Chat ID where you want to receive notifications.
* `TARGET_ACCOUNT`: The Instagram username you want to monitor (e.g., `"ylmzacihan"`).
* `INSTA_SESSION_ID`: Your Instagram account's `sessionid` cookie. You can find this by logging into Instagram on your browser, opening Developer Tools (F12), and navigating to Application > Cookies.

## ⚠️ Crucial Anti-Ban Warning (Must Read)

Instagram has strict rate limits to prevent bot activity. To ensure your account is not flagged, restricted, or banned by Instagram, **you must set the `time.sleep()` value to `1800` (which equals 30 minutes)** in the main loop.

```python
# Correct configuration for safe, long-term tracking
time.sleep(1800) 

```

*Note: Do not leave this value at 60 seconds (1 minute) for continuous use. Aggressive API requests will inevitably lead to an action block or account suspension.*

## Running 24/7 for Free

You do not need to keep your personal computer running to use this script. IGFollowAudit is designed to run autonomously in the background.

You can deploy this code on any free Python execution platform or cloud runner (such as **PythonAnywhere**, **Replit**, or even a basic server/Raspberry Pi setup). Simply upload the script to the cloud environment, install the requirements, and run it. The bot will continuously monitor the account 24/7 without any further input.
