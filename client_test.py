import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price =getDataPoint(quote)
        expected_price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
        self.assertEqual(price, expected_price)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price =getDataPoint(quote)
        expected_price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
        self.assertEqual(price, expected_price)

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_calculatePriceBidLowerThanAsk(self):
    quotes = [
      {'top_ask': {'price': 118.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price =getDataPoint(quote)
        expected_price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
        self.assertEqual(price, expected_price)

  def test_getDataPoint_with_zero_bid_ask_prices(self):
    quotes = [
      {'top_ask': {'price': 111.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 118.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 101.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        stock, bid_price, ask_price, price =getDataPoint(quote)
        expected_price = (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
        self.assertEqual(price, expected_price)

  def test_getRatio_divide_by_zero(self):
      # I tested the getRatio when dividing by zero
      self.assertIsNone(getRatio(100, 0))

  def test_getRatio_zero_numerator(self):
      # I tested getRatio when the first price is zero
      self.assertEqual(getRatio(0, 100), 0)

if __name__ == '__main__':
    unittest.main()
