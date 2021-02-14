import pandas as pd
from idcempy import imnl
import os

DAT = pd.read_stata(
    os.getcwd()+"/data/replicationdata.dta", convert_categoricals=False)

x = ['educ', 'party7', 'agegroup2']
z = ['educ', 'agegroup2']
y = ['vote_turn']

order = [0, 1, 2]
second_order = [1, 0, 2]
torder = [2, 1, 0]

binflatecat = "baseline"
sinflatecat = "second"
tinflatecat = "third"


def test_imnls():
    model = imnl.imnlmod(DAT, x, y, z, order, binflatecat)
    smodel = imnl.imnlmod(DAT, x, y, z, second_order, sinflatecat)
    tmodel = imnl.imnlmod(DAT, x, y, z, torder, tinflatecat)
    assert model.modeltype == smodel.modeltype == tmodel.modeltype
