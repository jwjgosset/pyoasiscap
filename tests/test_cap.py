"""
..  codeauthor:: Charles Blais
"""
from pyoasiscap import cap


def test_cap():
    capxml = cap.from_file('tests/examples/oasis-cap-example.xml')
    print(capxml)


def test_cap2():
    capxml = cap.from_file('tests/examples/oasis-cap-example2.xml')
    print(capxml)
