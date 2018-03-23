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