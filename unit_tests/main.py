#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""Survey server unit tests main module."""

import sys, os
import unittest
import test_survey_basic
import test_survey_serialization


def main():
    suite = unittest.TestSuite([
        test_survey_basic.suite(),
        test_survey_serialization.suite(),
    ])
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if len(result.errors) > 0 or len(result.failures) > 0:
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())

