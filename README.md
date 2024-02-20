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

These levels were determined by a Relative in the Medical Domain. 


## HTML Files Content:
### interactive_map_AED_and_interventions.html
Interactive map showing the position of the AEDs in blue and the position of the interventions in red. You can select the intervention you see by level of AED need (3=AED absolutely necessary, 0=AED not required)

### interactive_map_closest_AED_distance.hmtl
Interactive map showing the interventions of AED need level 2 and higher, with a waiting time that was more than 5 minutes. The points are colored on a scale proportionate to the distance to the closest AED on the map by Manhattan distance (log scale for visibility).

### interactive_map_closest_AED_large_distances.html
Interactive map showing the interventions of AED need level 2 and higher, with a waiting time that was more than 5 minutes, and where the distance to the closest AED (in Manhattan distance) was more than 1km. The points are also colored proportionately to the distance to the closest AED.

