import json
import numpy as np
import glob
from astropy.io import fits
import scipy.integrate as integrate
import sys
from sourcextractor.config import *

image_file = 'image_file_path'
psf_file   = '/shares/feldmann.ics.mnf.uzh/Haojie/SE++/new_psf_jwst.fits'

##measurement images into the list
image_files = []

image_files.append(MeasurementImage(fits_file=image_file,
                                    weight_type='background',
                                    psf_file =psf_file))
top = ImageGroup(images=image_files)
mesgroup = MeasurementGroup(top)

# some settings for the fiting
set_engine('levmar')
set_meta_iterations(3)
set_meta_iteration_stop(0.0001)
set_deblend_factor(2.5) # lower if it is not converging
set_max_iterations(150)
#constant_background = 0.0

# define the sersic parameters and initialize
rad = FreeParameter(lambda o: o.radius, Range(lambda v, o: (.1 * v, 10*v), RangeType.EXPONENTIAL)) ##(.1 *v. 5*v)
sersic = FreeParameter(1.0, Range((0.3, 5.5), RangeType.LINEAR))  #0.1, 8.0
sersic_ratio = FreeParameter(lambda o: o.aspect_ratio, Range((0.1, 1.0), RangeType.EXPONENTIAL)) ##(.1, 1)
angle = FreeParameter(lambda o: o.angle)
angle_deg = DependentParameter(lambda x: np.fmod(x,np.pi/2.0)/np.pi*180.0, angle)


# intialize position and flux
x,y    = get_pos_parameters()
ra,dec = get_world_position_parameters(x, y)
flux   = get_flux_parameter()
#mag = DependentParameter(lambda f: -2.5 * np.log10(f) + MAG_ZEROPOINT, flux)


# add the model to setup the fit
add_model(mesgroup, SersicModel(x, y, flux, rad, sersic_ratio, angle, sersic))


# make the flux column
add_output_column('flux_test', flux)
#add_output_column("mag_VIS", mag)

# make the positional columns
add_output_column('x', x)
add_output_column('y', y)
add_output_column('ra', ra)
add_output_column('dec', dec)

# make the sersic columns
add_output_column('radius', rad)
add_output_column('sersic_ratio', sersic_ratio)
add_output_column('sersic', sersic)
add_output_column('angle_deg', angle_deg)
