from copy import deepcopy

from gsuid_core.utils.error_reply import ERROR_CODE
from gsuid_core.sv import get_plugin_available_prefix

prefix = get_plugin_available_prefix("RocomUID")

RC_ERROR_CODE = deepcopy(ERROR_CODE)

def get_error(retcode: int) -> str:
    msg_list = [f"❌错误代码为: {retcode}"]
    if retcode in RC_ERROR_CODE:
        msg_list.append(f"📝错误信息: {RC_ERROR_CODE[retcode]}")
    return "\n".join(msg_list)
