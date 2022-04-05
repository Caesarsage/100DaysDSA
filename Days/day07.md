# COMPUTER NETWORKING

The internet is a collection of computer networks

## How it started - The internet

US Set up the ARPA (Advance research program agency) for researching new for technology.

ARPA developed the ARPANET for them to communicate with each other. ARPANET was in MIT, Stanford, Utah and VC LA. They used
TCP/IP protocol to make this communication possible.

First web site had just hyperlinks and no search engines , etc.

## Protocols

Rules for communicating between two or more computers. The internet society create these rules.

TCP helps send data to reach it desired destination and consider its reach
UDP (user datagram protocol) to send data without considering if its reach everyone e.g video conferencing.
HTTP used by web browser, that define the format of data transfer between client and servers

IP Address are unique code used to identify websites. e.g X.X.X.X and each X has number 0 to 225. Ip address are used to determine where your application are located.

PORT No are used to determine which application you ae using to communicate/ it is 16bit.

Internet are connected together deep underground with fibre cables connecting thw world together.

$ curl ip config/all -s : get the ip address of your internet provider

- LAN (local area network) : for small area connection of computers through ethernets, wifi
- MAN (Metropolitan area network): for across the city
- WAN (wide area network): Across countries using optical fibre cables
- Frame relay : Help connect LAN to WAN
  
Internet Service Provider (ISP)

## OSI MODEL

- Application layer - This is implemented in software and users interact with it e.g browsers
- Presentation layer - Converts data (in character, numbers, files, etc) to machine representable binary format, its encrypt data, provide abstraction, compressed data
- Session layer - Helps in setting up and managing up connections and enables sending and receiving of data, Authentication, Authorization
- Transport layer - Transfer data through (1) segmentation with port no, destination source and sequence no(for reassembling) , (2) Flow control to control amount of data being transport (3) Error control.
- Network layer - Works for the transmission of the received data segment from one computer to another that is located in a diff network. This is where you find the routers. It helps in logical addressing through sender/Receiver IP assigning forming an IP packet so data reach destination.
- Data link layer - Allows to directly communicate with computers and host. Perform two function, controls are data are control form the media and add mask address
- Physical layer - Contains the hardware

### How the OSI MODEL WORKS - sending data to your friend

Send data from Application layer to presentation layer then to session layer and to transport layer which make it into packets and segments and then to network layer which assign the Ip addresses and then to the Data link layer which assign the mask addresses and send to the physical router. The physical router send the data to the physical layer of your friend and moves all, from data link to application layer of your friend.

TCP/IP MODEL

This is the internet protocol suite and layer reduces

- Application layer
- Transport layer
- Network layer
- Data link
- Physical

# DEEP DIVE INTO EACH LAYER

## Application layer

- user interaction
- WhatsApp, browsers, etc
- where : devices
- protocols
- client - server architecture (request and response)
  - P2P , Peer to  peer communication e.g bittorrent

### Protocols.

- web protocols:
  - TCP/IP
    - HTTP : Client - Server architecture (request and response), it uses TCP. it does not store any information about the user info. it is a stateless protocol
    - DHIP
    - FTP (file transfer protocol)
    - SMTP : sending emails etc
    - POP3 or IMAC : for receiving emails
    - SSH
    - VNC (Virtual Network computing)
  - Telnet (enable user to manage an account or device remotely. Very low level): port 23
  - UDP : stateless connection

- Sockets :Used for messaging between devices
- Ports :Tells us which device we are working with.
  - Ephemeral ports exist on client side only
