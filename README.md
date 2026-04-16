# SDN Static Routing using Ryu Controller

**Name:** Shreya Shenoy  
**SRN:** PES2UG24CS487  
**Subject:** CN ORANGE PROBLEM  
**Question:** 4  

---

## Problem Statement
Implement static routing using SDN controller by installing flow rules manually.

---

## Setup
`sudo apt install mininet`  
`pip3 install ryu` 

---

## Run
`ryu-manager controller/static_controller.py`  

`sudo mn --custom topology/topo.py --topo static --controller remote` 

---

## Expected Output
- Hosts can ping each other  
- Flow rules installed in switches  
- Static path followed  

---

## Testing
- pingall → checks connectivity between hosts  
- iperf → measures throughput  
- flow table inspection → verifies match-action rules  

---

## Results

### 1. Controller Initialization & Switch Connection

When the Ryu controller is started, it waits for switches to connect. Once Mininet is launched, switches establish a connection with the controller. This confirms proper interaction between the **control plane (controller)** and **data plane (switches)**.

![Controller Output](results/controller_output.png)

---

### 2. Topology Verification

The `nodes` command in Mininet shows all devices in the network.  
Here, we observe:
- 2 hosts → h1, h2  
- 2 switches → s1, s2  

This confirms that the intended topology has been created correctly.

![Topology Nodes](results/nodes.png)

---

### 3. Connectivity Test (Ping)

The `pingall` command checks connectivity between all hosts in the network.  
The result shows **0% packet loss**, meaning:
- packets are successfully forwarded  
- routing path is correctly implemented  

This validates that the static flow rules are working as expected.

![Ping Output](results/ping.png)

---

### 4. Flow Table Inspection (Core of Static Routing)

Flow tables define how packets are handled by switches. These rules are installed by the controller.

#### Switch s1:
- Packets entering from host (in_port=1) are forwarded to switch s2 (port 2)  
- Packets coming back are sent to host h1  

![Flow Table s1](results/flows_s1.png)

#### Switch s2:
- Packets from s1 are forwarded to host h2  
- Reverse traffic is sent back to s1  

![Flow Table s2](results/flow_s2.png)

These entries clearly demonstrate **match-action rules**, where:
- match → input port  
- action → output port  

This confirms that routing is **static**, not dynamically learned.

---
The `iperf` tool is used to measure throughput between hosts.  
The output shows successful connection and data transfer between h1 and h2.

This proves that:
- network is not only connected  
- but also capable of handling data transfer efficiently  

![Iperf Output](results/iperf.png)

---
### 6. Failure Scenario (Without Controller)

When the controller is not running, switches do not have any flow rules installed. As a result, packets cannot be forwarded between hosts.

This demonstrates that the network behavior is completely dependent on the SDN controller.

![Failure Ping](results/failure_ping.png)
---

## Commands Executed

### 1. Clone Repository
```bash
cd ~/Desktop
git clone https://github.com/shenoyshree22/sdn-static-routing.git
cd sdn-static-routing
### 5. Performance Testing (iperf)
```
### 2.Install Dependencies
```bash
sudo apt update
sudo apt install python3-pip mininet -y
pip3 install ryu
```
### 3.Fix Ryu Dependency Issue (for my VM due to compatibility)
```bash
pip3 uninstall eventlet -y
pip3 install eventlet==0.30.2
pip3 install greenlet==1.1.3
```
### 4. in terminal 1, Run Ryu Controller
```bash
ryu-manager controller/static_controller.py
```
### 5. in terminal 2, Run Mininet Topology
```bash
sudo mn --custom topology/topo.py --topo static --controller remote
```
### 6. Testing Commands (Inside Mininet)
```bash
nodes
pingall
sh ovs-ofctl dump-flows s1
sh ovs-ofctl dump-flows s2
h2 iperf -s &
h1 iperf -c h2
```
### 7. (EXTRA) faiure scenario, by stopping the Run Ryu Controller
```bash
just pressing Ctrl + C
```
cleaning previous instances
```bash
sudo mn -c
```
and running mininet again ,
```bash
sudo mn --custom topology/topo.py --topo static --controller remote
```
now test connectivity only to get ping failing cause of flow rules
```bash
pingall
```
---

## Explanation

- SDN separates control and data planes  
- The controller installs flow rules in switches  
- Switches follow these rules instead of making independent decisions  
- No routing protocol is used → all paths are predefined  
- This is called **static routing using SDN**

---

## Conclusion

- Static routing successfully implemented using Ryu controller  
- Flow rules correctly define packet forwarding paths  
- Network connectivity verified using ping  
- Flow tables confirm controller-based routing  
- Performance validated using iperf  

---

## Results Folder
Screenshots are also available in the `results` folder for reference.
