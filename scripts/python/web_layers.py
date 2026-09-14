"""
Functions for adding and inspecting web layers.

"""

import arcpy


def get_or_add_web_layer(map_object, url, layer_name):
    """
    Return an existing layer or add the web-service layer
    to the map if it isn't already added.

    """

    existing_layers = map_object.listLayers(layer_name)

    if existing_layers:
        print(f"Layer already present: {layer_name}")
        return existing_layers[0]

    print(f"Adding: {layer_name}")

    layer = map_object.addDataFromPath(url)
    layer.name = layer_name

    return layer

# Can remove later
def inspect_layer(layer):
    """Print basic information and field definitions."""

    print()
    print("=" * 70)
    print(f"LAYER: {layer.name}")
    print("=" * 70)

    desc = arcpy.Describe(layer)

    print(f"Data type: {desc.dataType}")

    if hasattr(desc, "shapeType"):
        print(f"Geometry: {desc.shapeType}")

    try:
        count = int(arcpy.management.GetCount(layer)[0])
        print(f"Feature count: {count:,}")
    except Exception:
        print("Feature count: could not be retrieved")

    print("\nFIELDS:")

    for field in arcpy.ListFields(layer):
        print(
            f"  {field.name:<30} "
            f"{field.type:<15} "
            f"{field.aliasName}"
        )

    print()