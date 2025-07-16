# Math-Funktion-Simulation-Software
This is a little special project. Written nearly entirely by Python it is practically a Programm made out of lot's of Scripts. Its a Powerfull and max-funktional (Math)Funktion-Visualisation Software that is no longer an minimalistic Example.
**A powerful, script‑based Python application for visualizing and analyzing mathematical functions.** it also has a set of predefined funktions, exponential, for transformers(elctric), sin and so on, a lot of them, just the names wxampl.: f(x) = ... .

---
<img width="1185" height="874" alt="image" src="https://github.com/user-attachments/assets/9bb33d4e-b573-4b31-b217-dc115f29b0b3" />

---

## Overview

This project provides an interactive GUI that lets users define, visualize and evaluate multivariate mathematical functions. It is no longer a minimal example—but a full‑featured core tool for exploring functions of any number of variables.

---
Python interpreter is required -just pack all the scripts in one Dir and run the Main.py
---

## Core Functionality

1. **Function Definition Interface**  
   - Users can enter any function `f(x, y, z, a, b, c, d, …)` using standard Python syntax.  
   - The GUI validates the expression and detects variable names automatically.  
   - A selectable “domain” (definition range) can be set for each variable before evaluation.

2. **Domain Selection Window**  
   - Specify lower/upper bounds (and step size) for each independent variable.  
   - Support for continuous ranges and discrete sets.  
   - Real‑time validation of domain consistency.

3. **Execution Trigger**  
   - A single “Compute” button launches the evaluation.  
   - Inputs are locked during computation to prevent accidental changes.

4. **Results Window**  
   - **Component Plots:** One graph per variable/component showing how the output varies.  
   - **Statistical Summaries:** Min, max, mean, standard deviation for each output dimension.  
   - **Domain vs. Range Table:** Side‑by‑side table listing each variable’s definition range and the corresponding computed output range.

---

## Workflow (User Perspective)

1. **Open Application**  
2. **Enter Function**  
   - Example placeholder: `f(x, z) = x**2 + sin(z)`  
3. **Define Domains**  
   - e.g. `x ∈ [–10, 10]`, `z ∈ [0, π]`  
4. **Press “Compute”**  
5. **Inspect Results**  
   - View plots and tables in the secondary window  
6. **Adjust & Recompute**  
   - Tweak domain or function and rerun as needed

---

## Next Steps
