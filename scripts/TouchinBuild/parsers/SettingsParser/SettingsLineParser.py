import re

from parsers.LineParser import LineParser
from parsers.SettingsParser.PathParser import PathParser


class SettingsLineParser(LineParser):
	def __init__(self):
		LineParser.__init__(self)

	def parseLine(self, line):
		assert line is not None

		pathAndValue = self.splitToPathAndValue(line)

		path = pathAndValue[0]
		value = pathAndValue[1]

		pathParser = PathParser()
		pathSegments = pathParser.parse(path)

		result = {
			'segments' : pathSegments,
			'value' : value
		}

		return result

	def splitToPathAndValue(self, line):

		propPathRegexp = r"^(?P<prop_path>[\w.]+)"
		valueRegexp = "'(?P<value>.*)'"

		regexpSource = propPathRegexp + r'\s*=\s*' + valueRegexp
		regexp = re.compile(regexpSource, re.UNICODE)

		match = regexp.match(line)
		self._guardMatch(match, line, regexpSource)

		propPath = match.group('prop_path')
		value = match.group('value')

		return propPath, value