# General Nexus Aurora data processing notes


### Data formats
VICAR data can be read in Python by hacking the VICAR2PNG package
https://github.com/jesstess/vicar2png

### Mapping sources
- [Openplanetarymap](https://openplanetarymap.netlify.app/): high resolution MOLA DEM and RGB maps with many locale names and good color scales.
- [Other Mars maps](http://chrisherwig.org/planets/): high resolution MOLA DEM and RGB maps without place names but also good color scales.

### Data sources
- Mars MOLA DEM (2GB): https://astrogeology.usgs.gov/search/map/Mars/GlobalSurveyor/MOLA/Mars_MGS_MOLA_DEM_mosaic_global_463m
	- Slopes: [link](https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA02809)
	- Detailed descriptions of some maps: [link](https://pgda.gsfc.nasa.gov/products/62)
- TES mineral and thermal intertia maps (RGB only): https://www.mars.asu.edu/data/
- Elemental abundances maps: https://grs.lpl.arizona.edu/latestresults.jsp (data download: https://grs.lpl.arizona.edu/specials/Smoothed_rebinned_map_data)
- Crude TES Mars climate maps [link](http://planetologia.elte.hu/mcdd/climatemaps.html)
- TES raw data [link](http://tes.asu.edu/products/index.html)
	- mineralogy
	- Albedo
	- Thermal inertia
	- Low spatial resolution of 3 x 6 km, high spectral resolution
- THEMIS (Mars Odyssey) general research page (lots of data) [link](https://themis.asu.edu/researchers)
	- Image product info: [link](http://static.mars.asu.edu/pds/ODTSDP_v1/document/sdpsis.pdf)
	- High spatial resolution of 100 m, low spectral resolution.
- Links to maps of all Mars images across all missions [link](https://themis.asu.edu/maps)  
	Includes
	- THEMIS
	- HiRISE
	- MOC
	- CTS
	- HRSC
	- Viking
- JMARS: all kinds of imagery easily accessible [link](https://jmars.mars.asu.edu/)
- Mars Trek: interactive data visualization [link](https://trek.nasa.gov/mars/)
- Mars Orbital Data Explorer [link](https://ode.rsl.wustl.edu/mars/indexProductSearch.aspx)
	- Includes HRSC DTM data
- HRSC data viewer [link](https://maps.planet.fu-berlin.de/#map=3/1333606.08/0)

#### MRO specific data
General information: [wikipedia](https://en.wikipedia.org/wiki/Mars_Reconnaissance_Orbiter#Instruments)
- CRISM spectrometer - surface mineralogy: [link](http://crism-map.jhuapl.edu/#)  
	More general info ([source](crism-map.jhuapl.edu/popinterpret.php)):
	> Compositional information on the surface is concentrated in four of the browse products (vnir_fem, ir_maf, ir_phy, and ir_hyd). Not all of the sites exhibit spectral evidence for mineralogical diversity. If a location is covered in dust, it appears red in vnir_fem and bland in the other products. Sites with diversity in igneous mineralogy will appear interesting in ir_maf. Sites with minerals formed by interaction of crustal rocks with liquid water will appear interesting in ir_phy and ir_hyd.

	> Sites that have water ice on the surface or as clouds will appear pink, yellow or green in ir_ice, whereas those with carbon dioxide frost on the surface will appear bluish.

	> In addition to those caveats, many of the parameters in the latter four browse products have dependencies on solar incidence angle, surface slopes, atmospheric conditions, detector artifacts, and response to phases other than what the products were intended to show. For example, ir_phy and ir_hyd can have bluish colors due to spectral effects of water ice, either as surface frosts or atmospheric hazes. Illumination geometry or atmospheric dust and ice hazes can create artifacts in vnir_fem, ir_maf, ir_phy, and ir_hyd. ir_phy is particularly susceptible to detector artifacts.

	Info on individual bands in the derived product RGB images: [link](crism-map.jhuapl.edu/popir.php)

- HiRISE/CTX imagery: https://www.uahirise.org/hiwish/browse
	- HiRISE: ~50 cm resolution, RGB, low coverage
	- CTX: ~6 m resolution, grayscale (500 - 800 nm), high coverage

- Mars Climate Sounder (MCS)
	[More info](https://www.planetary.org/explore/projects/mcs/)

### Papers
- MRO/MCS column dust climatology [link](https://www.researchgate.net/publication/334558532_Martian_Year_34_Column_Dust_Climatology_from_Mars_Climate_Sounder_Observations_Reconstructed_Maps_and_Model_Simulations)

### TODO
- TES maps
- THEMIS maps (can apparently produce hematite maps and has been done for multiple regions before)
- CRISM detailed mineralogy maps (see image to the right [here](https://themis.asu.edu/node/5390))
