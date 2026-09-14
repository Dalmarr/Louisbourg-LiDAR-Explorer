"""
Constants and settings for other scripts regarding 
the selection of LiDAR tiles.

"""

MAP_NAME = "01_LiDAR_QA"

# NAD83(CSRS)v6 / UTM Zone 20N
MAP_SPATIAL_REFERENCE = 22620

NATIONAL_HISTORIC_SITES_URL = (
    "https://nsgiwa.novascotia.ca/arcgis/rest/services/"
    "BASE/BASE_NSTDB_10K_Delimiter_Boundaries_UT83/MapServer/1"
)

LIDAR_TILES_URL = (
    "https://nsgiwa.novascotia.ca/arcgis/rest/services/"
    "ELEV/ELEV_LIDAR_ELEVATION_UT83/MapServer/2"
)

NHS_LAYER_NAME = "NS_National_Historic_Sites"
LIDAR_LAYER_NAME = "NS_LiDAR_Tiles"