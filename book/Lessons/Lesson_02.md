# Lesson 2: Acid/Base Equilibrium \& Reaction Kinetics

**Acids and bases** are core concepts in chemistry. We have seen many examples of reaction mechanisms that require **strongly acidic or basic** conditions. 

First we must learn about the world beyond the *pH* scale. What is the acidity of a mixture of 1% sulphuric acid in water? How would you calculate or **measure** it? Now, what is the acidity of a 99% mixture? Does *pH* have any meaning here? We need a way to measure the acidity of **very strong acid mixtures** so that we can use this value in **experiments**. You are now ready at last to learn the truth.

**Reaction Kinetics** are also an important tool for investigating mechanism. **Rate laws**, integrated rate **equations**, transition state **theory**, the **Arrhenius** and **Eyring** equations, and more are in your toolbox and ready to be deployed. We will create rate laws for **complex reactions** and plot the integrated rate laws using *Python* tools. We will consider how chemical kinetics experiments are **designed**. We will return to the idea of the **reaction coordinate** and explore how we can interpret the structure of the transition state using **Hammond's postulate**.  

Reactions that require **acid** will have **rates** dependant on the **activity** of acid (or base). One such **measure** of acid activity is *p*H. We will use the **rate law** for a reation that requires acid and/or base to interpret a **pH-rate profile**.

<hr>

## Lesson Schedule

This lesson will take place over **six class meetings** and will begin with **review** of acid/base equilibria and cpmplex rate laws. 

### Class Meetings

The information for each of these class meetings can be accessed directly by the links in the sidebar.

6. **Review of Bronsted Theory**
    - We will review the math of **acid-base equilibria** and the Henderson-Hasselbalch equation. We will explore *pH* as a score of acidity of a system and extend the scale to infinity in both directions using other **acidity functions**.
7. **Structure and *pK<sub>a</sub>***
    - The *pK<sub>a</sub>* value of a group can be altered by **changing the structure** of the molecule or the nature of the surrounding **environment**. Here is a first step in **correlating** structure with chemical properties.
8. **Review of Reaction Kinetics \& Catalysis**
    - Rate laws allow us to predict reaction rates. We will explore **rate laws** involving catalysis.
9. **General \& Specific Catalysis**
    - We will define the different **types of acid/base catalysis** and explore cases in reactions we already know.
11. **Brønsted Plots**
    - When **proton transfer** is involved in a reaction mechanism we can identify if it occurs **before, during or after** the rate-determining step using a Brønsted plot.
10. **pH-Rate Profiles**
    - The apparent **rate constant** of a reaction can **change with *pH*** if acid/base catalysis is involved. We can discern mechanistic information by ploting rate vs. *pH*.

### Assignments

Each lesson includes one or more assignments. **Check the page** for each of the two assignments for this lesson. Check the **due dates** and make a plan so that you can complete each assignment with time to spare.

2. **Assignment \#2**
    - This assignment will have you discuss the **core tenets** of physical organic chemistry.
3. **Assignment \#3**
    - This assignment have you **interpret** a Brønsted plot. You will start with the rate **data** and will exercise your skills in **data analysis** as part of the exercise.

<hr>

## Learning Goals

After completing this lesson by **reading** the suggested textbook sections, **practicing** the problems, **participating** in class exercises and performing the **activities** of the assignments, you should be able to&hellip;

- Understand that *pH* is an **acidity function**.
- Understand **how** the Hammett acidity function **is determined** for various acid mixtures.
- Determine the **extent of protonation** of a reactant at various *pH* or *H<sub>0</sub>* values.
- **Calculate** the *pK<sub>a</sub>* of a reactant from equilibrium data.
- Understand the **effect of resonance, induction, steric strain and electrostatic effects** on the *K<sub>a</sub>* value of an acidic functional group.
- Be able to **predict** which of two related acids is stronger and explain why.
- Understand the role of **solvent** in determining the *K<sub>a</sub>* value of an acidic functional group.
- Identify the likely **rate-determining step** in a reaction and construct a **rate law** from a reaction scheme.
- **Define and apply** the Hammond postulate, the reactivity-selectivity principle, microscopic reversibility and the Curtin-Hammett principle.
- Describe how to use the idea of **kinetic vs. thermodynamic control** to provide a strategy for maximizing the yield of desired reaction products.
- **Design an experiment** to investigate reaction kinetics in a given reaction
- **Construct** a rate law from a **complex reaction scheme** using the pre-equilibrium
assumption of steady-state assumption.
- Be able to **interpret data** from reaction kinetics **experiments**.
- Describe the various ways that a reaction can be **catalyzed** and understand how the reaction coordinate is changed with catalysis.
- Construct a **rate law** for a catalyzed reaction.
- Understand the difference between **specific and general** acid/base catalysis.
    - Describe the difference in **rate-determining step** and the structure of the **transition state** in each case.
    - Construct rate laws for **specific and general acid/base catalysis** and be able to interpret reaction kinetics to confirm the rate law.
- Be able to interpret a ***pH*-rate profile**.
- Understand the **Brønsted relationship** in acid/base catalysis and how **Brønsted plots** can be used to investigate acid/base catalyzed reactions.

That seems like a lot, but it is **mostly review** of your skills from Physical Chemistry. 

<br>

## Resources 

You may find the following resources **useful** as you explore the ideas for this week's lesson. **Links** to these resources are available below. All of these resources **appear** in the class meeting pages and are **collected** here for your convenience. The most important resource in this course will be your **textbook**, but always look for more.

### Textbook Resources

These **resources** are directly related to this lesson and may be assigned reading.  

Over the five class meetings you will be asked to read the following textbook sections. 

> **Readings**: Chapters 5.1 to 5.3 (27 pages), 5.4 (9 pages), 7.1 to 7.5 (41 pages), 9.1 to 9.3 (34 pages), 9.4 (7 pages), 8.5 (3 pages).

That is **121 pages** in total. Over the **ten business days** of this lesson you will need to read about **12 pages a day**. Most of it is **review**. There are a lot of pictures and tables, so it's not as much as it looks like.

### Resources from Me

These are **extra resources** intended to provide more information for reviewing your previous organic chemistry. Below are a series of reviews of topics in organic chemistry that I have written for my students over the years.

- [**Acid-Base Tutorial**](./Lesson_02/08-T9-Acid-Base.pdf) \[PDF\] I wrote this review for my biochemistry class several years ago. It may be useful in **reviewing the basics** of acid-base equilibria.

- [**Integrating Rate Equations**](./Lesson_02/09-T21-Integrating_Simple_Rate_Equations.pdf) \[PDF\] I wrote this document several **years ago** for my physical organic class as a review of previous topics in **reaction kinetics**. It presents the basics of creating a rate law and integrating it to obtain an equation that relates the concentration of reactants (or products) to time. Such equations will enable you to obtain **rate constants** from conc. vs. time data.

### pKa data Tables

These tables contain many entries for acids in water and DMSO. 

- [**Williams’ Compilation of *pK<sub>a</sub>* Tables**](https://organicchemistrydata.org/hansreich/resources/pka/) \[Web\] This is a famous compilation of *pK<sub>a</sub>* data assembled by R. Williams based on an earlier compilation by Westheimer & Jencks.
- [**Reich’s *pK<sub>a</sub>* Table**](https://organicchemistrydata.org/hansreich/resources/pka/) \[Web\] This is a compilation of *pK<sub>a</sub>* data curated by Hans Reich. These values are mostly from the famous Bordwell table of *pK<sub>a</sub>* values in DMSO.  
- [**Evans’ *pK<sub>a</sub>* Table**](https://organicchemistrydata.org/hansreich/resources/pka/) \[Web\] This is a shorter version of Reich’s compilation of DMSO *pK<sub>a</sub>* data combined with corresponding water *pK<sub>a</sub>* data from Williams’ table. 
- [**A Short *pK<sub>a</sub>* Table**](https://cactus.utahtech.edu/smblack/chem2310/summary_pages/pKa_chart.pdf) \[Web\] This is a compilation of *pK<sub>a</sub>* data curated by Sarah Black. This table focuses on general cases of functional groups and will give a quick survey of *pK<sub>a</sub>* values. 
- [**Another Short *pK<sub>a</sub>* Table**](https://myersorganic.netlify.app/2511_Files/Chapter3-pKa%20table.pdf) \[Web\] This is a compilation of *pK<sub>a</sub>* data curated by Brian Myers. This table focuses on general trends in functional groups. 

(L02PythonLink)= 
### A Bit of Python

In some of the class meetings we will be **plotting data** in class to make a point. We could use MS Excel very easily. However, it is time to start considering more versatile and **powerful tools** available via the ***Python*** programming language and its ecosystem. In class, I will do all my coding using AI tools. We are not programmers. Below is a great website for starting in *Python* in chemistry.

- **[Scientific Computing for Chemists with Python](https://weisscharlesj.github.io/SciCompforChemists/notebooks/introduction/intro.html)** \[Web via GitHub\] This is a web textbook produced by Charles J. Weiss. It is an excellent way to learn the basics of *Python* and the many tools available for chemists.


Below are some **websites** that I have made over the years **to help** my students navigate *Python.* 

- **[Documenting Data Analysis](https://blinkletter.github.io/PythonPresentation/start.html)** \[Web via GitHub \& Colab\] I created this website to support a presentation in the departmental seminar series in which I argued that we all should use *Python* notebooks to document our data analysis and plots. Feel free to steal everything.

- **[Math \& *Python*](https://blinkletter.github.io/MathWithPython/start.html)** \[Web via GitHub \& Colab\] I created this website to show students how to use *Python* as your calculator. If you use a *Python* notebook you can document all your math to help your future self when you need to repeat a calculation. You can reuse the code to repeat the same calculation with different data and save time. You can find your error and then recalculate without needing to repeat every step. 

- **[Steal This Code](https://blinkletter.github.io/StealThisCode/start.html)** \[Web via GitHub \& Colab\] This is another website that I created to present more examples of using *Python* to perform calculations and data analysis. Steal it all.


You do not have to learn *Python* -- but you do need to learn what it can **make possible**. You will then learn **what you need when you need** it as you progress in you career.

###  Truth and Reconcilliation Day

This year it will impact our class as it falls on a Wednesday,  however **Truth & Reconcilliation Day** is not a holiday. Time to do the work.

I suggest that you complete the following reading and think about how our shared past affects our present and our future.

- **Read "[Where are the Children Buried?](https://ehprnh2mwo3.exactdn.com/wp-content/uploads/2021/05/AAA-Hamilton-cemetery-FInal.pdf)"** \[Web\] available from the [**National Centre of Truth and Reconcilliation**](https://nctr.ca/) \[Web\].

