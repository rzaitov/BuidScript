import unittest
from parsers.InstallProfileParser import InstallProfileParser


class TestInstallProfile(unittest.TestCase):
	def setUp(self):
		self.parser = InstallProfileParser()

	def test_parse(self):
		line = "install profile 'Path/To/Profile.mobileprovision'"
		src = self.parser.parseLine(line)

		self.assertEqual('Path/To/Profile.mobileprovision', src)
