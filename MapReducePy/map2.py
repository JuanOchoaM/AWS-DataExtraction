#!/usr/bin/env python
import sys
from datetime import datetime

def parse_date(timestamp):
    return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S+00:00")

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) == 5:
        timestamp, instance_type, os, az, price = parts
        if os == "Linux/UNIX" and az.startswith("eu-central-1"):
            try:
                hour = parse_date(timestamp).hour
                if 9 <= hour < 17:
                    hour_str = parse_date(timestamp).strftime("%H:00")
                    print('%s,%s,%s\t%s,%s' % (instance_type, os, az, hour_str, price))
            except ValueError:
                continue
