# Assignment 4

## Exsecise 1.5
Author: 仲逸飞 
Student No.: 2014301020166 
Date: 2016/10/07

------

## Abstract
Consider again a decay problem with two types of nuclei A and B, but now suppose that nuclei of type A decay into ones of type B, while nuclei of type B decay into ones of type A. Solve this system of equations for the numbers of nuclei.

##Background
According to the Problem 1.5, we know the corresponding rate equation are

![picture 1](https://github.com/jsxhzyf/compuational_physics_N2014301020166/blob/master/Assignment_4/picture1.PNG)

where for simplicity we have assumed thet the two types of decay are characterized by the same time constant, .

##Main body
From the question and equations, we can deduce expressions for NA and  NB that (the derivation process is much and hard to input, so I just skip it here:

![picture 2](https://github.com/jsxhzyf/compuational_physics_N2014301020166/blob/master/Assignment_4/picture2.PNG)

where NA0 and NB0  are initial value of NA and NB . 
Substitute these results into the rate equations, then we can get the following formulas: 

![picture 3](https://github.com/jsxhzyf/compuational_physics_N2014301020166/blob/master/Assignment_4/picture3.PNG)

So far, we can use these formulas to sketch NA and NB  by coding.

##Code

```python
import pylab as pl
import numpy as np
class resonance:
    na = input('number_A = ')
    nb = input('number_B = ')
    tau = input('time_constant = ')
    td = input('time_of_duration = ')
    tp = input('time_step = ')
    def __init__(self, number_A = na, number_B = nb, time_constant = tau, time_of_duration = td, time_step = tp):
        #unit of time is second
        self.n_A = [number_A]
        self.n_B = [number_B]
        self.init_na = number_A
        self.init_nb = number_B
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        self.sum = number_A + number_B
        print("Initial number of nuclei_A ->", number_A)
        print("Initial number of nuclei_B ->", number_B)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)
    def calculate(self):
        for i in range(self.nsteps):
            tmp_A = self.n_A[i] + (self.sum/self.tau - 2*self.n_A[i]/self.tau)*self.dt
            tmp_B = self.n_B[i] + (self.sum/self.tau - 2*self.n_B[i]/self.tau)*self.dt
            self.n_A.append(tmp_A)
            self.n_B.append(tmp_B)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        pl.plot(self.t, self.n_A, 'b', label = "$N_{A}$")
        pl.plot(self.t, self.n_B, 'r', label = "$N_{B}$")
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        x = np.linspace(0, self.time, self.nsteps)  
        na_analytic = (self.init_na + self.init_nb) / 2 + 0.5 * (self.init_na - self.init_nb) * np.exp(-2 / self.tau * x)
        nb_analytic = (self.init_na + self.init_nb) / 2 - 0.5 * (self.init_na - self.init_nb) * np.exp(-2 / self.tau * x)
        pl.plot(x, na_analytic, 'b--', label = "theoretical value of $N_{A}$")
        pl.plot(x, nb_analytic, 'r--', label = "theoretical value of $N_{A}$")
        pl.legend()
        pl.show()
a = resonance()
a.calculate()
a.show_results()
```

Here we can set the initial value of number_A, number_B, time_constant, time_of_duration and time_step to satisfy different calculating requirements.

##Figure
When number_A = 300, number_B = 0, time_constant = 1, time_of_duration = 5 and time_step = 0.05, we can get the figure: 

![picture 4](https://github.com/jsxhzyf/compuational_physics_N2014301020166/blob/master/Assignment_4/picture4.PNG)

t is reasonable that if we set the time step dt  smaller, the simulation values will be closer to theoretical ones.

##Conclusion

In fact, errors always exist in calculating and plotting even precision drafting by computer. However, these errors can usually be controlled and reduced to a negligible level that not affect results.

##Acknowledgement
Thanks for DJ's help.







