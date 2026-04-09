# Detailed Explanation – SDN Static Routing using Ryu

## 1. Introduction to SDN

Software Defined Networking (SDN) is a networking paradigm that separates the **control plane** from the **data plane**.

- **Control Plane** → decides how packets should flow (handled by controller)
- **Data Plane** → forwards packets based on rules (handled by switches)

In this project, the **Ryu controller** acts as the control plane and OpenFlow switches act as the data plane.

---

## 2. Static Routing in SDN

Static routing means that paths are **predefined manually** rather than dynamically learned.

- No routing protocols (like OSPF, RIP)
- Controller explicitly installs flow rules
- Packets follow fixed paths

In this project:
- Traffic from h1 → h2 follows a fixed path via s1 → s2
- Reverse path is also explicitly defined

---

## 3. OpenFlow and Flow Rules

Communication between controller and switches happens using the **OpenFlow protocol**.

Each switch maintains a **flow table** consisting of rules.

Each rule has:

### 1. Match
Defines conditions to match packets:
- in_port
- MAC/IP (optional)

### 2. Action
Defines what to do:
- forward to a port
- drop packet

---

## 4. Controller Logic

The controller listens for switch connections using:

- `switch_features_handler`

When a switch connects:
- Controller identifies it using **DPID (Datapath ID)**
- Installs flow rules using `add_flow()`

### Example Logic:

#### Switch s1:
- If packet comes from h1 → send to s2  
- If packet comes from s2 → send to h1  

#### Switch s2:
- If packet comes from s1 → send to h2  
- If packet comes from h2 → send to s1  

---

## 5. Packet Flow in the Network

### Forward Path:
h1 → s1 → s2 → h2

### Reverse Path:
h2 → s2 → s1 → h1

This path is fixed and controlled entirely by the controller.

---

## 6. Testing and Validation

### 1. Ping Test
- Ensures connectivity between hosts
- Result: 0% packet loss

### 2. Flow Table Inspection
- Verified using:
ovs-ofctl dump-flows s1
ovs-ofctl dump-flows s2
- Confirms that rules are installed correctly

### 3. Iperf Test
- Measures throughput between hosts
- Confirms network performance

---

## 7. Key Observations

- Switches do not learn automatically
- All decisions are made by the controller
- Flow rules directly determine packet forwarding
- Removing controller → network stops working

---

## 8. Advantages of SDN Static Routing

- Full control over network behavior
- Predictable routing paths
- Easy to debug and monitor
- Centralized management

---

## 9. Limitations

- Not scalable for large networks
- No adaptability to failures
- Requires manual configuration

---

## 10. Conclusion

This project demonstrates how SDN can be used to implement static routing using a centralized controller.

- Flow rules define complete network behavior
- Controller manages all routing decisions
- Network performance and correctness verified through testing