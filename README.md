# SDN Static Routing using Ryu Controller

## Problem Statement
Implement static routing using SDN controller by installing flow rules manually.

## Setup
sudo apt install mininet
pip3 install ryu

## Run
ryu-manager controller/static_controller.py

sudo mn --custom topology/topo.py --topo static --controller remote

## Expected Output
- Hosts can ping each other
- Flow rules installed in switches
- Static path followed

## Testing
- pingall
- iperf
- flow table inspection

## Results
(screenshots attached below & also check results folder)