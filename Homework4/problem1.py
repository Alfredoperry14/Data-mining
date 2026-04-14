import numpy as np
# There are 5 yes and 3 no for the breakpoint at less than 72.5
# There are 4 yes and 2 no for the breakpoint greater than 72.5


less_than = -5/8*np.log2(5/8) - 3/8*np.log2(3/8)
greater_than = -2/6*np.log2(2/6) - 4/6*np.log2(4/6)


ans = 8/14*less_than + 6/14*greater_than
print(ans)