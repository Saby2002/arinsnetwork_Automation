#!/usr/bin/env python

from genie import testbed
from pprint import pprint


# Load the testbed 
testbed = testbed.load("./testbeds/external_testbed.yml")

# Select the device we want to test
device = testbed.devices["XR1"]

device.connect()

# Parse 1st command 
ip_interface_brief_output = device.parse("show ip interface brief")

pprint(ip_interface_brief_output)


# Parse 2nd command
version = device.parse("show version")
pprint(version)


