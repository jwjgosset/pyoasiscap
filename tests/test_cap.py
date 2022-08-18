"""
..  codeauthor:: Charles Blais
"""
from pyoasiscap import cap

from pyoasiscap.alert import Alert, Status


def test_cap():
    capxml = cap.from_file('tests/examples/oasis-cap-example.xml')
    print(capxml)


def test_cap2():
    capxml = cap.from_file('tests/examples/oasis-cap-example2.xml')
    print(capxml)


def test_cap_from_dict():
    capxml = cap.from_file('tests/examples/oasis-cap-example2.xml')
    obj = capxml.asdict()
    assert obj['status'] == 'Actual'

    capxml = Alert(**obj)
    assert capxml.status == Status.actual
