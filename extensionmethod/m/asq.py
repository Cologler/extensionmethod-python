# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

'''
https://github.com/sixty-north/asq is a power module for iterable object.

install: pip install asq
'''

def patch_types(*types):
    asq = None

    try:
        import asq.initiators
    except ImportError:
        return

    from .. import ext_method

    @ext_method(*types)
    def query(self):
        return asq.initiators.query(self)

patch_types(
    list,
    tuple,
    dict,
    type({}.keys()),
    type({}.values()),
    type({}.items()),
)
