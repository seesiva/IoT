# IoT Platforms

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