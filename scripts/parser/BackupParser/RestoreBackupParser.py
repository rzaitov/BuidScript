from parser.LineParser import LineParser
import re


class RestoreBackupParser(LineParser):
	def parseLine(self, line):
		assert line is not None

		regexpSource = r'restore from backup\s*'
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

	def isValidLine(self, line):
		assert line is not None

		isValid = line.startswith('restore from backup')

