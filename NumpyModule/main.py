
#                            NUMPY MODULE

#Example 1 :
"""
import numpy as np 
X=np.linspace(0,6,7)  # length of beam 6m is divided into 7 equals parts(Final Value Exists)
W=5
M=W*(X**2)/2  # bedning moment function, M=5X
print(M)
"""

#                                TASK 1 
"""
import numpy as np
X=np.linspace(0,10,11)
W=8
M=W*(X**2)/2
print(f"Max. Bending Moment     : {M.max():.3f} KNM")
print(f"Min. Bending Moment     : {M.min():.3f} KNM")
print(f"Mean Of Bending Moment  : {M.mean():.3f} KNM")
print(f"Sum Of Bending Moment   : {M.sum():.3f} KNM")
"""

#                             INDEXING AND SLICING 

#                                TASK 2 
"""
import numpy as np
X=np.linspace(0,10,11)
W=8
M=W*(X**2)/2
print(f"Moment at midspan : {M[5]} KNM")
print(f"First three moments are : {M[:3]} KNM")
print(f"Moments greater than 30 KNM are : {M[M>30]} KNM")
"""

#                        np.zeros() and np.ones()

#                                 TASK 3
"""
import numpy as np
W=5
X=np.linspace(0,10,11)
M=np.zeros(len(X))
M = W*(X**2)/2
print(f"The array : {M}")
"""
