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



🙏 Disclaimer
This is a basic visual-detection tool—not connected to the WhatsApp API.

It won't read or interact with messages—just monitors for any change in the screen region.

✅ To-Do / Future Ideas
Add a GUI to easily set the monitor region.

Add support for different triggers or alarms.

Smart filtering (only react to specific keywords or contacts).

📬 Feedback or Suggestions?
Feel free to open an issue or drop me a message on LinkedIn!
I'd love to hear how you'd improve it or use it differently.
