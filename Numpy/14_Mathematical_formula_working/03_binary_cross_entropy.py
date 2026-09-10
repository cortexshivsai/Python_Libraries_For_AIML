import numpy as np
n=int(input("Enter Number of samples:"))
actual=np.random.randint(0,2,n)
predicted=np.random.uniform(0,1,n)
def bce(actual,predicted):
    f1=(-1/n)*((actual*np.log(predicted))+((1-actual)*(np.log(1-predicted))))
    print("Binary Cross Entropy:\n ",f1)
    f=np.mean((-1/n)*((actual*np.log(predicted))+((1-actual)*(np.log(1-predicted)))))
    print("Average Binary Cross Entropy: ",f)

bce(actual,predicted)    


