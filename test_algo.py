import pytest
import unittest
import algo

def test_choice_piece():
    assert set(algo.algoritm([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP").choice_piece()) in [set('BDEP'), set('BDCF'), set('BDFP'), set('BLCF'), set('DCES'), set('DEPS'), set('FDCS'), set('LCES'), set('LEPS'), set('FLPS')]
    assert algo.algoritm(["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP",None],"LFPS").choice_piece() == None

def test_choice_pos():
    assert algo.algoritm([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP").choice_pos() in [0,2,4,5,6,7,8,10,11,14,15]
    assert algo.algoritm(["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP",None],"LFPS").choice_pos() == 15

def test_run():
    assert type(algo.algoritm().run({"request": "play",
                                     "lives": 3,
                                     "errors": None,
                                     "state": {
                                         "players": ["LUR", "FKY"],
                                         "current": 0,
                                         "board": [None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],
                                         "piece": "BLEP"
                                         }})) == dict

def test_winner():
    assert algo.algoritm([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP").winner() == None
    assert algo.algoritm(["SDEC","BDEC","BDFP","SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP").winner() == 1