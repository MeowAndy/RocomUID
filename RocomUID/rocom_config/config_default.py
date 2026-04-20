from typing import Dict

from gsuid_core.utils.plugins_config.models import (
    GSC,
    GsStrConfig,
    GsBoolConfig,
    GsListStrConfig,
)

CONFIG_DEFAULT: Dict[str, GSC] = {
    "RCPrefix": GsStrConfig(
        "插件命令前缀（确认无冲突再修改）",
        "用于设置RocomUID前缀的配置",
        "rc",
    ),
    "RC_wegame_key": GsStrConfig(
        "wegame后台数据key",
        "使用wegame获取数据的key",
        "",
    )
}
