import csv
import re
import json
import argparse
from collections import defaultdict 
from colorama import Fore, Style, init
from datetime import datetime, timedelta
import streamlit as st 
import pandas as pd 

st.set_page_config(page_title="Brute-Force Attack Detector", layout="centered")
st.title("Brute-Force Attack Detector")
st.markdown("Upload an SSH log file(e.g., `/var/log/auth.log`) to detect repeated failed login attempts.")

#Upload section 
uploaded_file = st.file_uploader("Upload Lop File", type=["log", "txt"])
threshold = st.slider("Failed attempt threshold", 1, 20, 5)
window = st.slider("Time window (in seconds)", 30, 600 ,60)

#def parser function 
def parse_log(file, threshold, window):
    failures = defaultdict(list)
    flagged_ips = {}
    for line in file:
        decoded = line.decode("utf-8")
        match = re.search(
            r'^(?P<timestamp>\w{3}\s+\d+\s[\d:]+).*Failed password.*from (?P<ip>\d+\.\d+\.\d+\.\d+)', decoded 
        )
        if match:
            ip = match.group("ip")
            timestamp_str = match.group("timestamp")
            current_year = datetime.now().year
            try:
                timestamp = datetime.strptime(f"{current_year} {timestamp_str}", "%Y %b %d %H:%M:%S")
                failures[ip].append(timestamp)
            except ValueError:
                continue

    for ip, timestamps in failures.items():
        timestamps.sort()
        for i in range(len(timestamps)):
            count = 1 
            for j in range(i+1, len(timestamps)):
                if (timestamps[j] - timestamps[i]).total_seconds() <= window:
                    count += 1
                else:
                    break
            if count > threshold:
                flagged_ips[ip] = count
                break
    return flagged_ips
# When file is uploaded, process and display
if uploaded_file:
    results = parse_log(uploaded_file, threshold, window)
    if results:
        st.success(f"Detected {len(results)} suspicious IP9s)!")
        df = pd.DataFrame(list(results.items()), columns=["IP Address", "Failed Attempts"])
        st.dataframe(df)

        #Export buttons
        st.download_button("Download CSV", df.to_csv(index=False), file_name="suspicious_ips.csv", mime="text/csv")
        st.download_button("Download JSON", df.to_json(indent=4), file_name="suspicious_ips.json",mime="application/json")
    else:
        st.info("No suspicious activity found based on the selected threshold and time window.")