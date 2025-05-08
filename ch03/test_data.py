import pandas as pd
import numpy as np

print(pd.__version__)  # Print Pandas version
print(np.__version__)  # Print NumPy version
data = pd.DataFrame({"A": np.random.rand(10)})
print(data)
