# Bluetooth Connectivity with Linux (Ubuntu)
The experiments made with Bluetooth with Raspberry PI

## Step - 1: Bluetooth necessary updates
'''
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install bluetooth
sudo apt-get install bluez
sudo apt-get install python-bluez
'''

## Step -2: Enable bluetooth in control mode
'''
sudo bluetoothctl
agent on
default-agent
'''

## Step-3: Scan for bluetooth devices
'''
scan on 
'''

## Step-4: Pair the devices which you would like to pair upon
'''
pair <<Bluetooth Device MacID>>
'''
Example:
pair E0:DD:C0:F1:E8:02

It will check for pair confirmation with a 6 digit number on the both the devices which needs to be acknowledged. After this the service will be resolved and pairing status would be yes against the Mac ID.

## Step-5: Use the connected device to play with GATT Attributes
Handling of GATT Attributes can be dealt through select-attribute commands.
