# python-raspi-uart

Small wrapper of the pyserial library to use with the raspberry pi. UART in raspi 3 model B is available at `/dev/ttyS0`. However serial login terminal must be disabled in the kernel options before using `/dev/ttyS0` device file.

UART Pins are:
* GND: Pin  6
* TXD: Pin  8 or GPIO14
* RXD: Pin 10 or GPIO15

https://github.com/JVGD/python-raspi-uart/blob/master/readme/Raspi_pinout.png
![Raspi pinout](https://github.com/JVGD/python-raspi-uart/blob/master/readme/Raspi_pinout.png "Raspi pinout")


Quick usage example would be:

```python
import uart

# Getting an UART with default conf:
#   'devicefile':'/dev/ttyS0', 
#   'baudrate': '9600',
#   'timeout': 25
u = uart.Uart()

# Send characters over UART with new
# line at the end
u.sendn("raspi: Hi buddy!")

# Receive data over UART till new line
# character
rx = u.readline()
print rx
```
