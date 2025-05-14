import pytest
import unittest
import algo
import ABPruning

def test_choice_piece():
    assert set(algo.algoritm([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP").choice_piece()) in [set('BDEP'), set('BDCF'), set('BDFP'), set('BLCF'), set('DCES'), set('DEPS'), set('FDCS'), set('LCES'), set('LEPS'), set('FLPS')]
    assert algo.algoritm(["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP",None],"LFPS").choice_piece() == None
    
def test_run():
    result = algo.algoritm().run({
   "request": "play",
   "lives": 3,
   "errors": [],
   "state": {
  "players": ["LUR", "FKY"],
  "current": 0,
  "board": [None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],
  "piece": "BLEP"
    }})
    assert type(result) == dict

def test_pieces_list():
    a = ABPruning.pieces_list([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None],"LBEP")
    for i in range(len(a)):
        a[i] = set(a[i])
    assert a == [set('EDPB'), set('DCFB'), set('DPFB'), set('CLFB'), set('EDSC'), set('EDSP'), set('DSCF'), set('ELSC'), set('ELSP'), set('LSPF')]
    assert ABPruning.pieces_list(["BDEC","BDEP","BDFC","BDFP","BLEC","BLFC","BLEP","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLFC","SLEP",None],"LFPS") == []

def test_lineValue():
    assert ABPruning.lineValue(["BDEC","BDEP","BDFC","BDFP"]) == 20
    assert ABPruning.lineValue(["BDEC","BDEP","BDFC","SLFP"]) == 4

def test_align():
    assert ABPruning.align(["BDEC","BDEP","BDFC", None, None, 'CSLE', None, None, None, None, None, None, None, None, None, None],"BDFP") == 3
    assert ABPruning.align(["BDEC", None, "BDFC", None, None, 'CSLE', None, None, None, None, None, None, None, None, None, None],"BDFP") == None

def test_winner():
    assert ABPruning.winner([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None]) == None
    assert ABPruning.winner(["BDEC","BDEP","BDFC", "BDFP", None, 'CSLE', None, None, None, None, None, None, None, None, None, None]) == 1

def test_gameOver():
    assert ABPruning.gameOver(["BDEC","BDEP","BDFC", "BDFP", None, 'CSLE', None, None, None, None, None, None, None, None, None, None]) == True
    assert ABPruning.gameOver([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None]) == False

def test_moves():
    result = ABPruning.moves([None,"BDEC",None,"SDFP",None,None,None,None,None,"SLFC",None,None,"BLFP","BLEC",None,None])
    for i in result:
        assert i in [15, 4, 11, 14, 8, 7, 10, 6, 0, 5, 2]

def test_apply():
    assert ABPruning.apply(["BDEC","BDEP","BDFC", None, None, 'CSLE', None, None, None, None, None, None, None, None, None, None],"BDFP",3) == ['BDEC', 'BDEP', 'BDFC', 'BDFP', None, 'CSLE', None, None, None, None, None, None, None, None, None, None]

def test_heuristic():
    assert ABPruning.heuristic(["BDEC","BDEP","BDFC", None, None, 'CSLE', None, None, None, None, None, None, None, None, None, None],1) == 59
    assert ABPruning.heuristic(["BDEC","BDEP","BDFC", "BDFP", None, 'CSLE', None, None, None, None, None, None, None, None, None, None],1) == 400
    assert ABPruning.heuristic(["BDEC","BDEP","BDFC", "BDFP", None, 'CSLE', None, None, None, None, None, None, None, None, None, None],0) == -400

def test_negamaxWithPruningIterativeDeepening():
    assert ABPruning.negamaxWithPruningIterativeDeepening(["BDEC","BDEP","BDFC", None, None, 'CSLE', None, None, None, None, None, None, None, None, None, None],"BDFP", 0,0) == (None, 3, None)
    result = ABPruning.negamaxWithPruningIterativeDeepening(["BDEC",None,"BDFC", None, None, 'CSLE', None, None, None, None, None, None, None, None, None, None],"BDFP", 0,0)
    assert result[0:2] == (-52, 14) or result[0:2] == (46, 9)