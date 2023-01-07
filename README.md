# CRITIC_cross-efficiency_DEA Application to Kao (2015)
Kao (2015) [^1] evaluated the physic department of twenty universities by the hierarchical data envelopment analysis(DEA) model. Based on the network DEA, the department system is 
decomposed into four subordiantes 
1. $E^{U}$ (teaching of undergarduates)
2. $E^{G}$ (teaching of graduates)
3. $E^{R}$ (research)  
4. $E^{S}$ (services)

Below is a diagram depicting a hierarchical network structure with **2** inputs and 
**7** outputs.
<img width="451" alt="Screenshot 2023-01-07 at 17 46 17" src="https://user-images.githubusercontent.com/76271974/211163720-4a1e64ba-1bba-45fd-ad84-f82cbba54af1.png">

Taking the resource-allocation problem between the undergraduate and graduate sections,
Kao (2015) defined the following shared-inputs hierarhical network DEA model after 
decomposititon.

<img width="392" alt="Screenshot 2023-01-07 at 17 58 34" src="https://user-images.githubusercontent.com/76271974/211164198-4e633dbe-6b81-4370-8470-705bf5881f60.png">

Note that $\alpha_{1},\alpha_{2},\alpha_{3}$ represent the allocating proportion of inputs 
to teaching (Unit 1), research (Unit2) and service (Unit3), while $\beta_{1}, \beta_{2}$ 
indicate the allocation proportion for undergraduate (Unit 1-1)and graduate divisions 
(Unit 1-2). 

In above model, the first five constraints control the efficiency range of the overall 
inputs and four units - _the efficiency of each unit should be no greater than 1_. And the fifth constraint defines the range of  allocation indexes $\alpha_{1},\alpha_{2},\alpha_{3}$ , $\beta_{1}, \beta_{2}$.Then, let's see the model result by Kao (2015).

<img width="558" alt="Screenshot 2023-01-07 at 17 41 55" src="https://user-images.githubusercontent.com/76271974/211163543-fc0d7cfb-2757-4721-98b4-f33599b15d48.png">

The second column in the table above is the network DEA result by CCR model, in which over
half of DMUs are evaluated as efficient. Compared with CCR model result, the result in
the third column shows better discrimintory power.

However, there are three issues exist:
1. lacking of peer-evaluated result, making the result less acceptable by DMUs.
2. The subordinate efficiency 
3.

[^1]: Kao, C. (2015). Efficiency measurement for hierarchical network systems. Omega, 51, pp.121–127. doi:10.1016/j.omega.2014.09.008.
 
