# ###################################################
# Copyright (C) 2008 The OpenAnno Team
# team@openanno.org
# This file is part of OpenAnno.
#
# OpenAnno is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################

import sqlite3
import re

class DbReader(object):
	"""Class that handles connections to sqlite databases"""
	def __init__(self, file):
		"""Init function, opens the connection to a database and creates a cursor for that database
		@var file: str containing the database file.
		"""

		self.connection = sqlite3.connect(file)
		self.connection.isolation_level = None
		def regexp(expr, item):
			r = re.compile(expr)
			return r.match(item) is not None
		self.connection.create_function("regexp", 2, regexp)
		self.cur = self.connection.cursor()

	def __call__(self, command, *args):
		"""Executes a sql command.
		@var command: str containing the raw sql command, with ? as placeholders for values (eg. SELELCT ? FROM ?).
		@var args: tuple containing the values to add into the command.
		"""
		if not sqlite3.complete_statement(command):
			if sqlite3.complete_statement(command + ';'):
				command = command + ';'
			else:
				raise 'Error, no complete sql statement provided by "' + command + '".'
		try:
			self.cur.execute(command, args)
			return SqlResult(self.cur.fetchall(), None if self.cur.rowcount == -1 else self.cur.rowcount, self.cur.lastrowid)
		except sqlite3.Error, e:
			print "An error occurred:", e.args[0]
			return SqlError(e.args[0])

	def execute_script(self, script):
		"""Executes a multiline script.
		@var script: multiline str containing an sql script."""
		return self.cur.executescript(script)

class SqlError(object):
	"""Represents a SQL error"""

	def __init__(self, error):
		self.success, self.error, self.rows, self.affected, self.id = False, error, None, None, None

class SqlResult(object):
	"""Represents a SQL result"""

	def __init__(self, rows, affected, id):
		self.success, self.error, self.rows, self.affected, self.id = True, None, rows, affected, id

	def __getattr__(self, name):
		return getattr(self.rows, name)
	def __add__(self, *args, **kwargs): return self.rows.__add__(*args, **kwargs)
	def __contains__(self, *args, **kwargs): return self.rows.__contains__(*args, **kwargs)
	def __delitem__(self, *args, **kwargs): return self.rows.__delitem__(*args, **kwargs)
	def __delslice__(self, *args, **kwargs): return self.rows.__delslice__(*args, **kwargs)
	def __eq__(self, *args, **kwargs): return self.rows.__eq__(*args, **kwargs)
	def __ge__(self, *args, **kwargs): return self.rows.__ge__(*args, **kwargs)
	def __getitem__(self, *args, **kwargs): return self.rows.__getitem__(*args, **kwargs)
	def __getslice__(self, *args, **kwargs): return self.rows.__getslice__(*args, **kwargs)
	def __gt__(self, *args, **kwargs): return self.rows.__gt__(*args, **kwargs)
	def __hash__(self, *args, **kwargs): return self.rows.__hash__(*args, **kwargs)
	def __iadd__(self, *args, **kwargs): return self.rows.__iadd__(*args, **kwargs)
	def __imul__(self, *args, **kwargs): return self.rows.__imul__(*args, **kwargs)
	def __iter__(self, *args, **kwargs): return self.rows.__iter__(*args, **kwargs)
	def __le__(self, *args, **kwargs): return self.rows.__le__(*args, **kwargs)
	def __len__(self, *args, **kwargs): return self.rows.__len__(*args, **kwargs)
	def __lt__(self, *args, **kwargs): return self.rows.__lt__(*args, **kwargs)
	def __mul__(self, *args, **kwargs): return self.rows.__mul__(*args, **kwargs)
	def __ne__(self, *args, **kwargs): return self.rows.__ne__(*args, **kwargs)
	def __repr__(self, *args, **kwargs): return self.rows.__repr__(*args, **kwargs)
	def __reversed__(self, *args, **kwargs): return self.rows.__reversed__(*args, **kwargs)
	def __rmul__(self, *args, **kwargs): return self.rows.__rmul__(*args, **kwargs)
	def __setitem__(self, *args, **kwargs): return self.rows.__setitem__(*args, **kwargs)
	def __setslice__(self, *args, **kwargs): return self.rows.__setslice__(*args, **kwargs)
