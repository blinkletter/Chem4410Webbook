# 10: pH-Rate Profiles

**General** and **specific** acid/base catalysis are important catalytic strategies employed by enzymes. We will use the field of bio-organic chemistry to **model** enzyme reactions and investigate these catalytic tools. We will demonstrate interactive *Python* to **explore the math** of the *pH* rate profile and **calculate** kinetic parameters for the reactions involved.

<hr>

## Before

> **Read** Chapter 9.3 and 9.4 <br>
> **Attempt**  the following problems from Chapter 9:  6, 8, 11 \& 12

<hr>

## During

We will explore the example of **phenyl acetate hydrolysis**. We will derive the **rate law** for the system and interpret the ***pH*-rate profile**.

In class we will be using the following handout to guide our discussion.

>  **Handout**: The handout that will be made available in class can also be accessed [**here**](../Lesson_02/4410_Handout_11.pdf) \[PDF\]. This will be given to students in class. There is no need to print a copy.

<hr>

## After

After our class exercises, I highly recommend that you try the following problems

> **Attempt**  the following problems from Chapter 9: 4

<hr>

## Learning Goals
After participating in the before, during and after of this class meeting you will have explored the following learning goals of lesson \#2&hellip;

- Understand the difference between **specific and general** acid/base catalysis.
    - Describe the difference in **rate-determining step** and the structure of the **transition state** in each case.
    - Construct rate laws for **specific and general acid/base catalysis** and be able to interpret reaction kinetics to confirm the rate law.
- Be able to interpret a ***pH*-rate profile**.

<hr>

## Resources

I have used **other discussions** in this class meeting **in the past**. They may be helpful in interpretting today's exploration topic.

### Explorations

- [**Exploration: pH-rate Profiles in Ester and Carbonate Hydrolysis**](../Lesson_02/10-Ester-carbamate.pdf) \[PDF\] An exploration of pH-rate profiles for the hydrolysis of phenyl bacronates and phenyl esters.
- [**Exploration: The Changing Value of $K_w$**](../Lesson_02/10-KW_NIST_Exploration.pdf) \[PDF\] Like all equilibria, $K_w$ changes with temperature. There are tables af data available for values of $K_w$ at every temperature between 0 and 100 $^\circ C$. In this short exploration I attempt to interpret the literature for calculating the value of $K_w$ at any temperature and pressure.

### Python Plotting

We are continuing to explore the world of data analysis using *Python* tools. {ref}`Resources are presented in the main page for Lesson #2<L02PythonLink>` that provide an introduction to *Python* and examples to help you learn.

### Jupyter Notebooks

The following ***Jupyter* notebooks** are made available below via *Google* Colab. I may use some of these for calculations during the class meeting. 


- **pH-rate Profiles in Ester and Carbonate Hydrolysis**: The notebooks below provide the code and data analysis for the corresponding exploration described above.
    - [**Code from Handout**](../../notebooks/M10_Ester_Carbamate_pH-Rate_Profile/calcs.ipynb) \[via Colab\] This is the code presented in the handout.
    - [**Figures 5 to 10**](../../notebooks/M10_Ester_Carbamate_pH-Rate_Profile/pH-RateProfileEsters_MoreData.ipynb) \[via Colab\] Plots of pH-rate profiles for carbonates.
    - [**Figure 2**](../../notebooks/M10_Ester_Carbamate_pH-Rate_Profile/pH-RateProfileEsters-FancyPlots.ipynb) \[via Colab\] Plots of pH-rate profiles for diclofenac esters.
- [**The Changing Value of $K_w$**](../../notebooks/M10_Water_Ion_Product/water_ion_product.ipynb) \[via Colab\] This notebook produced the plots, interpolations and data analysis in the document exploring **Changing Value of $K_w$** vs temperature described above.

- **Recommendations for Plotting**: The notebooks above feature examples of curve fitting and plooting. I use several methods to do this, but from now on I am going to focus on a single approach using the *LMFit* package. The notebooks below explain how to use *LMFit*.
    - [**Plotting recommendations - Part 1**](../../notebooks/M11_Plot_Recommendations/01_SimplePlots.ipynb) \[via Colab\] An example of a linear plot using LMFit. This notebook details how to use *LMFit* to perform a linear fit and how to present the plot with confidence and prediction intervals.
    - [**Plotting recommendations - Part 2**](../../notebooks/M11_Plot_Recommendations/02_CurvePlots.ipynb) \[via Colab\] An example of a curve fit plot using LMFit. This notebook details how to use *LMFit* to perform a non-linear optimization to a model and how to present the plot with confidence and prediction intervals.
    - [**Plotting recommendations - Part 3**](../../notebooks/M11_Plot_Recommendations/03_TheRecipeForPlots.ipynb) \[via Colab\] This is a shorter example presenting a minimal workflow.

