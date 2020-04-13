## unit tests for bmi_delta.py

import pytest

import sys, os
import numpy as np
sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))

from pyDeltaRCM import BmiDelta

# need to create a simple case of pydeltarcm object to test these functions
# will fix the random seed
np.random.seed(0)

# use test.yaml
delta = BmiDelta()

def test_initialize():
    '''
    test function BmiDelta.initialize
    '''
    delta.initialize(os.getcwd() + '/tests/test.yaml')
    assert delta._delta.f_bedload == 0.5

def test_update():
    delta.update()
    assert delta._delta._time == 1.0

def test_update_frac():
    delta.update_frac(1)
    assert delta._delta.time_step == 1.0