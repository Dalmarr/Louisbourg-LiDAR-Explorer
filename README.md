# Louisbourg Archaeological LiDAR Explorer

An interactive 3D GIS project exploring the archaeological landscape of
the Fortress of Louisbourg National Historic Site, Nova Scotia, using
airborne LiDAR, ArcGIS Pro, and the ArcGIS Maps SDK for Unity.

## Project Overview

The project develops an end-to-end LiDAR and 3D GIS workflow from raw
airborne point-cloud data through GIS processing and quality assurance
to an interactive Unity-based visualization.

The study area includes the reconstructed Fortress of Louisbourg and
its surrounding archaeological landscape.

## Technology

- ArcGIS Pro
- ArcGIS 3D Analyst
- ArcGIS Maps SDK for Unity
- Unity
- C#
- Python / ArcPy
- Git / GitHub

## Data Sources

### LiDAR

Government of Nova Scotia provincial LiDAR.

Initial source dataset:

- Acquisition year: 2018
- Source format: LAZ
- Source tiles: 12
- Source point count: 239,229,210
- Horizontal reference: NAD 1983 (CSRS) UTM Zone 20N
- Vertical reference: CGVD2013

Source classifications included:

- Class 2 — Ground
- Class 3 — Low Vegetation
- Class 4 — Medium Vegetation
- Class 5 — High Vegetation
- Class 9 — Water
- Class 17 — Bridge Deck

### Orthophotography

Nova Scotia Orthophotomap Database (NSODB).

Current imagery over the study area was acquired in 2024 and is used for:

- LiDAR QA/QC
- building and feature validation
- road and walkway delineation
- spatial alignment checks

Historical imagery closer to the 2018 LiDAR acquisition date is being
evaluated for final RGB point-cloud colorization.

### Transportation

Nova Scotia Road Network (NSRN).

Used as an authoritative reference for road-centreline geometry within
the study area.

## LiDAR Processing Workflow

Raw provincial LAZ
→ LAS Dataset
→ initial QA/QC
→ archaeological Area of Interest
→ Extract LAS
→ editable uncompressed LAS
→ classification correction
→ RGB colorization
→ point-cloud scene layer
→ ArcGIS Maps SDK for Unity

## QA/QC and Classification

Initial inspection identified several apparent classification anomalies
within the reconstructed fortress.

Elevated returns associated with non-vegetated buildings had been
classified primarily as medium or high vegetation. Building footprints
were digitized using imagery and elevation structure as independent
reference information.

An editable LAS working dataset was created from the original compressed
LAZ source data. Confirmed building returns were selectively reclassified
to LAS Class 6 (Building).

Grass-covered fortification surfaces, including portions of the King's
Bastion, were intentionally excluded from blanket building
reclassification because the LiDAR returns represent vegetation even
where that vegetation forms part of a built heritage structure.

This distinction preserves physical point-return classification while
allowing archaeological structures to be represented separately as
semantic GIS features.

Road and walkway classification QA is currently in progress.

## Project Structure

    gis/
        ArcGIS Pro project and supporting GIS configuration

    unity/
        Unity application

    scripts/
        Python / ArcPy utilities

    data/
        raw/
        staging/
        processed/

    outputs/
        maps/
        screenshots/
        video/
        web/

    docs/
        workflow/
        figures/
        portfolio/

    references/
        metadata/
        historic_maps/

Large source and derived geospatial datasets are intentionally excluded
from version control.

## Current Status

### Completed

- Project and repository setup
- 2018 provincial LiDAR acquisition
- LAS Dataset creation and initial QA/QC
- Study-area extraction
- Conversion from LAZ to editable LAS
- Building-footprint digitization
- Selective building reclassification to LAS Class 6

### In Progress

- Orthophoto integration
- Road and walkway QA/reclassification

### Planned

- RGB LiDAR colorization
- Bare-earth terrain generation
- Terrain derivatives and archaeological visualization
- Point Cloud Scene Layer creation
- ArcGIS Maps SDK for Unity integration
- Interactive 3D controls and layer switching
- Public-facing project demonstration

## Goal

The final application will provide an interactive 3D exploration of
Louisbourg using processed LiDAR and contextual GIS data, demonstrating
a workflow spanning point-cloud QA/QC, terrain processing, 3D GIS,
scene-layer delivery, and custom Unity development.
