# -*- coding: utf-8 -*-
#
# Copyright (c) 2019~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import ctypes

import forbiddenfruit

def _modify_type(type_: type, attrs: dict):
    if not isinstance(type_, type):
        raise TypeError
    for k, v in attrs.items():
        forbiddenfruit.curse(type_, k, v)
    ctypes.pythonapi.PyType_Modified(ctypes.py_object(type_)) # to clear cache

def ext_class(cls):
    '''
    Usage:

    ``` py
    @extension_class
    class StrExt(str):
        def first(self):
            return self[0]
    assert '123'.first() == '1'
    ```
    '''
    for name, attr in cls.__dict__.items():
        for base in cls.__bases__:
            attrs = {}
            if name[:2] != '__' and not hasattr(base, name):
                attrs[name] = attr
            _modify_type(base, attrs)

def ext_method(*clses, name=None):
    def wrapper(func):
        attrs = {}
        attrs[name or func.__name__] = func
        for cls in clses:
            _modify_type(cls, attrs)
        return func
    return wrapper
