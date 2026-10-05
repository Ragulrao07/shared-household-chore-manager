import time
import subprocess
import requests

PROMETHEUS_ALERTS_URL = "http://localhost:9090/api/v1/alerts"

def check_active_alerts():
    try:
        response = requests.get(PROMETHEUS_ALERTS_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        alerts = data.get("data", {}).get("alerts", [])
        firing = [a for a in alerts if a.get("state") == "firing"]
        return firing
    except Exception as e:
        print(f"Error querying Prometheus alerts: {e}")
        return []

def run_on_call_agent(alert):
    alert_name = alert.get("labels", {}).get("alertname", "UnknownAlert")
    summary = alert.get("annotations", {}).get("summary", "")
    description = alert.get("annotations", {}).get("description", "")
    env = alert.get("labels", {}).get("environment", "dev")

    print(f"\n🚨 [ALERT FIRING] {alert_name} in {env}!")
    print(f"Details: {summary} - {description}")
    print("Initiating headless on-call engineer session...\n")

    prompt = (
        f"You are the on-call engineer for this repository. An alert just fired: {alert_name} in {env}.\n"
        f"Alert description: {description}\n"
        "Investigate the root cause in chores/views.py. Reproduce the error.\n"
        "Make the smallest correction to fix the failure, run `python manage.py test`, "
        "and commit the fix with message: 'fix(on-call): resolve chore creation failure'."
    )

    # Launch headless aider session
    cmd = ["aider", "--message", prompt, "--yes"]
    try:
        subprocess.run(cmd, check=True)
        print("✅ On-call incident resolved and fix committed.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Automated remediation failed: {e}")

def main():
    print("🤖 AI On-Call Responder active. Monitoring Prometheus alert feed every 15s...")
    while True:
        firing_alerts = check_active_alerts()
        if firing_alerts:
            for alert in firing_alerts:
                run_on_call_agent(alert)
                time.sleep(60)  # Cool down after handling
        time.sleep(15)

if __name__ == "__main__":
    main()
