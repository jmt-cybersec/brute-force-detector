# scanner.py - Brute Force Login Detector

failed_logins = {}

with open("logs.txt", "r") as file:
    for line in file:
        if "LOGIN FAIL" in line:
            parts = line.strip().split(" ")
            ip = parts[-1]
            failed_logins[ip] = failed_logins.get(ip, 0) + 1

for ip, count in failed_logins.items():
    if count >= 2:
        print(f"⚠️  Suspicious activity detected from IP {ip}: {count} failed logins")
