# Security Policy - SneakerBrand (Mock Company)

## Purpose & Scope
Protect customer data, payment information, and creative assets (design files). Applies to owner, employees, contractors, and third-party services.

## Key Rules / Guidelines (minimum 3)
1. **Access Control**: Unique accounts for each user, enforce MFA on all admin accounts, use role-based permissions, disable inactive accounts within 7 days.
2. **Data Protection & Classification**: Classify data as Public, Internal, Confidential. Encrypt Confidential data at rest and in transit. Collect minimum required customer data.
3. **Backup & Recovery**: Daily incremental backups, weekly full backups; keep one encrypted off-site copy. Test restores quarterly.
4. **Acceptable Use**: No unauthorized software on business devices; personal devices must follow BYOD rules and be encrypted.
5. **Incident Reporting**: Report any suspected breach immediately to the Incident Lead. Use the Incident Report template in /docs.

## Maintaining the CIA Triad
- **Confidentiality**: MFA, encryption, access controls, NDA for contractors.
- **Integrity**: Checksums for backups, write-once logs, limited modification privileges.
- **Availability**: Regular backups, redundant storage, documented recovery procedures.

## Enforcement & Review
- Violations may lead to contract termination for contractors or disciplinary actions for staff.
- Review policy annually or after any security incident.
