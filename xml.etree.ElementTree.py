
import xml.etree.ElementTree as ET
xml_data = """<?xml version="1.0" encoding="UTF-8"?>
<smartwatches>
    <smartwatch>
        <name>Apple Watch Ultra 2</name>
        <marks>4.8/5</marks>
        <price>$799</price>
        <features>GPS, Health Tracking, Large OLED Display</features>
        <description>Designed for extreme conditions with advanced health and GPS functionalities, robust titanium build.</description>
    </smartwatch>
    <smartwatch>
        <name>Apple Watch Series 9</name>
        <marks>4.7/5</marks>
        <price>$399</price>
        <features>Always-On Display, Health Tracking, watchOS 10</features>
        <description>Improved performance, new health features, and better integration with iPhone.</description>
    </smartwatch>
    <smartwatch>
        <name>Samsung Galaxy Watch 6</name>
        <marks>4.5/5</marks>
        <price>$299</price>
        <features>Wear OS, AMOLED Display, Fitness Tracking</features>
        <description>Powerful fitness features, sleek design, optimized for Samsung phones.</description>
    </smartwatch>
    <smartwatch>
        <name>Google Pixel Watch 2</name>
        <marks>4.4/5</marks>
        <price>$349</price>
        <features>Google Services Integration, Health Tracking</features>
        <description>Seamless integration with Google services, versatile health and fitness features.</description>
    </smartwatch>
    <smartwatch>
        <name>Garmin Forerunner 965</name>
        <marks>4.6/5</marks>
        <price>$599</price>
        <features>Advanced Training Features, Long Battery Life</features>
        <description>Tailored for athletes with precise tracking and extensive training features.</description>
    </smartwatch>
    <smartwatch>
        <name>Fitbit Sense 2</name>
        <marks>4.3/5</marks>
        <price>$299</price>
        <features>Stress Management, Sleep Tracking, Heart Rate Monitoring</features>
        <description>Comprehensive health and fitness tracking capabilities.</description>
    </smartwatch>
    <smartwatch>
        <name>TicWatch Pro 3 Ultra</name>
        <marks>4.2/5</marks>
        <price>$299</price>
        <features>Wear OS, Long Battery Life, Premium Design</features>
        <description>Combines premium design with extensive health and fitness features.</description>
    </smartwatch>
</smartwatches>"""

# Parse XML data
root = ET.fromstring(xml_data)

# Print table header with proper spacing
print(f"{'Name':<30} {'Marks':<10} {'Price':<10} {'Features':<50} {'Description'}")
print("=" * 150)

# Extract and print smartwatch details
for smartwatch in root.findall("smartwatch"):
    name = smartwatch.find("name").text
    marks = smartwatch.find("marks").text
    price = smartwatch.find("price").text
    features = smartwatch.find("features").text
    description = smartwatch.find("description").text
    
    print(f"{name:<30} {marks:<10} {price:<10} {features:<50} {description}")

