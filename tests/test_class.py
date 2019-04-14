# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from extensionmethod import ext_class

def test_doc_example():
    @ext_class
    class StrExt(str):
        def first(self):
            return self[0]
    assert '123'.first() == '1'
