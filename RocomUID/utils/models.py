from typing import Any, Dict, List, Optional, Union

from msgspec import Struct

################
# 用户信息 #
################
class UserAward(Struct):
    nickname: str
    level: int
    avatar: str
    registerDate: str

class BattleInfo(Struct):
    matches: int
    wins: int
    rank: str

class ElvesInfo(Struct):
    totalElves: int
    colorfulElves: int
    shinyElves: int
    amazingElves: int

class CollectionInfo(Struct):
    pokedexCount: int
    costumeCount: int

class UserItemsInfo(Struct):
    elfEgg: int
    elfFruit: int

class UserInfo(Struct):
    basic: UserAward
    battle: BattleInfo
    elves: ElvesInfo
    collection: CollectionInfo
    items: UserItemsInfo

