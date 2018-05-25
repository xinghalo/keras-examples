import numpy as np
from keras.models import Sequential

model = Sequential()



a = np.array([[1,2],[3,4]])
sum0 = np.sum(a, axis=0)
sum1 = np.sum(a, axis=1)

print(sum0)
print(sum1)