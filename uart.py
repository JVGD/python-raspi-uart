import serial

class Uart(object):
	"""Class for managing the UART over
	the serial connection for the raspi"""

	# UART configuration info, in raspi 3 model B
	# before /dev/ttyS0 is available the serial 
	# login terminal must be disabled in the kernel 
	# options

	# UART Pins are:
	#	GND: Pin  6
	#	TXD: Pin  8 or GPIO14
	#	RXD: Pin 10 or GPIO15
	
	__conf = {
		'devicefile':'/dev/ttyS0', 
		'baudrate': '9600',
		'timeout': 25
	}
	__ser = None

	def __init__(self, devicefile=None, baudrate=None, timeout=2):
		"""Init Function
		Parameters:
			devicefile = device file (in linux /dev/ttyUSB0)
			baudrate = bauds per second 115200 
			timeout = timeout in secods 25
		"""
		if devicefile:
			self.__conf['devicefile'] = devicefile
		if baudrate:
			self.__conf['baudrate'] = baudrate
		if timeout:
			self.__conf['timeout'] = timeout

		# Opening the UART connection
		self.__open()

	def __open(self):
		"""Open serial connection"""
		self.__ser = serial.Serial(
			self.__conf['devicefile'], 
			self.__conf['baudrate'], 
			timeout=self.__conf['timeout'])

	def get_conf(self):
		"""Returns serial conf"""
		return self.__conf
	
	def close(self):
		"""Closes the serial connection"""
		self.__ser.close()

	def send(self, data):
		"""Send data over serial without any
		end character (data)"""
		self.__ser.write(str(data))
		
	def sendn(self, data):
		"""Send data over serial with new line
		(data+\\n)"""
		self.__ser.write(str(data) + "\n")
	
	def sendrn(self, data):
		"""Send data over serial with carriage
		return and new line (data+\\r\\n)"""
		self.__ser.write(str(data) + "\r\n")

	def readline(self):
		"""Reads data till new line character \\n
		or till EOF if no \\n found"""
		return self.__ser.readline()

	def read(self, nbytes):
		"""Reads nbytes bytes from UART"""
		assert isinstance(nbytes, int), "nbytes must be an integer"
		return self.__ser.read(nbytes)




