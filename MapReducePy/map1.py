#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    if len(parts) == 5:
        timestamp, instance_type, os, az, price = parts
        # Composite key: instance type + OS + availability zone
        composite_key = "%s,%s,%s" % (instance_type, os, az)
        print '%s\t%s' % (composite_key, price)
