# Key considerations

## References
https://iotsecurityfoundation.org/wp-content/uploads/2016/12/IoT-Security-Compliance-Framework.pdf

## Data & Privacy
* Communication on what data is being collected to the end users
* Management of encryption keys in a secure way
* No sensitive information is exposed
* Accurate timestamping of data


## Hardware
* Never using devices with default passwords.
* Keep updating the firmware for the latest patch
* All communications port(s), such as USB, RS232 etc., which are not used as part of the product’s normal operation are not physically accessible or are secured on the production devices. 
* The product's processor system has an irrevocable hardware secure boot process.
* Any debug interface, for example related I/O port(s) such as JTAG, is secured on the production devices.

### Firmware Application
* Where remote software upgrade can be supported by the device, when vulnerabilities are discovered, the software fix for the device is promptly made available.
* Where remote software upgrade can be supported by the device, the software images are digitally signed by an authorised trust entity.
* The product has measures to prevent unauthenticated software and files being loaded onto it. In the event that the product is intended to allow un-authenticated software, such software should only be run with limited permissions and/or sandbox
* A software update package has its digital signature, signing certificate and signing certificate chain, verified by the device before the update process begins.
* 

### PKI Signature Adoption
Ideal for:
* Embedded devices
* Resource constrained devices
* Microcontroller based devices with flash/firmware
* Any IoT device that needs to make their own KeyScaler calls for security operations 