"""
Functions for opening the ArcGIS Pro project and preparing the map.

"""

from pathlib import Path
import arcpy
from configuration import MAP_NAME, MAP_SPATIAL_REFERENCE


def get_project():
    """
    Use the currently open ArcGIS Pro project when possible.
    Otherwise find the .aprx in the gis/ folder.

    """

    try:
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        print(f"Using open ArcGIS Pro project: {aprx.filePath}")
        return aprx

    except Exception:
        script_path = Path(__file__).resolve()
        project_root = script_path.parents[2]
        gis_directory = project_root / "gis"
        aprx_files = list(gis_directory.glob("*.aprx"))

        if len(aprx_files) == 0:
            raise FileNotFoundError(f"No ArcGIS Pro project found in: {gis_directory}")

        if len(aprx_files) > 1:
            raise RuntimeError(
                f"More than one .aprx found in {gis_directory}. Expected exactly one."
            )

        aprx_path = aprx_files[0]
        print(f"Opening ArcGIS Pro project: {aprx_path}")
        return arcpy.mp.ArcGISProject(str(aprx_path))


def get_or_create_map(aprx):
    """
    Return the QA map, or create it if necessary.
    
    """

    maps = aprx.listMaps(MAP_NAME)

    if maps:
        qa_map = maps[0]
        print(f"Using existing map: {MAP_NAME}")
    else:
        qa_map = aprx.createMap(MAP_NAME, "MAP")
        print(f"Created map: {MAP_NAME}")

    spatial_ref = arcpy.SpatialReference(MAP_SPATIAL_REFERENCE)
    qa_map.spatialReference = spatial_ref

    print(f"Map coordinate system: {spatial_ref.name}")

    return qa_map