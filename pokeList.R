library(dplyr) # piping and such
library(tidyr) # replace_na
library(ggplot2) 
library(GLDEX) # which.na

data <- read.csv("Pokemon.csv", na="None")
data <- data[,-1]
data[data==""] <- "None" # Filling in the blanks

# Generation is numeric, change here to be character to plot
data$Generation = as.character(data$Generation)

mean(data[data$Generation == 1 & data$Evolution == "Final", ]$Attack)

ggplot(data, aes(x = Generation, 
                 y = Total, 
                 fill = Generation)) + 
  geom_boxplot(outlier.color="red", 
               outlier.shape=21, 
               outlier.fill="red",
               outlier.size=4) 

