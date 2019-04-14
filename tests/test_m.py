# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

def test_asq():
    import extensionmethod.m.asq

    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    result = words.query().order_by(len).then_by().take(5).select(str.upper).to_list()
    assert result == ['ONE', 'SIX', 'TEN', 'TWO', 'FIVE']
