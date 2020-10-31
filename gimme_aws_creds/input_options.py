from enum import Enum as LibEnum

class Enum(object):
  def __init__(self, options):
    self._enum = LibEnum('Enum', options)

  def has(self, value):
    return value in self._enum._member_names_

class AlwaysNeverAsk(Enum):
  def __init__(self):
    super().__init__('always never ask')

  @property
  def Always(self):
    return self._enum.always

  @property
  def Never(self):
    return self._enum.never

  @property
  def Ask(self):
    return self._enum.ask

  def resolve(self, value, default=None):
    if isinstance(value, str):
      value = value.lower()

    if value in [self.Always, self.Always.name, 'y', 'yes']:
      return self.Always
    if value in [self.Never, self.Never.name, 'n', 'no']:
      return self.Never
    if value in [self.Ask, self.Ask.name, 'a']:
      return self.Ask

    return default

alwaysNeverAsk = AlwaysNeverAsk()
