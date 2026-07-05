import sys
from parser import parse_log_file
from detector import detect_bruteforce
from reporter import generate_report


def main():
    if len(sys.argv) < 2:
        print('Usage: python main.py <logfile>')
        return

    logfile = sys.argv[1]

    events = parse_log_file(logfile)
    alerts = detect_bruteforce(events)
    report = generate_report(events, alerts)

    print('\n=== Security Report ===')
    print(f"Failed Logins: {report['failed_logins']}")
    print(f"Alerts: {len(report['alerts'])}")

    for alert in report['alerts']:
        print(f"[!] {alert['ip']} -> {alert['attempts']} attempts")


if __name__ == '__main__':
    main()
