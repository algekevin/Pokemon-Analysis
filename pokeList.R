library(dplyr) # piping and such
library(tidyr) # replace_na
library(ggplot2) 
library(GLDEX) # which.na
library(reshape) # melt

# Reading in Data ----
data <- read.csv("Pokemon.csv", na="None")
data <- data[,-1]
data[data==""] <- "None" # Filling in the blanks

# Generation is numeric, change here to be character to plot
data$Generation = as.character(data$Generation)
data$Legendary = as.logical(data$Legendary)

mean(data[data$Generation == 1 & data$Evolution == "Final", ]$Attack)
View(df_final)

# + Final Evolution DF ----
df_final <- data[data$Evolution == "Final",]

# + Final Evo No Legendary DF ----
df_final_no_leg <- df_final[df_final$Legendary == FALSE,]

# + Mega Evolution DF ----
df_mega <- data[data$Evolution == "Mega",]

# + Water DF ----
df_water <- df_final[df_final$Type.1 == "Water" | 
                     df_final$Type.2 == "Water",]

# + Fire DF
df_fire <- df_final[df_final$Type.1 == "Fire" |
                    df_final$Type.2 == "Fire",]

# . . . . . . . ----

# All pokemon ----
# + Total Stats ----
# ++ Boxplot ----

ggplot(data, aes(x = Generation, 
                 y = Total,
                 fill = Generation)) +
  stat_boxplot(geom="errorbar") +
  geom_boxplot(outlier.color=NULL, 
               outlier.shape=21,
               outlier.size=3)


# Final evolution ----
# + All ----
# ++ Total Stats ----
# +++ Violin + Box ----

ggplot(df_final, aes(x = Generation, 
                     y = Total, 
                     fill = Generation)) + 
  geom_violin(alpha=0.01) + 
  stat_boxplot(geom="errorbar") +
  geom_boxplot(outlier.shape=21,
               outlier.size=3,
               width=0.15) #+ 
#  geom_point(size=1,
#             position=position_jitter(0.2),
#             alpha=0.4)


# +++ Boxplot ----
ggplot(df_final, aes(x = Generation, 
                     y = Total, 
                     fill = Generation)) + 
  stat_boxplot(geom="errorbar") +
  geom_boxplot(outlier.shape=21,
               outlier.size=3) 

# + Fire vs Water ----
# ++ Boxplot ----

tmp_water <- df_water
for(i in 1:nrow(df_water)){
  if(df_water[i, "Type.1"] != "Water"){
    tmp_water[i, "Type.1"] = "Water"
  }
}

tmp_fire <- df_fire
for(i in 1:nrow(df_fire)){
  if(df_fire[i, "Type.1"] != "Fire"){
    tmp_fire[i, "Type.1"] = "Fire"
  }
}

ggplot(rbind(tmp_water, tmp_fire), aes(x = Generation, 
                 y = Total,
                 fill = Type.1)) + 
  stat_boxplot(geom="errorbar") +
  geom_boxplot(outlier.shape=21,
               outlier.size=2) + 
  labs(title="Water vs. Fire Total Stats by Generation",
       fill="Type")
  

# Mega Evolution ----
# + All ----
# ++ Total Stats ----
# +++ Boxplot ----
ggplot(df_final, aes(x = Generation, 
                     y = Total, 
                     fill = Generation)) + 
  stat_boxplot(geom="errorbar") +
  geom_boxplot(outlier.shape=21,
               outlier.size=3) 

# Final Evo No Legendary ----
# + All ----
# ++ Total Stats ----
# +++ Violin + Box ----
ggplot(df_final_no_leg, aes(x = Generation, 
                            y = Total, 
                            fill = Generation)) + 
  geom_violin(alpha=0.01) + 
  stat_boxplot(geom="errorbar") +
  geom_boxplot(outlier.shape=21,
               outlier.size=3,
               width=0.15)

