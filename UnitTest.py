#!/usr/bin/env python

import unittest

class SortedDict(dict):
    """
    Dictionary that maintains keys in sorted order (by time of definition).
    """
    def __init__(self, *args, **kwargs):
        super(SortedDict, self).__init__(*args, **kwargs)
        self._key_order = []

    def __setitem__(self, key, value):
        if key not in self:
            self._key_order.append(key)
        super(SortedDict, self).__setitem__(key, value)

    def keys(self):
