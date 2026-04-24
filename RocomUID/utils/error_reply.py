from copy import deepcopy

from gsuid_core.utils.error_reply import ERROR_CODE
from gsuid_core.sv import get_plugin_available_prefix


def get_prefix() -> str:
    return get_plugin_available_prefix("RocomUID")


prefix = get_prefix()


def get_uid_hint() -> str:
    cur_prefix = get_prefix()
    return f"你还没有绑定过uid哦!\n请使用[{cur_prefix}绑定uid123456]命令绑定!"


UID_HINT = get_uid_hint()

RC_ERROR_CODE = deepcopy(ERROR_CODE)

RC_ERROR_CODE = {
    4001: "您的token已过期，请重新绑定token",
    4002: f"您的token无效，请重新检查token并绑定，token获取方式请输入【{prefix}token帮助】查询"
}

def get_error(retcode: int) -> str:
    msg_list = [f"❌错误代码为: {retcode}"]
    if retcode in RC_ERROR_CODE:
        msg_list.append(f"📝错误信息: {RC_ERROR_CODE[retcode]}")
    return "\n".join(msg_list)
