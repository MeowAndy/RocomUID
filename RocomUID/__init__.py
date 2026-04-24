from gsuid_core.sv import Plugins

from .rocom_config.rocom_config import get_rc_prefix

Plugins(name="RocomUID", force_prefix=[get_rc_prefix()], allow_empty_prefix=False)
