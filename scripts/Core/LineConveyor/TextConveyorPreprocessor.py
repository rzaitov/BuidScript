class TextConveyorPreprocessor:
	def __init__(self):
		self.processors = []

	def addProcessor(self, processor):
		assert processor is not None

		self.processors.append(processor)

	def processText(self, text):
		assert text is not None

		for processor in self.processors:
			text = processor.processText(text)

		return text