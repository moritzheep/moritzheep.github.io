---
title: "Image Segmentation from Shadow-Hints using Minimum Spanning Trees"
authors:
- admin
- Eduard Zell
date: '2024-07-01'
# publishDate: '2024-07-24T19:44:00.516385Z'
publication_types:
- book
publication: '*Association for Computing Machinery*'
doi: 10.1145/3641234.3671025
abstract: "We propose a novel image segmentation method from shadow masks. These shadow masks are used to detect outline points which are Delaunay triangulated. Our algorithm operates on these triangulations to close incomplete contours and create an image segmentation."

url_pdf: 'https://dl.acm.org/doi/pdf/10.1145/3641234.3671025'
url_code: ''
url_dataset: ''
url_poster: 'https://dl.acm.org/doi/suppl/10.1145/3641234.3671025/suppl_file/SIGGRAPH24_Poster.pdf'
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: ''
  focal_point: Right
  preview_only: false

tags:
- "Shadow Segmentation"

# sections: [Overview, Results]
---

## Overview
![screen reader text](overview.png "Starting from a set of shadow masks, we use templates to extract light-to-shadow transitions. After combining these transitions into an edge strength and direction, we apply non-maximum suppression to obtain thin outlines. The segmentation is performed on a Delaunay triangulation of the detected outline points.")
