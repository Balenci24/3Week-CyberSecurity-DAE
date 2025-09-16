#!/usr/bin/env python3
# Simple log parser (demo) - detects brute-force SSH, high-value orders, ransomware notes, DoS
import re, json, datetime, sys

def parse(logfile):
    failed_login_pattern = re.compile(r"Failed password .* from (?P<ip>\\d+\\.\\d+\\.\\d+\\.\\d+)")
    order_pattern = re.compile(r"New order .* amount=(?P<amount>[\\d\\.]+).*ip=(?P<ip>\\d+\\.\\d+\\.\\d+\\.\\d+)")
    refund_pattern = re.compile(r"Refund request .* amount=(?P<amount>[\\d\\.]+).*")
    ransomware_pattern = re.compile(r"ransomware|All your .* encrypted|Contact attacker", re.IGNORECASE)
    dos_pattern = re.compile(r"DoS|requests in \d+s from (?P<ip>\\d+\\.\\d+\\.\\d+\\.\\d+)", re.IGNORECASE)

    failed_logins = {}
    alerts = []

    with open(logfile, 'r') as fh:
        for line in fh:
            line=line.strip()
            try:
                mtime = line.split('Z')[0]+'Z'
                ts = datetime.datetime.fromisoformat(mtime.replace('Z',''))
            except:
                ts = None
            m = failed_login_pattern.search(line)
            if m:
                ip = m.group('ip')
                failed_logins.setdefault(ip, []).append(ts)
                recent = [t for t in failed_logins[ip] if (ts - t).total_seconds() <= 300]
                if len(recent) >= 3:
                    alerts.append({'type':'Brute-Force Login','ip':ip,'count':len(recent),'time':ts.isoformat()})
            m2 = order_pattern.search(line)
            if m2:
                amount = float(m2.group('amount')); ip = m2.group('ip')
                if amount > 1000.0:
                    alerts.append({'type':'High-Value Order','ip':ip,'amount':amount,'time':ts.isoformat()})
            if ransomware_pattern.search(line):
                alerts.append({'type':'Ransomware Message Detected','line':line,'time':ts.isoformat()})
            m4 = dos_pattern.search(line)
            if m4:
                ip = m4.group('ip') if m4.groupdict().get('ip') else 'unknown'
                alerts.append({'type':'Possible DoS','ip':ip,'time':ts.isoformat()})
    return alerts

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: log_parser.py <logfile>')
        sys.exit(1)
    alerts = parse(sys.argv[1])
    for a in alerts:
        print(json.dumps(a))
