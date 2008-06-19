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

class Settlement(object):
	"""The Settlement class describes a settlement and stores all the neccassary information
	like name, current inhabitants, lists of tiles and houses, etc belonging to the village."""
	def __init__(self, owner):
		"""
		@param owner: player that owns the settlement
		"""
		self.name = 'foo' # TODO: add name generator here
		self.owner = owner
		self._inhabitants = 0
		self.buildings = [] # List of all the buildings belonging to the settlement
		self.inventory = {}
		self.inventory['wood'] = 5
		self.inventory['tools'] = 6
		self.inventory['bricks'] = 7
		self.inventory['food'] = 8
		self.inventory_size = 30

	def alter_inventory(self, ressource, num):
		"""Changes the invertory ressources by the factor num
		@param ressource: string representing the ressource
		@param num: int how the ressource is to be changed. (Can be 2 if you want to add 2 or could be -4 if you wanted to remove 4)
		"""
		self.inventory[ressource] += num
		if self.inventory[ressource] > self.inventory_size:
			self.inventory = self.inventory_size
		elif self.inventory[ressource] < 0:
			raise Exception, 'Removed more from the inventory than was in it.'

	def remove_building(self, building):
		pass

	def get_building(self, x, y):
		for b in self.buildings:
			if b.x <= x < b.x + b.__class__.size[0] and b.y <= y < b.y + b.__class__.size[1]:
				return b
		else:
			return None
