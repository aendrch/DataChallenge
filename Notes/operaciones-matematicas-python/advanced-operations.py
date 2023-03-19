lysergic_planet_input = input('Enter the distance from the sun for the lysergic planet in KM: ')
acid_planet_input = input('Enter the distance from the sun for the acid planet in KM: ')

lysergic_planet = int(lysergic_planet_input)
acid_planet = int(acid_planet_input)

distance_km = acid_planet - lysergic_planet
print(abs(distance_km))
