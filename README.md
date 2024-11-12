The attached ods file contains measurements of the source and target distances measured from images of network samples.
Measurements are collected for source strains of approximately, 25, 50 and 75% for various aging durations. The inactive measurements are before applied strain. Active measurements are once strain is applied. 

allostery_extract.py reads this data from the spreadsheet, makes adjustment to net distance changes for the source to adjust for measured strain differences because the actuator blocks the node, and computes the strains.
The data is output in a pickle file which contains strain data, pixel to cm conversions for the image, aging times, and the original source node distance in cm. 
Some notes in the file indicate the type of information gathered from a specific sample. 

The output pickle file is attached. 
