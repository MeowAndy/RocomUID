from gsuid_core.utils.plugins_config.gs_config import StringConfig

from .config_default import CONFIG_DEFAULT
from ..utils.resource.RESOURCE_PATH import CONFIG_PATH

RC_CONFIG = StringConfig("RocomUID", CONFIG_PATH, CONFIG_DEFAULT)

_DEFAULT_PREFIX = "rc"


def get_rc_prefix() -> str:
    """读取控制面板配置的命令前缀，异常时回落默认 rc。"""
    try:
        value = RC_CONFIG.get_config("RCPrefix").data
    except Exception:
        return _DEFAULT_PREFIX

    if value is None:
        return _DEFAULT_PREFIX

    prefix = str(value).strip()
    return prefix or _DEFAULT_PREFIX


RC_GAME_NAME = get_rc_prefix()
