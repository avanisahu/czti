dataset=('/home/avani/Desktop/czti/czti_sample_data/20160331_T01_112T01_9000000406_level2/modeM0/AS1T01_112T01_9000000406cztM0_level2_bc.evt')
from astropy.io import fits
hdu=fits.open(dataset)
from matplotlib import pyplot as plt
import numpy as np

for i in range(1,5):
	x=hdu[i].data["TIME"]
	a = np.array([4]) 
	fig = plt.subplot( 2, 3, i)

	import math
	w = 25
	n = math.ceil((x.max() - x.min())/w)
	ax = plt.hist(x, bins = n)
	plt.show()
