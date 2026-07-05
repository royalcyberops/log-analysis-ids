import json


def generate_report(events, alerts, output_file='reports/report.json'):
    report = {
        'failed_logins': len(events),
        'alerts': alerts
    }

    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(report, file, indent=4)

    html = f'''<html><body><h1>Security Report</h1><p>Failed Logins: {len(events)}</p><p>Alerts: {len(alerts)}</p></body></html>'''

    with open('reports/report.html', 'w', encoding='utf-8') as file:
        file.write(html)

    return report
