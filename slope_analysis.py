import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
	data_fname = f'{dataloc}Arsia_mons_spiral_railway_height.csv'
	plot_fname = 'Arsia_Mons_spiral_railway_gradient.png'

	df = pd.read_csv(data_fname)

	distance = df['Distance (Km)'] #km
	elevation = df['HRSC MOLA Blended DEM (200m)']/1000 #km

	dx = np.diff(distance)
	dy = np.diff(elevation)

	gradient = dy/dx


	fig, ax = plt.subplots(figsize = (9, 4), nrows = 1, ncols = 2)
	ax = ax.flatten()

	ax[0].plot(distance[1:], gradient*100, linewidth = 0.5)
	ax[0].grid(linestyle = ':')

	ax[0].set_xlabel('Along profile distance [km]')
	ax[0].set_ylabel('Gradient [%]')
	ax[0].set_title('Profile gradient')


	ax[1].plot(df['Longitude'], df['Latitude'])

	ax[1].grid(linestyle = ':')
	ax[1].set_xlabel('Longitude')
	ax[1].set_ylabel('Latitude')
	ax[1].set_title('Profile path')

	fig.savefig(f'Plots/{plot_fname}', dpi = 200, bbox_inches = 'tight')
	plt.close()

if __name__ == '__main__':
	main()
