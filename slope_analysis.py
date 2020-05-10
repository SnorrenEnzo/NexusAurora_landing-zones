import numpy as np
import pandas as pd

import os

import matplotlib.pyplot as plt
import matplotlib.image as mimg

#for smoothing the data
from scipy.ndimage.filters import gaussian_filter1d

dataloc = 'JMARS_elevation_profiles/'


def main():
	"""
	Data used: JMARS layer "Surface properties" -> "Topography" -> "Elevation"
	-> "HRSC MOLA Blended DEM 200m v2"

	1. Make profile using the selection tool and clicking on the map (double click
	to finish the profile), while having the MOLA DEM layer selected.
	2. Now double click the MOLA DEM layer and go to "Chart". There you can see the
	elevation profile.
	3. Right click the plot and select "Save to CSV".
	"""
	### Adjust input filenames here
	data_fname = f'{dataloc}MOLA_elevation_profile_Hellas_NW.csv'
	profile_image_fname = f'JMARS_screenshots/MOLA_DEM_Hellas_NW.png'
	plot_fname = 'Hellas_NW_railway_gradient.png'


	#load data
	df = pd.read_csv(data_fname)
	print(df.columns)

	distance = df['Distance (Km)'] #km
	elevation = df['HRSC MOLA Blended DEM 200m v2']/1000 #km

	#get gradient
	dx = np.diff(distance)
	dy = np.diff(elevation)
	gradient = dy/dx

	#smooth the gradient
	smooth_scale = 5 #km
	#figure out the smoothing scale in array element units
	print(f'Median sample spacing: {np.median(dx):0.02f} km')
	smooth_scale_elements = smooth_scale/np.median(dx)
	smooth_gradient = gaussian_filter1d(gradient, smooth_scale_elements)


	#plot
	fig, ax = plt.subplots(figsize = (9, 4), nrows = 1, ncols = 2)
	ax = ax.flatten()

	ax[0].plot(distance[1:], smooth_gradient*100, linewidth = 0.5)
	ax[0].grid(linestyle = ':')

	ax[0].set_xlabel('Along profile distance [km]')
	ax[0].set_ylabel('Gradient [%]')
	ax[0].set_title(f'Profile gradient smoothed at {smooth_scale} km scales')


	if os.path.exists(profile_image_fname):
		#show here a screenshot of the DEM and the drawn profile
		img = mimg.imread(profile_image_fname)
		ax[1].imshow(img)
		ax[1].set_xticks([])
		ax[1].set_yticks([])
		ax[1].set_title('Profile on DEM')
	else:
		ax[1].plot(df['Longitude'], df['Latitude'])

		ax[1].grid(linestyle = ':')
		ax[1].set_xlabel('Longitude')
		ax[1].set_ylabel('Latitude')
		ax[1].set_title('Profile path')


	fig.savefig(f'Plots/{plot_fname}', dpi = 200, bbox_inches = 'tight')
	plt.close()

if __name__ == '__main__':
	main()
