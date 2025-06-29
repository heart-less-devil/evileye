# EvilEye

**DISCLAIMER: This tool is for educational and research purposes only. Do not use it to harass, spam, or attack others. Misuse may be illegal and can result in severe consequences.**

## Description

EvilEye is a Python script that automates reporting and login attempts against a specified Instagram account using multiple threads and proxies. It is intended for research and educational purposes only.

## Features
- Automated reporting of a target Instagram account
- Simulated login attempts (login flood)
- Multi-threaded execution
- Proxy support

## Requirements
- Python 3.x
- `requests` library
- `fake-useragent` library

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/evileye.git
   cd evileye
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Configuration

Edit the `config.json` file with your desired settings. Example:

```json
{
  "target_account": "target_username_or_id",
  "report_count": 10,
  "threads": 3,
  "proxies": [
    "http://proxy1:port",
    "http://proxy2:port"
  ]
}
```

- `target_account`: The username or ID of the Instagram account to target.
- `report_count`: Number of report attempts.
- `threads`: Number of threads to use per report batch.
- `proxies`: List of proxy addresses to use.

## Usage

Run the script with:
```sh
python evileye.py
```

## Legal & Ethical Notice
- This tool is for educational and authorized research only.
- Do not use it to attack, harass, or spam others.
- The author is not responsible for any misuse. 