# fldigi-ssdv
![image](https://github.com/radio-satellites/fldigi-ssdv/assets/114111180/a6bf4339-c8ea-4ded-83b4-ce99668473e5)

Transmit SSDV images over HF using *any* mode in fldigi!

# Running
You'll need the SSDV binary in the directory (see https://github.com/fsphil/ssdv). Clone the directory, and run make. 

# Sending images

You will need to run "ssdv -e encoded.jpg output.bin" first in order to encode the image (output.bin is a must). Then, you'll need to start the script send.py to transmit them to fldigi (which also needs to be running!). 

# Receiving images

IT SHOULD BE KNOWN that currently, there's no syncword correlation... so the packet start and end flags MUST be received for a good packet. 

Run rx.py (with fldigi running), and wait for imagery. Once it starts coming, click showimagery.py for a live preview. 

