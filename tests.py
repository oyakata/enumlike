# -*- coding:utf-8 -*-
import unittest

import enumlike


class EnumLikeTest(unittest.TestCase):
    def _makeOne(self):
        return enumlike.EnumLike(
            (1, "foo", u"ラベル1"),
            (2, "bar", u"ラベル2"),
            (3, "baz", u"ラベル3"),
        )

    def test(self):
        obj = self._makeOne()
        self.assertEqual(obj.foo, 1)
        self.assertEqual(obj.bar, 2)
        self.assertEqual(obj.baz, 3)
        self.assertEqual(obj["foo"], 1)
        self.assertRaises(KeyError, lambda: obj["foo?"])
        self.assertEqual(obj.verbose(1), u"ラベル1")
        self.assertRaises(KeyError, lambda: obj.verbose(4))

    def test_choices(self):
        obj = self._makeOne()
        expect = ((1, u"ラベル1"), (2, u"ラベル2"), (3, u"ラベル3"))
        self.assertEqual(obj.choices, expect)
        self.assertEqual(tuple(list(obj)), expect)

    def test_as_dict(self):
        obj = self._makeOne()
        self.assertEqual(obj.as_dict(), {"foo": 1, "bar": 2, "baz": 3})


if __name__ == "__main__":
    unittest.main()
