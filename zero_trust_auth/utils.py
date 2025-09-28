import uuid
import hashlib
import time

state_timezone_map = {
# est
        "VA": "EST", "NC": "EST", "NY": "EST", "FL": "EST", "GA": "EST", "PA": "EST",
# cnt
        "TX": "CST", "IL": "CST", "TN": "CST", "AL": "CST", "WI": "CST",
# mtn
        "CO": "MST", "UT": "MST", "AZ": "MST", "NM": "MST",
# pacifc
        "CA": "PST", "WA": "PST", "OR": "PST", "NV": "PST",
}

def get_mac_hash():
    """"Getting mac address"""
    mac = uuid.getnode()
    mac_str = ":".join([f"{(mac >> ele) & 0xff:02x}" for ele in range(40, -8, -8)])
    return hashlib.sha256(mac_str.encode()).hexdigest()

def get_system_timezone():
    return time.tzname[0]
