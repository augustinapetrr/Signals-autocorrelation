import signal_preparation, autocorrelation, graphs
#from imports import pd, plt, mdates

# Swiss Francs to U.S. Dollar Spot Exchange Rate
francs_to_dollar = signal_preparation.get_data("data/DEXSZUS.csv", 'observation_date', 'DEXSZUS')
autocor_francs_to_dollar = autocorrelation.autocorrelation_function(francs_to_dollar)
graphs.graphs_rendering(francs_to_dollar, autocor_francs_to_dollar)

# Monthly natural gas prices
natural_gas_prices = signal_preparation.get_data("data/monthly_natural_gas_prices.csv", 'Month', 'Price')
autocor_natural_gas_prices = autocorrelation.autocorrelation_function(natural_gas_prices)
graphs.graphs_rendering(natural_gas_prices, autocor_natural_gas_prices)
