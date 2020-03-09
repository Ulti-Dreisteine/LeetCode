# -*- coding: utf-8 -*-
"""
Created on 2020/3/9 20:33

@Project -> File: LeetCode -> 121-买卖股票的最佳时机.py

@Author: luolei

@Email: dreisteine262@163.com

@Describe: 求解买卖股票的最佳时机
"""


def _cal_trends(l: list, mid_idx: int, N: int):
	"""
	计算三点前后两两的趋势
	:param l: list, 待计算list
	:param mid_idx: int, 中点的在prices中的index
	:param N: int, prices记录长度
	"""
	if len(l) == 3:
		a, b, c = l
	elif len(l) == 2:
		if mid_idx == 0:
			a, b, c = 2 * l[0] - l[1], l[0], l[1]
		elif mid_idx == N - 1:
			a, b, c = l[0], l[1], 2 * l[1] - l[0]
		else:
			raise ValueError('ERROR: invalid mid_idx = {}'.format(mid_idx))
	else:
		raise ValueError('ERROR: invalid l, length = {}'.format(len(l)))
	
	def _trend(x, y):
		if x < y:
			return 'up'
		elif x == y:
			return 'flat'
		else:
			return 'down'
	
	return [_trend(a, b), _trend(b, c)]
	
	
def search_max_profit(prices: list) -> (int, int, int):
	"""
	计算所有可能的利润
	:param prices: list, 股票价格随时间变化记录
	:return:
		best_buy: int, 最佳买入时刻
		best_sell: int, 最佳卖出时刻
		max_profit: 最大利润
	"""
	N = len(prices)
	best_buy_loc, best_sell_loc, max_profit = None, None, 0
	
	# 从左往右搜索潜在买入时刻.
	for i in range(N - 1):
		if i == 0:
			l = prices[:2]
		else:
			l = prices[i - 1: i + 2]
		trends = _cal_trends(l, i, N)
		
		buy_loc_ = None
		if i == 0:
			if trends[0] != 'down':
				buy_loc_ = i
		else:
			if (trends[0] != 'up') & (trends[1] != 'down'):
				buy_loc_ = i
		
		if buy_loc_ is None:
			continue
		else:
			# 确定该买入时刻后, 继续往下搜索潜在的卖出时刻.
			for j in range(buy_loc_ + 1, N):
				if j == N - 1:
					l = prices[-2:]
				else:
					l = prices[j - 1: j + 2]
				trends = _cal_trends(l, j, N)
				
				sell_loc_ = None
				if j == N - 1:
					if trends[0] != 'down':
						sell_loc_ = j
				else:
					if (trends[0] != 'down') & (trends[1] != 'up'):
						sell_loc_ = j
				
				if sell_loc_ is None:
					continue
				else:
					print(buy_loc_, sell_loc_)
					profit = prices[sell_loc_] - prices[buy_loc_]
					
					if profit > max_profit:
						best_buy_loc, best_sell_loc, max_profit = i, j, profit
	
	return best_buy_loc, best_sell_loc, max_profit
	
	
if __name__ == '__main__':
	prices = [3, 2, 1, 2, 3, 4, 5, 4, 5, 3, 2, 1, 9, 20, 50]
	best_buy, best_sell, max_profit = search_max_profit(prices)
	




