Sneaker Security Project - Artifacts
===================================

Files produced (path: /mnt/data/sneaker_security_project):
- mock_data_customers.csv : Sample fake customer CSV for mock data handling
- fake_logs.txt : Simulated logs covering failed logins, high-value order, refund, malware, ransom note, DoS
- alerts.txt : Alerts produced by a simple log parser scanning fake_logs.txt
- encryption_demo.txt : Demonstration of AES-256-CBC via OpenSSL + SHA256/MD5 hashes (if OpenSSL available)
- incident_report_sample.md : Filled sample incident report walking through detection, containment, eradication, recovery
- README_Project_Artifacts.md : (this file) mapping and quick instructions

Notes:
- If OpenSSL is not available in your environment, replace the encryption demo with Python 'cryptography' Fernet or run openssl locally.
- These artifacts are mock data for an academic project and do NOT contain real personal data.

