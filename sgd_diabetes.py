import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data: 20 samples of sugar intake (g/day) vs. diabetes risk (%)
np.random.seed(42)
sugar_intake=np.random.uniform(50,200,20)
diabetes_risk=0.3*sugar_intake+np.random.normal(0,5,20)+10

# Stochastic Gradient Descent implementation
def sgd_linear_regression(X,y,lr=0.0001,epochs=1000):
    m,b,n=0.0,0.0,len(X)
    losses=[]
    for epoch in range(epochs):
        indices=np.random.permutation(n)
        X_shuffled,y_shuffled=X[indices],y[indices]
        total_loss=0
        for i in range(n):
            xi,yi=X_shuffled[i],y_shuffled[i]
            y_pred=m*xi+b
            dm,db=-2*xi*(yi-y_pred),-2*(yi-y_pred)
            m-=lr*dm
            b-=lr*db
            total_loss+=(yi-y_pred)**2
        losses.append(total_loss/n)
    return m,b,losses

# Run SGD
slope,intercept,losses=sgd_linear_regression(sugar_intake,diabetes_risk)

# Print results
print(f"Learned slope: {slope:.3f}")
print(f"Learned intercept: {intercept:.3f}")

# Plot data and fitted line
plt.scatter(sugar_intake,diabetes_risk,color='blue',label='Data points')
plt.plot(sugar_intake,slope*sugar_intake+intercept,color='red',label='Fitted line')
plt.xlabel('Sugar Intake (g/day)')
plt.ylabel('Diabetes Risk (%)')
plt.title('Sugar Intake vs. Diabetes Risk')
plt.legend()
plt.show()

# Plot loss over epochs
plt.plot(losses)
plt.xlabel('Epoch')
plt.ylabel('Mean Squared Error')
plt.title('Loss over Epochs')
plt.show()
