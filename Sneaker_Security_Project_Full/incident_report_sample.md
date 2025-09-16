# Incident Report - Sample Event
**Incident ID:** INC-20250916-001
**Date/Time Detected:** 2025-09-16T18:17:26.237509Z
**Detected By:** Automated log parser
**Incident Type:** Brute-force SSH + Ransomware note detected (correlated)
**Affected Assets:** host1 (design workstation), webapp orders
**Summary:** Multiple failed SSH login attempts from IP 203.0.113.5 followed by a ransom note detected in system logs and antivirus malware quarantine event.
**Detection Evidence:** See fake_logs.txt lines with failed logins and ransom note; alerts.txt produced by parser.
**Containment Actions Taken:** 
- Isolated host1 from network (disabled network interface in VM snapshot)
- Revoked user credentials and reset admin passwords
- Stopped web services temporarily to prevent further spread
**Eradication Steps:** 
- Performed AV scan and quarantined malicious files (as noted in logs)
- Removed suspicious binaries and patched vulnerable services
**Recovery Steps:** 
- Restored design files from encrypted off-site backup (verified integrity)
- Monitored systems for 14 days for reoccurrence
**Notification:** Notified affected customers per CT breach notification guidance (mock data)
**Root Cause (preliminary):** Weak/older SSH credentials exposed to brute-force; lack of network segmentation allowed attacker to reach sensitive host.
**Lessons Learned / Recommendations:** 
- Enforce MFA for all admin access
- Implement network segmentation for design workstations
- Harden SSH (disable password auth, use keys) and implement fail2ban
