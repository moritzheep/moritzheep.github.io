---
title: "Fast Normal Integration for Photometric Stereo Using Coarse-to-Fine Meshing"

aliases:
- "/coarse-to-fine-meshing/"

authors:
- admin
- florianbernard
date: '2027-01-04'
publishDate: '2025-04-15'
publication_types:
- inproceedings
publication: '*IEEE Winter Conference on Applications of Computer Vision (WACV)*'
# doi: "10.1109/CVPR52734.2025.00543"
# abstract: "Normal integration is a fundamental but computationally demanding step in photometric stereo. While recent mesh-based techniques have successfully mitigated the scaling issues of dense pixel grids by employing adaptive triangle meshes, they now suffer from a new bottleneck. By adopting a top-down strategy -- starting with a high-resolution grid and successively removing redundant vertices -- these methods spend a significant part of their total runtime on mesh generation rather than the integration step itself. In this paper, we propose a novel, coarse-to-fine adaptive meshing framework that resolves this overhead. Our method initially constructs a very low-resolution Conforming Delaunay Triangulation of the foreground contour and progressively refines the mesh from the bottom up, guided by quadric error metrics. Because the final mesh resolution is approached from below, our algorithm processes significantly fewer vertices during the intermediate stages. This structural shift drastically accelerates the mesh creation phase while preserving the state-of-the-art runtime benefits and geometric fidelity of mesh-based normal integration."

# url_pdf: 'https://www.ais.uni-bonn.de/papers/CVPR_2025_Heep_with_Supplementary.pdf'
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
- "Normal Integration"

#sections: [Motivation, Overview, Results]
---
# Coming soon
