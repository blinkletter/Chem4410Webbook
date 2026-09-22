# Python Collection

This page contains **links** to all the *Python* resources that I developed for calculations, plotting and data analysis. Its mostly **just for myself** so I can find it all again easily. But you **might find it useful**. If not now, then perhaps in graduate school. **Clone** the *github* repository and take it all with you.

The collection contains *Python* notebooks and *Jupyter* web-books that are connected to specific **lessons**, subject **explorations** and **examples** presented during the course. 

The **web-books** are served from github.com or from the UPEI server that supports this course information web-book on **moodle**. You would only have access to the UPEI pages while registered in this course, so **steal them** early. The notebooks are available on *Google colab* via the *github* repository so you can access them at any time as long as you **save** the link or clone the repository. **Steal** it all. Ask me how; I will help. That is the way knowledge progresses.

## *Python* Web-books

The following resources are web-books served from github.com. I wrote them for various classes and presentations in the past and regularly steal from them when making new projects. Who needs AI when you have cut-and-paste?

- [**Chem 4410 Notebooks**]( https://blinkletter.github.io/4410PythonNotebooks/) \[Web\] This is a web-book version of most of the *Google colab* **notebooks** listed in the section below. 
- [**Steal This Code**](https://blinkletter.github.io/StealThisCode/) \[Web\] A **collection** of code; much of it is **repeated** in other web-books linked here. Some of it **might be useful**.
- [**Data Analysis in *Python***](https://blinkletter.github.io/PythonPresentation/start.html) \[Web\] This web-book explores how to present data using *Python* for **fitting** models and presenting **plots**. It includes depicting **error bars** and **confidence** intervals. 
- [**Math with *Python***](https://blinkletter.github.io/MathWithPython/start.html) \[Web\] Some **examples** of common math used in **chemistry** are interpreted using *Python* rather than my eleven-dollar calculator. Calculators are so old-school. Why not use *Python* for all your **calculations** so that you methodology is **documented** and any errors can be found and corrected **easily** by others. No one know what my fat fingers did on my calculator but everyon can find my typos in *Python* (for practice, find the typo in this paragraph.) 
- [**Simplified Hückel Molecular Orbitals**](https://blinkletter.github.io/SHMOT/start.html) \[Web\] In this course, we used to spend a week on matrix math to interpret molecular orbitals of conjugated systems. It didn't seem to be a great value in the end so I dropped it. We now use the [**Hulis web app**](https://ctom-ism2.github.io/hulis/index.shtml) \[Web\] from Aix-Marseille Université in France.
- [**Using *GAMESS***](https://blinkletter.github.io/UsingGAMESS/start.html) \[Web\] Once I had students attempt to **install** *GAMESS* on their personal computers and use it in this course. What was I thinking? Too much time was spent in **trouble shooting** when I could just have easily presented the **graph** that would result instead. The old instructions are **archived** in this web-book for those who want to make a personal **project** of it.
- [**Biochem Web-Book**](https://blinkletter.github.io/3530Biochem/) \[Web\] This web-book contains pages and *Python* code that I used in my **biochemistry** course. There might be some stuff **worth stealing** and using for this course. Always **steal**; never re-invent a wheel.

## Colab Notebooks Listed by Class Meeting

### Lesson 2

- [**Catenary Curve Calculations**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_09/CatenaryCurve.ipynb) \[via Colab\]. This is a Jupyter notebook for creating a plot catenary curve. This is a mathematical model for a hanging rope and I used it to create diagrams for the Hammond postulate. Take a look if you are interested.

- [**Numerical Methods using *Python***](https://www.southampton.ac.uk/~fangohr/teaching/python/book/html/16-scipy.html) \[Web\] A short tutorial focusing on numeric integration methods. 

- [**Mathematical *Python***](https://patrickwalls.github.io/mathematicalpython/) \[Web\] An introduction to mathematical computing using *Python*.

- [**StackExchange**](https://scicomp.stackexchange.com/questions/24066/solve-rate-equations-with-different-reaction-orders-using-scipy-ode) \[Web\] No one programs anymore. The whole world is run on code copied from StackExchange and similar websites. This is where ChaGPT copied all its "knowledge from" for coding. that is just one example of from where I stole the code for numerical intergration. Never re-invent a wheel. Steal and give credit; it's not plagiarism if we acknowledge the source.

-----

### Meeting \#6

- [**Hammett Acidity Function of Nitric Acid**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_08/HNO3_Acidity_Function.ipynb) \[via Colab\] Plot a set of data for the Hammett acidity function of various mixtures of nitric acid and water. Then use a interpolation to estimate the $H_0$ at any concentration. 
- [**Hammett Acidity Function Using Indicators**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_08/HNO3_Acidity_Function_Calcs.ipynb) \[via Colab\] Calculate the acidity function of various mixture of nitric acid using aninline indicators. Moving step-by-step, we can begin with indicators of unknown $pK_a$ values and move thorugh mixtures of increasing acidity to determine the $H_0$ value of 100% $\rm HNO_3$ 
- [**A Workbook for a Textbook Problem**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_08/Question5_13.ipynb) \[via Colab\] Let a *Python* notebook be your well-documented calculator. Here is a notebook set up to help solve the math in problem 13 of chapter 5. 
- [**Tables of Acidity Functions**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_08/H0_Data.ipynb) \[via Colab\] This is exactly the same as the first notebook in the list above except it contain data for many different acid/water mixtures. You can select a different acid by chaning the filesname of the data set. 


-----

### Meeting \#7

- [**An Example of Correlations**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_08/Correlations.ipynb) \[via Colab\] We would expect the $pK_a$ values of acids to correlate in different solvents. There should be a proportional relationship and there is -- except when there isn't. Explore your first example of correlation studies in this course. there will be many more. <br>
- [**A Look Ahead to Kinetics**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_08/LookAheadToKinetics.ipynb) \[via Colab\] Reaction kinetics are math. Python notebooks are great at keeping track of your math.


-----

### Meeting \#8

- [**Reactions Kinetics Webbook**](https://blinkletter.github.io/StealThisCode/6_PhysOrgExamples/6_0_Introduction.html) \[via GitHub\]. This is a Jupyter webbook created from several Jupyter notebooks. You can run the notebooks in Google Collab by clicking on the "rocket" icon at the upper right corner of the page. You can also download the notebook for any page of the book by using the download link. It is currently part of the [**Steal This Code**](https://blinkletter.github.io/StealThisCode/) \[Web\] collection.


-----

### Meeting \#10

- [**Acid Catalysis Notebook**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_19_Ester_Carbonate_pH_profile/pH-RateProfileEsters.ipynb) \[via Colab\] 
- [**The Changing Value of $K_w$**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_10/water_ion_product.ipynb) \[via Colab\]
- [**Aspirin Hydrolysis Calculations**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_10/aspirin_notebook_with_uncertainty.ipynb) \[via Colab\] This is a Jupyter notebook and data sets that were used to create the plots for the aspirin pH-rate profiles presented in the discussion in the handout above. If you look through it you will see how all the math, plots and curve fits are described and documented in text and in code. Anyone can now see exactly how I produced the diagrams.

----

### Meeting \#12

- Explore this [**Jupyter notebook**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_14/Table1and2_ClassExamples.ipynb) \[via Colab\] that contains the code and data for plotting and interpreting Hammett plots of acid and base-catalyzed hydrolysis of esters based on data in **table 1 and table 2 of the handout**. It should be examined before class as you complete questions 1 through 6 in the handout.
- [**Plots of table 4 data**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_14/Table_4_Plots.ipynb) \[via Colab\] 
- [**Plots of table 5 data**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_14/Table_5_Plots.ipynb) \[via Colab\] 

-------

### Meeting \#13

- Explore this [**Jupyter notebook**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_14/Table1and2_ClassExamples.ipynb) \[via Colab\] NEEDS UPDATING that contains the code and data for plotting and interpreting Hammett plots of acid and base-catalyzed hydrolysis of esters based on data in **table 1 and table 2 of the handout**. It should be examined before class as you complete questions 1 through 6 in the handout.
- [**Plots of table 6 data**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_14/Table_6_Plots.ipynb) \[via Colab\] 
- [**Plots of table 7 data**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_14/Table_7_Plots.ipynb) \[via Colab\] 
- [**Brown-Okamoto Jupyter notebook**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_15/15-BrownOkamoto_Python_Notebook.ipynb) \[via Colab\] 
- [**Yukawa-Tsuno Jupyter notebook**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_15/15-YukawaTsunoFitNotebook.ipynb) \[via Colab\] 

------

### Meeting \#14

- Explore the [**jupyter notebook**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_16/16_Class_Handout_Problems.ipynb) \[via Colab\] that presents the code and plots in data plots handout \#3
- Explore the [**jupyter notebook**](https://colab.research.google.com/github/blinkletter/4410PythonNotebooks/blob/main/Class_16/16-EstroneSyn.ipynb) \[via Colab\] that contains the code and data for the plots presented in the handout.


