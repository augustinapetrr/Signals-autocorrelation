import signal_preparation, autocorrelation, graphs
#from imports import pd, plt, mdates

# Swiss Francs to U.S. Dollar Spot Exchange Rate
print("Swiss Francs to U.S. Dollar Spot Exchange Rate")
francs_to_dollar = signal_preparation.get_data("data/DEXSZUS.csv", 'observation_date', 'DEXSZUS')
autocor_francs_to_dollar = autocorrelation.autocorrelation_function(francs_to_dollar)
print(f"Inertia duration: {autocorrelation.inertia_duration(autocor_francs_to_dollar)} days")
graphs.graphs_rendering(francs_to_dollar, autocor_francs_to_dollar, "Days", 2)

# Monthly natural gas prices
print("Monthly natural gas prices")
natural_gas_prices = signal_preparation.get_data("data/monthly_natural_gas_prices.csv", 'Month', 'Price')
autocor_natural_gas_prices = autocorrelation.autocorrelation_function(natural_gas_prices)
print(f"Inertia duration: {autocorrelation.inertia_duration(autocor_natural_gas_prices)} months")
graphs.graphs_rendering(natural_gas_prices, autocor_natural_gas_prices, "Months", 2)

# US unemployment rate
print("US unemployment rate")
unemployment_rate = signal_preparation.get_data("data/unemployment.csv", 'observation_date', 'LNS14000024')
autocor_unemployment_rate = autocorrelation.autocorrelation_function(unemployment_rate)
print(f"Inertia duration: {autocorrelation.inertia_duration(autocor_unemployment_rate)} months")
graphs.graphs_rendering(unemployment_rate, autocor_unemployment_rate, "Months", 5)

# Global CO2 Emissions from Fossil Fuels
print("Global CO2 Emissions from Fossil Fuels")
co2_emissions = signal_preparation.get_data("data/global_co2.csv", 'Year', 'Total')
autocor_co2_emissions = autocorrelation.autocorrelation_function(co2_emissions)
print(f"Inertia duration: {autocorrelation.inertia_duration(autocor_co2_emissions)} years")
graphs.graphs_rendering(co2_emissions, autocor_co2_emissions, "Years", 10)

# Lithuania population
print("Lithuania population")
ltu_population = signal_preparation.get_data("data/Lithuania-population.csv", 'Date', 'Population')
autocor_ltu_population = autocorrelation.autocorrelation_function(ltu_population)
print(f"Inertia duration: {autocorrelation.inertia_duration(autocor_ltu_population)} years")
graphs.graphs_rendering(ltu_population, autocor_ltu_population, "Years", 5)

# Noised monthly natural gas prices
print("Noised monthly natural gas prices")
noise_levels = [2.8, 4.5, 9.0]
noised_natural_gas_prices = autocorrelation.signal_with_noise(natural_gas_prices, noise_levels)
for i in range(len(noise_levels)):
    autocor_noised = autocorrelation.autocorrelation_function(noised_natural_gas_prices[i])
    print(f"Inertia duration: {autocorrelation.inertia_duration(autocor_noised)} months")
    graphs.graphs_rendering(noised_natural_gas_prices[i], autocor_noised, "Months", 2)