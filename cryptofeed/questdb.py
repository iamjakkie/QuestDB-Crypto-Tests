
from cryptofeed import FeedHandler
from cryptofeed.backends.quest import TradeQuest
from cryptofeed.defines import TRADES
from cryptofeed.exchanges import Coinbase, Gemini


QUEST_HOST = '127.0.0.1'
QUEST_PORT = 9009




def main():
   f = FeedHandler()
   f.add_feed(Coinbase(channels=[TRADES], symbols=['BTC-USD'], callbacks={TRADES: TradeQuest(host=QUEST_HOST, port=QUEST_PORT)}))
   f.add_feed(Gemini(channels=[TRADES], symbols=['BTC-USD'], callbacks={TRADES: TradeQuest(host=QUEST_HOST, port=QUEST_PORT)}))
   f.run()




if __name__ == '__main__':
   main()
