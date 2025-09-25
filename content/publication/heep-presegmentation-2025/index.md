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
## Citation

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
