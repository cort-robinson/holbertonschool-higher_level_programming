#!/usr/bin/python3
"""Defines class_to_json"""
import json
MyClass = __import__('10-my_class').MyClass


def class_to_json(obj):
    """Returns dictionary description with simple data
    structure for JSON serialization of object"""
    return obj.__dict__
