# GUI Constants for Interactive SD

DIFFUSERS_CONTROLNET_MODEL = [
    "Automatic",

    "brad-twinkl/controlnet-union-sdxl-1.0-promax",
    "xinsir/controlnet-union-sdxl-1.0",
    "xinsir/anime-painter",
    "TheMistoAI/MistoLine",
    "Eugeoter/noob-sdxl-controlnet-canny",
    "Eugeoter/noob-sdxl-controlnet-lineart_anime",
    "Eugeoter/noob-sdxl-controlnet-depth",
    "Eugeoter/noob-sdxl-controlnet-normal",
    "Eugeoter/noob-sdxl-controlnet-softedge_hed",
    "Eugeoter/noob-sdxl-controlnet-scribble_pidinet",
    "Eugeoter/noob-sdxl-controlnet-scribble_hed",
    "Eugeoter/noob-sdxl-controlnet-manga_line",
    "Eugeoter/noob-sdxl-controlnet-lineart_realistic",
    "Eugeoter/noob-sdxl-controlnet-depth_midas-v1-1",
    "r3gm/controlnet-noobai-openpose-sdxl-fp16",
    "r3gm/controlnet-rough-coating-v1-sdxl-fp16",
    "r3gm/controlnet-line2color-v2-sdxl-fp16",
    "r3gm/controlnet-recolor-anime-sdxl-fp16",
    "r3gm/controlnet-Xdog_sketch-sdxl-fp16",
    "r3gm/controlnet-inpaint-dreamer-sdxl-fp16",
    "r3gm/controlnet-union-promax-sdxl-fp16",
    "r3gm/controlnet-inpaint-anime-sdxl-fp16",
    "r3gm/controlnet-kohaku-canny-sdxl-fp16",
    "r3gm/controlnet-openpose-sdxl-1.0-fp16",
    "r3gm/controlnet-canny-scribble-integrated-sdxl-v2-fp16",
    "r3gm/controlnet-union-sdxl-1.0-fp16",
    "r3gm/controlnet-lineart-anime-sdxl-fp16",
    "r3gm/control_v1p_sdxl_qrcode_monster_fp16",
    "r3gm/controlnet-tile-sdxl-1.0-fp16",
    "r3gm/controlnet-recolor-sdxl-fp16",
    "r3gm/controlnet-openpose-twins-sdxl-1.0-fp16",
    "r3gm/controlnet-qr-pattern-sdxl-fp16",
    "dimitribarbot/controlnet-dwpose-sdxl-1.0",
    "dimitribarbot/controlnet-openpose-sdxl-1.0-safetensors",
    "Yakonrus/SDXL_Controlnet_Tile_Realistic_v2",
    "briaai/BRIA-2.3-ControlNet-Recoloring",
    "briaai/BRIA-2.3-ControlNet-Canny",
    "briaai/BRIA-2.3-ControlNet-Pose",

    "lllyasviel/control_v11p_sd15_openpose",
    "lllyasviel/control_v11p_sd15_canny",
    "lllyasviel/control_v11f1p_sd15_depth",
    "lllyasviel/control_v11p_sd15_inpaint",
    "monster-labs/control_v1p_sd15_qrcode_monster",
    "yuanqiuye/qrcode_controlnet_v3",
]

URL_HYP = "https://huggingface.co/ByteDance/Hyper-SD/resolve/main/Hyper-"
URL_PCM = "https://huggingface.co/wangfuyun/PCM_Weights/resolve/main/"
OPTIMIZATION_PARAMS = {
    "None": [30, 7.5, 'DPM++ 2M', 'None', 'None', '', "", ""],
    "SPO": [30, 7.5, 'DPM++ 2M', 'spo-sd-v1-5_4k-p_10ep_lora_diffusers.safetensors', "spo_sdxl_10ep_4k-data_lora_diffusers.safetensors", "", "https://huggingface.co/SPO-Diffusion-Models/SPO-SD-v1-5_4k-p_10ep_LoRA/resolve/main/spo-sd-v1-5_4k-p_10ep_lora_diffusers.safetensors", "https://huggingface.co/SPO-Diffusion-Models/SPO-SDXL_4k-p_10ep_LoRA/resolve/main/spo_sdxl_10ep_4k-data_lora_diffusers.safetensors"],
    "DPO": [30, 7.5, 'DPM++ 2M', 'sd_1_5_dpo_lora_v1-128dim.safetensors', "sd_xl_dpo_lora_v1-128dim.safetensors", "", "https://civitai.com/api/download/models/269377", "https://civitai.com/api/download/models/269354"],
    "DPO Turbo": [8, 2.5, 'TCD', '', "sd_xl_dpo_turbo_lora_v1-128dim.safetensors", "", "", "https://huggingface.co/benjamin-paine/sd-dpo-offsets/resolve/a8751154f72cc87613067082f53e906abfac05d2/sd_xl_dpo_turbo_lora_v1-128dim.safetensors"],
    "Hyper 12step": [12, 5., 'TCD', 'Hyper-SD15-12steps-CFG-lora.safetensors', "Hyper-SDXL-12steps-CFG-lora.safetensors", "", f"{URL_HYP}SD15-12steps-CFG-lora.safetensors", f"{URL_HYP}SDXL-12steps-CFG-lora.safetensors"],
    "Hyper 8step": [8, 5., 'TCD', 'Hyper-SD15-8steps-CFG-lora.safetensors', "Hyper-SDXL-8steps-CFG-lora.safetensors", "", f"{URL_HYP}SD15-8steps-CFG-lora.safetensors", f"{URL_HYP}SDXL-8steps-CFG-lora.safetensors"],
    "Hyper 4step": [4, 0, 'TCD', 'Hyper-SD15-4steps-lora.safetensors', "Hyper-SDXL-4steps-lora.safetensors", "", f"{URL_HYP}SD15-4steps-lora.safetensors", f"{URL_HYP}SDXL-4steps-lora.safetensors"],
    "Hyper 2step": [2, 0, 'TCD', 'Hyper-SD15-2steps-lora.safetensors', "Hyper-SDXL-2steps-lora.safetensors", "", f"{URL_HYP}SD15-2steps-lora.safetensors", f"{URL_HYP}SDXL-2steps-lora.safetensors"],
    "Hyper 1step": [1, 0, 'TCD', 'Hyper-SD15-1step-lora.safetensors', "Hyper-SDXL-1step-lora.safetensors", "", f"{URL_HYP}SD15-1step-lora.safetensors", f"{URL_HYP}SDXL-1step-lora.safetensors"],
    "PCM 16step": [16, 4., 'TCD', 'pcm_sd15_normalcfg_16step_converted.safetensors', "pcm_sdxl_normalcfg_16step_converted.safetensors", "SGM Uniform", f"{URL_PCM}sd15/pcm_sd15_normalcfg_16step_converted.safetensors", f"{URL_PCM}sdxl/pcm_sdxl_normalcfg_16step_converted.safetensors"],
    "PCM 8step": [8, 4., 'TCD', 'pcm_sd15_normalcfg_8step_converted.safetensors', "pcm_sdxl_normalcfg_8step_converted.safetensors", "SGM Uniform", f"{URL_PCM}sd15/pcm_sd15_normalcfg_8step_converted.safetensors", f"{URL_PCM}sdxl/pcm_sdxl_normalcfg_8step_converted.safetensors"],
    "PCM 4step": [4, 2., 'TCD', 'pcm_sd15_smallcfg_4step_converted.safetensors', "pcm_sdxl_smallcfg_4step_converted.safetensors", "SGM Uniform", f"{URL_PCM}sd15/pcm_sd15_smallcfg_4step_converted.safetensors", f"{URL_PCM}sdxl/pcm_sdxl_smallcfg_4step_converted.safetensors"],
    "PCM 2step": [2, 1., 'TCD', 'pcm_sd15_smallcfg_2step_converted.safetensors', "pcm_sdxl_smallcfg_2step_converted.safetensors", "SGM Uniform", f"{URL_PCM}sd15/pcm_sd15_smallcfg_2step_converted.safetensors", f"{URL_PCM}sdxl/pcm_sdxl_smallcfg_2step_converted.safetensors"],
    "Lightning 8step": [8, 0., 'Euler', '', "sdxl_lightning_8step_lora.safetensors", "SGM Uniform", "", "https://huggingface.co/ByteDance/SDXL-Lightning/resolve/main/sdxl_lightning_8step_lora.safetensors"],  # for realistic use 'Euler a trailing'
    "Lightning 4step": [4, 0., 'Euler', '', "sdxl_lightning_4step_lora.safetensors", "SGM Uniform", "", "https://huggingface.co/ByteDance/SDXL-Lightning/resolve/main/sdxl_lightning_4step_lora.safetensors"],
    "Lightning 2step": [2, 0., 'Euler', '', "sdxl_lightning_2step_lora.safetensors", "SGM Uniform", "", "https://huggingface.co/ByteDance/SDXL-Lightning/resolve/main/sdxl_lightning_2step_lora.safetensors"],
    "DMD2 4step": [4, 0., 'LCM', '', 'dmd2_sdxl_4step_lora_fp16.safetensors', '', '', 'https://huggingface.co/tianweiy/DMD2/resolve/main/dmd2_sdxl_4step_lora_fp16.safetensors'],
    "Flash 4step": [4, 0., 'LCM', 'jasperai/flash-sd', 'jasperai/flash-sdxl', 'SGM Uniform', '', ''],
    "LCM": [8, 0., 'LCM Auto-Loader', '', "", "", "", ""],
    "TCD": [8, 0., 'TCD Auto-Loader', '', "", "", "", ""],
}
VALID_OPTI_LORA = list(OPTIMIZATION_PARAMS.keys())[1:18]

MODELS_PROMPT_ENHANCER = [
    "None",
    "Lamini medium",
    "Lamini long",
    "T5 flux",
    "MagicPrompt",
    "Daspartho prompt",
    "SmolLM2",
]

QUALITY_PROMPT_LIST = [
    {
        "name": "None",
        "prompt": [],
        "negative_prompt": [],
    },
    {
        "name": "Common",
        "prompt": ['(masterpiece)', '(best quality)', '(ultra-detailed)', 'intricate details'],
        "negative_prompt": ['longbody', 'lowres', 'bad anatomy', 'bad hands', 'missing fingers', 'pubic hair', 'extra digit', 'fewer digits', 'worst quality', 'low quality', 'very displeasing', '(bad)'],
    },
    {
        "name": "Animagine Common",
        "prompt": ['anime artwork', 'anime style', 'vibrant', 'studio anime', 'highly detailed', 'masterpiece', 'best quality', 'very aesthetic', 'absurdres'],
        "negative_prompt": ['lowres', '(bad)', 'text', 'error', 'fewer', 'extra', 'missing', 'worst quality', 'jpeg artifacts', 'low quality', 'watermark', 'unfinished', 'displeasing', 'oldest', 'early', 'chromatic aberration', 'signature', 'extra digits', 'artistic error', 'username', 'scan', '[abstract]'],
    },
    {
        "name": "Realistic Common",
        "prompt": ['RAW photo', 'sharp details', 'hyperrealistic', 'dynamic pose', 'dynamic background', 'cinematic lighting'],
        "negative_prompt": ['octane render', 'render', 'drawing', 'anime', 'worst quality', 'low quality', 'bad photo', '3d', '2d', 'painting', 'cartoons', 'sketch', 'bad photography', 'blurry', 'open mouth', 'bad anatomy', 'bad hands', 'missing fingers', 'deformed iris', 'deformed pupils', 'deformed eyes', 'bad eyes', 'deformed face', 'ugly face', 'bad face', 'deformed hands', 'bad hands', 'fused fingers', 'morbid', 'mutilated', 'mutation', 'disfigured'],
    },
    {
        "name": "Pony Common",
        "prompt": [],
        "negative_prompt": ['busty', 'ugly face', 'mutated hands', 'low res', 'blurry face', 'black and white', 'the simpsons', 'overwatch', 'apex legends'],
    },
    {
        "name": "Pony Anime Common",
        "prompt": ['masterpiece', 'best quality', 'very aesthetic', 'absurdres'],
        "negative_prompt": ['busty', 'ugly face', 'mutated hands', 'low res', 'blurry face', 'black and white', 'the simpsons', 'overwatch', 'apex legends'],
    },
    {
        "name": "Pony Realism Common",
        "prompt": ['RAW photo', 'sharp details', 'hyperrealistic', 'dynamic pose', 'dynamic background', 'cinematic lighting'],
        "negative_prompt": ['octane render', 'render', 'drawing', 'anime', 'worst quality', 'low quality', 'bad photo', '3d', '2d', 'painting', 'cartoons', 'sketch', 'bad photography', 'blurry', 'open mouth', 'bad anatomy', 'bad hands', 'missing fingers', 'deformed iris', 'deformed pupils', 'deformed eyes', 'bad eyes', 'deformed face', 'ugly face', 'bad face', 'deformed hands', 'bad hands', 'fused fingers', 'morbid', 'mutilated', 'mutation', 'disfigured'],
    },
    {
        "name": "Animagine Standard v3.0",
        "prompt": ['masterpiece', 'best quality'],
        "negative_prompt": ['lowres', 'bad anatomy', 'bad hands', 'text', 'error', 'missing fingers', 'extra digit', 'fewer digits', 'cropped', 'worst quality', 'low quality', 'normal quality', 'jpeg artifacts', 'signature', 'watermark', 'username', 'blurry', 'artist name'],
    },
    {
        "name": "Animagine Standard v3.1",
        "prompt": ['masterpiece', 'best quality', 'very aesthetic', 'absurdres'],
        "negative_prompt": ['lowres', '(bad)', 'text', 'error', 'fewer', 'extra', 'missing', 'worst quality', 'jpeg artifacts', 'low quality', 'watermark', 'unfinished', 'displeasing', 'oldest', 'early', 'chromatic aberration', 'signature', 'extra digits', 'artistic error', 'username', 'scan', '[abstract]'],
    },
    {
        "name": "Animagine Light v3.1",
        "prompt": ['(masterpiece)', 'best quality', 'very aesthetic', 'perfect face'],
        "negative_prompt": ['(low quality', 'worst quality:1.2)', 'very displeasing', '3d', 'watermark', 'signature', 'ugly', 'poorly drawn'],
    },
    {
        "name": "Animagine Heavy v3.1",
        "prompt": ['(masterpiece)', '(best quality)', '(ultra-detailed)', 'very aesthetic', 'illustration', 'disheveled hair', 'perfect composition', 'moist skin', 'intricate details'],
        "negative_prompt": ['longbody', 'lowres', 'bad anatomy', 'bad hands', 'missing fingers', 'pubic hair', 'extra digit', 'fewer digits', 'cropped', 'worst quality', 'low quality', 'very displeasing'],
    },
    {
        "name": "Animagine v4.0 Common",
        "prompt": ['masterpiece', 'high score', 'great score', 'absurdres'],
        "negative_prompt": ['lowres', 'bad anatomy', 'bad hands', 'text', 'error', 'missing finger', 'extra digits', 'fewer digits', 'cropped', 'worst quality', 'low quality', 'low score', 'bad score', 'average score', 'signature', 'watermark', 'username', 'blurry'],
    },
    {
        "name": "One obsession Common",
        "prompt": ['masterpiece', 'best quality', 'amazing quality', 'very awa', 'absurdres', 'newest', 'very aesthetic', 'depth of field', 'highres'],
        "negative_prompt": ['worst quality', 'normal quality', 'anatomical nonsense', 'bad anatomy', 'interlocked fingers', 'extra fingers', 'watermark', 'simple background', 'transparent', 'low quality', 'logo', 'text', 'signature', 'face backlighting', 'backlighting'],
    },
    {
        "name": "NoobAI Common",
        "prompt": ['masterpiece', 'best quality', 'newest', 'absurdres', 'highres'],
        "negative_prompt": ['worst quality', 'old', 'early', 'low quality', 'lowres', 'signature', 'username', 'logo', 'bad hands', 'mutated hands', 'mammal', 'anthro', 'furry', 'ambiguous form', 'feral', 'semi-anthro'],
    },
    {
        "name": "Nova Pony Common",
        "prompt": [],
        "negative_prompt": ['score_4', 'score_5', '3d', 'jpeg artifacts', 'username', 'watermark', 'signature', 'normal quality', 'worst quality', 'large head', 'low quality', 'text', 'error', 'missing fingers', 'extra digits', 'fewer digits', 'bad eye'],
    },
    {
        "name": "Nova Illustrious Common",
        "prompt": ['BREAK', 'depth of field', 'volumetric lighting'],
        "negative_prompt": ['old', 'oldest', 'cartoon', 'graphic', 'text', 'painting', 'crayon', 'graphite', 'abstract', 'glitch', 'deformed', 'mutated', 'ugly', 'disfigured', 'long body', 'lowres', 'bad anatomy', 'bad hands', 'missing fingers', 'extra digits', 'fewer digits', 'cropped', 'very displeasing', '(worst quality)', '(bad quality)', 'bad anatomy', 'sketch', 'jpeg artifacts', 'watermark', 'username', 'signature', 'simple background', 'conjoined', 'bad ai-generated'],
    },
]

NOVA_PONY_PREFIX = ['score_9', 'score_8_up', 'score_7_up', 'score_6_up', 'score_5_up', 'score_4_up', 'source_anime', 'BREAK']
NOVA_ILLUS_PREFIX = ['masterpiece', 'best quality', 'amazing quality', 'very aesthetic', 'high resolution', 'ultra-detailed', 'absurdres', 'newest', 'scenery']
PONY_PREFIX = ['score_9', 'score_8_up', 'score_7_up', 'BREAK']
PONY_NEGATIVE_PREFIX = ['score_4', 'score_5', 'score_6', 'score_1', 'score_2', 'score_3']
PONY_ANIME_PREFIX = ['source_anime']
PONY_NEGATIVE_REALISM_AND_ANIME = ['source_pony', 'source_furry', 'source_cartoon']

AVAILABLE_PREFIX_LIST = [
    {
        "name": "Pony Common",
        "prompt": PONY_PREFIX,
        "negative_prompt": PONY_NEGATIVE_PREFIX,
        "var_negative_prompt": -3,
    },
    {
        "name": "Pony Anime Common",
        "prompt": PONY_ANIME_PREFIX + PONY_PREFIX,
        "negative_prompt": PONY_NEGATIVE_REALISM_AND_ANIME + PONY_NEGATIVE_PREFIX,
        "var_negative_prompt": -3,
    },
    {
        "name": "Pony Realism Common",
        "prompt": PONY_PREFIX,
        "negative_prompt": PONY_NEGATIVE_REALISM_AND_ANIME + PONY_NEGATIVE_PREFIX,
        "var_negative_prompt": -3,
    },
    {
        "name": "Nova Pony Common",
        "prompt": NOVA_PONY_PREFIX,
        "negative_prompt": [],
    },
    {
        "name": "Nova Illustrious Common",
        "prompt": NOVA_ILLUS_PREFIX,
        "negative_prompt": [],
    },
]

all_original_resolutions = [
    # SDXL
    [1152, 896], [1216, 832], [1344, 768], [1536, 640], [1792, 512],
    [1280, 720], [1920, 1080], [2048, 856], [1920, 800],
    [768, 768], [704, 1280], [1280, 1280], [1280, 800],
    [1024, 1536], [768, 1280], [704, 1408],
    [1536, 1536], [1728, 1344], [1824, 1248], [2016, 1152],
    # SD 1.5
    [512, 512], [512, 768], [640, 640], [384, 512],
    [768, 768], [576, 704], [832, 512],
]
ratios = [
    2/3, 3/4, 4/5, 16/9, 1/1, 4/3, 1.43, 1.66, 16/10,
    1.85, 2.35, 2.39, 1.618, 2/1, 21/9, 6/5, 32/27, 71/40
]
