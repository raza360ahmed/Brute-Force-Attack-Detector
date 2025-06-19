README.md
# 🛡️ Brute-Force Attack Detector

A Python-based tool (with both **Streamlit GUI** and **command-line interface**) to detect brute-force SSH login attempts from log files such as `/var/log/auth.log`.

## 🔍 Features

- Upload SSH logs via GUI or command line
- Detect repeated failed login attempts
- Customize detection threshold and time window
- Output results as CSV or JSON
- Highlights suspicious IPs with timestamp and attempted username
- Colorized terminal output for CLI
- Ready for SOC analysts and cybersecurity projects

---

## 📦 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/brute-force-detector.git
cd brute-force-detector
pip install -r requirements.txt
🚀 Usage
✅ GUI Mode (Streamlit)

streamlit run detector.py
Upload .log or .txt files

Customize detection settings

Export results

🖥️ CLI Mode
python detector.py --file auth.log --threshold 5 --window 60
Automatically detects brute-force attempts

Colorized terminal output

📁 Project Structure
brute-force-detector/
├── detector.py
├── auth.log            # (sample)
├── README.md
├── .gitignore
├── requirements.txt
🧪 Sample Log File
Use the included auth.log file for testing or point it to your server's /var/log/auth.log