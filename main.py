import PyPDF2
import time

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

def convert_pdf_to_text_file(pdf_path, output_filename="extracted_text.txt"):
  """
  Converts a PDF file to a text file in the current directory.

  Args:
      pdf_path: Path to the PDF file.
      output_filename: Optional name for the output text file (default: "extracted_text.txt").
  """
  with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
      text += page.extract_text()

    if "iso 14001" in text.lower():
      print("true")
    else:
      print("false")
#   # Write the text to a file
#   with open(output_filename, 'w', encoding="utf-8") as text_file:
#     text_file.write(text)

# Example usage
pdf_path = r"BASF_Report_2019.pdf"
convert_pdf_to_text_file(pdf_path)  # Use default filename

# (Rest of your code)

end_time = time.time()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.2f} seconds")

