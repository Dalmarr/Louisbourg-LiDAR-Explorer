"""

Stage 1 - Source layer inspection

"""

import arcpy


from configuration import (
    NATIONAL_HISTORIC_SITES_URL,
    LIDAR_TILES_URL,
    NHS_LAYER_NAME,
    LIDAR_LAYER_NAME
)
from project_setup import get_project, get_or_create_map
from web_layers import get_or_add_web_layer, inspect_layer


def main():
    print("\nLouisbourg LiDAR Explorer")
    print("Stage 1 - Source layer inspection\n")

    arcpy.env.overwriteOutput = True

    aprx = get_project()
    qa_map = get_or_create_map(aprx)

    historic_sites = get_or_add_web_layer(
        qa_map,
        NATIONAL_HISTORIC_SITES_URL,
        NHS_LAYER_NAME
    )

    lidar_tiles = get_or_add_web_layer(
        qa_map,
        LIDAR_TILES_URL,
        LIDAR_LAYER_NAME
    )

    inspect_layer(historic_sites)
    inspect_layer(lidar_tiles)

    aprx.save()

    print("Stage 1 completed successfully.")
    print("ArcGIS Pro project saved.")


if __name__ == "__main__":
    main()