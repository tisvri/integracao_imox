"""
Padrões de mapeapento de braços:
  ARM_MAPPING=1:1,Não alocado:1,2:2,Alocado:2
  ARM_1_PATTERN_ENV=OTHER_ARM_NAME
  ARM_1_LABEL=Não alocado
  ARM_2_PATTERN_ENV=PK_ARM_NAME
  ARM_2_LABEL=Alocado


"""

from __future__ import annotations

import os
from typing import Dict, Optional
from integracao.config import config
import dotenv

dotenv.load_dotenv(override=True)


def load_arm_mapping() -> Dict[str, int]:
    """
    Load ARM_MAPPING from environment variable and return a mapping of arm names to arm IDs.
    Format: "Key1:Value1,Key2:Value2,..."
    Example: "1:1,Não alocado:1,2:2,Alocado:2"
    """

    raw = config.ARM_MAPPING
    mapping: Dict[str, int] = {}
    for pair in raw.split(","):
        pair = pair.strip()
        if ":" not in pair:
            continue
        key, val = pair.rsplit(":", 1)
        mapping[key.strip().lower()] = int(val.strip())
    return mapping

def load_arm_polotrial_patterns() -> Dict[int, Dict[str, str]]:
    """
    Dinamically load Polotrial arm patterns for the project from environment variables.
    Search for ARM_{n}_PATTERN_ENV and ARM_{n}_LABEL in the .env file 
    """

    patterns: Dict[int, Dict[str,str]] = {}

    # Fixed mapping: retrieves attributes directly from config.py

    arm_definitions = {
        1: ("ARM_1_PATTERN_ENV", "ARM_1_LABEL"),
        2: ("ARM_2_PATTERN_ENV", "ARM_2_LABEL"),
    }

    for n, (pattern_env_attr, label_attr) in arm_definitions.items():
        pattern_env_key = getattr(config, pattern_env_attr, None)
        label = getattr(config, label_attr, None)
        if not pattern_env_key or not label:
            continue
        # pattern_env_key is the name of the environment variable that contains the pattern to match for this arm (e.g. "PK_ARM_NAME")
        pattern_value = getattr(config, pattern_env_key, "")
        patterns[n] = {
            "pattern" : pattern_value,
            "label": label
        }
    return patterns


# Singletons loaded only once at module import
ARM_MAPPING = load_arm_mapping()
ARM_POLOTRIAL_PATTERNS = load_arm_polotrial_patterns()


def parse_randomization_group(value) -> Optional[int]:
    if value is None:
        return None
    s=str(value).strip().lower()
    if not s:
        return None
    return ARM_MAPPING.get(s)