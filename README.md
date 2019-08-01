# LatLongPlotting
Plots the location of mobile network towers across Mexico based on data from http://opencellid.org/


extensio_mno_clusters.py

Dataset of mobile network towers was obtained from opencellid.org. This data set of latitude and longitude coordinates is then plotted on a scatter chart and subjected to Kmeans clustering. The clusters which are larger in size indicate lesser density of mobile network towers whereas smaller and concentrated clusters are more denser with mobile network towers.


mexico_mno_generations.py

Here we filter the mobile network tower location data based on 2G/3G/4G network technology and plot each of them seperately to show the geograhic spread across Mexico. 
