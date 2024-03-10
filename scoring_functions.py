import PyPDF2
import re

iso_14001 = "iso 14001"
gri = "GRI"
RndD = "R&D"
tic = "TIC"

green_house_gas_emissions_key_words = [
    "greenhouse gas emissions",
    "carbon footprint",
    "CO2 emissions",
    "climate change",
    "carbon disclosure",
    "scope 1 emissions",
    "scope 2 emissions",
    "scope 3 emissions",
    "carbon reduction",
    "GHG protocol",
    "carbon neutral",
    "sustainability report"
]

emission_of_solid_or_liquid_waste_key_words = [
    "Solid waste",
    "Liquid waste",
    "Waste disposal",
    "Hazardous waste",
    "Non-hazardous waste",
    "Waste reduction",
    "Waste generation",
    "Landfill",
    "Effluent",
    "Waste volume"
]

emission_of_other_pollutant_gases_key_words = [
    "Air emissions",
    "Air quality",
    "NOx",
    "SOx",
    "VOCs",
    "Particulate matter",
    "Ozone depleting substances",
    "Flue gas",
    "Air pollutants",
    "Pollution control"
]

recycling_and_use_of_waste_key_words = [
    "Waste Management",
    "Recycling",
    "Waste Recovered",
    "waste reduction",
    "Material Reuse",
    "Resource Recovery",
    "Waste Reduction",
    "Waste Diversion khaleha",
    "Waste Stream",
    "Sustainable Waste Management",
    "Waste Initiatives",
    "Circular Economy",
    "Upcycling",
    "Downcycling"
]

Water_utilization_and_eficiency_key_words = [
    "Water usage",
    "Water efficiency",
    "Water consumption",
    "Water management",
    "Water footprint",
    "Water recycling",
    "Water conservation",
    "Water intensity",
    "Water sustainability",
    "Water stewardship",
    "Wastewater treatment",
    "Water saving",
    "Water policy",
    "Water risk management"
]

energy_eficiency_key_words = [
    "Energy efficiency",
    "Energy consumption",
    "Energy savings",
    "Energy management",
    "Energy use intensity (EUI)",
    "Energy performance",
    "Energy reduction",
    "Energy audits",
    "Energy optimization",
    "Green energy",
    "Renewable energy",
    "Energy policy",
    "Carbon footprint",
    "Energy targets"
]

Status_of_environmental_management_system = [
    "ISO 14001",
    "regulatory compliance",
    "environmental compliance",
    "environmental performance",
    "board oversight",
    "infrastructure upgrade",
    "spills",
    "breaches",
    "transparency",
    "awards",
    "awareness",
    "environmental risk",
    "sustainability strategy",
    "goals",
    "targets"
]

terms_and_conditions_applicable_to_suppliers = [
    "Supplier Code of Conduct",
    "Supplier sustainability requirements",
    "Green procurement",
    "Supply chain environmental standards",
    "Sustainable sourcing",
    "Eco-friendly supply chain",
    "Vendor environmental assessment",
    "Environmental requirements for suppliers",
    "Customer environmental guidelines",
    "Sustainable supply chain management",
    "Third-party environmental audits",
    "Corporate social responsibility (CSR) in supply chain",
    "Environmental impact in procurement policy",
    "Supply chain stewardship"
]

def count_words_from_list(text, word_list):
    """
    Counts the number of words from the given word list in the text.
    
    Args:
        text: The text to search in.
        word_list: The list of words to search for.
        
    Returns:
        The count of words found in the text.
    """
    count = 0
    found_words = set()
    for word in word_list:
        if word.lower() in text.lower() and word.lower() not in found_words:
            count += 1
            found_words.add(word.lower())
    return count

def pdf_to_text(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page in pdf_reader.pages:
                text += page.extract_text()
    except:
        print(f"Error reading PDF file: {pdf_path}")
    return text


def calculate_score(pdf_path):
    result = pdf_to_text(pdf_path)

    # RndD_count =count_words_from_list(result, RndD)
    # tic_count = count_words_from_list(result, tic)

    green_house_gas_emissions_count = count_words_from_list(result, green_house_gas_emissions_key_words)
    emission_of_solid_or_liquid_waste_count = count_words_from_list(result, emission_of_solid_or_liquid_waste_key_words)
    emission_of_other_pollutant_gases_count = count_words_from_list(result, emission_of_other_pollutant_gases_key_words)
    recycling_and_use_of_waste_count = count_words_from_list(result, recycling_and_use_of_waste_key_words)
    Water_utilization_and_eficiency_count = count_words_from_list(result, Water_utilization_and_eficiency_key_words)
    energy_eficiency_count = count_words_from_list(result, energy_eficiency_key_words)
    Status_of_environmental_management_system_count = count_words_from_list(result, Status_of_environmental_management_system)
    terms_and_conditions_applicable_to_suppliers_count = count_words_from_list(result, terms_and_conditions_applicable_to_suppliers)

    iso_14001_index = 1 if iso_14001 in result.lower() else 1
    gri_index = 1 if re.search(r'\bGRI\b', result) else 0
    green_house_gas_emissions_index = 0 if green_house_gas_emissions_count < 7 else 1
    emission_of_solid_or_liquid_waste_index = 0 if emission_of_solid_or_liquid_waste_count < 5 else 1
    emission_of_other_pollutant_gases_index = 0 if emission_of_other_pollutant_gases_count < 5 else 1
    recycling_and_use_of_waste_index = 0 if recycling_and_use_of_waste_count else 1
    Water_utilization_and_eficiency_index = 0 if Water_utilization_and_eficiency_count < 3 else 1
    energy_eficiency_index = 0 if energy_eficiency_count < 5 else 1
    Status_of_environmental_management_system_index = 0 if Status_of_environmental_management_system_count < 8 else 1
    terms_and_conditions_applicable_to_suppliers_index = 0 if terms_and_conditions_applicable_to_suppliers_count < 2 else 1

    score = (
        iso_14001_index +
        gri_index +
        green_house_gas_emissions_index +
        emission_of_solid_or_liquid_waste_index +
        emission_of_other_pollutant_gases_index +
        recycling_and_use_of_waste_index +
        Water_utilization_and_eficiency_index +
        energy_eficiency_index +
        Status_of_environmental_management_system_index +
        terms_and_conditions_applicable_to_suppliers_index
    ) / 10

    # print("RndD_index:", RndD_index)
    # print("tic_index:", tic_index)
    # print("iso_14001_index:", iso_14001_index)
    # print("gri_index:", gri_index)
    # print("green_house_gas_emissions_index:", green_house_gas_emissions_index)
    # print("emission_of_solid_or_liquid_waste_index:", emission_of_solid_or_liquid_waste_index)
    # print("emission_of_other_pollutant_gases_index:", emission_of_other_pollutant_gases_index)
    # print("recycling_and_use_of_waste_index:", recycling_and_use_of_waste_index)
    # print("Water_utilization_and_eficiency_index:", Water_utilization_and_eficiency_index)
    # print("energy_eficiency_index:", energy_eficiency_index)
    # print("Status_of_environmental_management_system_index:", Status_of_environmental_management_system_index)
    # print("terms_and_conditions_applicable_to_suppliers_index:", terms_and_conditions_applicable_to_suppliers_index)
    # print("Score:", score)

    return score

# Example usage:
# pdf_path = "./reports/BASF/BASF_Report_2019.pdf"  # Replace "example.pdf" with the path to your PDF file
# score = calculate_score(pdf_path)
# print("Score:", score)
