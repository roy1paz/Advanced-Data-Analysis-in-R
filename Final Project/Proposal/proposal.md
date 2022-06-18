---
title: "Project Proposal"
author: "Roy Paz, Tzahi Katz, Noam Munz"
output:
  html_document:
    df_print: paged
---

```{r load-packages, echo=FALSE, message = FALSE, warning=FALSE}
library(knitr)
library(tidyverse)
library(broom)
library(htmltools)
library(dplyr)
library(gridExtra)
library(tidyverse)
library(usmap)
library(ggplot2)
library(gtable)
library(echarts4r)
library(gapminder)
library(echarts4r.maps)
library(grid)
```

```{r setup, include = FALSE}
opts_chunk$set(echo=FALSE) # hide source code in the document
```

## 1. Introduction
In the last two decades the quality of air in our living spaces has declined following a rampant increase in production and manufacturing due to rising of global consumerism. In this project we will research whether the quality of air has an immediate effect on health outcomes among pregnant women and infants.\

This type of research will help determine if and how society can change its production and manufacturing methods in order to improve health among it's members.\

In the recent years both volume and affect of mass production and standards of tracking and storing data have increased which in turn provides an accessible information with critical importance to be explored.\

Approaching this research will be done by analyzing data provided by several US agencies and discovering and understanding relations between different data points leading to conclusions. All sets contain data collected in the United States from 2003 to 2020.

## 2. Data

We will use three data sets to research the topic.

**Air quality data:** \
a data set detailing the air quality in the United States in 2003-2020.\
Data are available by state and year. 
The set contains:\
- different types of chemical compounds and their prevalence in the air.\
- an Index that indicates the quality of air, denoted by AQI.\
- count of days in respect to varying levels of air quality.\
Further information about the data dimensions and source can be found in the README appendix.\

**Infant birth data:**\
a data set detailing birth and fertility information in the United States in 2007-2020.\
Data are available by state, year of birth and variety of statistical information regarding infant measurements.\
The data contains:\
- Number of births and fertility rates.\
- Division of cases by mothers age.\
- weight and other information regarding the distribution of weight by different categories.\
Further information about the data dimensions and source can be found in the README appendix.\

**Infant death data:**\
a data set detailing, births, health complications, deaths, and causes of deaths among babies under 1 year of age as well as their mothers in the United States in 2007-2019.\
The data contains:\
- Division of cases by mothers age\
- Chapter code which indicates the health complication / cause of death.\
- number of deaths in proportion to the number of births.\
Further information about the data dimensions and source can be found in the README appendix.\


## 3. Preliminary results
\
```{r, echo=FALSE, warning=FALSE, message=FALSE}
# loading data
AQI_data = read.csv(file = 'C:\\Users\\roy1p\\PycharmProjects\\BGU python\\Advanced Programming project\\Final Data\\air quality\\aqi_by_State_2003-2020.csv')
birth_data = read.csv(file = "C:\\Users\\roy1p\\PycharmProjects\\BGU python\\Advanced Programming project\\Final Data\\Infant Birth\\Infant_Birth_2007-2020.csv")
death_data = read.csv(file ="C:\\Users\\roy1p\\PycharmProjects\\BGU python\\Advanced Programming project\\Final Data\\Infant Death\\Infant_Death_2007-2019.csv")

# filter only 2007-2019 from the data
AQI_data = AQI_data %>% filter(Year <= 2019 & Year >= 2007)
birth_data = birth_data %>% filter(Year <= 2019 & Year >= 2007)
birth_data["State"][birth_data["State"] == "District of Columbia"] <- "District Of Columbia"

# normalizing air quality days count in proportion to number of days sampled
AQI_data$Good.Days = with(AQI_data,Good.Days/Days.with.AQI)
AQI_data$Moderate.Days = with(AQI_data,Moderate.Days/Days.with.AQI)
AQI_data$Unhealthy.for.Sensitive.Groups.Days = with(AQI_data,Unhealthy.for.Sensitive.Groups.Days/Days.with.AQI)
AQI_data$Unhealthy.Days = with(AQI_data,Unhealthy.Days/Days.with.AQI)
AQI_data$Very.Unhealthy.Days = with(AQI_data,Very.Unhealthy.Days/Days.with.AQI)
AQI_data$Hazardous.Days = with(AQI_data,Hazardous.Days/Days.with.AQI)
AQI_data$X90th.Percentile.AQI = with(AQI_data,X90th.Percentile.AQI/Days.with.AQI)
AQI_data$Median.AQI = with(AQI_data,Median.AQI/Days.with.AQI)
AQI_data$Days.CO = with(AQI_data,Days.CO/Days.with.AQI)
AQI_data$Days.NO2 = with(AQI_data,Days.NO2/Days.with.AQI)
AQI_data$Days.Ozone = with(AQI_data,Days.Ozone/Days.with.AQI)
AQI_data$Days.SO2 = with(AQI_data,Days.SO2/Days.with.AQI)
AQI_data$Days.PM2.5 = with(AQI_data,Days.PM2.5/Days.with.AQI)
AQI_data$Days.PM10 = with(AQI_data,Days.PM10/Days.with.AQI)

# fixing death rate column
for (i in 1:nrow(death_data)) {
  death_data[i,12] = (gsub("\\(Unreliable\\)", "", death_data[i,12]))
}
death_data <- transform(death_data, Death.Rate = as.numeric(Death.Rate))
```

#### Plot No. 1
```{r,  echo=FALSE, warning=FALSE, message=FALSE}
# figure No. 1
colnames(AQI_data)[which(names(AQI_data) == "State")] <- "state"
AQI_data2019 = AQI_data %>% filter(Year == 2019)
AQI_data2007 = AQI_data %>% filter(Year == 2007)

map2019 = plot_usmap(data = AQI_data2019, values = "Moderate.Days", color = "Black", labels = TRUE, )+
  labs(title = "2019", subtitle = "Precentage of Moderate Days") + 
  scale_fill_continuous(
    low = "white", high = "red", name = "Percentage", label = scales::percent) +
  theme(legend.position = "right")+ theme(plot.title = element_text(hjust = 0.5), plot.subtitle = element_text(hjust=0.5))
map2019$layers[[2]]$aes_params$size <- 1.3

map2007 = plot_usmap(data = AQI_data2007, values = "Moderate.Days", color = "Black", labels = TRUE, )+
  labs(title = "2007", subtitle = "Precentage of Moderate Days") + 
  scale_fill_continuous(
    low = "white", high = "red", name = "Percentage", label = scales::percent
  ) +
  theme(legend.position = "right") + theme(plot.title = element_text(hjust = 0.5), plot.subtitle = element_text(hjust=0.5))
map2007$layers[[2]]$aes_params$size <- 1.3

grid.arrange(map2007, map2019,nrow = 1, top=textGrob("Percentage of Days with Moderate AQI in USA\nGrouped by State", gp=
gpar(fontsize=12, font=3)), bottom = textGrob("*Moderate days are days in which the AQI is between 50-100\nSource: epa.gov - AQI Datasets", gp=gpar(fontsize=8, font=3)))
colnames(AQI_data)[which(names(AQI_data) == "state")] <- "State"
```
\

In the above plot you can see how different states are affected by air pollution in 2007 and how it shifted through the years to 2019. In some states it changed for the better and in some for the worse.\
Exploring health, mortality and morbidity outcomes in different states in those years can help us gain insight and determine if a correlation exists between the air quality and forementioned outcomes and analyze what factors are influencing the correlation the most.\
\
\

#### Plot No. 2

```{r, echo=FALSE, warning=FALSE, message=FALSE}
death_data_grouped_age = death_data %>% group_by(State, Year.of.Death, Age.of.Mother) %>% summarise_at(vars("Death.Rate"),mean)

death_data_2019 = death_data_grouped_age %>% filter(Year.of.Death == 2019)

ggplot(death_data_2019, aes(x= reorder(State, -Death.Rate,sum), y= Death.Rate))+
  geom_col(width = 0.8, aes(fill= Age.of.Mother))+
  labs(title="Infant Mortality Rate By in USA 2019", subtitle = "state and mother's age",x= "State", y = "Mortality Rate", caption= "Infant Mortality Rate: deaths per 1000 births\nSource: CDC WONDER - Linked Birth / Infant Death Records, 2007-2019",fill = "Age of Mother")+
  theme_bw()+
  theme(axis.text.x = element_text(angle = 90, vjust = 0.2, hjust=1, size= 7),
        axis.text.y = element_text(size= 8),
        axis.title.x = element_text(margin = unit(c(3, 0, 0, 0), "mm")),
        panel.border=element_rect(fill=NA))+ scale_fill_brewer(palette = "BrBG")
```


\
\

This graph details the death rate by country and age of mother (range). these results can be directly compared to the states AQI to test correlation. but further analyzing will be needed for any meaningful interpretation.\
Also, it is immediately visible that there is a correlation between infant's death rate and the mother's age when giving birth - the youngest and oldest age groups make a sizable proportion of the overall deaths. furthermore, in states with low death rates it seems that almost none of the deaths are from women belonging to groups 15-19 and 40-44.  

#### Plot No. 3
```{r, echo=FALSE, warning=FALSE, message=FALSE}
#''' group by the tables '''
grouped_birth_data = data.frame(birth_data["Year"],birth_data["State"], birth_data["Age.of.Mother.10"],birth_data["Average.Birth.Weight"],birth_data["Standard.Deviation.for.Average.Birth.Weight"])
grouped_birth_data = grouped_birth_data %>% group_by(Year,State) %>% summarise_at(vars('Average.Birth.Weight',"Standard.Deviation.for.Average.Birth.Weight"),mean)

#''' remove unmatch States '''
AQI_data = AQI_data %>% filter(State != "Country Of Mexico", State != "Puerto Rico", State != "Virgin Islands")

# ''' make one data frame for AQI table and Birth table'''
wei_gas_data = data.frame(AQI_data["Year"], AQI_data["State"], AQI_data["Days.PM2.5"], AQI_data["Days.SO2"], AQI_data["Days.CO"], AQI_data["Days.PM10"], AQI_data["Days.NO2"], AQI_data["Days.Ozone"], grouped_birth_data["Average.Birth.Weight"], grouped_birth_data["Standard.Deviation.for.Average.Birth.Weight"])


# plot from here
graph_SO2 = ggplot(wei_gas_data,aes(x = Days.SO2))+
  geom_smooth(aes(y = Average.Birth.Weight), color="#FFB74D")+
  theme_bw()+
  scale_x_continuous(labels = scales::percent)+
  labs(x="Precentage of days with So2 as main pollutant", y = "")+
  theme(axis.title = element_text(size = 9))


graph_PM2.5 = ggplot(wei_gas_data,aes(x = Days.PM2.5))+
  geom_smooth(aes(y = Average.Birth.Weight), color="#FFB74D")+
    theme_bw()+
  scale_x_continuous(labels = scales::percent)+
  labs(x="Precentage of days with PM2.5 as main pollutant", y = "")+
  theme(axis.title = element_text(size = 9))


graph_PM10 = ggplot(wei_gas_data,aes(x = Days.PM10))+
  geom_smooth(aes(y = Average.Birth.Weight), color="#FFB74D")+
    theme_bw()+
  scale_x_continuous(labels = scales::percent)+
  labs(x="Precentage of days with PM10 as main pollutant", y = "")+
  theme(axis.title = element_text(size = 9))


graph_OZONE = ggplot(wei_gas_data,aes(x = Days.Ozone))+
  geom_smooth(aes(y = Average.Birth.Weight), color="#FFB74D")+
    theme_bw()+
  scale_x_continuous(labels = scales::percent)+
  labs(x="Precentage of days with Ozone as main pollutant", y = "")+
  theme(axis.title = element_text(size = 9))


graph_NO2 = ggplot(wei_gas_data,aes(x = Days.NO2))+
  geom_smooth(aes(y = Average.Birth.Weight), color="#FFB74D")+
    theme_bw()+
  scale_x_continuous(labels = scales::percent)+
  labs(x="Precentage of days with NO2 as main pollutant", y = "")+
  theme(axis.title = element_text(size = 9))

graph_CO = ggplot(wei_gas_data,aes(x = Days.CO))+
  geom_smooth(aes(y = Average.Birth.Weight), color="#FFB74D")+
  theme_bw()+
  scale_x_continuous(labels = scales::percent)+
  labs(x="Precentage of days with CO as main pollutant", y = "")+
  theme(axis.title = element_text(size = 9))
  
grid.arrange(graph_PM2.5, graph_SO2, graph_CO,graph_OZONE,graph_PM10, graph_NO2, ncol=2, top="Effects of Different types of Gases on Birth Weight\nIn USA in 2007-2019", left="Average Birth Weight (grams)", bottom= "Shadow surrounding the line represent a 95% confidence interval")
```
\

This plot demonstrates a correlation between the prevalence of different types of gases to the birth weight of infants.\
Although all averages seem to be considered healthy weights for newborns, there seems to be a trend for some gases like So2 and PM2.5.\
Exploring Morbidity in infants and how it relates to weight could grant us vital information in regards to the affects of air quality on infant's health.\

## 4. Data analysis plan
To answer our research question we will use air quality data (explanatory, X) to explore correlating health outcomes in infants and pregnant women (response, Y). results in different states and different years will be used as comparison groups.

To answer our question we will use data visualization and data manipulation methods such as plotting, mutating, pivoting, building statistical models, and interpreting the results.

**Team Work**\
The work will be divided into 5 main tasks:\
- Researching the topic and collecting data.\
- Tidying the data to a workable state.\
- Manipulating the data to fit visualization needs.\
- Visualizing relations between Data points.\
- Reviewing the project\

Each task will be done by one or two members of the team and then corresponded to the rest.\
Reviewing will be done by the entire team.\

## Appendix

### Data README

```{r include_data_readme, comment='', warning=FALSE}
cat(readLines('../data/README.md'), sep = '\n')
cat(readLines('../data/sources.md'), sep = '\n')
```

### Source code

```{r, ref.label=knitr::all_labels(), echo=TRUE, eval=FALSE}

```
