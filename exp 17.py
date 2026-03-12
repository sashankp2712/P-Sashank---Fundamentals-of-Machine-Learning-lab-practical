# Mobile Price Prediction using Linear Regression

ram = [2,4,6,8,12]
price = [8000,12000,18000,25000,35000]

n=len(ram)

mean_x=sum(ram)/n
mean_y=sum(price)/n

num=0
den=0

for i in range(n):
    num+=(ram[i]-mean_x)*(price[i]-mean_y)
    den+=(ram[i]-mean_x)**2

b1=num/den
b0=mean_y-b1*mean_x

print("Model: price =",b0,"+",b1,"* RAM")

x=float(input("Enter RAM: "))
prediction=b0+b1*x

print("Predicted Mobile Price:",prediction)
