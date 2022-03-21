__author__ = 'Hari'

#from placeholders import *
from basics import*

notes = '''
 Identity and equality are 2 concepts which most beginners are confused about.
 The 'is' operator is used to test identity and == is used to test equality.

 Two objects are identical if they are the same object
 Two objects can be equal even if they are not the same object, if they are of the same type and the type defines some
 equality semantics. E.g. all string objects with content "abc" are equal irrespective of where the objects are in memory,
 two lists can be equal if all elements in them are equal in same order etc.
'''

def test_identity_equality_lists():
    a = []
    b = []
    assert (a is b) == (a is b)
    assert (a ==b)  == (a == b)

    a.append("one")
    assert (a is b) == (a is b)
    assert (a==b) == (a == b)

    c = []
    d = c
    assert (c is d) == (c is d)
    assert (c==d) == (c == d)

    c.append("one")
    assert ( c is d) == (c is d)
    assert (c==d) == (c == d)

def test_identity_equality_string():
    a = b = "hello"

    assert (a is b) == (a is b)
    assert (a==b) == (a == b)

    c = "hello"
    d = "".join(["hel", "lo"])
    assert (c is d) == (c is d)
    assert (c==d)  == (c == d)

def test_identity_equality_numbers():
    a = b = 10000
    assert (a is b) == (a is b)
    assert (a==b) == (a == b)

    c = 10000
    d = int("10000")
    assert (c is d) == (c is d)
    assert (c==d) == (c == d)

def test_identity_equality_small_numbers():
    """
    why do small numbers behave differently? google and find out!
    """
    a = b = 10
    assert  (a is b) == (a is b)
    assert  (a==b) == ( a == b)

    c = 10
    d = int("10")
    assert (c is d) == (c is d)
    assert (c == d) == (c == d)

def test_identity_equality_None():
    a = b = None
    assert (a is b) == (a is b)
    assert (a==b) == (a == b)

    a = None
    b = None
    assert (a is b) == (a is b)
    assert (a ==b) == (a == b)


notes_on_none = '''
None is a builtin constant as you can see above. This allows you to write more
readable code like if x is None: instead of if x == None:
'''
'''
three_things_i_learnt = """
-
-
-
"""

time_taken_minutes = ___
'''

