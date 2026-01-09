company_name = "GreenCorp"
emissions = [500.0, 480.0, 420.0, 390.0, 350.0]

total_emissions = sum(emissions)
number_of_years = len(emissions)
average_emissions = total_emissions / number_of_years

print(f"Average annual emissions: {average_emissions} tons.")

print("---Annual Check---")
for year_emission in emissions:
	if year_emission < 400:
		print(f"{year_emission} is a 'Low Emission' year.")
	else:
		print(f"{year_emission} is a 'High Emission' year.")

