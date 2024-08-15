The main file called files_generation.ipynb is aimed to generated the required configuration files for detection, measurement in SourceXtractor++, it also does a image filtering, PSF convolution, noise addtion based on the specified filter, PSF and noise level in the ipynb file and save them into the corresponding file paths.

Parameters Adjustment:\
In the files_generation.ipynb, below the cell where functions are defined, the 'INPUT PARAMETERS' are specifically for our SKIRT simulations. The 'CONFIG PARAMETERS' are used in the detection configuration files and they are the main parameters that we might need to adjust. 'std' define the noise level with the same units as the image itself, for JWST NIRCam detections, its MJy/sr.

Below are the template files, PSF and filter that are required, the uploaded once are for my private use. One can adjust as he/she needs.

How to use:\
Normally, I just would run the .ipynb file on cluster, then the files are generated under specific directory corresponding to their file name, however if it's not applicable, we may also convert the .ipynb file into .py file to run it as a slurm job. With the SourceXtractor++ installed, we can directly run SE++ through the files.
