"""

"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

from vicar2png_python3 import process_metadata, extract_image


datapath = 'Data/'
plotpath = 'Plots/'

def elemental_abundances():
	"""
	Plot elemental abundances using .tab files from
	https://grs.lpl.arizona.edu/specials/Smoothed_rebinned_map_data

	More info:
	https://grs.lpl.arizona.edu/latestresults.jsp
	"""

	#import data
	fname = f'{datapath}Elemental_abundances/Cl_SR_5x5.tab'

	rawdata = np.loadtxt(fname)

	lat_raw = rawdata[:,0]
	lon_raw = rawdata[:,1]
	conc_raw = rawdata[:,2]

	#determine original 2D shape
	unique_lats, lats_counts = np.unique(lat_raw, return_counts = True)
	n_lats = len(lats_counts)
	n_lons = lats_counts[0]

	#now reshape
	lat = lat_raw.reshape((n_lats, n_lons))
	lon = lon_raw.reshape((n_lats, n_lons))
	conc = conc_raw.reshape((n_lats, n_lons))

	#set all values larger than 9999 to nan
	conc[conc > 9999] = np.nan

	cmap = 'BuPu'
	#
	# fig, ax = plt.subplots()
	# ax.imshow(conc, cmap = cmap)
	#
	# fig.savefig('test.png')
	# plt.close()

	m = Basemap(projection='kav7',lon_0=0,resolution='c')

	#draw data
	m.pcolor(lon, lat, conc, cmap = cmap, latlon = True)

	cax = m.colorbar(location = 'bottom')
	cax.ax.set_xlabel('Cl concentration [%Wt]')

	m.drawparallels(np.arange(-90.,120.,30.), labels = [1, 0, 0, 1])
	m.drawmeridians(np.arange(0.,360.,60.), labels = [1, 0, 0, 1])

	#also obtain name data
	m.readshapefile('MARS_nomenclature/MARS_nomenclature', 'name')

	size_threshold = 800 #km

	print(f'Total number of surface featuers: {len(m.name)}')
	for info, name_coordinates in zip(m.name_info, m.name):
		if info['diameter'] > size_threshold:
			#we only want to plot large scale features, so larger than e.g. 100 km
			plt.text(name_coordinates[0], name_coordinates[1], info['name'], ha = 'center', va = 'center', fontsize = 3)

	plt.title('Cl concentration on Mars')

	plt.savefig(f'{plotpath}Cl_concentration.png', dpi = 300, bbox_inches = 'tight')
	plt.close()
	# plt.show()

def load_VICAR_data(infile):
	"""
	Load VICAR data using a hack of the VICAR2PNG library
	"""

	try:
		metadata_fd = open(infile, "r")
	except (IOError, OSError) as e:
		print(sys.stderr, "Could not open ", infile, "to process metadata.")
		print(sys.stderr, e.message)
		exit(1)

	vicar_metadata = process_metadata(metadata_fd)

	try:
		image_fd = open(infile, "rb")
	except (IOError, OSError) as e:
		print(sys.stderr, "Could not open ", infile, "to process image.")
		print(sys.stderr, e.message)
		exit(1)

	pixels = extract_image(vicar_metadata, image_fd)

	return pixels

def process_TES_mineral_maps():
	"""
	Data source: https://www.mars.asu.edu/data/
	"""

	vicar_fname = f'{datapath}VICAR_data/TES_Hematite_numeric.vicar'

	vicar_pixels = load_VICAR_data(vicar_fname)

	print(vicar_pixels)

def process_MOLA_DEM():
	"""
	Data source: https://astrogeology.usgs.gov/search/map/Mars/GlobalSurveyor/MOLA/Mars_MGS_MOLA_DEM_mosaic_global_463m
	"""
	pass

def main():
	process_TES_mineral_maps()




if __name__ == '__main__':
	main()
