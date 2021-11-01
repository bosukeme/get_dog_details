"""
Static Variables From Leather
"""

def generate_leather_water_and_co2_savings_tables(lea_lea_sold, lea_col_sold, leather_water_used_static_dict, co2_static_dict):
    """
    Water Savings Table
    """

    # Build function that creates the leather_water_dict
    trad_l_collar = leather_water_used_static_dict['Traditional Leather Collar']
    rec_l_collar = leather_water_used_static_dict['Recycled Leather Collar']
    trad_l_leash = leather_water_used_static_dict['Traditional Leather Leash']
    rec_l_leash = leather_water_used_static_dict['Recycled Leather Leash']

    # For the collar
    leather_water_collar_dict = {
        'Traditional Leather Collar' : {'Litres Of Water Used': trad_l_collar, 'Total': int(lea_col_sold*trad_l_collar), 'Bath Tubs' : int(lea_col_sold*trad_l_collar*0.013)},
        'Recycled Leather Collar' : {'Litres Of Water Used': rec_l_collar, 'Total': int(lea_col_sold*rec_l_collar), 'Bath Tubs' : int(lea_col_sold*rec_l_collar*0.013)}
    }
    leather_water_collar_dict['Leather Collar Savings'] = {'Litres Of Water Used': round(trad_l_collar-rec_l_collar,3), 'Total': int(lea_col_sold*(trad_l_collar-rec_l_collar)), 'Bath Tubs' : int((lea_col_sold*(trad_l_collar-rec_l_collar))*0.013)}


    # For the leash
    leather_water_leash_dict = {
        'Traditional Leather Leash' : {'Litres Of Water Used': trad_l_leash, 'Total': int(lea_lea_sold*trad_l_leash), 'Bath Tubs' : int(lea_lea_sold*trad_l_leash*0.013)},
        'Recycled Leather Leash' : {'Litres Of Water Used': rec_l_leash, 'Total': int(lea_lea_sold*rec_l_leash), 'Bath Tubs' : int(lea_lea_sold*rec_l_leash*0.013)}
    }
    leather_water_leash_dict['Leather Leash Savings'] = {'Litres Of Water Used': round(trad_l_leash-rec_l_leash,3), 'Total': int(lea_lea_sold*round(trad_l_leash-rec_l_leash,3)), 'Bath Tubs' : int((lea_lea_sold*(trad_l_leash-rec_l_leash))*0.013)}

    # Combine leather and leash to create the leather_water_dict
    leather_water_dict = leather_water_collar_dict.copy()
    leather_water_dict.update(leather_water_leash_dict)


    """
    co2 Savings Table
    """


    # Create the co2 dict
    co2_collar = co2_static_dict['Collar Average']
    co2_leash = co2_static_dict['Leash']

    co2_dict = {
        'Collar Average' : {'Litres Of Water Used': co2_collar, 'Total': int(lea_col_sold*co2_collar), 'Tonnes Saved' : int(lea_col_sold*co2_collar/1000)},
        'Recycled Leather Leash' : {'Litres Of Water Used': co2_leash, 'Total': int(lea_lea_sold*co2_leash), 'Tonnes Saved' : int(lea_lea_sold*co2_leash/1000)}
    }

    return leather_water_dict, co2_dict


def generate_polyester_water_and_co2_savings_tables(num_dog_beds_sold, avg_bed_weight):
    """
    Now work on generating all the tables required from the Polyester table
    """
    polyester_co2_tonne_static_dict = {
        'Virgin Polyester' : 5357,
        'Recycled Polyester' : 1339
    }

    ## For the polyester co2 tonne dict
    # Get the static variables
    vir_pol = polyester_co2_tonne_static_dict['Virgin Polyester']
    rec_pol = polyester_co2_tonne_static_dict['Recycled Polyester']

    polyester_co2_tonne_dict = {
        'Virgin Polyester' : {'Tonne': vir_pol, 'KG': round(vir_pol/1000,3)},
        'Recycled Polyester' : {'Tonne': rec_pol, 'KG': round(rec_pol/1000,3)}
    }

    ## For the polyester co2 savings dict - it takes in the polyester_co2_tonne_dict as well as avg_bed_weight and num_dog_beds_sold
    # Create the polyester co2 savings dict
    vir_kg = polyester_co2_tonne_dict['Virgin Polyester']['KG']
    rec_kg = polyester_co2_tonne_dict['Recycled Polyester']['KG']

    polyester_co2_savings_dict = {
        'Virgin Polyester' : {'CO2': round(vir_kg*avg_bed_weight,3), 'Total CO2 - KG': int(round(vir_kg*avg_bed_weight,3)*num_dog_beds_sold), 'Total CO2 - Tonne' : int((round(vir_kg*avg_bed_weight,3)*num_dog_beds_sold)/1000)},
        'Recycled Polyester' : {'CO2': round(rec_kg*avg_bed_weight,3), 'Total CO2 - KG': int(round(rec_kg*avg_bed_weight,3)*num_dog_beds_sold), 'Total CO2 - Tonne' : int((round(rec_kg*avg_bed_weight,3)*num_dog_beds_sold)/1000)}
    }

    polyester_co2_savings_dict['Polyester CO2 Savings'] = {'CO2': round((vir_kg-rec_kg)*avg_bed_weight,3), 'Total CO2 - KG': int(round((vir_kg-rec_kg)*avg_bed_weight,3)*num_dog_beds_sold), 'Total CO2 - Tonne' : int((round((vir_kg-rec_kg)*avg_bed_weight,3)*num_dog_beds_sold)/1000)}


    # Now for the polyester co2 miles dict
    polyester_co2_miles_dict = {
        'Average Co2 per mile - KG' : 0.41,  
    }
    polyester_co2_miles_dict['Miles Saved'] = int(polyester_co2_savings_dict['Polyester CO2 Savings']['Total CO2 - KG'] * polyester_co2_miles_dict['Average Co2 per mile - KG'])
    polyester_co2_miles_dict['Miles Around World'] = 24901
    polyester_co2_miles_dict['Equivalent Saving'] = int(polyester_co2_miles_dict['Miles Saved']/polyester_co2_miles_dict['Miles Around World'])

    # Now for the water usage static dict - note that CBM stands for cubic meters
    polyester_water_usage_static_dict = {
        'Water Usage Per Tonne (CBM)': 71000,
        'Water Saving For Recycled (%)': 86,
        'Average Bath Size (CBM)': 0.13,
        'Water In Olympic Pool': 2500
    }
    polyester_water_usage_static_dict['Water Usage Per KG (CBM)'] = polyester_water_usage_static_dict['Water Usage Per Tonne (CBM)']/1000


    ## For the polyester water savings dict - it takes in the polyester_water_usage_static_dict as well as avg_bed_weight and num_dog_beds_sold
    # Create the polyester water savings dict
    wp_kg = polyester_water_usage_static_dict['Water Usage Per KG (CBM)'] # water used per kg cbm
    avg_bath_cbm = polyester_water_usage_static_dict['Average Bath Size (CBM)']
    water_olymp = polyester_water_usage_static_dict['Water In Olympic Pool']
    water_sv_perc = polyester_water_usage_static_dict['Water Saving For Recycled (%)']
    # print(wp_kg)

    polyester_water_savings_dict = {
        'Virgin Polyester' : {'Water Used (CBM)': int(wp_kg*avg_bed_weight), 'Total Water': int(round(wp_kg*avg_bed_weight,3)*num_dog_beds_sold), 'Bath Tubs' : int(round(wp_kg*avg_bed_weight,3)*avg_bath_cbm), 'Total Bath' : int(round(wp_kg*avg_bed_weight,3)*avg_bath_cbm*num_dog_beds_sold), 'Olympic Pools': int((round(wp_kg*avg_bed_weight,3)*num_dog_beds_sold)/water_olymp)},
        'Recycled Polyester' : {'Water Used (CBM)': int((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100))), 'Total Water': int(round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),3)*num_dog_beds_sold), 'Bath Tubs' : int(round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),3)*avg_bath_cbm), 'Total Bath' : int(round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),3)*avg_bath_cbm*num_dog_beds_sold), 'Olympic Pools': int((round((wp_kg*avg_bed_weight) * (1-(water_sv_perc/100)),3)*num_dog_beds_sold)/water_olymp)}
    }

    # Get all the variables from the current calculations
    wat_sav_kg = polyester_water_savings_dict['Virgin Polyester']['Water Used (CBM)'] - polyester_water_savings_dict['Recycled Polyester']['Water Used (CBM)']
    polyester_water_savings_dict['Polyester Water Savings'] = {'Water Used (CBM)': wat_sav_kg, 'Total Water': int(round(wat_sav_kg,3)*num_dog_beds_sold), 'Bath Tubs' : int(round(wat_sav_kg,3)*avg_bath_cbm), 'Total Bath' : int(round(wat_sav_kg,3)*avg_bath_cbm*num_dog_beds_sold), 'Olympic Pools': int((round(wat_sav_kg,3)*num_dog_beds_sold)/water_olymp)}

    ## Now generate the oil savings dict
    oil_savings_dict = {
        '1 Tonne Of Recycled PET Saves': 0.7,
        '1 KG Of Recycled PET Save': 86,
        'Total Weight Polyester (Tonne)': 0.13,
        'Total Barrels Of Oil': 2500,
        'Barrels Of Oil Saved': 2500,
        'Barrels Saved': 2500
    }
    oil_savings_dict['1 KG Of Recycled PET Save'] = oil_savings_dict['1 Tonne Of Recycled PET Saves']/1000
    oil_savings_dict['Total Weight Polyester (Tonne)'] = int(avg_bed_weight*num_dog_beds_sold/1000)
    oil_savings_dict['Total Barrels Of Oil'] = int(avg_bed_weight*num_dog_beds_sold/1000)
    oil_savings_dict['Barrels Of Oil Saved'] = int((avg_bed_weight*num_dog_beds_sold/1000) * 0.3)
    oil_savings_dict['Barrels Saved'] = int(oil_savings_dict['1 Tonne Of Recycled PET Saves'] * oil_savings_dict['Total Weight Polyester (Tonne)'])

    return polyester_co2_tonne_dict, polyester_co2_savings_dict, polyester_co2_miles_dict, polyester_water_usage_static_dict, polyester_water_savings_dict, oil_savings_dict

"""
Main function
"""
def generate_sustainability_tables(num_dog_beds_sold, avg_bed_weight, lea_lea_sold, lea_col_sold):
    
    """
    Static Dicts for Leather
    """
    co2_static_dict = {
        'Collar Average' : 0.5584,
        'Leash' : 1.5356
    }

    ## Static variables for leather_water_used
    leather_water_used_static_dict = {
        'Traditional Leather Collar': 5.296,
        'Recycled Leather Collar': 0.5296,
        'Traditional Leather Leash': 16.0204,
        'Recycled Leather Leash': 1.4564
    }

    """
    Static Variables From Leather Tab
    """
    """
    ELeather per m² (SLi2) Table
    """
    eleather_pm2_SLi2_dict = {
        'Climate Change (Kg Of CO₂ Saved)' : 34.9,
        'Water Consuption (m³ Saved)' : 0.331,
        'Water Consuption (Liters Saved)' : 331,
        'Land Use (% Saved)' : 77,
        '10,000m² Eleather (Liters Saved)' : 3310000,
    }

    # create the olympic swimming pool variable from the 10km2 eleather variable 
    eleather_pm2_SLi2_dict['10,000m² Eleather (Olympic Swimming Pools)'] = round(eleather_pm2_SLi2_dict['10,000m² Eleather (Liters Saved)']/2500000,3)

    """
    Generate the preliminary tables
    """
    ## Generate the tables for leather analysis
    leather_water_dict, co2_dict = generate_leather_water_and_co2_savings_tables(lea_lea_sold, lea_col_sold, leather_water_used_static_dict, co2_static_dict)

    ## Generate the tables for polyester analysis
    polyester_co2_tonne_dict, polyester_co2_savings_dict, polyester_co2_miles_dict, polyester_water_usage_static_dict, polyester_water_savings_dict, oil_savings_dict = generate_polyester_water_and_co2_savings_tables(num_dog_beds_sold, avg_bed_weight)

    """
    Now to structure out the final output as we expect it
    """
    dog_bed_analysis_input_table = {
        'No. Of Dog Beds Sold Per Year' : num_dog_beds_sold,
        'Average Weight Of Dog Bed (kg)' : avg_bed_weight
    }

    #* For this table, note that the column name for the table keys is 'Raw Material'
    carbon_footprint_analysis_table = {
        'Dog Beds Made From Virgin Polyester' : {'Co2 Per Ton': polyester_co2_savings_dict['Virgin Polyester']['Total CO2 - Tonne'], 'Water Used (Bath Tubs)': polyester_water_savings_dict['Virgin Polyester']['Total Bath'], 'Barrels Of Oil': oil_savings_dict['Total Barrels Of Oil']},
        'Dog Beds Made From RECYCLED Polyester' : {'Co2 Per Ton': polyester_co2_savings_dict['Recycled Polyester']['Total CO2 - Tonne'], 'Water Used (Bath Tubs)': polyester_water_savings_dict['Recycled Polyester']['Total Bath'], 'Barrels Of Oil': oil_savings_dict['Barrels Of Oil Saved']},
        'Total Saving' : {'Co2 Per Ton': polyester_co2_savings_dict['Polyester CO2 Savings']['Total CO2 - Tonne'], 'Water Used (Bath Tubs)': polyester_water_savings_dict['Polyester Water Savings']['Total Bath'], 'Barrels Of Oil': oil_savings_dict['Barrels Saved']}
    }

    leather_collar_and_leash_analysis_input_table = {
        'No. Of Leather Collars Sold' : lea_lea_sold,
        'No. Of Leather Leashes Sold' : lea_col_sold
    }

    leather_collar_and_leash_analysis_table = {
        'Traditional Leather Collar' : {'Litres Of Water Used': leather_water_dict['Traditional Leather Collar']['Total'], 'Water Used (Bath Tubs)': leather_water_dict['Traditional Leather Collar']['Bath Tubs']},
        'Recycled leather Collar' : {'Litres Of Water Used': leather_water_dict['Recycled Leather Collar']['Total'], 'Water Used (Bath Tubs)': leather_water_dict['Recycled Leather Collar']['Bath Tubs']},
        'Collar Water Saving' : {'Litres Of Water Used': leather_water_dict['Leather Collar Savings']['Total'], 'Water Used (Bath Tubs)': leather_water_dict['Leather Collar Savings']['Bath Tubs']},
        'Traditional Leather Leash' : {'Litres Of Water Used': leather_water_dict['Traditional Leather Leash']['Total'], 'Water Used (Bath Tubs)': leather_water_dict['Traditional Leather Leash']['Bath Tubs']},
        'Recycled leather Leash' : {'Litres Of Water Used': leather_water_dict['Recycled Leather Leash']['Total'], 'Water Used (Bath Tubs)': leather_water_dict['Recycled Leather Leash']['Bath Tubs']},
        'Leash Water Saving' : {'Litres Of Water Used': leather_water_dict['Leather Leash Savings']['Total'], 'Water Used (Bath Tubs)': leather_water_dict['Leather Leash Savings']['Bath Tubs']},
    }

    co2_saving_per_item_table = {
        'Recycled Leather Collar' : co2_dict['Collar Average']['Tonnes Saved'],
        'Recycled Leather Leash' : co2_dict['Recycled Leather Leash']['Tonnes Saved']
    }

    return dog_bed_analysis_input_table, carbon_footprint_analysis_table, leather_collar_and_leash_analysis_input_table, leather_collar_and_leash_analysis_table, co2_saving_per_item_table


