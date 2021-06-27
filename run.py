import os

from TwitchChannelPointsMiner import TwitchChannelPointsMiner
twitch_miner = TwitchChannelPointsMiner(os.getenv('USER'), os.getenv('PASSWORD'))
twitch_miner.analytics(host="127.0.0.1", port=3000, refresh=5) 
twitch_miner.mine(followers=True)