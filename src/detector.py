from collections import Counter


def detect_bruteforce(events, threshold=5):
    ips = [event['ip'] for event in events if event['type'] == 'failed_login']
    counts = Counter(ips)

    alerts = []

    for ip, count in counts.items():
        if count >= threshold:
            alerts.append({
                'ip': ip,
                'attempts': count,
                'alert': 'Potential brute-force attack'
            })

    return alerts
