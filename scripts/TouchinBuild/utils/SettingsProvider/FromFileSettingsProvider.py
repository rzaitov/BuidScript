from Core.SettingsProviderBase import SettingsProviderBase
from parsers.SettingsParser.SettingsParser import SettingsParser


class FromFileSettingsProvider(SettingsProviderBase):
	def __init__(self):
		SettingsProviderBase.__init__(self)

	def fetchSettings(self):
		settingsFile = open('scripts/settings.txt')
		content = settingsFile.read()

		parser = SettingsParser()
		parser.parse(content)

		return parser.settings