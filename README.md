# 🛎️ WhatsApp Alarm Bot (Simple Python Script)

This is a lightweight Python script that watches a part of your screen (where WhatsApp messages appear) and plays an alarm sound when it detects a new message.

> It's not fancy—just a small utility that helped me stay on top of important group messages while working.

---

## 🔍 What It Does

- Monitors a region of your screen using `pyautogui`.
- Takes periodic screenshots and compares them to detect changes.
- Plays an alarm sound when a change (like a new message) is detected.

---

## 🧠 Why I Built It

I often miss WhatsApp messages on my laptop while multitasking. This little bot helps by making sure I hear an alarm whenever a new message appears in a specific group chat.

---

## 🛠️ Technologies Used

- Python 3
- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [playsound](https://pypi.org/project/playsound/)

---

## 🧾 How It Works

1. Opens WhatsApp Web or Desktop and navigates to the group chat you want to monitor.
2. Script takes a screenshot of a defined region of your screen.
3. Every few seconds, it compares a new screenshot with the previous one.
4. If there's any difference, it plays an alarm sound.

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/whatsapp-alarm-bot.git
cd whatsapp-alarm-bot


**### 2. Install dependencies**
bash
Copy
Edit
pip install pyautogui playsound

**### 3. Set up the alarm sound path**
Replace the path to the .wav file in the script with your own path:

python
Copy
Edit
alarm_sound_path = "C:\\Path\\To\\Your\\alarm.wav"

**### 4. Adjust the monitor region**
Update the coordinates in the script to match the location where messages appear on your screen:

python
Copy
Edit
monitor_region = (left, top, width, height)
Tip: Run pyautogui.displayMousePosition() in a separate script or use a screen tool to help get coordinates.

