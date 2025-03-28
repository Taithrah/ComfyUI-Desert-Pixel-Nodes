"""
Optimized nodes for ComfyUI (Refactored)
"""

import logging
import os
from typing import Dict, Type

# region ################### LOGGING SETUP ###################
# Get the directory of the current .py file
script_dir = os.path.dirname(os.path.abspath(__file__))
log_path = os.path.join(script_dir, "dp_nodes_debug.log")

# Configure logging before any imports
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("DP_Nodes")
# endregion

# region ################### NODE IMPORTS ###################
try:
    # Initialize mappings with type hints
    NODE_CLASS_MAPPINGS: Dict[str, Type] = {}
    NODE_DISPLAY_NAME_MAPPINGS: Dict[str, str] = {}
    WEB_DIRECTORY = "js"

    logger.info("Starting DP Nodes initialization...")

    # Core dependencies
    try:
        logger.info("Core dependencies loaded successfully")
    except ImportError as e:
        logger.error(f"Failed to import core dependencies: {str(e)}")
        raise

    # Organized node imports by category
    # Animation Nodes
    # Specialized Components
    from .nodes.dp_add_background_to_png import DP_Add_Background_To_Png
    from .nodes.dp_advanced_sampler import DP_Advanced_Sampler
    from .nodes.dp_animation_calculator_5inputs import DP_Animation_Calculator_5_Inputs
    from .nodes.dp_animation_calculator_10inputs import (
        DP_Animation_Calculator_10_Inputs,
    )
    from .nodes.dp_animation_int_selectors import (
        DP_Diff_Int_8step_selector,
        DP_Draggable_Int_1step,
        DP_Draggable_Int_4step,
        DP_Draggable_Int_8step,
        DP_Transition_Frames_Selector,
    )

    # Image Processing
    from .nodes.dp_big_letters import DP_Big_Letters
    from .nodes.dp_broken_token import DP_Broken_Token
    from .nodes.dp_checkpoint_loader import DP_Load_Checkpoint_With_Info
    from .nodes.dp_clean_prompt import DP_clean_prompt
    from .nodes.dp_clean_prompt_travel import DP_Clean_Prompt_Travel
    from .nodes.dp_condition_mixer import DP_Condition_Switch

    # Advanced Features
    from .nodes.dp_controlnet import (
        DP_ControlNetApplyAdvanced,
        DP_Load_Controlnet_Model_With_Name,
    )
    from .nodes.dp_crazy_prompt_mixer import DP_Crazy_Prompt_Mixer

    # Generators
    from .nodes.dp_crazy_random_prompt_generator import DP_Random_Crazy_Prompt_Generator

    # Control and Utilities
    from .nodes.dp_create_simple_json import DP_create_json_file
    from .nodes.dp_draggable_floats import (
        DP_Draggable_Floats_1,
        DP_Draggable_Floats_2,
        DP_Draggable_Floats_3,
    )

    # Video Processing
    from .nodes.dp_fast_slow_motion import DP_FastSlowMotion
    from .nodes.dp_float_stepper import DP_Float_Stepper
    from .nodes.dp_image_color_analyzer import DP_Image_Color_Analyzer
    from .nodes.dp_image_color_effect import DP_Image_Color_Effect
    from .nodes.dp_image_effect_processor import DP_Image_Effect_Processor
    from .nodes.dp_image_empty_latent_switch_flux import (
        DP_Image_Empty_Latent_Switch_Flux,
    )
    from .nodes.dp_image_empty_latent_switch_sdxl import (
        DP_Image_Empty_Latent_Switch_SDXL,
    )
    from .nodes.dp_Image_Grid_To_Image import DP_Image_Grid_To_Image
    from .nodes.dp_Image_Slice_To_Grid import DP_Image_Slice_To_Grid
    from .nodes.dp_image_slide_show import DP_Image_Slide_Show
    from .nodes.dp_image_strip import DP_Image_Strip
    from .nodes.dp_image_strip_edege_mask import DP_Strip_Edge_Masks
    from .nodes.dp_latent_split import DP_Latent_Split
    from .nodes.dp_load_image import DP_Load_Image_Effects
    from .nodes.dp_load_image_minimal import DP_Load_Image_Minimal
    from .nodes.dp_load_image_small import DP_Load_Image_Effects_Small
    from .nodes.dp_load_image_with_seed import DP_Load_Image_With_Seed
    from .nodes.dp_lora_random_strength_controller import (
        DP_Lora_Random_Strength_Controller,
    )
    from .nodes.dp_lora_strength_controller import DP_Lora_Strength_Controller
    from .nodes.dp_model_loaders import (
        DP_Load_Dual_CLIP_With_Info,
        DP_Load_UNET_With_Info,
    )

    # Text and Prompt Handling
    from .nodes.dp_prompt_inverter import DP_Prompt_Inverter
    from .nodes.dp_prompt_manager_small import (
        DP_Prompt_Manager_Small,
        DP_Prompt_Mode_Controller,
    )
    from .nodes.dp_prompt_styler import DP_Prompt_Styler
    from .nodes.dp_prompt_token_compressor import DP_SmartPromptCompressor
    from .nodes.dp_prompt_travel_prompt import DP_Prompt_Travel_Prompt
    from .nodes.dp_quick_model_link import DP_symlink
    from .nodes.dp_random_character import DP_Random_Character
    from .nodes.dp_random_logo_style_generator import DP_Random_Logo_Style_Generator
    from .nodes.dp_random_min_max import DP_random_min_max
    from .nodes.dp_random_psychedelic_punk_generator import (
        DP_Random_Psychedelic_Punk_Generator,
    )
    from .nodes.dp_random_vehicle_generator import DP_Random_Vehicle_Generator
    from .nodes.dp_randon_superhero_prompt_generator import (
        DP_Random_Superhero_Prompt_Generator,
    )
    from .nodes.dp_sampler_with_info import DP_Sampler_With_Info
    from .nodes.dp_save_preview_image import DP_Save_Preview_Image
    from .nodes.dp_simple_width_height import DP_Aspect_Ratio_Picker
    from .nodes.dp_string_switches import (
        DP_3_String_Switch_Or_Connect,
        DP_5_String_Switch_Or_Connect,
        DP_10_String_Switch_Or_Connect,
    )
    from .nodes.dp_string_with_switch import (
        DP_2_String_Switch,
        DP_String_Text,
        DP_String_Text_With_Sdxl_Weight,
    )
    from .nodes.dp_switch_controller import DP_Switch_Controller
    from .nodes.dp_text_preview import DP_Text_Preview
    from .nodes.dp_video_effect_sender_receiver import (
        DP_Video_Effect_Receiver,
        DP_Video_Effect_Sender,
    )
    from .nodes.dp_video_flicker import DP_Video_Flicker
    from .nodes.dp_video_looper import DP_Video_Looper
    from .nodes.dp_video_transition import DP_Video_Transition

    logger.info("All node imports completed successfully")

    # region ################### NODE MAPPING CONFIGURATION ###################
    # Single source of truth for node mappings
    NODE_CLASS_MAPPINGS = {
        # Animation Nodes
        "DP Animation Calculator 5 Inputs": DP_Animation_Calculator_5_Inputs,
        "DP Animation Calculator 10 Inputs": DP_Animation_Calculator_10_Inputs,
        "DP Transition Frames Selector": DP_Transition_Frames_Selector,
        "DP Diff Int 8step Selector": DP_Diff_Int_8step_selector,
        "DP Draggable Int 1step": DP_Draggable_Int_1step,
        "DP Draggable Int 4step": DP_Draggable_Int_4step,
        "DP Draggable Int 8step": DP_Draggable_Int_8step,
        # Image Processing
        "DP Big Letters": DP_Big_Letters,
        "DP Image Color Analyzer": DP_Image_Color_Analyzer,
        "DP Image Color Effect": DP_Image_Color_Effect,
        "DP Image Effect Processor": DP_Image_Effect_Processor,
        "DP Image Empty Latent Switch Flux": DP_Image_Empty_Latent_Switch_Flux,
        "DP Image Empty Latent Switch SDXL": DP_Image_Empty_Latent_Switch_SDXL,
        "DP Image Slide Show": DP_Image_Slide_Show,
        "DP Image Strip": DP_Image_Strip,
        "DP Strip Edge Masks": DP_Strip_Edge_Masks,
        "DP Load Image Effects": DP_Load_Image_Effects,
        "DP Load Image Effects Small": DP_Load_Image_Effects_Small,
        "DP Load Image Minimal": DP_Load_Image_Minimal,
        "DP Save Preview Image": DP_Save_Preview_Image,
        "DP Image Slice To Grid": DP_Image_Slice_To_Grid,
        "DP Image Grid To Image": DP_Image_Grid_To_Image,
        # Text and Prompts
        "DP Prompt Inverter": DP_Prompt_Inverter,
        "DP Broken Token": DP_Broken_Token,
        "DP Clean Prompt": DP_clean_prompt,
        "DP Clean Prompt Travel": DP_Clean_Prompt_Travel,
        "DP Prompt Manager Small": DP_Prompt_Manager_Small,
        "DP Prompt Styler": DP_Prompt_Styler,
        "DP Prompt Mode Controller": DP_Prompt_Mode_Controller,
        "DP Prompt Token Compressor": DP_SmartPromptCompressor,
        "DP Text Preview": DP_Text_Preview,
        # Control and Utilities
        "DP Create Json File": DP_create_json_file,
        "DP Draggable Floats 1": DP_Draggable_Floats_1,
        "DP Draggable Floats 2": DP_Draggable_Floats_2,
        "DP Draggable Floats 3": DP_Draggable_Floats_3,
        "DP Lora Strength Controller": DP_Lora_Strength_Controller,
        "DP Lora Random Strength Controller": DP_Lora_Random_Strength_Controller,
        "DP Set New Model Folder Link": DP_symlink,
        "DP Random Min Max": DP_random_min_max,
        "DP Aspect Ratio Picker": DP_Aspect_Ratio_Picker,
        "DP 2 String Switch": DP_2_String_Switch,
        "DP String Text": DP_String_Text,
        "DP String Text With Sdxl Weight": DP_String_Text_With_Sdxl_Weight,
        "DP Switch Controller": DP_Switch_Controller,
        # Video Processing
        "DP Fast Slow Motion": DP_FastSlowMotion,
        "DP Video Effect Sender": DP_Video_Effect_Sender,
        "DP Video Effect Receiver": DP_Video_Effect_Receiver,
        "DP Video Flicker": DP_Video_Flicker,
        "DP Video Looper": DP_Video_Looper,
        "DP Video Transition": DP_Video_Transition,
        # Generators
        "DP Random Crazy Prompt Generator": DP_Random_Crazy_Prompt_Generator,
        "DP Random Character": DP_Random_Character,
        "DP Random Logo Style Generator": DP_Random_Logo_Style_Generator,
        "DP Random Superhero Prompt Generator": DP_Random_Superhero_Prompt_Generator,
        "DP Random Psychedelic Punk Generator": DP_Random_Psychedelic_Punk_Generator,
        "DP Crazy Prompt Mixer": DP_Crazy_Prompt_Mixer,
        "DP Random Vehicle Generator": DP_Random_Vehicle_Generator,
        # Advanced Features
        "DP ControlNet Apply Advanced": DP_ControlNetApplyAdvanced,
        "DP Load Controlnet Model With Name": DP_Load_Controlnet_Model_With_Name,
        "DP Load Checkpoint With Info": DP_Load_Checkpoint_With_Info,
        "DP Load UNET With Info": DP_Load_UNET_With_Info,
        "DP Load Dual CLIP With Info": DP_Load_Dual_CLIP_With_Info,
        "DP Advanced Sampler": DP_Advanced_Sampler,
        "DP Sampler With Info": DP_Sampler_With_Info,
        # Specialized Components
        "DP Add Background To Png": DP_Add_Background_To_Png,
        "DP 10 String Switch Or Connect": DP_10_String_Switch_Or_Connect,
        "DP 3 String Switch Or Connect": DP_3_String_Switch_Or_Connect,
        "DP 5 String Switch Or Connect": DP_5_String_Switch_Or_Connect,
        "DP Latent Split": DP_Latent_Split,
        "DP Condition Switch": DP_Condition_Switch,
        "DP Float Stepper": DP_Float_Stepper,
        "DP Prompt Travel Prompt": DP_Prompt_Travel_Prompt,
        "DP Load Image With Seed": DP_Load_Image_With_Seed,
    }

    # Auto-generate display names with exceptions
    NODE_DISPLAY_NAME_MAPPINGS = {
        key: key.replace("_", " ").title() for key in NODE_CLASS_MAPPINGS.keys()
    }

    # Manual display name overrides
    NODE_DISPLAY_NAME_MAPPINGS.update(
        {
            "DP ControlNet Apply Advanced": "DP ControlNet Apply (Advanced)",
            "DP Load Controlnet Model With Name": "DP Load ControlNet Model",
            "DP String Text With Sdxl Weight": "DP String Text With SDXL Weight",
            "DP Add Background To Png": "DP Add Background to PNG",
        }
    )

    logger.info(f"Registered {len(NODE_CLASS_MAPPINGS)} nodes")
    logger.debug(f"Node classes: {list(NODE_CLASS_MAPPINGS.keys())}")

except Exception as e:
    logger.critical(f"Initialization failed: {str(e)}", exc_info=True)
    NODE_CLASS_MAPPINGS = {}
    NODE_DISPLAY_NAME_MAPPINGS = {}
    WEB_DIRECTORY = "./js"

# Required exports
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
