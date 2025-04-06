import signal_preparation, autocorrelation, graphs
#from imports import pd, plt, mdates

# NATURAL GAS
natural_gas_prices = signal_preparation.get_data_gas()
autocor_natural_gas_prices = autocorrelation.autocorrelation_function(natural_gas_prices)
graphs.graphs_rendering(natural_gas_prices, autocor_natural_gas_prices)
