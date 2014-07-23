# -*- coding:utf-8 -*-


class EnumLike(object):
    """An enum like object for using django-form-choices.

    Each choice element should be a tuple (value, key, label)
    like this...

    >>> choices = EnumLike((1, "spam", u"SPAM"), (2, "egg", u"EGG"))
    >>> choices['spam']
    1
    >>> choices.verbose(2)
    u'EGG'
    >>> tuple(choices)
    ((1, u'SPAM'), (2, u'EGG'))
    >>> 'egg' in choices
    True
    >>> 'jam' in choices
    False
    """
    def __init__(self, *iterable):
        values = []
        names = []
        labels = []
        for x, y, z in iterable:
            values.append(x)
            names.append(y)
            labels.append(z)
        self._names = tuple(names)
        self._values = tuple(values)
        self._labels = tuple(labels)
        for name, value in zip(names, values):
            setattr(self, name, value)
        self.choices = tuple(zip(values, labels))
        self._dict = dict(zip(names, values))
        self._verbose = dict(zip(values, labels))
        self._prop = dict(zip(values, names))

    def as_dict(self):
        return self._dict

    def __iter__(self):
        return iter(self.choices)

    def __contains__(self, item):
        return item in self._names

    def __getitem__(self, key):
        return self._dict[key]

    def verbose(self, value):
        return self._verbose[value]

    def prop(self, value):
        return self._prop[value]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
