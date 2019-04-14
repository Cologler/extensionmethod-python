# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

'''
https://github.com/sixty-north/asq is a power module for iterable object.
'''

asq = None

try:
    import asq.initiators
except ImportError:
    pass

if asq is not None:
    from .. import ext_method

    @ext_method(list, tuple)
    def query(self):
        return asq.initiators.query(self)
