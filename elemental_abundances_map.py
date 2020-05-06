"""
Data source:
https://grs.lpl.arizona.edu/specials/Smoothed_rebinned_map_data

More info:
https://grs.lpl.arizona.edu/latestresults.jsp
"""

from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt


def main():
	#import data
	fname = 'Data/Cl_SR_5x5.tab'

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

	plt.savefig('Cl_concentration.png', dpi = 300, bbox_inches = 'tight')
	plt.close()
	# plt.show()




if __name__ == '__main__':
	main()
