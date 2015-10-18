class raspberryPiData:

	devices = []
	count = 0
	rssiThreshold = 0
	timeOutValue = 0 

	def __init__(self,rssiThreshold,timeOutValue):

		self.rssiThreshold = rssiThreshold
		self.timeOutValue = timeOutValue

	def getSenseObject(self,bluetoothAddress):
		for obj in self.devices:
			if(obj.bluetoothAddress == bluetoothAddress):
				return obj

		