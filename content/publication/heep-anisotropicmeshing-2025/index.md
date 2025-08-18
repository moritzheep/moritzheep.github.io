---
title: "Feature-Preserving Mesh Decimation for Normal Integration"

aliases:
- "/anisotropic-screen-meshing/"

authors:
- admin
- svenbehnke
- eduardzell
date: '2025-06-11'
publishDate: '2025-04-15'
publication_types:
- inproceedings
publication: '*IEEE Conference on Computer Vision and Pattern Recognition (CVPR)}*'
# doi: "10.1007/978-3-031-72920-1_25"
abstract: "This work improves normal integration for 3D surface reconstruction by replacing dense pixel grids with sparse anisotropic triangle meshes. By adapting mesh density to local geometry -- preserving detail in complex areas while simplifying flat regions -- we achieve significant compression. This reduces processing time from hours to minutes for high-resolution images while maintaining accuracy"

url_pdf: 'https://www.ais.uni-bonn.de/papers/CVPR_2025_Heep_with_Supplementary.pdf'
url_preprint: 'https://arxiv.org/abs/2504.00867'
url_code: 'https://github.com/moritzheep/anisotropic-screen-meshing'
# url_dataset: ''
url_poster: 'poster.pdf'
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

sections: [Motivation, Overview, Results]
---
## Motivation
Normal integration reconstructs 3D surfaces from normal maps obtained e.g. by photometric stereo. These normal maps capture surface details down to the pixel level but require large computational resources for integration at high resolutions. In this work, we replace the dense pixel grid with a sparse anisotropic triangle mesh before normal integration. We adapt the triangle mesh to the local geometry in the case of complex surface structures and remove oversampling from flat featureless regions.
For high-resolution images, the resulting compression reduces normal integration runtimes from hours to minutes while maintaining high surface accuracy.
## Overview
Our algorithm iteratively refines an existing triangle mesh in screen space based on the observed surface normals from photometric stereo. We initialize this triangle mesh by covering each *foreground* pixel with two triangles. We then repeatedly

1. **Collapse Edges** that are inconsequential for the surface shape,
2. **Align Edges** with ridges and furrows of the underlying surface and
2. **Move Vertices** onto ridges and furrows.

The result is a triangle mesh that is much sparser than the original pixel grid and well-adapted to represent the underlying surface after normal integration. 
<div style="display: flex; justify-content: space-between;">
  <figure style="width: 30%; margin: 0; text-align: center;">
    <img src="figures/image_cv01_rot000_anisotropic_GT_low.svg" alt="Low Resolution" style="width: 100%;">
    <figcaption>Low Resolution</figcaption>
  </figure>
  <figure style="width: 30%; margin: 0; text-align: center;">
    <img src="figures/image_cv01_rot000_anisotropic_GT_mid.svg" alt="Mid Resolution" style="width: 100%;">
    <figcaption>Mid Resolution</figcaption>
  </figure>
  <figure style="width: 30%; margin: 0; text-align: center;">
    <img src="figures/image_cv01_rot000_anisotropic_GT_high.svg" alt="High Resolution" style="width: 100%;">
    <figcaption>High Resolution</figcaption>
  </figure>
</div>
The sparsity is controlled either explicitly by setting a vertex budget or implicitly by setting a limit on the allowed deviation from the underlying surface.

## Result
{{< mesh-comparison 
    modelA="meshes/david_2048_20k_iso.glb" 
    modelB="meshes/david_2048_20k_ours.glb" 
    titleA="Isotropic" 
    titleB="Ours"
    height="800px"
    caption="Final triangle meshes after integration for isotropic remeshing and our anisotropic decimation. Despite having comparably many vertices, our anisotropic decimation preserves details much better."
>}}

Our results show that careful alignment of vertices and edges to ridges and furrows of the underlying surface is key to surpassing the quality of previous methods and maintaining high geometric faithfulness even at high compression ratios. Conversely, we achieve comparable results to pixel-based methods at moderate compression ratios. Our method is versatile and allows balancing runtime and quality. It can be adjusted to the needs of almost any photometric stereo pipeline. We included mesh files in the [supplementary material](https://drive.google.com/uc?export=download&id=1VaV_LrEw-LG2u2VpW7cDcjJjfyHCDcxh) to give an impression of the quality of our method.

## Citation

```
@InProceedings{Heep_2025_CVPR,
    author    = {Heep, Moritz and Behnke, Sven and Zell, Eduard},
    title     = {Feature-Preserving Mesh Decimation for Normal Integration},
    booktitle = {Proceedings of the Computer Vision and Pattern Recognition Conference (CVPR)},
    month     = {June},
    year      = {2025},
    pages     = {5783-5792}
}
```
