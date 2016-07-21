__author__ = 'ONicholls'


from yahoo_finance import Share
from pprint import pprint

ShareObject = Share('BP')

print(ShareObject.get_open())
print
print(ShareObject.get_price())
print
#
ShareObject.refresh()
print(ShareObject.get_price())

print(ShareObject.get_trade_datetime())

pprint(ShareObject.get_historical('2016-05-23', '2016-05-29'))

# closes = [c['Close'] for c in ShareObject.get_historical('2016-05-23', '2016-05-29')]
#
# print(closes)

