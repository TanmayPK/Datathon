# Datathon

## AED need levels explaination

In the interactive maps, the interventions were classifier by their AED need levels : 

0 - AED not required.
Ex : Non medical complaints, e.g small fires, animal rescue

1 - AED not likely needed.
Ex (among many) : Eye problems, non-traumatic bleeding

2 - AED might be necessary. 
Ex : Unconscious, chest pain, Respiratory problems

3 - AED absolutely necessary. 
Ex : Cardiac arrest

These levels were determined by a Relative in the Medical Domain, where he looked at every possible types of events present in the interventions dataset and determined if an AED was likely to be of use before the ambulance arrives at the scene. An intermediary need level was assigned to event types that were deemed to have a possibility to evolve into something requiring an AED. The AED need level assigned to each event type is available in data/cause_aed_need.txt


## HTML Files Content:
### interactive_map_AED_and_interventions.html
Interactive map showing the position of the AEDs in blue and the position of the interventions in red. You can select the intervention you see by level of AED need (3=AED absolutely necessary, 0=AED not required)

### interactive_map_closest_AED_distance.hmtl
Interactive map showing the interventions of AED need level 2 and higher, with a waiting time that was more than 5 minutes. The points are colored on a scale proportional to the distance to the closest AED on the map by Manhattan distance (log scale for visibility).

### interactive_map_closest_AED_large_distances.html
Interactive map showing the interventions of AED need level 2 and higher, with a waiting time that was more than 5 minutes, and where the distance to the closest AED (in Manhattan distance) was more than 1km. The points are also colored proportionately to the distance to the closest AED.

## Image Files Content:

### mean_aed_distance_city_center_300m.png
Bar plot showing the mean Manhattan distance (in km) to the closest AED for interventions with an AED need level of 2 or more, in a circle of radius 300m with its center in the center of different cities. We intended this plot as a measure of how the quality of AEDs placement was in a given city center. Note that not many Flemish cities were included, because we lacked the intervention data to do so.
