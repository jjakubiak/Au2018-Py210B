#!/usr/bin/env/python3

"""
Tim Meese
Au2018-Py210B
Mailroom Part 4 assignment
"""

import pytest
from mailroom_part4 import create_report_task
from mailroom_part4 import send_thankyou_multiple_donors_task
from mailroom_part4 import send_thankyou_single_donor_test
from mailroom_part4 import add_single_donor_test
from pathlib import Path

thankyou_file_list = []

def test_report():
    outlines = create_report_task()
    assert(5 == len(outlines))

def test_thankyou_files():
    global thankyou_file_list
    thankyou_file_list = send_thankyou_multiple_donors_task()
    for test_file in thankyou_file_list:
        try:
            test_file_path = Path(test_file)
            assert(test_file_path.is_file())
        except FileNotFoundError:
            assert(False)

def test_single_thankyou():
    fname = 'Jim'
    lname = 'Smith'
    amount = 50.0
    key = (fname, lname)
    add_single_donor_test(fname, lname, amount)
    thankyou_lines = send_thankyou_single_donor_test(key)
    assert fname in thankyou_lines[0]
    assert str(amount) in thankyou_lines[1]
    assert str(amount) in thankyou_lines[2]




