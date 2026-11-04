---
title: "Manifold Embedding of Deep Image Features for Image Matching via Neural Adjoint Maps"

# aliases:
# - "/anisotropic-screen-meshing/"

authors:
- nafieelamrani
- admin
- florianbernard
date: '2026-12-06'
publishDate: '2026-11-03'
publication_types:
- inproceedings
publication: '*Advances in Neural Information Processing Systems (NeurIPS)*'
# doi: "10.1109/CVPR52734.2025.00543"
abstract: "Estimating semantic correspondences between different object instances of similar categories in real-world images is a fundamental challenge in computer vision. While the recent progress in foundation models has significantly advanced solutions for such difficult image correspondence problems, respective methods are often insufficiently regularised. For example, common nearest-neighbour matching with foundation model features often results in noisy correspondences, which is particularly prominent when solving for dense correspondences. In this work, we tackle image matching via functional maps, which have been popularised for 3D shape matching due to their powerful spectral formalism utilising an efficient low-dimensional linear representation. However, functional maps require that domains (in our cases the rectangular image grids) are equipped with an informative and non-trivial geometry. To define a meaningful manifold structure for images, we use Galerkin's method from finite elements to derive a discrete Laplace-Beltrami operator (LBO) based on a manifold embedding of deep image features. Further, we leverage a neural adjoint map that allows to represent non-linear mappings. We demonstrate that our method sets the new state of the art among zero-shot image correspondence methods on multiple dense correspondence benchmarks of real-world images."
# external_link: "https://lovc.cs.uni-bonn.de/index.php/publications/"
url_pdf: 'https://arxiv.org/pdf/2611.05083'
url_preprint: 'https://arxiv.org/abs/2611.05083'
url_code: 'https://github.com/NafieAmrani/NAMI'
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
- "Image Matching"
- "Functional Maps"
- "Finite Elements"

# sections: [Motivation, Overview, Results]
---
For additional information, please read the [preprint](https://arxiv.org/pdf/2611.05083).
