---
title: "Image Pre-Segmentation from Shadow Masks"

# aliases:
# - "/anisotropic-screen-meshing/"

authors:
- admin
- amaldevparakkat
- eduardzell
date: '2025-09-29'
publishDate: '2025-04-15'
publication_types:
- inproceedings
publication: '*Vision, Modeling, and Visualization (VMV)*'
doi: "10.2312/vmv.20251239"
abstract: "Image segmentation has gained a lot of attention in the past. When working with photometric stereo data, we discovered that shadow cues provide valuable spatial information, especially when combining multiple images of the same scene under different lighting conditions. In the following, we present a robust method to pre-segment images, relying heavily on shadow masks as the main input. We first detect object contours from light to shadow transitions. In the second step, we run an image segmentation algorithm based on Delaunay triangulation that is capable of closing the gaps between contours. Our method requires spatial input data but is free from training data. Initial results look promising, generating pre-segmentations close to recent data-driven image segmentation algorithms."

url_pdf: 'https://diglib.eg.org/bitstreams/15774b70-9f88-4ed3-a792-296bb54a825b/download'
# url_preprint: 'https://arxiv.org/abs/2504.00867'
# url_code: 'https://github.com/moritzheep/anisotropic-screen-meshing'
# url_dataset: ''
# url_poster: 'poster.pdf'
# url_project: ''
# url_slides: ''
# url_source: ''
# url_video: 'https://www.youtube.com/watch?v=6m2SKqb1M5M'

image:
  caption: ''
  focal_point: Right
  preview_only: false

tags:
- "Shadow Segmentation"

# sections: [Motivation, Overview, Results]
---
## Motivation

While deep learning methods dominate image segmentation, they struggle with similar colors, complex textures, and require millions of annotated images. We propose a training-free approach that leverages shadow masks from photometric stereo data. Our key insight: changing light positions create shadow-to-light transitions that reveal object boundaries independent of colour or texture.

## Overview

Our two-stage pipeline transforms shadow information into image segments:

1. **Contour Detection**: We detect object boundaries by analyzing shadow-to-light transitions across multiple lighting conditions, combining shadow masks with albedo and surface normal gradients for robustness.

2. **Delaunay Segmentation**: Detected contours are converted into a Delaunay triangulation, then progressively coarsened using a modified minimum spanning tree algorithm. Edge weights encode contour strength, preserving strong boundaries while merging weak ones.

The method allows resegmentation in real-time and requires no training data.

## Results

Our analytical approach achieves competitive results compared to state-of-the-art methods:

- **Strong performance** on textured objects and similar-colored regions where traditional methods fail
- **Complementary inputs**: shadows detect boundaries, albedo/normals add robustness
- **Interactive control**: real-time adjustment of segmentation granularity via a single user parameter

**Limitations**: Best suited for scenes with multiple objects or well-separated parts.

Shadow information provides a powerful, underutilized signal for image segmentation—achieving results close to deep learning methods without any training data.

```
@InProceedings{Heep_2025_VMV,
    booktitle = {Vision, Modeling, and Visualization},
    title     = {{Image Pre-Segmentation from Shadow Masks}},
    author    = {Heep, Moritz and Parakkat, Amal Dev and Zell, Eduard},
    year      = {2025},
    publisher = {The Eurographics Association},
    doi       = {10.2312/vmv.20251239}
}
```
