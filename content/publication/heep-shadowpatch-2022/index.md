---
title: 'ShadowPatch: Shadow Based Segmentation for Reliable Depth Discontinuities
  in Photometric Stereo'
authors:
- admin
- Eduard Zell
date: '2022-10-01'
publishDate: '2024-06-17T11:50:34.010317Z'
publication_types:
- article-journal
publication: '*Computer Graphics Forum*'
doi: 10.1111/cgf.14707
abstract: Abstract Photometric stereo is a well‐established method with outstanding
  traits to recover surface details and material properties, like surface albedo or
  even specularity. However, while the surface is locally well‐defined, computing
  absolute depth by integrating surface normals is notoriously difficult. Integration
  errors can be introduced and propagated by numerical inaccuracies from inter‐reflection
  of light or non‐Lambertian surfaces. But especially ignoring depth discontinuities
  for overlapping or disconnected objects, will introduce strong distortion artefacts.
  During the acquisition process the object is lit from different positions and self‐shadowing
  is in general considered as an unavoidable drawback, complicating the numerical
  estimation of normals. However, we observe that shadow boundaries correlate strongly
  with depth discontinuities and exploit the visual structure introduced by self‐shadowing
  to create a consistent image segmentation of continuous surfaces. In order to make
  depth estimation more robust, we deeply integrate photometric stereo with depth‐from‐stereo.
  Having obtained a shadow based segmentation of continuous surfaces, allows us to
  reduce the computational cost for correspondence search in depth‐from‐stereo. To
  speed‐up computation further, we merge segments into larger meta‐segments during
  an iterative depth optimization. The reconstruction error of our method is equal
  or smaller than previous work, and reconstruction results are characterized by robust
  handling of depth‐discontinuities, without any smearing artifacts.

# links:
# - name: URL
#   url: https://onlinelibrary.wiley.com/doi/10.1111/cgf.14707

url_pdf: 'https://onlinelibrary.wiley.com/doi/epdf/10.1111/cgf.14707'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: 'https://youtu.be/XYmJOfnWTHg?si=3G22FUG2L24ZBlOh'

image:
  caption: ''
  focal_point: ''
  preview_only: false
---
