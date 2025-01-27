import unittest
import datetime
import locale
from urllib.request import urlopen

from byro.utils import Utils


class IntervalCzech(unittest.TestCase):

	def setUp(self):
		locale.setlocale(locale.LC_ALL, "cs_CZ.utf8")

	def tearDown(self):
		pass

	def test_interval_leden(self):
		real = Utils.define_interval('leden', 2015)
		firstJan = datetime.date(2015, 1, 1)
		lastJan = datetime.date(2015, 1, 31)
		expect = (firstJan, lastJan, "leden")
		self.assertEqual(real, expect)

	def test_interval_duben(self):
		real = Utils.define_interval('duben', 2015)
		firstJan = datetime.date(2015, 4, 1)
		lastJan = datetime.date(2015, 4, 30)
		expect = (firstJan, lastJan, "duben")
		self.assertEqual(real, expect)


class IntervalEnglish(unittest.TestCase):

	def setUp(self):
		locale.setlocale(locale.LC_ALL, "en_US.utf8")

	def tearDown(self):
		pass

	def test_interval_january(self):
		real = Utils.define_interval('January', 2015)
		firstJan = datetime.date(2015, 1, 1)
		lastJan = datetime.date(2015, 1, 31)
		expect = (firstJan, lastJan, "January")
		self.assertEqual(real, expect)

	def test_interval_april(self):
		real = Utils.define_interval('April', 2015)
		firstJan = datetime.date(2015, 4, 1)
		lastJan = datetime.date(2015, 4, 30)
		expect = (firstJan, lastJan, "April")
		self.assertEqual(real, expect)


class PickTime(unittest.TestCase):

	def setUp(self):
		self.time = "10:00-11:00"
		self.rawtext = "INF department meeting"

	def test_pict_time(self):
		texts = [
			self.time + " " + self.rawtext,
			" " + self.time + "   " + self.rawtext,
			self.time + "* " + self.rawtext
			]
		expected = (self.time, self.rawtext)

		for t in texts:
			with self.subTest(t=t, expected=expected):
				returned = Utils.pick_time(t)
				self.assertEqual(returned, expected)

	def test_pick_time_fail(self):
		returned = Utils.pick_time(self.rawtext)
		expected = ("?", self.rawtext)
		self.assertEqual(returned, expected)

	def test_pict_time_1_digit(self):
		returned = Utils.pick_time("9:00-10:00 text")
		expected = ("9:00-10:00", "text")
		self.assertEqual(returned, expected)


class SplitFilename(unittest.TestCase):

	def setUp(self):
		pass

	def test_split_filename(self):
		names = [("file", ".md"), ("file", ".tex"),
				 ("file.md", ".pdf"), ("file-with_extra.symbols", ".txt")]
		for n in names:
			with self.subTest(n=n):
				name = n[0] + n[1]
				res = Utils.split_filename(name)
				self.assertEqual(res[0], n[0])
				self.assertEqual(res[1], n[1])
