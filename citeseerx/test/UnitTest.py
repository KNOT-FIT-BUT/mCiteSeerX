#!/usr/bin/env python
from citeseerx import basicSearch
from citeseerx import extendedSearch
import unittest
import sys
import string


class TestSequenceFunctions(unittest.TestCase):

    # testing BasicSearch

    # test should raise ValueError exception
    def test_exception1(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = basicSearch("windows", False, 6)
        except:
            raised = True
        self.assertEquals(raised, True)

    # test should raise ValueError exception
    def test_exception2(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = basicSearch("windows", "Cau", 3)
        except:
            raised = True
            self.assertEquals(raised, True)

    # test searching phrase windows without citations sort Relevance
    def test_searching1(self):
        slovnik = dict()
        raised=False
        try:
            slovnik = basicSearch("windows", False, 0)
        except:
            raised = True
        self.assertEquals(raised, False)
    # test searching multiple Phrase:windows linux sort Relevance

    def test_searching2(self):
        slovnik = dict()
        raised=False
        try:
            slovnik = basicSearch("windows linux", False, 0)
        except:
            raised=True
            self.assertEquals(raised, False)
    # test  searching phrase "nieco" sort Relevance should have 6 results

    def test_searching3(self):
        slovnik = dict()
        slovnik = basicSearch("nieco", False, 0)
        self.assertEquals(len(slovnik), 6)

    #
    # Testing ExtendedSearch
     # test should raise ValueError exception bad Value of AuttorAfi
    def test_exception_extend1(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = extendedSearch("windows", False, "HI", 0, "Bill", False,False, False, [], 30, False, 0)
        except:
            raised = True
        self.assertEquals(raised, True)

    # test should raise ValueError exception bad Value of SortBy
    def test_exception_extend2(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = extendedSearch("windows", False, False,False, "Fact", "Bill", False, True, [
                                     1900, 2000], 30, False, 66)
        except:
            raised = True
        self.assertEquals(raised, True)
    # test should raise ValueError exception bad Value of MinCitations(True,
    # should be false or numeric value)

    def test_exception_extend2(self):
        slovnik = dict()
        raised = False
        try:
            slovnik = extendedSearch("windows", False, False, "Fact", "Bill", False, True, [
                                     1900, 2000], True, False, 0)
        except:
            raised = True
        self.assertEquals(raised, True)

    # test searching phrase windows without citations sort Relevance,no title,no AutorAffi,
    # Public Venue "Fact",Keywords - Bill, no Abstract, Year True  - 1900 - 2000,
    # no Mincitations, Include citations - yes, Sort -Relevance
    def test_searching_extend1(self):
        slovnik = dict()
        raised=False
        try:
            slovnik = extendedSearch("windows", False, False, "Fact", "Bill", False, False, True, [
                                 1900, 2000], False, False, 0)
        except:
            raised=True
        self.assertEquals(raised, False)
    # test searching phrase windows linux without citations sort Relevance,no title,no AutorAffi,
    # Public Venue "Fact",Keywords - Bill, no Abstract, Year True  - 1900 - 2000,
    # no Mincitations, Include citations - yes, Sort -Relevance

    def test_searching_extend2(self):
        slovnik = dict()
        raised=False
        try:
            slovnik = extendedSearch("windows linux", False, False, "Fact", "Bill", False, False, True, [
                                     1900, 2000], False, False, 0)
        except:
            raised=True
        self.assertEquals(raised, False)
    # test searching phrase "nieco" without citations sort Relevance,no title,no AutorAffi,
    # Public Venue "Fact",Keywords - Bill, no Abstract, Year True  - 1900 - 2000,
    # no Mincitations, Include citations - yes, Sort -Relevance - should have
    # 6 results

    def test_searching_extend3(self):
        slovnik = dict()
        slovnik = extendedSearch("nieco", False, False, "Fact", "Bill", False, False, True, [
                                 1900, 2000], False, False, 0)
        self.assertEquals(len(slovnik), 0)


if __name__ == '__main__':
    unittest.main()
