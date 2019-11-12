import numpy as np 
import os
os.environ["OMP_NUM_THREADS"] = '8' 
os.environ["OPENBLAS_NUM_THREADS"] = '8' 
os.environ["MKL_NUM_THREADS"] = '8' 
os.environ["VECLIB_MAXIMUM_THREADS"] = '4' 
os.environ["NUMEXPR_NUM_THREADS"] = '4' 
import numpy as np
import time

np.show_config()

start_time=time.time()
a = np.random.randn(5000, 50000)
b = np.random.randn(50000, 5000)
ran_time=time.time()-start_time
print("time to complete random matrix generation was %s seconds" % ran_time)
np.dot(a, b)
print("time to complete dot was %s seconds" % (time.time() - start_time - ran_time))