# PARENT CLASS FOR ALL ERRORS:
class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    def as_string(self):
        result = f'\033[91m{self.error_name}: {self.details}\033[0m'
        return result

# ERRORS:
class IllegalCharException(Error):
  def __init__(self, details):
      super().__init__('IllegalCharacterException', details)

class StackOverflowError(Error):
	def __init__(self, details):
		super().__init__('StackOverflowError', details)

class UndefinedFunctionError(Error):
		def __init__(self, details):
			super().__init__('UnknownFunctionError', details)

class UndefinedVariableError(Error):
	def __init__(self, details):
		super().__init__('UndefinedVariableError', details)