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

# US unemployment rate
unemployment_rate = signal_preparation.get_data("data/unemployment.csv", 'observation_date', 'LNS14000024')
autocor_unemployment_rate = autocorrelation.autocorrelation_function(unemployment_rate)
graphs.graphs_rendering(unemployment_rate, autocor_unemployment_rate)

# Global CO2 Emissions from Fossil Fuels
co2_emissions = signal_preparation.get_data("data/global_co2.csv", 'Year', 'Total')
autocor_co2_emissions = autocorrelation.autocorrelation_function(co2_emissions)
graphs.graphs_rendering(co2_emissions, autocor_co2_emissions)

# Lithuania population
ltu_population = signal_preparation.get_data("data/Lithuania-population.csv", 'Date', 'Population')
autocor_ltu_population = autocorrelation.autocorrelation_function(ltu_population)
graphs.graphs_rendering(ltu_population, autocor_ltu_population)