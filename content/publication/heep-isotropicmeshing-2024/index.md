---
title: "An Adaptive Screen-Space Meshing Approach for Normal Integration"

aliases:
- "/adaptive-screen-meshing/"

authors:
- admin
- Eduard Zell
date: '2024-10-01'
publishDate: '2024-10-01'
publication_types:
- inproceedings
#publication: '*Association for Computing Machinery*'
#doi: 10.1145/3641234.3671025
abstract: "Reconstructing surfaces from normals is a key component of photometric stereo. This work introduces an adaptive surface triangulation in the image domain and afterwards performs the normal integration on a triangle mesh. Our key insight is that surface curvature can be computed from normals. Based on the curvature, we identify flat areas and aggregate pixels into triangles. Compared to pixel grids, our triangle meshes adapt locally to surface details and yield much sparser representations. We derive a mesh-based formulation of the normal integration problem. Here, the sparser representations yield major runtime benefits."

# url_pdf: 'https://dl.acm.org/doi/pdf/10.1145/3641234.3671025'
url_code: 'https://github.com/moritzheep/adaptive-screen-meshing'
url_dataset: ''
url_poster: 'poster.pdf'
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://www.youtube.com/watch?v=6m2SKqb1M5M'

image:
  caption: ''
  focal_point: Right
  preview_only: false

tags:
- "Normal Integration"

# sections: [Overview, Results]
---

## Motivation
Increasing the resolution of the normal map improves the accuracy of fine structures but increases computational complexity. In smooth, featureless regions, this added complexity yields little additional information. 
![Output of our Adaptive Screen-Space Meshign Approach at different quality settings.](overview.svg "Our screen-space remeshing pipeline decimates smooth, featureless areas efficiently before the normal integration while preserving high-frequency details. Depicted results illustrate high, mid and low-resolution triangulations.")
We introduce an adaptive screen-space meshing approach to reduce complexity before integration and give a full derivation of the normal integration on general triangle meshes.

By focusing on fine details and removing redundant information, we can avoid the quadratic growth of variables with increasing geometric resolution in pixel-based methods. 

## Overview
{{< youtube 6m2SKqb1M5M >}}

To create a feature-adaptive mesh before the actual surface integration, we must reliably predict detailed surface areas and adjust the density of the triangle mesh accordingly. We extract the surface curvature from the normal maps and use it to calculate an optimal edge length to keep the expected deviation between the triangle mesh and the underlying smooth surface below a user defined threshold.

## Results

{{< image-comparison left-img="images/david_heep2022.png" right-img="images/david_ours.png" left-label="Pixel-Wise" right-label="Ours" caption="Integration results for pixel-based integration and mesh-based integration with 20k pixels/vertices respectively. Our adaptive vertex placement preserves high-frequency details much better than the regular pixel grid.">}}
