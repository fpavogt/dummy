# -*- coding: utf-8 -*-
'''
dummy: a bare-bone Python library to debug https://stackoverflow.com/questions/79887269/

Copyright (c) 2026 F.P.A. Vogt; frederic.vogt@alumni.anu.edu.au

Distributed under the terms of the GNU General Public License v3.0 or later.

SPDX-License-identifier: GPL-3.0-or-later
'''

from dummy import dummy_fct

def test_dummy_fct():
    """ Basic test of the dummy function."""

    assert dummy_fct() is True
