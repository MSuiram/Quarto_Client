import pytest
import unittest
import algo
import ABPruning

def test_choice_piece():
    assert set(algo.algoritm([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP").choice_piece()) in [set('BDEP'), set('BDCF'), set('BDFP'), set('BLCF'), set('DCES'), set('DEPS'), set('FDCS'), set('LCES'), set('LEPS'), set('FLPS')]
    assert algo.algoritm(["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP",None],"LFPS").choice_piece() == None

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
    
def test_pieces_list():
    a = ABPruning.pieces_list([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP")
    for i in range(len(a)):
        a[i] = set(a[i])
    assert a == [set('EDPB'), set('DCFB'), set('DPFB'), set('CLFB'), set('EDSC'), set('EDSP'), set('DSCF'), set('ELSC'), set('ELSP'), set('LSPF')]
    assert ABPruning.pieces_list(["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP",None],"LFPS") == []

def test_lineValue():
    assert ABPruning.lineValue(["BDEC","BDEP","BDFC","BDFP"],"LFPS") == 2

def test_align():
    assert ABPruning.align(print(["BDEC","BDEP","BDFC", None, None, 'CSLE', None, None, None, None, None, None, None, None, None, None],"BDFP")) == 3
