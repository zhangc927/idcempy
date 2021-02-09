# IDCeMPy: Estimation of "Inflated" Discrete Choice Models

*Nguyen K. Huynh, Sergio Bejar, Nicolas Schmidt, Vineeta Yadav, Bumba Mukherjee*

<!-- badges: start -->

[![PyPI version fury.io](https://badge.fury.io/py/ziopcpy.svg)](https://pypi.org/project/ziopcpy/0.1.2/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/ziopcpy.svg)](https://pypi.org/project/ziopcpy/0.1.2/)
[![Downloads](https://pepy.tech/badge/ziopcpy)](https://pepy.tech/project/ziopcpy)
[![Project Status: Active â€“ The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
<!-- badges: end -->

**IDCeMPy** is a Python package which:

* Makes it easy to compose and fit ordered probit models when your discrete outcome variable is "inflated"  in either the zero or middle categories without (ZiOP/MiOPC) and with correlated errors (ZiOPC/MiOPC).    
* Fits inflated multi-nomial logit (iMNL) models that account for the preponderant (and heterogeneous) share
of observations in the baseline or any other lower category in unordered polytomous choice
outcomes.
* Allows you to easily compute the goodness-of-fit tests (AIC and Log-likelihood) and assess the performance (Vuong Test) of the "inflated" choice models with respect to standard ordered probit (OP) and multi-nomial logit (MNL) models. 

**IDCeMPy** uses Newton numerical optimization methods to estimate the "inflated" discrete choice models described above via Maximum Likelihood Estimation (MLE).  
**IDCeMPY** is compatible with [Python](https://python.org) 3.7+

## Getting Started

You can try **IDCeMPy** now by downloading it from GitHub or PyPi.
On [readthedocs](https://ziopcpy.readthedocs.io/) you will find the installation guide, a complete overview of all the fueatures included in **IDCeMPy**, and example scripts of all the models. 

## Why **IDCeMPy**?

Researchers in natural and social sciences typically use Ordered Probit (OP) and Multi-Nomial Logit (MNL) models when working with discrete outcome variables that have more than two categories.  Using those models, however, may lead to biased inferences when:

* The lowest category of the outcome variable presents an excess of "zeros" (i.e. Zero Inflation) that are generated from different d.g.p's.
* An excessive number of observations are in the middle categories of the outcome variable (i.e. Middle Inflation), and generated by distinct d.g.p's.
* The lower outcome categories incorporate an
excessive share and heterogeneous pool of observations. 
  
**IDCePy** combines two probability distributions by estimating two latent (split and outcome-stage)
equations in zero and middle inflated OP models, and MNL models with unordered outcome variables, allowing to statistically assess the inflated share
of observations in your ordered outcome variable.

## Functions in the **IDCePy** Package

| Function         | Description                                                                                                          |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| `opmod`; `iopmod`; `iopcmod` | fit the standard OP model, the zero-inflated and middle inflated OP models without correlated errors (ZiOP and MiOP), and the zero-inflated and middle inflated OP model with correlated errors (ZiOPC and MiOPC) respectively. |
|`opresults`; `iopresults`; `iopcresults`| Stores and presents the covariate estimates, the Variance-Covariance (VCV) matrix, and goodness-of-fit statistics (Log-Likelihood and AIC) of `opmod`, `iopmod`, and `iopcmod` respectively. |
| `iopfit`; `iopcfit`| Computes the fitted probabilities from the ZiOP, MiOP, ZiOPC and MiOPC models respectively.|
| `vuong_opiop`;  `vuong_opiopc` | Calculates the Vuong test statistic to compare the performance of the OP versus the ZiOP, ZiOPC, MiOP or MiOPC models respectively.|
|`bimnlmod` | fits and inflated multi-nomial Logit (BiNML) model.|
|`bimnlresults` | Stores and presents the covariate estimates, the Variance-Covariance (VCV) matrix, and the goodness-of-fit statistics (Log-Likelihood and AIC) of `bimnlmod`.|

## Dependencies
- scipy
- numpy
- pandas

## Installation

From [PyPi](https://pypi.org/project/ziopcpy/0.1.2/):

```sh
$ pip install ziopcpy
```

## Using the Package

We illustrate the functionality of **IDCePy** using data from the National Youth Tobacco Survey (2018) and XXXX (xxx). 

First, import `ZiopcPy`, required packages, and dataset.
```
from ziopcpy import ziopcpy
import pandas as pd
import urllib
url= 'https://github.com/hknd23/ziopcpy/raw/master/data/tobacco_cons.csv'
DAT= pd.read_csv(url)
```
We now specify arrays of variable names (strings) X, Y, Z.
```
X = ['age', 'grade', 'gender']
Y = ['cig_count']
Z = ['age']
```
In addition, we define an array of starting parameters before estimating the `ziopc` model. 
```
pstart = np.array([.1, .15, .001, .2, .3, .3, .001, .2, .01, .01])
```
The following line of code creates a `ziopc` regression object model.
```
ziopc_tob = iopcmod('ziopc', pstartziopc, data, X, Y, Z, method='bfgs',
                    weights=1, offsetx=0, offsetz=0)
```
The results of this example are stored in a class (`ZiopcModel`) with the following attributes:
  * *coefs*: Model coefficients and standard errors
  * *llik*: Log-likelihood
  * *AIC*: Akaike information criterion
  * *vcov*: Variance-covariance matrix

We, for example, can print out the covariate estimates, standard errors, *p* value and *t* statistics by typing:
```
print(ziopc_tobb.coefs)
```
```
              2.5%     97.5%      Coef        SE         p    tscore
cut1     -1.140210  2.643246  0.751518  0.965167  0.436192  0.778640
cut2     -1.209736 -0.130255 -0.669995  0.275378  0.014974 -2.433003
cut3     -2.769668  0.324247 -1.222711  0.789264  0.121339 -1.549179
cut4     -2.442634  1.208168 -0.617233  0.931327  0.507493 -0.662746
Z int    -2.158451  2.020689 -0.068881  1.066107  0.948484 -0.064610
Z age    -1.059072  1.024847 -0.017112  0.531612  0.974321 -0.032190
X age    -0.120082  0.254096  0.067007  0.095454  0.482689  0.701984
X grade  -0.447309  0.111297 -0.168006  0.142502  0.238408 -1.178975
X gender -2.421751  0.795825 -0.812963  0.820810  0.321959 -0.990439
rho      -1.575206  3.306348  0.865571  1.245294  0.487009  0.695073  
```
Or the Akaike Information Criterion (AIC):
```
print(ziopc_tobb.AIC)
```
```
16061.716497590078
```

## Reduced Specification of MiOPC?

## Reduced Specification of BiMNL?

```
from zmiopc import bimnl
url= 'https://github.com/hknd23/zmiopc/raw/main/data/replicationdata.dta'
DAT= pd.read_stata(url)
```
```
x = ['educ', 'party7', 'agegroup2']
z = ['educ', 'agegroup2']
y = ['vote_turn']

```
```
order = [0, 1, 2]
inflatecat = "baseline"
```
```
model_imnl = bimnl.imnlmod(DAT, x, y, z, order, inflatecat)
```
```
                         Coef        SE    tscore             p       2.5%     97.5%
Inflation: int       -4.935359  2.777219 -1.777087  7.555400e-02 -10.378709  0.507991
Inflation: educ       1.885751  0.292772  6.441013  1.186791e-10   1.311917  2.459585
Inflation: agegroup2  1.294584  0.768073  1.685497  9.189278e-02  -0.210839  2.800007
1: int               -4.180341  1.635800 -2.555534  1.060251e-02  -7.386509 -0.974174
1: educ               0.333869  0.185150  1.803240  7.135053e-02  -0.029024  0.696763
1: party7             0.454282  0.056826  7.994322  1.332268e-15   0.342904  0.565660
1: agegroup2          0.954140  0.248334  3.842172  1.219502e-04   0.467407  1.440874
2: int                0.900318  1.564316  0.575535  5.649298e-01  -2.165742  3.966379
2: educ               0.156604  0.202956  0.771618  4.403406e-01  -0.241189  0.554397
2: party7            -0.576827  0.058101 -9.927954  0.000000e+00  -0.690706 -0.462949
2: agegroup2          0.916346  0.234650  3.905154  9.416528e-05   0.456431  1.376260
```


 
