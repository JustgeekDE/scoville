class Any(object):
    def __eq__(self, other):
        return True


class AnyStringWith(str):
    def __eq__(self, other):
        assert self in other, "'%s' does not contain '%s'" % (other, self)
        return True


class AnyStringWithOut(str):
    def __eq__(self, other):
        assert not self in other, "'%s' does contain '%s'" % (other, self)
        return True


class AnyListWithString(str):
    def __eq__(self, other):
        assert isinstance(other, list), "'%s' is not a list'" % (other)
        assert str(self) in other, "'%s' is not in %s'" % (str(self), str(other))
        return True
