
class Any(object):
    def __eq__(self, other):
        return True

class AnyStringWith(str):
    def __eq__(self, other):
        return self in other

class AnyStringWithOut(str):
    def __eq__(self, other):
        return not self in other

class AnyListWith(object):
    def __eq__(self, other):
        if isinstance(other, list):
            return self in other
        return False

