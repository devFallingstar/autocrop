# -*- coding: utf-8 -*-

"""Tests for autocrop"""

import cv2
import numpy as np
import os
import shutil

from autocrop.autocrop import gamma, crop




# Define directory change within context
@contextmanager
def integration(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    # copy files over to integration/
    shutil.copytree(

    try:
        yield
    finally:
        os.chdir(prevdir)
        # delete the temporary folder


def test_gamma_can_do_sqrt():
    """This function is so tightly coupled to cv2 it's probably useless.
    Still might flag cv2 or numpy boo-boos."""
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    expected = np.uint8([[15, 22, 27], [31, 35, 39], [42, 45, 47]])
    np.testing.assert_array_equal(gamma(img=matrix, correction=0.5), expected)


def test_crop_noise_returns_none():
    loc = 'tests/data/noise.png'
    noise = cv2.imread(loc)
    assert crop(noise) is None


def test_obama_has_a_face():
    loc = 'tests/data/obama.jpg'
    obama = cv2.imread(loc)
    assert len(crop(obama, 500, 500)) == 500
