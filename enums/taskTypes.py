from enum import Enum

class TaskType(Enum):

    # Standard Task Types
    BLOCK_PLACE = "blockplace"
    BLOCK_PLACE_CERTAIN = "blockplacecertain"
    BLOCK_BREAK = "blockbreak"
    BLOCK_BREAK_CERTAIN = "blockbreakcertain"
    BREEDING = "breeding"
    BREWING = "brewing"
    BUCKET_EMPTY = "bucketempty"
    BUCKET_FILL = "bucketfill"
    COMMAND = "command"
    CONSUME = "consume"
    CRAFTING = "crafting"
    DEAL_DAMAGE = "dealdamage"
    DISTANCE_FROM = "distancefrom"
    ENCHANTING = "enchanting"
    EXP_EARN = "expearn"
    FARMING = "farming"
    FARMING_CERTAIN = "farmingcertain"
    INVENTORY = "inventory"
    MILKING = "milking"
    MOB_KILLING = "mobkilling"
    MOB_KILLING_CERTAIN = "mobkillingcertain"
    PERMISSION = "permission"
    PLAYER_KILLING = "playerkilling"
    PLAYTIME = "playtime"
    POSITION = "position"
    SHEARING = "shearing"
    TAMING = "taming"
    WALKING = "walking"
    FISHING = "fishing"
    FISHING_CERTAIN = "fishingcertain"

    # Essentials Task Types
    ESSENTIALS_BALANCE = "essentials_balance"
    ESSENTIALS_MONEYEARN = "essentials_moneyearn"

    # VotingPlugin Task Types (For Potential Future Usage Idk)
    VOTINGPLUGIN_VOTE = "votingplugin_vote"
