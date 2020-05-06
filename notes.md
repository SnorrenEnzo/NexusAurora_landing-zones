# General Nexus Aurora data processing notes


### Data formats
VICAR data can be read in Python by hacking the VICAR2PNG package
https://github.com/jesstess/vicar2png



### Data sources
- Mars MOLA DEM: https://astrogeology.usgs.gov/search/map/Mars/GlobalSurveyor/MOLA/Mars_MGS_MOLA_DEM_mosaic_global_463m
- TES mineral and thermal intertia maps: https://www.mars.asu.edu/data/
- Elemental abundances maps: https://grs.lpl.arizona.edu/latestresults.jsp (data download: https://grs.lpl.arizona.edu/specials/Smoothed_rebinned_map_data)

#### MRO
- CRISM spectrometer - surface mineralogy: http://crism-map.jhuapl.edu/#
	More info ([source](crism-map.jhuapl.edu/popinterpret.php)):
	> Compositional information on the surface is concentrated in four of the browse products (vnir_fem, ir_maf, ir_phy, and ir_hyd). Not all of the sites exhibit spectral evidence for mineralogical diversity. If a location is covered in dust, it appears red in vnir_fem and bland in the other products. Sites with diversity in igneous mineralogy will appear interesting in ir_maf. Sites with minerals formed by interaction of crustal rocks with liquid water will appear interesting in ir_phy and ir_hyd.

	> Sites that have water ice on the surface or as clouds will appear pink, yellow or green in ir_ice, whereas those with carbon dioxide frost on the surface will appear bluish.

	> In addition to those caveats, many of the parameters in the latter four browse products have dependencies on solar incidence angle, surface slopes, atmospheric conditions, detector artifacts, and response to phases other than what the products were intended to show. For example, ir_phy and ir_hyd can have bluish colors due to spectral effects of water ice, either as surface frosts or atmospheric hazes. Illumination geometry or atmospheric dust and ice hazes can create artifacts in vnir_fem, ir_maf, ir_phy, and ir_hyd. ir_phy is particularly susceptible to detector artifacts.

- HiRISE/CTX imagery: https://www.uahirise.org/hiwish/browse
