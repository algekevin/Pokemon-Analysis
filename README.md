# Pokemon-Analysis
Analysis on Pokemon stuff

Reading of a file into a dataframe, filtering some aspects of this dataframe for other things(final evolutions, for example). 

Dataframes can then be used for slicing however you'd like, just have to do modifications or pretty simplistic queries. 
Some examples of what can be done are in the code already, and different dataframes are made for each type of Pokemon.

The main goal here was to get the final evolutions into their own data frame, track each generation of final stage stats, and
display them with a graph to easily identify things and see if the averages have increased over time. 

The reason only final stages are included is simple. Some generations may have more stage one and two evolutions which will
generally have lower stats than the final stage, resulting in a slightly skewed average. Also, the final stages are usually
what people care to look into the most. 

An IV Calculator without a GUI is also included here, but is commented out because it's not the main purpose of the code.
