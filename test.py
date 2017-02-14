#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: eph

import unittest
from random import randrange

import fisher


class TestFisher(unittest.TestCase):

    def test_with_scipy(self, samples=100):
        from scipy.stats import fisher_exact
        for _ in range(samples):
            a = randrange(randrange(randrange(randrange(65536)+1)+1)+1)
            b = randrange(randrange(randrange(randrange(65536)+1)+1)+1)
            c = randrange(randrange(randrange(randrange(65536)+1)+1)+1)
            d = randrange(randrange(randrange(randrange(65536)+1)+1)+1)
            lp, rp, tp = fisher.test1(a, b, c, d)
            self.assertLessEqual(lp, 1)
            self.assertLessEqual(rp, 1)
            self.assertLessEqual(tp, 1)
            self.assertAlmostEqual(lp, fisher_exact([[a, b], [c, d]], 'less')[1])
            self.assertAlmostEqual(rp, fisher_exact([[a, b], [c, d]], 'greater')[1])
            self.assertAlmostEqual(tp, fisher_exact([[a, b], [c, d]], 'two-sided')[1])
            self.assertAlmostEqual(lp, fisher.test1l(a, b, c, d))
            self.assertAlmostEqual(rp, fisher.test1r(a, b, c, d))
            self.assertAlmostEqual(tp, fisher.test1t(a, b, c, d))

if __name__ == '__main__':
    unittest.main()
