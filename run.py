import os

from TwitchChannelPointsMiner import TwitchChannelPointsMiner
twitch_miner = TwitchChannelPointsMiner(os.getenv('USER'), os.getenv('PASSWORD'))
twitch_miner.mine(followers=True)