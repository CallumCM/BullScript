class Token:
	def __init__(self, typ, value=None, index=0):
		self.type = typ
		self.value = value
		self.index = index
	def __repr__(self):
	  if self.value: return f'{self.type}:{self.value}'
	  return f'{self.type}'