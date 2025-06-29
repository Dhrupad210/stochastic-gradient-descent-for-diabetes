# Stochastic Gradient Descent for Diabetes Risk Prediction

## 🧠 Overview

This project demonstrates a simple **Stochastic Gradient Descent (SGD)** implementation from scratch to model the relationship between **daily sugar intake (g/day)** and **diabetes risk (%)** using synthetic data. By applying **linear regression**, this educational tool helps learners understand how SGD can be used in a biological context to predict health risks based on lifestyle choices.

  

## 📊 Features

- 🧪 **Synthetic Dataset**: Generates 20 samples simulating sugar intake (50–200 g/day) and corresponding diabetes risk.
- ⚙️ **SGD Implementation**: Trains a linear regression model to fit a noisy linear relationship.
- 📈 **Visualizations**:
  - **Scatter plot** of sugar intake vs. diabetes risk with a fitted regression line.
  - **Loss curve** showing mean squared error across training epochs.
- 🧵 Lightweight and well-commented code — great for beginners!

  

## 🔧 Requirements

- Python 3.6+
- NumPy
- Matplotlib

Install dependencies with:

```bash
pip install numpy matplotlib
```

  

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Dhrupad210/stochastic-gradient-descent-for-diabetes.git
cd stochastic-gradient-descent-for-diabetes
```

  

## 🏃 Usage

Run the script using:

```bash
python sgd_diabetes.py
```

What it does:

- Simulates synthetic data
- Trains a linear regression model via SGD
- Prints the learned model parameters
- Displays:
  - A scatter plot with the regression line
  - A loss curve showing training convergence

## 📂 File Structure

```
stochastic-gradient-descent-for-diabetes/
├── sgd_diabetes.py         # Core script: data generation, model training, visualization
└── README.md               # Project documentation
```

## 🖥️ Example Output

### Console:
```
Learned slope: 0.298
Learned intercept: 10.123
```

### Plots:

- 📍 **Scatter Plot**:
  - X-axis: Sugar Intake (g/day)
  - Y-axis: Diabetes Risk (%)
  - Includes the learned linear fit (red line)

- 📉 **Loss Curve**:
  - X-axis: Epochs (up to 1000)
  - Y-axis: Mean Squared Error (MSE)
  - Shows how the model learns over time

  

## 🧬 Biological Context

Though the dataset is synthetic, it reflects a realistic pattern: **high sugar intake is associated with increased diabetes risk**. Noise is added to simulate real-world biological variability — like genetics, activity level, or diet. This project helps illustrate how even simple models can yield insights into health data.

  

## 📘 License

This project is open-source and freely available for educational and research purposes.

  

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue to discuss improvements or enhancements.

  

## ✨ Author

**Dhrupad Banerjee**  
GitHub: [@Dhrupad210](https://github.com/Dhrupad210)

  
