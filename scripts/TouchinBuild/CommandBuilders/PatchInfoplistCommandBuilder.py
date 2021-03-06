from commands.PatchInfoPlistCommand import PatchInfoPlistCommand
from parsers.InsideParser.InsideSetParser import InsideSetParser


class PatchInfoplistCommandBuilder:
	def __init__(self, valueProvider):
		assert valueProvider is not None

		self.__valueProvider = valueProvider

	def isPatchInfoPlist(self, line):
		assert line is not None

		parser = self.createParser()
		isValid = parser.isValidLine(line)

		return isValid

	def getCommandFor(self, line):
		parser = self.createParser()
		result = parser.parseLine(line)

		path = result[0]
		key = result[1]
		value = result[2]

		command = PatchInfoPlistCommand(path, key, value)
		return command

	def createParser(self):
		parser = InsideSetParser('plist')
		return parser

