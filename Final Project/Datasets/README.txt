# SISE2601 Project data description
================
Team Members: Roy Paz, Tzahi Katz, Noam Munz
#################################################################################################################

### Air Quality Data: [976 x 18]

Year: The year of the sampled data
_________________________________________________________________________________________________________________
State:: The state in which the data was collected.
_________________________________________________________________________________________________________________
Days with AQI: Number of days in the year having an Air Quality Index value. This is the number of days on which measurements from any monitoring site in the state were reported to the database.
_________________________________________________________________________________________________________________
Good Days: Number of days in the year having an AQI value 0 through 50.

_________________________________________________________________________________________________________________
Moderate Days: Number of days in the year having and AQI value 51 through 100.
_________________________________________________________________________________________________________________
Unhealthy for Sensitive Groups Days: Number of days in the year having an AQI value 101 through 150.
_________________________________________________________________________________________________________________
Unhealthy Days: Number of days in the year having an AQI value 151 through 200.
_________________________________________________________________________________________________________________
Very Unhealthy Days: Number of days in the year having an AQI value 201 through 300.
_________________________________________________________________________________________________________________
Hazardous Days: Number of days in the year having an AQI value 301 or higher.  Note: The official AQI hazardous category range is 301-500.  Values above 500 are considered “Beyond the AQI” and are included in the # Days Hazardous in this report.
_________________________________________________________________________________________________________________
Max AQI: The highest daily AQI value in the year.
_________________________________________________________________________________________________________________
90th Percentile AQI: 90 percent of daily AQI values during the year were less than or equal to the 90th percentile value.
_________________________________________________________________________________________________________________
Median AQI: Half of daily AQI values during the year were less than or equal to the median value, and half equaled or exceeded it
_________________________________________________________________________________________________________________
Days CO: Days in which CO was the main pollutant. range from 0 to 500.
_________________________________________________________________________________________________________________
Days NO2: Days in which NO2 was the main pollutant. ranges from 0 to 500.
_________________________________________________________________________________________________________________
Days Ozone: Days in which Ozone was the main pollutant. ranges from 0 to 500.
_________________________________________________________________________________________________________________
Days SO2: Days in which SO2 was the main pollutant. ranges from 0 to 500.
_________________________________________________________________________________________________________________
Days PM2.5: Days in which PM2.5 was the main pollutant. ranges from 0 to 500.
_________________________________________________________________________________________________________________

Days.PM10: Days in which PM10 was the main pollutant. ranges from 0 to 500.
_________________________________________________________________________________________________________________

#################################################################################################################

### Infant Birth Data: [6488 x 16]
ID: Row ID - represents row number.
_________________________________________________________________________________________________________________
Year: The year in which the data was collected in.
_________________________________________________________________________________________________________________
State: The state in which the data was collected.
_________________________________________________________________________________________________________________
Age of Mother: division of the data by mother's age in years (grouped).
_________________________________________________________________________________________________________________
Births: Number of total births.
_________________________________________________________________________________________________________________
Female Population: total female population.
_________________________________________________________________________________________________________________
Fertility Rate: Number of expected births per 1000 women. (births divided by female population multiplied by 1000).
_________________________________________________________________________________________________________________
Average Birth Weight: The average weight of an infant in grams.
_________________________________________________________________________________________________________________
Standard Deviation for Average Birth Weight: Standard deviation of infant's average weight.
_________________________________________________________________________________________________________________
Average LMP gestational Age: Age of infant from last menstrual period, also known as gestational age in weeks.
_________________________________________________________________________________________________________________
Standard Deviation for Average LMP Gestational Age: Standard deviation for Average LMP gestational age.
_________________________________________________________________________________________________________________
Average OE Gestational Age: Average gestational Age by obstetrician's estimate in weeks.
_________________________________________________________________________________________________________________
Standard Deviation for Average Gestational Age: Standard deviation for average gestational age by obstetrician's estimate.
_________________________________________________________________________________________________________________

#################################################################################################################

### Infant Death Rate: [6818 x 12]
_________________________________________________________________________________________________________________
ID: Row ID - represents row number.
_________________________________________________________________________________________________________________
State: The state in which the data was collected.
_________________________________________________________________________________________________________________
Year of Death: The state in which the data was collected.
_________________________________________________________________________________________________________________
Age of Mother: division of the data by mother's age in years (grouped).
_________________________________________________________________________________________________________________
ICD Chapter: a code that represents the health complication / cause of death. a map to all ICD-10 codes can be found [here](https://www.icd10data.com/ICD10CM/Codes).
_________________________________________________________________________________________________________________
Deaths: Number of total deaths.
_________________________________________________________________________________________________________________
Births: Number of total births.
_________________________________________________________________________________________________________________
Death Rate: Number of expected deaths per 1000 births. (deaths divided by births multiplied by 1000).
_________________________________________________________________________________________________________________

#################################################################################################################

### Income by State: [6818 x 12]
_________________________________________________________________________________________________________________
State: The state in which the data was collected.
_________________________________________________________________________________________________________________
Year of Death: The state in which the data was collected.
_________________________________________________________________________________________________________________
Average: The average income per person