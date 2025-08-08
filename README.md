# 🐍 Internet Speed Complaint Bot

This Python script automates the process of checking your internet speed and tweeting a complaint to your internet service provider if the speed is below a promised threshold. It uses Selenium WebDriver to interact with [Speedtest.net](https://www.speedtest.net/) and [X (formerly Twitter)](https://x.com), and is configured to run with the Brave browser.

---

## 🚀 Features

- Automatically launches Brave browser and runs a speed test
- Extracts download and upload speeds from Speedtest.net
- Logs into X using credentials stored in environment variables
- Posts a tweet complaining about slow internet speeds

---

## 🛠️ Technologies Used

- **Python 3**
- **Selenium WebDriver** for browser automation
- **Brave Browser** as the Chromium-based browser
- **Pyperclip** for clipboard operations
- **dotenv** for secure environment variable management

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install selenium python-dotenv pyperclip
