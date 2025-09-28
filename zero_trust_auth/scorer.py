from datetime import datetime
from utils import state_timezone_map

def evaluate_signals(current, baseline):
    """Checking current values against baseline and return a trust decision"""
    reasons = []

    if current["ip"] not in baseline ["trusted_ips"]:
        reasons.append(f'ip: {current["ip"]} not trusted')

    if current["city"] not in baseline ["trusted_cities"]:
        reasons.append(f'City: {current["city"]} not trusted')

    if current["country"] not in baseline["trusted_countries"]:
        reasons.append(f'Country: {current["country"]} not trusted')

    if current["mac"] not in baseline["trusted_macs"]:
        reasons.append(f'mac adress not trusted: {current["mac"][:8]}...')

    state = current["state"]
    sys_tz = current["timezone"]

    if state in state_timezone_map:
        expected_tz = state_timezone_map[state]
        if expected_tz not in sys_tz:
            reasons.append(f'Timezone mismatch: state {state} expected {expected_tz}, system reports {sys_tz}')

    score = 100 - (len(reasons)*30)
    score = max(score, 0)

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "status":"Granted" if not reasons else "Denied",
        "score": score,
        "reasons": reasons
    }
