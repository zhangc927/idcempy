# IDCeMPy: Estimation of "Inflated" Discrete Choice Models

*Nguyen K. Huynh, Sergio Bejar, Vineeta Yadav, Bumba Mukherjee*

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
  
**IDCeMPy** combines two probability distributions by estimating two latent (split and outcome-stage)
equations in zero and middle inflated OP models, and MNL models with unordered outcome variables, allowing to statistically assess the inflated share
of observations in your ordered outcome variable.

## Functions in the **IDCeMPy** Package

| Function         | Description                                                                                                          |
| ---------------- | -------------------------------------------------------------------------------------------------------------------- |
| `opmod`; `iopmod`; `iopcmod` | fit the standard OP model, the zero-inflated and middle inflated OP models without correlated errors (ZiOP and MiOP), and the zero-inflated and middle inflated OP model with correlated errors (ZiOPC and MiOPC) respectively. |
|`opresults`; `iopresults`; `iopcresults`| Stores the covariate estimates, the Variance-Covariance (VCV) matrix, and goodness-of-fit statistics (Log-Likelihood and AIC) of `opmod`, `iopmod`, and `iopcmod` respectively. |
| `iopfit`; `iopcfit`| Computes the fitted probabilities from the model objects described avobe.|
| `vuong_opiop`;  `vuong_opiopc` | Calculates the Vuong test statistic to compare the performance of the OP versus the ZiOP, ZiOPC, MiOP or MiOPC models respectively.|
|`bimnlmod` | fits and inflated multi-nomial Logit (iNML) model.|
|`bimnlresults` | Stores and presents the covariate estimates, the Variance-Covariance (VCV) matrix, and the goodness-of-fit statistics (Log-Likelihood and AIC) of `bimnlmod`.|

## Dependencies
- scipy
- numpy
- pandas

## Installation

From [PyPi](https://pypi.org/project/ziopcpy/0.1.2/):

```sh
$ pip install IDCeMPy
```

## Using the Package

### Example 1: Zero-inflated Ordered Probit Models with Correlated Errors (ZiOPC)
We first illustrate how **IDCeMPy** can be used to estimate models when the ordered outcome variable presents "zero-inflation." 
For that purpose we use data from the 2018 [National Youth Tobacco Dataset](https://www.cdc.gov/tobacco/data_statistics/surveys/nyts/index.htm).  As mentioned above, **IDCeMPy** allows you to estimate "Zero-inflated" Ordered Probit models with and without correlated errors.

We demonstrate the use of a "Zero-inflated" Ordered Probit Model with correlated errors (ZMiOPC).  An example of the ZiOP model withou correlated erros can be found in the documentation of the package. 

First, import `IDCeMPy`, required packages, and dataset.
```
from idcempy import ziopcpy
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
pstart = np.array([.01, .01, .01, .01, .01, .01, .01, .01, .01, .01])
```
The following line of code creates a ziopc regression object model.
```
ziopc_tob = ziopcpy.iopcmod('ziopc', pstartziopc, data, X, Y, Z, method='bfgs',
                    weights=1, offsetx=0, offsetz=0)
```
If you like to estimate your model without correlated errors, you only substitute the parameter 'ziopc' for 'ziop'.


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
                          Coef        SE     tscore             p       2.5%      97.5%
cut1                   1.696160  0.044726  37.923584  0.000000e+00   1.608497   1.783822
cut2                  -0.758095  0.033462 -22.655678  0.000000e+00  -0.823679  -0.692510
cut3                  -1.812077  0.060133 -30.134441  0.000000e+00  -1.929938  -1.694217
cut4                  -0.705836  0.041432 -17.036110  0.000000e+00  -0.787043  -0.624630
Inflation: int         9.538072  3.470689   2.748178  5.992748e-03   2.735521  16.340623
Inflation: gender_dum -9.165963  3.420056  -2.680062  7.360844e-03 -15.869273  -2.462654
Ordered: age          -0.028606  0.008883  -3.220369  1.280255e-03  -0.046016  -0.011196
Ordered: grade         0.177541  0.010165  17.465452  0.000000e+00   0.157617   0.197465
Ordered: gender_dum    0.602136  0.053084  11.343020  0.000000e+00   0.498091   0.706182
rho                   -0.415770  0.074105  -5.610526  2.017123e-08  -0.561017  -0.270524
```
Or the Akaike Information Criterion (AIC):
```
print(ziopc_tobb.AIC)
```
```
16061.716497590078
```
`split_effects` calculates the change in predicted probabilities of the outome variable when 'gender_dum' equals 0, and when 'gender_dum' equals 1. The box plots below illustrate the change in predicted probablities using the values from the 'ziopc' dataframe.
```
ziopcgender = idcempy.split_effects(ziopc_tob, 1)
```



```
ziopcgender.plot.box(grid='False')
```



### Example 2: "Middle-inflated" Ordered Probit Models with Correlated Errors (MiOPC)
You can also use **IDCeMPy** to estimate "inflated" Ordered Probit models if your outcome variable presents inflation in the "middle" category. For the sake of consistency, we present below the code needed to estimate a "Middle-inflated" Ordered Probit Model with correlated errors. Data fot this example comes from Elgün and Tillman ([2007](https://journals.sagepub.com/doi/10.1177/1065912907305684)).   

First, load the dataset.
```
url= 'https://github.com/hknd23/zmiopc/raw/main/data/EUKnowledge.dta'
data= pd.read_stata(url)

```
Now, define the lists with names of the covariates you would like to include in the split-stage (Z) and the second-stage (X) as well as the name of your "middle-inflated" outcome variable (Y).
```
Y = ["EU_support_ET"]
X = ['Xenophobia', 'discuss_politics']
Z = ['discuss_politics', 'EU_Know_obj']
```
Run the model and print the results:
```
miopc_EU = ziopc.iopcmod('miopc', DAT, X, Y, Z)
```
```
print(miopc_EU.coefs)

                              Coef    SE  tscore     p   2.5%  97.5%
cut1                        -1.370 0.044 -30.948 0.000 -1.456 -1.283
cut2                        -0.322 0.103  -3.123 0.002 -0.524 -0.120
Inflation: int              -0.129 0.021  -6.188 0.000 -0.170 -0.088
Inflation: discuss_politics  0.192 0.026   7.459 0.000  0.142  0.243
Inflation: EU_Know_obj       0.194 0.027   7.154 0.000  0.141  0.248
Ordered: Xenophobia         -0.591 0.045 -13.136 0.000 -0.679 -0.502
Ordered: discuss_politics   -0.029 0.021  -1.398 0.162 -0.070  0.012
rho                         -0.707 0.106  -6.694 0.000 -0.914 -0.500
```
`ordered_effects()` calculates the change in predicted probabilities when the value of a covarariate changes. The box plots below display the change in predicted probabilities when Xenophobia increases one standard deviation from its mean value.
```
xeno = ziopc.ordered_effects(miopc_EU, 2, nsims=10000)
xeno.plot.box(grid='False')
```
![alt text](https://github.com/hknd23/zmiopc/blob/main/graphics/MiOPC_Xenophobia.png)

### Example 3: Estimation of "inflated" Multinomial Logit Models 
Unordered polytomous outcome variables sometimes present inflation in the baseline category, and not accounting for it could lead you to make faulty inferences.  But **IDCeMPy** has functions that make it easier for you to estimate Multinomial Logit Models that account for such inflation (iMNL).  This example shows how you can estimate iMNL models easily. 
Data comes from Arceneaux and Kolodny ([2009](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1540-5907.2009.00399.x))


We begin by importing the `bimnl` library and dataset.
```
from zmiopc import bimnl
url= 'https://github.com/hknd23/zmiopc/raw/main/data/replicationdata.dta'
data= pd.read_stata(url)
```
Define the outcome variable (y) covariates in the split-stage (z) and second-stage (x).
```
x = ['educ', 'party7', 'agegroup2']
z = ['educ', 'agegroup2']
y = ['vote_turn']

```
```
order = [0, 1, 2]
inflatecat = "baseline"
```
The following line of code estimates the "inflated" Multinomial Logit Model (iMNL).
```
imnl_2004vote = bimnl.imnlmod(data, x, y, z, order, inflatecat)
```
Print the est
```
                       Coef    SE  tscore     p    2.5%  97.5%
Inflation: int       -4.935 2.777  -1.777 0.076 -10.379  0.508
Inflation: educ       1.886 0.293   6.441 0.000   1.312  2.460
Inflation: agegroup2  1.295 0.768   1.685 0.092  -0.211  2.800
1: int               -4.180 1.636  -2.556 0.011  -7.387 -0.974
1: educ               0.334 0.185   1.803 0.071  -0.029  0.697
1: party7             0.454 0.057   7.994 0.000   0.343  0.566
1: agegroup2          0.954 0.248   3.842 0.000   0.467  1.441
2: int                0.900 1.564   0.576 0.565  -2.166  3.966
2: educ               0.157 0.203   0.772 0.440  -0.241  0.554
2: party7            -0.577 0.058  -9.928 0.000  -0.691 -0.463
2: agegroup2          0.916 0.235   3.905 0.000   0.456  1.376
```


 
