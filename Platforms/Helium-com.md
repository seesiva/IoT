# Helium

## About 
* Name: Helium.com
* Website: www.helium.com
* Platform: Combination of Hardware and Software
## Key Features
* Device Management
* Secure Communications
* OTA Firmware Update
* Real-Time Events

## Architecture
                        -----------------               -----------------
                        |   Device      |               |   Device      |
                        |   Helium Aotm |               |   Helium Aotm |                      
                        -----------------               -----------------  
                                |                               |                                
                        -------------------------------------------------
                        |                   802.15.4                    |                                   
                        -------------------------------------------------
                                                |
                        -------------------------------------------------
                        |                   Helium Element              |                                   
                        -------------------------------------------------
                            Ethernet Backhaul| TCP over TLS | Cellular
                        -------------------------------------------------
                                                |
                         -------------------------------------------------
                        |            Helium Cloud Router                 |                                   
                        --------------------------------------------------
                        |                   Dashboard                    |                                   
                        --------------------------------------------------
                        |                   Channels                     |                                   
                        --------------------------------------------------  
                                                |
                                                |
                                                |
                        --------------------------------------------------
                        |   ------------------      ----------------      |
                        |   | Cloud Platform |      |Cloud Platform|      |
                        |   ------------------      ----------------      |
                        |          Business Application/Service           |
                        --------------------------------------------------

## Technical Features
* Protocol: MQTT & HTTP
* Integerated with AWS IoT Platform

## Essential benefits
* Ability to connect to different channels like (Google IoT, AWS IoT)
* Channel Variables and 
* Configurtion variables help switch between channels which is good in case of need for replicating data for mission critical systems across different channels
* Need to extend the data points through the Channels and we might need to build application on top of it

# Hardware Availability
* Through Distributors https://www.mouser.com/new/helium/helium-starter-kits/
## Risks
* What if one the channels are not allowed to operate on this model

## Reference Use cases
Meeting room occupancy - https://www.hackster.io/64742/people-counting-with-helium-grid-eye-and-raspberry-pi-49f601
