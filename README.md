# Interactive Stable Diffusion
A widgets interface based on ipywidgets library for Stable Diffusion.


## Colab

| Colab | Info
| --- | --- |
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/R3gm/SD_diffusers_interactive/blob/main/Stable_diffusion_interactive_notebook.ipynb)  | Interactive-SD Official

Note: In this Colab, it is advisable to use the 'Generate in GUI' cell to keep your session active and prevent disconnection issues due to inactivity.

## GUI

![image](https://github.com/R3gm/SD_diffusers_interactive/assets/114810545/eecfc3f7-54d7-4951-a595-8c98f59a5d89)


## Features:

### Prompt Control:
- **Positive Prompt:** Guide the model's image generation.
- **Negative Prompt:** Specify elements to avoid in the generated image.
- **Prompt Weights:** Emphasize or de-emphasize prompt aspects.
- **Long Prompts:** Manage lengthy prompts with unlimited characters.

### Image Quality Control:
- **Steps:** Determine denoise steps of image generation.
- **CFG:** Adjust creativity vs. strict adherence to prompt.
- **Sampler:** Reduce image noise through denoising.
- **Seed:** Set seed for reproducibility or use -1 for random.
- **Clip Skip:** Skip prompt adherence layers.

### Style and Adaptation:
- **LoRA:** Store small modifications to SD model for efficiency.
- **Embeddings:** Adapt model to a particular style.
- **FreeU:** Improve diffusion model sample quality at no cost.
- **VAE:** Choose VAE for different results.
- **LCM:** Generate images with Latent Consistency Models.
- **ControlNet:** Enhance context-aware image generation.
- **Styles:** Add specific styles to generation.

### Inpainting and Image Modification:
- **Inpaint:** Modify images or remove objects using diffusion model.
- **Img2img:** Modify existing images based on text prompts.
- **Adetailer:** Automate inpainting with adjustable strength.

### Resolution Enhancement:
- **High-resolution:** Increase image size proportionally.
- **Upscaling Tools:** Select different models and options for High-resolution.

### Additional Points:
- **Compatibility**: Support for both ckpt and diffusers models, such as `cagliostrolab/animagine-xl-3.0`.
- **Model version:** SD 1.5 and SDXL diffusers support
- **Save images:** Automatically save the generated images and specify the saving directory.
- **Generation Data:** Utilize generation data from previously generated images and configure the parameters in the GUI; currently, this functionality is only available for specific parameters.
