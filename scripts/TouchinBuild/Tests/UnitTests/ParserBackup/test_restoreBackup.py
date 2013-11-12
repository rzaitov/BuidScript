import unittest
from parsers.ParserBackup.RestoreBackupParser import RestoreBackupParser


class TestRestoreBackup(unittest.TestCase):
	def setUp(self):
		self.parser = RestoreBackupParser()

	def test_parseCurrentDir(self):
		line = "restore   from  backup '.'"
		folderPath = self.parser.parseLine(line)

		self.assertEqual('.', folderPath)

	def test_parseRelativePath(self):
		line = "restore from backup '../Some/Path'"
		folderPath = self.parser.parseLine(line)

		self.assertEqual('../Some/Path', folderPath)

	def test_parseAbsPath(self):
		line = "restore from backup '/Some/Abs/Path'"
		folderPath = self.parser.parseLine(line)

		self.assertEqual('/Some/Abs/Path', folderPath)