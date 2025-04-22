import pytest
import unittest
import algo

def test_choice_piece():
    assert set(algo.algoritm([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP").choice_piece()) in [set('BDEP'), set('BDCF'), set('BDFP'), set('BLCF'), set('DCES'), set('DEPS'), set('FDCS'), set('LCES'), set('LEPS'), set('FLPS')]
    assert algo.algoritm(["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP"],"LFPS").choice_piece() == None