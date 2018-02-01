# BLE
Bluetooth Low Energy

* Also called as Bluetooth Smart
* Wireless protocol

## Advantages
* Low energy consumption

## Bluetooth Classic Vs Bluetooth Smart
* Short-Range communication
* Data Synchronization
* Help in forming a Piconet
### Bluetooth Smart
* Released in 2010
* Bluetooth Core Version 4.0
* Fast connection times 
* Efficient Power Management
### Hub Spoke (Piconet) multiple 1:1

    #---------------#       |------Device1
    #               #       |  
    #   Laptop      #--------------Device2
    #               #       |
    #---------------#       |------Device3

## What is Bluetooth Mesh?
* Formally launched in July 2017
* Blueooth Mesh capability enables many-to-many (m:m) device communications and is optimized for creating large-scale device networks.
* Bluetooth Mesh is networking technology
* Bluetooth Mesh -----------Uses---------> Bluetooth LE

### Essential characteristics of Bluetooth Mesh
* Coverage of very large areas
* "Just works interoperability"
* The ability to monitor and control large numbers of devices
* Optimized, low energy consumption
* Efficient use of radio resources, leading to scalability
* Compatibility with currently available smartphone, tablet and personal computer products
* Industry-standard, government-grade security

### Key terms and concepts on Bluetooth Mesh
* Devices which are part of a mesh network are  called `nodes` and those which are not are called `unprovisioned devices`. 
* Some nodes have multiple, constituent parts, each of which can be independently controlled. In Bluetooth
mesh terminology, these parts are called `elements`. 
* The process which transforms an unprovisioned device into a node is called `provisioning`.
* Provisioning is a secure procedure which results in an unprovisioned device possessing a series of encryption keys and being known to the Provisioner device, typically a tablet or smartphone. One of these keys is called the network key or `NetKey` for short.
* Bluetooth uses `Pub/Sub 
* Communication in the mesh network is `messageoriented` and many message types are defined, each with its own, unique opcode. Messages fall within one of two broad categories namely `acknowledged` or `unacknowledged messaging` pattern
* Devices in a Bluetooth mesh network each have a set of independent `State` values, representing some condition of the device.
* `Model` defines the specification on Device State, State Transitions, Messages and other associated behaviours.


### Mesh Network Example
![Bluetooth Mesh](https://github.com/seesiva/IoT/blob/master/Images/Bluetooth%20Wireless%20Mesh.png)

### References
* Bluetooth Blog - http://blog.bluetooth.com
