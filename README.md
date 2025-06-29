Stochastic Gradient Descent for Diabetes Risk Prediction
Overview
This project implements a Stochastic Gradient Descent (SGD) algorithm from scratch to model the relationship between daily sugar intake (g/day) and diabetes risk (%) using synthetic data. The model employs linear regression, optimized via SGD, to predict diabetes risk based on sugar consumption. The implementation includes data generation, model training, and visualization of results, making it an educational tool for understanding SGD in a biological context.
The synthetic dataset simulates 20 samples, where diabetes risk is modeled as a noisy linear function of sugar intake, reflecting a simplified biological relationship between high sugar consumption and increased diabetes risk.
Features

Generates synthetic data for 20 samples of sugar intake (50–200 g/day) and corresponding diabetes risk.
Implements SGD to optimize linear regression parameters (slope and intercept).
Visualizes:
Scatter plot of sugar intake vs. diabetes risk with the fitted regression line.
Loss curve (mean squared error) over training epochs.


Lightweight and easy-to-understand code for learning purposes.

Requirements

Python 3.6+
NumPy (pip install numpy)
Matplotlib (pip install matplotlib)

Install dependencies:
pip install numpy matplotlib

Installation

Clone the repository:git clone https://github.com/Dhrupad210/stochastic-gradient-descent-for-diabetes.git


Navigate to the project directory:cd stochastic-gradient-descent-for-diabetes



Usage

Run the main script:python sgd_diabetes.py


The script will:
Generate synthetic data for sugar intake and diabetes risk.
Train a linear regression model using SGD.
Output the learned slope and intercept to the console.
Display two plots:
Data Plot: Sugar intake vs. diabetes risk with the fitted regression line.
Loss Plot: Mean squared error over 1000 epochs.





File Structure

sgd_diabetes.py: Core script containing data generation, SGD implementation, and visualization logic.

Example Output

Console:Learned slope: 0.298
Learned intercept: 10.123


Plots:
Scatter plot with a red regression line showing the relationship between sugar intake and diabetes risk.
Line plot showing the convergence of the mean squared error during training.



Biological Context
The project uses a simplified model to explore how high sugar intake may correlate with increased diabetes risk. While the data is synthetic, it mimics a plausible scenario where excessive sugar consumption contributes to higher risk, with added noise to represent real-world variability (e.g., genetic factors, lifestyle).
