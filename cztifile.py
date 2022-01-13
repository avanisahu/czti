dataset=('/home/avani/Desktop/czti/czti_sample_data/20160331_T01_112T01_9000000406_level2/modeM0/AS1T01_112T01_9000000406cztM0_level2_bc.evt')
from astropy.io import fits
hdu=fits.open(dataset)
hdu
hdu[1].header
hdu[1].data
hdu[1].data["TIME"]
import matplotlib.pyplot as plt
x=[1.97325456e+08, 1.97325456e+08, 1.97325456e+08, ...,
       1.97326754e+08, 1.97326754e+08, 1.97326754e+08]
plt.hist(x, bins = 175)    
plt.show()
