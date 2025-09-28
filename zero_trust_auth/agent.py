# The goal of this script is to help varify the authenticy of users ip addresses, for our zero-trust authenticator.
import os
import geocoder
import time

from scorer import evaluate_signals
from storage import load_baseline, save_report
from utils import get_mac_hash, get_system_timezone
from alerts import send_slack_alert

slack_token = os.gentev("slack_bot_token")
slack_channel = "#security-alerts"

def get_current_vars():
    """Fetching network and system info..."""
    g = geocoder.ip("me")
    return{
        "ip": g.ip,
        "city": g.json.get("city"),
        "state": g.json.get("state"),
        "country": g.json.get("country"),
        "mac" : get_mac_hash(),
        "timezone": get_system_timezone()
    }

def main():
    baseline = load_baseline()
    suspect_var = 0
    
    current = get_current_vars()
    report = evaluate_signals(current, baseline)
    save_report(report)
    print(report)

    if report["status"] == "Denied":
        return
    
    snapshot = current
    while report["status"] == "Granted":
        time.sleep(60)
        updated = get_current_vars()

        if snapshot != updated:
            print("Changed Enviornment")

            if snapshot["ip"] != updated["ip"]:
                print(f'ip changed:{snapshot["ip"]} --> {updated["ip"]}')
                suspect_var +=1

            if snapshot["city"] != updated["city"]:
                print(f'City changed:{snapshot["city"]} --> {updated["city"]}')
                suspect_var +=1

            report = evaluate_signals(updated, baseline)
            save_report(report)
            print(report)

            if report["score"]< 50:
                if slack_token:
                    send_slack_alert(slack_token, slack_channel, f"low trust score dedicted: {report}")
            else:
                print("Cannot send alert, no slack token set.")
            print("Locking session, trust score too low")
            break

            snapshot = updated

if __name__ == "__main__":
    main()
