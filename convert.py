import xml.etree.ElementTree as ET
import os

print('function getPoints() { var points = [');

for i in os.listdir('./inputs'):
	if i.endswith(".tcx"): 
		tree = ET.parse('./inputs/' + i)
		doc = tree.getroot()

		positions = doc.findall('.//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Position')

		for position in positions:
			lat = position.find('./{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}LatitudeDegrees').text
			lng = position.find('./{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}LongitudeDegrees').text
			
			print('new google.maps.LatLng(', lat, ',', lng, '),')
		continue
		
print(']; return points;}')
