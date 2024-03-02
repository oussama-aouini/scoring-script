import PyPDF2
import time
import re

start_time = time.time()

greenHouseGasEmissionsIndicators = [
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

emissionOfSolidOrLiquidWasteIndicators  = [
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

emissionOfOtherPollutantGasesIndicators = [
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

recyclingAndUseOfWasteIndicators  = [
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

WaterUtilizationAndEficiencyIndicators = [
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

EnergyEficiencyIndicators = [
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

EMS = [
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

bullet_points = [
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

# Your script code here

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

def convert_pdf_to_text_file(pdf_path):
    """
    Converts a PDF file to a text file in the current directory and checks the existence
    of words in the lists in the extracted text.
    
    Args:
        pdf_path: Path to the PDF file.
    """
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Count words from each indicator list
        greenhouse_gas_count = count_words_from_list(text, greenHouseGasEmissionsIndicators)
        waste_emission_count = count_words_from_list(text, emissionOfSolidOrLiquidWasteIndicators)
        pollutant_gas_count = count_words_from_list(text, emissionOfOtherPollutantGasesIndicators)
        recycling_count = count_words_from_list(text, recyclingAndUseOfWasteIndicators)
        water_utilization_count = count_words_from_list(text, WaterUtilizationAndEficiencyIndicators)
        energy_efficiency_count = count_words_from_list(text, EnergyEficiencyIndicators)
        ems_count = count_words_from_list(text, EMS)
        bullet_points_count = count_words_from_list(text, bullet_points)

        # Check the existence of "GRI"
        gri_count = 1 if re.search(r'\bGRI\b', text) else 0

        iso_14001_value = 1 if "iso 14001" in text.lower() else 0
        greenhouse_gas_value = 0 if greenhouse_gas_count < 7 else 1
        waste_emission_value = 0 if waste_emission_count < 5 else 1
        pollutant_gas_value = 0 if pollutant_gas_count < 5 else 1
        recycling_value = 0 if recycling_count < 1 else 1
        water_utilization_value = 0 if water_utilization_count < 3 else 1
        energy_efficiency_value = 0 if energy_efficiency_count < 5 else 1
        ems_value = 0 if ems_count < 8 else 1
        bullet_points_value = 0 if bullet_points_count < 2 else 1

        total_score = (iso_14001_value + greenhouse_gas_value + waste_emission_value +
                       pollutant_gas_value + recycling_value + water_utilization_value +
                       energy_efficiency_value + ems_value + bullet_points_value + gri_count)

        print("Number of words found from each list:")
        if "iso 14001" in text.lower():
            print("iso 14001: 1")
        else:
            print("iso 14001 0")
        print("Greenhouse Gas Emissions Indicators:", 0 if greenhouse_gas_count < 7 else 1)
        print("Emission of Solid or Liquid Waste Indicators:",0 if waste_emission_count < 5 else 1)
        print("Emission of Other Pollutant Gases Indicators:",0 if  pollutant_gas_count < 5 else 1)
        print("Recycling and Use of Waste Indicators:",0 if recycling_count else 1)
        print("Water Utilization and Efficiency Indicators:", 0 if water_utilization_count < 3 else 1)
        print("Energy Efficiency Indicators:", 0 if energy_efficiency_count < 5 else 1)
        print("EMS:", 0 if ems_count < 8 else 1)
        print("Existence of terms and conditions applicable to suppliers and/or customers regarding environmental:", 0 if bullet_points_count < 2 else 1)
        print("GRI:", gri_count)
        print("Total Score:", total_score)

        print("GRI:", len(re.findall(r'\bGRI\b', text)))

# Example usage
pdf_path = r"BASF_Report_2019.pdf"
convert_pdf_to_text_file(pdf_path)

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.2f} seconds")
