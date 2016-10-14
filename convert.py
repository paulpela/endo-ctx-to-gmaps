import xml.etree.ElementTree as ET
import os
import os.path
import sys

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        print("Error: file " + sys.argv[1] + " already exists. Aborting.", file=sys.stderr)
        sys.exit(1)

    output_file = open(sys.argv[1], "w")
else:
    output_file = sys.stdout

print('function getPoints() { var points = [', file=output_file);

for i in os.listdir('./inputs'):
	if i.endswith(".tcx"): 
		tree = ET.parse('./inputs/' + i)
		doc = tree.getroot()

		positions = doc.findall('.//{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Position')

		for position in positions:
			lat = position.find('./{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}LatitudeDegrees').text
			lng = position.find('./{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}LongitudeDegrees').text
			
			print('new google.maps.LatLng(', lat, ',', lng, '),', file=output_file)
		continue
		
print(']; return points;}', file=output_file)
