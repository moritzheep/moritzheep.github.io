---
title: "Feature-Preserving Mesh Decimation for Normal Integration"

aliases:
- "/anisotropic-screen-meshing/"

authors:
- admin
- Sven Behnke
- Eduard Zell
date: '2024-06-11'
publishDate: '2024-03-26'
publication_types:
- inproceedings
publication: '*CVPR*'
# doi: "10.1007/978-3-031-72920-1_25"
# abstract: "Reconstructing surfaces from normals is a key component of photometric stereo. This work introduces an adaptive surface triangulation in the image domain and afterwards performs the normal integration on a triangle mesh. Our key insight is that surface curvature can be computed from normals. Based on the curvature, we identify flat areas and aggregate pixels into triangles. Compared to pixel grids, our triangle meshes adapt locally to surface details and yield much sparser representations. We derive a mesh-based formulation of the normal integration problem. Here, the sparser representations yield major runtime benefits."

# url_pdf: 'https://dl.acm.org/doi/pdf/10.1145/3641234.3671025'
# url_preprint: 'https://arxiv.org/abs/2409.16907'
# url_code: 'https://github.com/moritzheep/adaptive-screen-meshing'
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

# sections: [Overview, Results]
---
Cooming Soon
{{< mesh-comparison 
    modelA="meshes/david_2048_20k_iso.glb" 
    modelB="meshes/david_2048_20k_ours.glb" 
    titleA="Isotropic" 
    titleB="Ours"
    height="800px"
    caption="Final triangle meshes after integration for isotropic remeshing and our anisotropic decimation. Despite having comparably many vertices, our anistropic decimation preserves details much better."
>}}
