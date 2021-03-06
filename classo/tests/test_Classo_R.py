import numpy as np
import matplotlib.pyplot as plt

from ..compact_func import (
    pathlasso,
    Classo
)

from ..solve_R1 import problem_R1, Classo_R1
from ..solve_R2 import problem_R2, Classo_R2
from ..solve_R3 import problem_R3, Classo_R3, pathlasso_R3
from ..solve_R4 import problem_R4, Classo_R4

from ..misc_functions import random_data


m, d, d_nonzero, k, sigma = 30, 20, 5, 1, 0.5
matrices, sol = random_data(m, d, d_nonzero, k, sigma, zerosum = True, seed = 10)

d1 = d//2
w = np.array( [0.9]*d1 + [1.1]*(d-d1))

"""
Test of Classo 
"""


def test_Classo_R1_all_methods_match():
    
    lam = 0.05
    tol = 1e-2
    pb = problem_R1(matrices, "Path-Alg")
    beta_ref = Classo_R1(pb, lam)

    pb = problem_R1(matrices, "DR")
    beta = Classo_R1(pb, lam)
    print( np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) )
    assert  np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) < tol

    pb = problem_R1(matrices, "P-PDS")
    beta = Classo_R1(pb, lam)
    print( np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) )
    assert  np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) < tol


    pb = problem_R1(matrices, "PF-PDS")
    beta = Classo_R1(pb, lam)
    print( np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) )
    assert  np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) < tol

def test_Classo_R2_all_methods_match():

    rho = 1.345
    lam = 0.1
    tol = 1e-2
    
    pb = problem_R2(matrices, "Path-Alg", rho)
    beta_ref = Classo_R2(pb, lam)

    pb = problem_R2(matrices, "DR", rho)
    beta = Classo_R2(pb, lam)
    print( np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) )
    assert  np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) < tol

    pb = problem_R2(matrices, "P-PDS", rho)
    beta = Classo_R2(pb, lam)
    print( np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) )
    assert  np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) < tol

    pb = problem_R2(matrices, "PF-PDS", rho)
    beta = Classo_R2(pb, lam)
    print( np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) )
    assert  np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) < tol

def test_Classo_R3_all_methods_match():
    
    lam = 0.1
    tol = 1e-2
    pb = problem_R3(matrices, "Path-Alg")
    beta_ref, s_ref = Classo_R3(pb, lam)

    pb = problem_R3(matrices, "DR")
    beta, s = Classo_R3(pb, lam)


    print( np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) )
    
    assert  np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) < tol

def test_Classo_R4_all_methods_match():

    lam = 0.1
    rho = 1.345
    tol = 1e-2
    pb = problem_R4(matrices, "Path-Alg", rho)
    beta_ref, s_ref = Classo_R4(pb, lam)

    pb = problem_R4(matrices, "DR", rho)
    beta, s = Classo_R4(pb, lam)

    print( np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) )

    assert  np.sum(abs(beta_ref-beta))  /  np.sum(abs(beta_ref)) < tol
