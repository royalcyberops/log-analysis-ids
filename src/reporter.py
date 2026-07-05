import json


def generate_report(events, alerts, output_file='reports/report.json'):
    report = {
        'failed_logins': len(events),
        'alerts': alerts
    }

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(report, file, indent=4)

    return report
