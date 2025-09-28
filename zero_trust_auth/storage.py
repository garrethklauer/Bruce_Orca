import json

def load_baseline(path="baseline.json"):
    """Load trusted baseline data from JSON file."""
    with open(path, "r") as f:
        return json.load(f)
    
def save_report(report, path="sec_report.log"):
    """"Append sec report to log file"""
    with open(path, "a") as f:
        f.write(json.dumps(report)+"\n")