# Incident Response Playbook - SneakerBrand (Mock Company)

## Roles & Contacts
- Incident Lead: __________________ (Name, phone, email)
- External IT / Forensics: __________________
- E-commerce Platform Support: (Shopify/Square/etc.)

## Detection Methods (at least one)
- **Automated Log Monitoring**: Scripts or lightweight collectors that parse auth logs, webapp logs, and payment events and generate alerts (see /log_parser.py).
- **User Reports**: Staff or customers reporting suspicious emails, charges, or behavior.
- **Endpoint Alerts**: Antivirus/EDR alerts on workstations.

## Incident Handling Phases
1. **Prepare**: Backups, contact list, baseline configurations, and mock-data environment.
2. **Detect & Analyze**: Correlate alerts (logs, endpoint, user reports). Create event timeline and classify severity.
3. **Contain**:
   - Short-term: Isolate affected host (remove network access), disable compromised accounts, block malicious IPs.
   - Long-term: Apply firewall rules, segment vulnerable networks.
4. **Eradicate**: Remove malware, close exploited vectors (patch, replace keys), and verify system cleanliness.
5. **Recover**: Restore from clean backups, validate integrity, return services to production cautiously while monitoring.
6. **Lessons Learned**: Post-incident review and update policies and playbooks.

## Evidence Preservation & Chain of Custody (brief)
- Capture disk images with `dd` and calculate SHA256 hashes.
- Preserve logs (copy original files + checksums) and network captures (pcap) with timestamps.
- Maintain a chain-of-custody form recording who handled evidence, when, and actions performed.

## Sample Playbooks (by incident type)
### A. Ransomware / Malware
- Detect: AV quarantine alert, ransom note in logs.
- Contain: Isolate host, power off if needed, block attacker IPs.
- Eradicate: Run AV, remove malicious binaries, patch exploited services.
- Recover: Restore design files from encrypted backups; validate checksums.
- Notify: Follow CT breach notification rules if personal data was exposed.

### B. Brute-force / Unauthorized Access
- Detect: Repeated failed login alerts, new admin user creation.
- Contain: Block source IPs, rotate credentials, enforce MFA.
- Eradicate: Harden authentication (disable password auth for SSH; use keys), install fail2ban.
- Recover: Review logs for lateral movement; restore integrity of affected systems.

### C. Payment Fraud / High-Value Order Fraud
- Detect: High-value orders, multiple orders from same IP, charge disputes.
- Contain: Pause suspicious orders, flag account, notify payment processor.
- Eradicate: Revoke compromised API keys, rotate credentials.
- Recover: Reconcile financials, notify affected customers per legal requirements.

## Severity Matrix (example)
- **Critical**: Ransomware encrypting customer data or systems, confirmed data exfiltration.
- **High**: Multiple unauthorized access events, large-scale DoS, high-value fraud in progress.
- **Medium**: Single compromised workstation, phishing click with no credential theft confirmed.
- **Low**: Minor policy violations, non-sensitive data exposed briefly.

