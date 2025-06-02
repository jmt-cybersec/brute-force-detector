# 🛡️ Brute-Force Login Detector

A basic Python script that detects brute-force login attempts by flagging IP addresses with multiple failed login attempts.

## 🔍 What it Does
This tool parses a `logs.txt` file to identify:
- Repeated login failures from the same IP
- Signs of brute-force activity

### When to use?
- Brute-force login attacks -
A brute-force attack is when someone tries to guess the correct password
by trying as many combinations as possible, as fast as possible.
- Or a bot guessing passwords **for a single user

## 🧪 Sample Log Format
Jan 01 00:00:01 LOGIN FAIL: user=john ip=192.168.1.10
Jan 01 00:00:03 LOGIN FAIL: user=john ip=192.168.1.10
Jan 01 00:00:04 LOGIN SUCCESS: user=admin ip=192.168.1.11

** How to Run It **
1. Clone or download this repo
2. Make sure Python 3 is installed
3. Open Terminal in the project folder
4. Run: python3 scanner.py

## 🧪 Sample Output

When you run the script, you’ll see output like:
⚠️ Suspicious activity detected from IP 192.168.1.10: 2 failed logins


### 💡 What This Means:
This message tells you that the same IP address (`192.168.1.10`) has failed to log in multiple times. This is a common indicator of brute-force login attempts 
— where an attacker tries to guess a user’s password by submitting many guesses.

In a real-world environment, this could trigger:
- A firewall rule
- An automated alert to a security team
- IP blocking or throttling policies

## 🔧 Possible Next Steps

## As I'm still learning, here are a few simple ways I plan to improve this project ##
- **Make the alert limit customizable** – Instead of always checking for 2 failed logins, allow the user to choose the number.
- **Add color to the output** – Make the warning messages easier to spot in the terminal.
- **Read from different log files** – Let the user choose which log file to scan.
- **Ignore successful logins** – Only show failed ones to keep the output clean.
- **Save results to a new file** – Export the suspicious IPs to a `.txt` file for record-keeping.

These steps will help me understand Python better and make this tool more useful.

> I’m always looking to improve my code and learn more — feedback is welcome!

**🙋 About Me**
I'm currently studying Computing and Information Systems with a minor in AI/ML. I'm building small, real-world security tools to learn how Python and automation play a role in modern cybersecurity.

GitHub: [@jmt-cybersec](https://github.com/jmt-cybersec)




