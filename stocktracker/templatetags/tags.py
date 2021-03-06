from django import template
from stocktracker.methods import format_stock_info, due_diligence
import py_trading

# templatetags vs static/tags?
register = template.Library()

@register.filter(name='stocks_from_portfolio')
def stocks_from_portfolio(portfolio):
	'''
	'portfolio' would be the Portfolio model
	'''
	print('stocks_from_portfolio', portfolio.stocks)
	return format_stock_info(portfolio.stocks)

# Add the methods for turning a Portfolio into a list of stocks with all of its values
# Portfolio.objects.all(), format_stock_info, {% for stock in stocks %}
@register.filter(name='get_all_portfolios')
def get_all_porfolios(portfolios):
	for portfolio in portfolios.all():
		print(portfolio.stocks)
	return portfolios.all()

@register.filter(name='stock_due_diligence')
def stock_due_diligence(stock):
	stock_object = py_trading.Stock(stock.ticker)
	return stock_object.big_money()

@register.filter(name='df_to_iter')
def df_to_iter(df):
	return df.values

@register.filter(name='df_values')
def df_columns(df):
	return df.columns