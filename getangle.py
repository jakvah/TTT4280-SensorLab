import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
import importdata as ipd
import buggesmatteland as bml


def getAngle(path):
    x_12 = 0.065
    x_13 = 0.065
    x_23 = 0.065
    a = 0.0563
    f_s = 31250 

    channels = 5

    [nomTp, rawData] = ipd.raspi_import(path,channels)

    rawData_up = ipd.preProc(rawData,10)

    # Henter rekker for corsscorr   
    seq1 = rawData[5:,0]
    seq2 = rawData[5:,1]
    seq3 = rawData[5:,2]

    # Fjerne DC
    seq1_no_dc = bml.removeDC(seq1) 
    seq2_no_dc = bml.removeDC(seq2)
    seq3_no_dc = bml.removeDC(seq3)

    # Beregner xCorr
    corr_12 = np.correlate(seq1_no_dc,seq2_no_dc,'full')
    corr_13 = np.correlate(seq1_no_dc,seq3_no_dc,'full')
    corr_23 = np.correlate(seq2_no_dc,seq3_no_dc,'full')

    # Alle autocorr har samme midtverdi
    corr_23_short = corr_23[31144:31344]
    corr_12_short = corr_12[31144:31344]
    corr_13_short = corr_13[31144:31344]

    # Python klarer ikke indexer på numpy lister tydeligvis. Lager nye identiske "vanlige" lister.
    corr_23_short_mod = []
    for sample in corr_23_short:
        corr_23_short_mod.append(sample)

    corr_13_short_mod = []
    for sample in corr_13_short:
        corr_13_short_mod.append(sample)

    corr_12_short_mod = []
    for sample in corr_12_short:
        corr_12_short_mod.append(sample)

    n_23 = corr_23_short_mod.index(max(corr_23_short_mod)) - (len(corr_23_short_mod))/2
    n_13 = corr_13_short_mod.index(max(corr_13_short_mod)) - (len(corr_13_short_mod))/2
    n_12 = corr_12_short_mod.index(max(corr_12_short_mod)) - (len(corr_12_short_mod))/2

    x_t = bml.determineX(x_12,x_13,x_23, n_12, n_13,n_23, f_s,a)
    vinkel = bml.calculateAngle(n_21 = n_12, n_31 = n_13, n_32 = n_23)

    if x_t < 0:
        vinkel = bml.calculateAngle(n_21 = n_12, n_31 = n_13, n_32 = n_23) + np.pi

    return vinkel