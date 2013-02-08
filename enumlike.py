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
    """
    def __init__(self, *iterable):
        values = []
        names = []
        labels = []
        for x, y, z in iterable:
            values.append(x)
            names.append(y)
            labels.append(z)
        self._names = names
        self._values = values
        self._lables = labels
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

    def __getitem__(self, name):
        return self._dict[name]

    def verbose(self, value):
        return self._verbose[value]

    def prop(self, value):
        return self._prop[value]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
