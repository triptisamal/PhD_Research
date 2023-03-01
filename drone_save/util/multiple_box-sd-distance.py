# Import libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Creating dataset
np.random.seed(10)
data1 = (
3.0 ,
6.164414002968976 ,
4.898979485566356 ,
3.0 ,
7.54983443527075 ,
0 ,
2.449489742783178 ,
3.7416573867739413 ,
3.3166247903554 ,
2.449489742783178 ,
5.0 ,
3.0 ,
4.47213595499958 ,
4.898979485566356 ,
4.123105625617661 ,
1.7320508075688772 ,
4.47213595499958 ,
1.0 ,
4.242640687119285 ,
5.744562646538029 ,
5.0990195135927845 ,
4.358898943540674 ,
4.123105625617661 ,
5.0 ,
5.0990195135927845 ,
3.605551275463989 ,
5.916079783099616 ,
4.58257569495584 ,
4.123105625617661 ,
1.0 ,
5.477225575051661 ,
4.358898943540674 ,
3.605551275463989 ,
2.23606797749979 ,
4.58257569495584 ,
6.0 ,
6.0 ,
1.7320508075688772 ,
2.23606797749979 ,
0 ,
3.7416573867739413 ,
5.0990195135927845 ,
6.708203932499369 ,
2.23606797749979 ,
0 ,
4.123105625617661 ,
4.123105625617661 ,
5.385164807134504 ,
5.830951894845301 ,
6.4031242374328485 ,
3.605551275463989 ,
2.23606797749979 ,
3.1622776601683795 ,
5.0 ,
5.0990195135927845 ,
2.449489742783178 ,
4.58257569495584 ,
3.3166247903554 ,
4.123105625617661 ,
3.4641016151377544 ,
5.196152422706632 ,
4.358898943540674 ,
3.1622776601683795 ,
3.1622776601683795 ,
5.916079783099616 ,
6.48074069840786 ,
3.4641016151377544 ,
6.164414002968976 ,
3.605551275463989 ,
3.4641016151377544 ,
3.605551275463989 ,
1.4142135623730951 ,
2.23606797749979 ,
2.23606797749979 ,
4.69041575982343 ,
7.0710678118654755 ,
2.23606797749979 ,
5.477225575051661 ,
0 ,
4.58257569495584 ,
3.605551275463989 ,
4.58257569495584 ,
2.0 ,
4.58257569495584 ,
4.47213595499958 ,
2.23606797749979 ,
4.242640687119285 ,
3.3166247903554 ,
4.123105625617661 ,
4.242640687119285 ,
3.7416573867739413 ,
3.1622776601683795 ,
3.0 ,
6.0 ,
5.385164807134504 ,
2.449489742783178 ,
5.196152422706632 ,
5.477225575051661 ,
5.0990195135927845 ,
4.123105625617661 ,
4.123105625617661 ,
4.898979485566356 ,
5.916079783099616 ,
1.4142135623730951 ,
0 ,
5.830951894845301 ,
3.3166247903554 ,
5.0990195135927845 ,
1.7320508075688772 ,
3.7416573867739413 ,
3.7416573867739413 ,
2.449489742783178 ,
5.916079783099616 ,
3.0 ,
3.7416573867739413 ,
4.58257569495584 ,
0 ,
5.0990195135927845 ,
3.7416573867739413 ,
3.0 ,
3.1622776601683795 ,
6.708203932499369 ,
0 ,
3.7416573867739413 ,
3.1622776601683795 ,
5.830951894845301 ,
5.0990195135927845 ,
4.242640687119285 ,
5.0990195135927845 ,
3.1622776601683795 ,
2.449489742783178 ,
5.385164807134504 ,
3.3166247903554 ,
5.744562646538029 ,
4.47213595499958 ,
5.830951894845301 ,
0 ,
4.123105625617661 ,
4.123105625617661 ,
4.242640687119285 ,
3.605551275463989 ,
3.3166247903554 ,
3.1622776601683795 ,
4.358898943540674 ,
3.605551275463989 ,
4.898979485566356 ,
4.69041575982343 ,
3.7416573867739413 ,
2.23606797749979 ,
7.0710678118654755 ,
4.58257569495584 ,
3.3166247903554 ,
5.0990195135927845 ,
2.23606797749979 ,
3.7416573867739413 ,
3.3166247903554 ,
2.8284271247461903 ,
6.557438524302 ,
5.916079783099616 ,
4.123105625617661 ,
3.605551275463989 ,
4.69041575982343 ,
3.7416573867739413 ,
4.0 ,
6.164414002968976 ,
3.7416573867739413 ,
4.47213595499958 ,
6.0 ,
2.449489742783178 ,
1.7320508075688772 ,
5.0990195135927845 ,
3.7416573867739413 ,
4.47213595499958 ,
1.7320508075688772 ,
4.123105625617661 ,
3.0 ,
3.3166247903554 ,
0 ,
5.0990195135927845 ,
3.7416573867739413 ,
4.58257569495584 ,
4.0 ,
0 ,
2.449489742783178 ,
1.4142135623730951 ,
3.1622776601683795 ,
0 ,
4.123105625617661 ,
4.242640687119285 ,
0 ,
1.0 ,
5.916079783099616 ,
5.196152422706632 ,
3.7416573867739413 ,
4.0 ,
5.477225575051661 ,
3.7416573867739413 ,
4.69041575982343 ,
3.0 ,
4.358898943540674 ,
5.916079783099616 ,
4.123105625617661 ,
3.1622776601683795 ,
3.7416573867739413 ,
6.48074069840786 ,
4.123105625617661 ,
2.8284271247461903 ,
4.123105625617661 ,
3.4641016151377544 ,
2.449489742783178 ,
3.3166247903554 ,
4.123105625617661 ,
5.744562646538029 ,
2.8284271247461903 ,
4.242640687119285 ,
3.1622776601683795 ,
5.744562646538029 ,
5.0990195135927845 ,
4.898979485566356 ,
2.449489742783178 ,
5.0990195135927845 ,
2.23606797749979 ,
6.0 ,
5.196152422706632 ,
5.0990195135927845 ,
3.7416573867739413 ,
2.23606797749979 ,
3.0 ,
3.4641016151377544 ,
4.58257569495584 ,
2.0 ,
2.23606797749979 ,
6.0 ,
2.23606797749979 ,
0 ,
2.23606797749979 ,
0 ,
2.23606797749979 ,
3.7416573867739413 ,
3.1622776601683795 ,
3.605551275463989 ,
4.58257569495584 ,
5.0990195135927845 ,
2.23606797749979 ,
3.605551275463989 ,
5.0 ,
3.7416573867739413 ,
4.123105625617661 ,
6.164414002968976 ,
5.0990195135927845 ,
4.123105625617661 ,
2.449489742783178 ,
5.477225575051661 ,
6.164414002968976 ,
3.1622776601683795 ,
5.477225575051661 ,
4.58257569495584 ,
3.7416573867739413 ,
5.744562646538029 ,
2.449489742783178 ,
4.69041575982343 ,
4.358898943540674 ,
0 ,
5.385164807134504 ,
6.48074069840786 ,
4.123105625617661 ,
5.916079783099616 ,
4.242640687119285 ,
3.7416573867739413 ,
0 ,
2.0 ,
2.8284271247461903 ,
6.557438524302 ,
0 ,
1.0 ,
5.477225575051661 ,
1.4142135623730951 ,
4.123105625617661 ,
3.4641016151377544 ,
4.0 ,
4.47213595499958 ,
2.23606797749979 ,
6.4031242374328485 ,
5.477225575051661 ,
3.4641016151377544 ,
3.7416573867739413 ,
5.916079783099616 ,
3.0 ,
0 ,
3.0 ,
3.3166247903554 ,
4.58257569495584 ,
0 ,
3.0 ,
0 ,
2.8284271247461903 ,
5.0990195135927845 ,
5.385164807134504 ,
4.58257569495584 ,
3.0 ,
5.196152422706632 ,
3.1622776601683795 ,
3.7416573867739413 ,
6.4031242374328485 ,
6.708203932499369 ,
5.0990195135927845 ,
3.4641016151377544 ,
2.449489742783178 ,
6.48074069840786 ,
5.477225575051661 ,
2.23606797749979 ,
0 ,
2.8284271247461903 ,
3.0 ,
4.58257569495584 ,
3.0 ,
5.830951894845301 ,
4.358898943540674 ,
3.0 ,
4.898979485566356 ,
3.3166247903554 ,
3.1622776601683795 ,
3.3166247903554 ,
5.0 ,
5.0990195135927845 ,
0 ,
2.8284271247461903 ,
3.605551275463989 ,
1.4142135623730951 ,
6.4031242374328485 ,
3.0 ,
3.7416573867739413 ,
4.123105625617661 ,
3.605551275463989 ,
3.0 ,
3.3166247903554 ,
5.0990195135927845 ,
6.4031242374328485 ,
5.196152422706632 ,
2.449489742783178 ,
4.123105625617661 ,
3.0 ,
3.7416573867739413 ,
7.3484692283495345 ,
3.605551275463989 ,
1.0 ,
2.0 ,
4.69041575982343 ,
4.47213595499958 ,
4.123105625617661 ,
3.3166247903554 ,
5.196152422706632 ,
6.164414002968976 ,
5.0 ,
3.7416573867739413 ,
0 ,
0 ,
3.605551275463989 ,
2.8284271247461903 ,
3.605551275463989 ,
4.242640687119285 ,
2.23606797749979 ,
4.69041575982343 ,
3.0 ,
3.1622776601683795 ,
4.58257569495584 ,
1.7320508075688772 ,
6.48074069840786 ,
2.23606797749979 ,
3.0 ,
4.123105625617661 ,
5.830951894845301 ,
6.164414002968976 ,
4.123105625617661 ,
6.4031242374328485 ,
0 ,
5.385164807134504 ,
3.0 ,
3.0 ,
4.358898943540674 ,
1.0 ,
1.0 ,
4.242640687119285 ,
4.898979485566356 ,
5.744562646538029 ,
0 ,
2.23606797749979 ,
3.7416573867739413 ,
3.3166247903554 ,
6.557438524302 ,
5.830951894845301 ,
5.477225575051661 ,
4.58257569495584 ,
2.449489742783178 ,
2.0 ,
3.7416573867739413 ,
5.0990195135927845 ,
5.0 ,
2.8284271247461903 ,
0 ,
0 ,
4.123105625617661 ,
0 ,
5.744562646538029 ,
3.605551275463989 ,
3.7416573867739413 ,
2.23606797749979 ,
4.123105625617661 ,
5.830951894845301 ,
4.123105625617661 ,
4.58257569495584 ,
3.7416573867739413 ,
5.385164807134504 ,
6.4031242374328485 ,
3.605551275463989 ,
1.0 ,
4.242640687119285 ,
3.7416573867739413 ,
7.0710678118654755 ,
3.4641016151377544 ,
3.1622776601683795 ,
5.830951894845301 ,
4.47213595499958 ,
3.3166247903554 ,
1.4142135623730951 ,
4.123105625617661 ,
3.3166247903554 ,
5.0990195135927845 ,
4.58257569495584 ,
4.242640687119285 ,
3.7416573867739413 ,
5.656854249492381 ,
4.242640687119285 ,
4.47213595499958 ,
5.385164807134504 ,
4.47213595499958 ,
5.385164807134504 ,
2.23606797749979 ,
2.8284271247461903 ,
3.7416573867739413 ,
2.0 ,
3.0 ,
3.0 ,
2.0 ,
3.0 ,
2.23606797749979 ,
0 ,
4.47213595499958 ,
4.358898943540674 ,
0 ,
5.656854249492381 ,
0 ,
5.744562646538029 ,
4.58257569495584 ,
7.0710678118654755 ,
3.3166247903554 ,
1.0 ,
3.0 ,
6.4031242374328485 ,
1.4142135623730951 ,
0 ,
5.916079783099616 ,
4.58257569495584 ,
5.830951894845301 ,
5.385164807134504 ,
3.1622776601683795 ,
3.7416573867739413 ,
3.605551275463989 ,
5.830951894845301 ,
4.69041575982343 ,
3.0 ,
4.58257569495584 ,
3.1622776601683795 ,
1.7320508075688772 ,
6.164414002968976 ,
3.1622776601683795 ,
2.449489742783178 ,
3.0 ,
0 ,
0 ,
6.164414002968976 ,
0 ,
2.8284271247461903 ,
4.123105625617661 ,
1.7320508075688772 ,
4.58257569495584 ,
3.0 ,
5.830951894845301 ,
4.123105625617661 ,
5.477225575051661 ,
5.0990195135927845 ,
3.3166247903554 ,
3.7416573867739413 ,
6.164414002968976 ,
6.0 ,
5.0990195135927845 ,
3.0 ,
0 ,
5.0990195135927845 ,
4.58257569495584 )


arr1=np.array(data1)
# finding the 1st quartile
q1 = np.quantile(arr1, 0.25)
# finding the 3rd quartile
q3 = np.quantile(arr1, 0.75)
med = np.median(arr1)
# finding the iqr region
iqr = q3-q1
# finding upper and lower whiskers
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
print(iqr, upper_bound, lower_bound)


outliers = arr1[(arr1 <= lower_bound) | (arr1 >= upper_bound)]
print('The following are the outliers in the boxplot:',format(outliers))


# boxplot of data within the whisker
#arr2 = arr1[(arr1 >= lower_bound) & (arr1 <= upper_bound)]




data2 = (1.4142135623730951 ,
3.7416573867739413 ,
6.4031242374328485 ,
3.7416573867739413 ,
7.810249675906654 ,
3.0 ,
0 ,
5.744562646538029 ,
2.8284271247461903 ,
5.385164807134504 ,
5.830951894845301 ,
4.47213595499958 ,
6.782329983125268 ,
0 ,
4.123105625617661 ,
0 ,
1.7320508075688772 ,
3.0 ,
0 ,
7.14142842854285 ,
1.0 ,
4.358898943540674 ,
3.7416573867739413 ,
0 ,
6.0 ,
4.58257569495584 ,
4.69041575982343 ,
0 ,
4.242640687119285 ,
0 ,
5.385164807134504 ,
2.8284271247461903 ,
4.69041575982343 ,
3.3166247903554 ,
0 ,
3.7416573867739413 ,
3.7416573867739413 ,
6.708203932499369 ,
0 ,
3.7416573867739413 ,
4.47213595499958 ,
6.4031242374328485 ,
5.0990195135927845 ,
2.23606797749979 ,
3.0 ,
0 ,
4.242640687119285 ,
4.898979485566356 ,
9.273618495495704 ,
4.123105625617661 ,
3.3166247903554 ,
8.717797887081348 ,
0 ,
3.3166247903554 ,
0 ,
4.898979485566356 ,
5.0 ,
0 ,
5.830951894845301 ,
8.366600265340756 ,
5.0 ,
0 ,
4.123105625617661 ,
7.0710678118654755 ,
3.0 ,
6.0 ,
6.4031242374328485 ,
0 ,
4.58257569495584 ,
6.164414002968976 ,
5.830951894845301 ,
4.898979485566356 ,
0 ,
2.23606797749979 ,
7.3484692283495345 ,
3.7416573867739413 ,
0 ,
6.708203932499369 ,
0 ,
1.4142135623730951 ,
7.14142842854285 ,
6.082762530298219 ,
7.0710678118654755 ,
7.54983443527075 ,
5.0 ,
6.708203932499369 ,
2.23606797749979 ,
5.0990195135927845 ,
3.7416573867739413 ,
0 ,
4.242640687119285 ,
5.0990195135927845 ,
2.449489742783178 ,
5.196152422706632 ,
5.0990195135927845 ,
6.708203932499369 ,
4.123105625617661 ,
5.830951894845301 ,
2.8284271247461903 ,
0 ,
2.23606797749979 ,
5.385164807134504 ,
5.916079783099616 ,
3.7416573867739413 ,
6.557438524302 ,
0 ,
0 ,
2.8284271247461903 ,
6.708203932499369 ,
2.449489742783178 ,
0 ,
5.0990195135927845 ,
0 ,
6.557438524302 ,
6.4031242374328485 ,
3.1622776601683795 ,
0 ,
5.830951894845301 ,
6.782329983125268 ,
6.164414002968976 ,
7.810249675906654 ,
3.3166247903554 ,
4.123105625617661 ,
0 ,
7.211102550927978 ,
6.708203932499369 ,
4.58257569495584 ,
0 ,
3.3166247903554 ,
3.605551275463989 ,
3.605551275463989 ,
5.385164807134504 ,
2.0 ,
4.47213595499958 ,
4.123105625617661 ,
0 ,
6.082762530298219 ,
6.708203932499369 ,
2.23606797749979 ,
0 ,
7.0710678118654755 ,
5.744562646538029 ,
2.8284271247461903 ,
0 ,
3.605551275463989 ,
5.830951894845301 ,
4.47213595499958 ,
6.0 ,
0 ,
2.8284271247461903 ,
6.324555320336759 ,
6.6332495807108 ,
5.0 ,
5.385164807134504 ,
6.4031242374328485 ,
2.23606797749979 ,
4.123105625617661 ,
7.810249675906654 ,
5.830951894845301 ,
4.123105625617661 ,
5.385164807134504 ,
5.0 ,
3.7416573867739413 ,
0 ,
7.0 ,
0 ,
9.848857801796104 ,
0 ,
3.1622776601683795 ,
6.0 ,
6.4031242374328485 ,
4.242640687119285 ,
3.7416573867739413 ,
2.449489742783178 ,
3.7416573867739413 ,
3.605551275463989 ,
6.557438524302 ,
7.211102550927978 ,
3.3166247903554 ,
0 ,
0 ,
4.898979485566356 ,
7.483314773547883 ,
2.449489742783178 ,
5.477225575051661 ,
3.3166247903554 ,
6.0 ,
4.123105625617661 ,
6.782329983125268 ,
3.605551275463989 ,
2.449489742783178 ,
5.0990195135927845 ,
6.164414002968976 ,
3.7416573867739413 ,
2.8284271247461903 ,
5.0 ,
3.0 ,
5.0 ,
3.7416573867739413 ,
6.164414002968976 ,
6.0 ,
3.7416573867739413 ,
6.708203932499369 ,
4.123105625617661 ,
5.656854249492381 ,
5.830951894845301 ,
4.242640687119285 ,
7.14142842854285 ,
2.23606797749979 ,
5.916079783099616 ,
0 ,
5.385164807134504 ,
6.557438524302 ,
6.324555320336759 ,
4.58257569495584 ,
1.4142135623730951 ,
4.47213595499958 ,
5.916079783099616 ,
0 ,
4.242640687119285 ,
5.385164807134504 ,
2.0 ,
6.557438524302 ,
4.898979485566356 ,
7.0710678118654755 ,
3.0 ,
5.477225575051661 ,
3.1622776601683795 ,
2.449489742783178 ,
6.708203932499369 ,
5.477225575051661 ,
4.123105625617661 ,
6.0 ,
0 ,
4.358898943540674 ,
4.123105625617661 ,
5.477225575051661 ,
3.7416573867739413 ,
7.14142842854285 ,
4.47213595499958 ,
5.0990195135927845 ,
5.744562646538029 ,
5.656854249492381 ,
2.0 ,
0 ,
5.916079783099616 ,
0 ,
6.164414002968976 ,
3.3166247903554 ,
4.242640687119285 ,
3.7416573867739413 ,
3.605551275463989 ,
1.4142135623730951 ,
4.47213595499958 ,
7.14142842854285 ,
4.358898943540674 ,
6.0 ,
0 ,
2.449489742783178 ,
2.23606797749979 ,
0 ,
6.6332495807108 ,
6.164414002968976 ,
4.58257569495584 ,
4.242640687119285 ,
6.082762530298219 ,
0 ,
7.0 ,
7.3484692283495345 ,
7.810249675906654 ,
3.1622776601683795 ,
1.4142135623730951 ,
3.4641016151377544 ,
2.449489742783178 ,
3.3166247903554 ,
5.0 ,
0 ,
9.273618495495704 ,
6.0 ,
6.782329983125268 ,
3.1622776601683795 ,
5.744562646538029 ,
5.744562646538029 ,
3.7416573867739413 ,
0 ,
4.47213595499958 ,
4.242640687119285 ,
7.0710678118654755 ,
3.605551275463989 ,
0 ,
6.324555320336759 ,
0 ,
3.1622776601683795 ,
3.0 ,
6.48074069840786 ,
5.0990195135927845 ,
0 ,
0 ,
4.58257569495584 ,
5.656854249492381 ,
5.385164807134504 ,
6.082762530298219 ,
4.123105625617661 ,
4.358898943540674 ,
0 ,
0 ,
3.4641016151377544 ,
5.830951894845301 ,
0 ,
3.7416573867739413 ,
6.0 ,
5.656854249492381 ,
4.242640687119285 ,
0 ,
3.3166247903554 ,
0 ,
4.58257569495584 ,
0 ,
0 ,
6.6332495807108 ,
0 ,
4.47213595499958 ,
4.898979485566356 ,
5.477225575051661 ,
5.477225575051661 ,
5.916079783099616 ,
5.916079783099616 ,
0 ,
3.3166247903554 ,
4.58257569495584 ,
5.0990195135927845 ,
2.449489742783178 ,
5.385164807134504 ,
5.196152422706632 ,
4.58257569495584 ,
5.744562646538029 ,
6.164414002968976 ,
4.123105625617661 ,
0 ,
5.196152422706632 ,
0 ,
0 ,
0 ,
7.280109889280518 ,
4.898979485566356 ,
7.0 ,
2.23606797749979 ,
2.449489742783178 ,
4.123105625617661 ,
3.1622776601683795 ,
4.898979485566356 ,
0 ,
5.477225575051661 ,
6.6332495807108 ,
3.7416573867739413 ,
3.7416573867739413 ,
6.4031242374328485 ,
6.4031242374328485 ,
6.4031242374328485 ,
0 ,
6.4031242374328485 ,
3.1622776601683795 ,
3.0 ,
7.14142842854285 ,
0 ,
0 ,
3.3166247903554 ,
7.14142842854285 ,
1.4142135623730951 ,
3.1622776601683795 ,
6.708203932499369 ,
0 ,
8.366600265340756 ,
2.23606797749979 ,
4.242640687119285 ,
1.0 ,
4.123105625617661 ,
5.196152422706632 ,
4.47213595499958 ,
3.3166247903554 ,
3.605551275463989 ,
3.7416573867739413 ,
0 ,
6.4031242374328485 ,
0 ,
0 ,
5.196152422706632 ,
7.3484692283495345 ,
5.477225575051661 ,
0 ,
6.164414002968976 ,
5.830951894845301 ,
4.69041575982343 ,
0 ,
3.0 ,
0 ,
2.23606797749979 ,
4.47213595499958 ,
5.744562646538029 ,
0 ,
3.1622776601683795 ,
5.0990195135927845 ,
1.4142135623730951 ,
5.0990195135927845 ,
1.4142135623730951 ,
6.164414002968976 ,
3.0 ,
1.7320508075688772 ,
8.54400374531753 ,
4.123105625617661 ,
4.58257569495584 ,
5.916079783099616 ,
4.358898943540674 ,
6.164414002968976 ,
0 ,
3.0 ,
0 ,
0 ,
5.916079783099616 ,
1.4142135623730951 ,
6.782329983125268 ,
3.1622776601683795 ,
5.0990195135927845 ,
9.273618495495704 ,
4.123105625617661 ,
4.58257569495584 ,
0 ,
0 ,
5.0990195135927845 ,
3.1622776601683795 ,
5.744562646538029 ,
0 ,
4.58257569495584 ,
5.830951894845301 ,
2.23606797749979 ,
0 ,
5.196152422706632 ,
5.916079783099616 ,
0 ,
0 ,
8.54400374531753 ,
3.1622776601683795 ,
4.123105625617661 ,
4.69041575982343 ,
2.0 ,
0 ,
4.123105625617661 ,
6.0 ,
7.280109889280518 ,
6.164414002968976 ,
6.164414002968976 ,
2.8284271247461903 ,
2.0 ,
5.830951894845301 ,
7.0710678118654755 ,
3.1622776601683795 ,
5.0990195135927845 ,
3.3166247903554 ,
3.7416573867739413 ,
4.242640687119285 ,
1.0 ,
1.4142135623730951 ,
3.0 ,
0 ,
7.0 ,
6.928203230275509 ,
0 ,
5.744562646538029 ,
1.7320508075688772 ,
5.196152422706632 ,
2.23606797749979 ,
6.4031242374328485 ,
6.164414002968976 ,
0 ,
2.23606797749979 ,
1.4142135623730951 ,
4.242640687119285 ,
0 ,
4.47213595499958 ,
8.660254037844387 ,
4.58257569495584 ,
2.0 ,
5.477225575051661 ,
3.4641016151377544 ,
4.898979485566356 ,
0 ,
6.164414002968976 ,
7.0 ,
4.242640687119285 ,
6.4031242374328485 ,
4.123105625617661 ,
4.47213595499958 ,
7.0710678118654755 ,
5.385164807134504 ,
0 ,
6.48074069840786 ,
3.3166247903554 ,
5.385164807134504 ,
5.196152422706632 ,
4.898979485566356 )



arr2=np.array(data2)
# finding the 1st quartile
q1 = np.quantile(arr2, 0.25)
# finding the 3rd quartile
q3 = np.quantile(arr2, 0.75)
med = np.median(arr2)
# finding the iqr region
iqr = q3-q1
# finding upper and lower whiskers
upper_bound = q3+(1.5*iqr)
lower_bound = q1-(1.5*iqr)
print(iqr, upper_bound, lower_bound)


outliers2 = arr2[(arr2 <= lower_bound) | (arr2 >= upper_bound)]
print('The following are the outliers in the boxplot:',format(outliers2))

#Converting unit to feet
arr1 = arr1*25
arr2 = arr2*25

data = np.array([arr1,arr2]) 
data = data.transpose()
df = pd.DataFrame(data, columns = ['216','343'])
plt.figure(figsize=(12, 7))
plt.title('Topology = Cubic Lattice',fontsize=16)
plt.suptitle('Distribution of Distance between Source and Destination',fontsize=24, y=1)
plt.xlabel("Number of Nodes")
plt.ylabel("Distance between source and destination (feet)")
df.boxplot()
plt.show()