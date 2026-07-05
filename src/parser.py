import re


def parse_log_file(log_file):
    events = []

    with open(log_file, 'r', encoding='utf-8') as file:
        for line in file:
            if 'Failed password' in line:
                ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if ip_match:
                    events.append({
                        'type': 'failed_login',
                        'ip': ip_match.group(1),
                        'raw': line.strip()
                    })

    return events
