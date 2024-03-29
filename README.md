# LatLongPlotting
Plots the location of mobile network towers across any country based on data from http://opencellid.org/

A sample chart generated from this code is also posted [here](https://www.reddit.com/r/dataisbeautiful/comments/co4h59/oc_india_mobile_network_towers/)

<p align="center">
  <table>
    <tr>
      <td>Mexico Cell Tower Penetration</td>
      <td><img src="https://github.com/1kautilya1/LatLongPlotting/blob/master/mexico_mno_clusters.png"></td>
    </tr>
    <tr>
      <td>2G Towers</td>
      <td><img src="https://github.com/1kautilya1/LatLongPlotting/blob/master/mexico_mno_2g_towers.png"></td>
    </tr>
    <tr>
      <td>3G Towers</td>
      <td><img src="https://github.com/1kautilya1/LatLongPlotting/blob/master/mexico_mno_3g_towers.png"></td>
    </tr>  
    <tr>
      <td>4G Towers</td>
      <td><img src="https://github.com/1kautilya1/LatLongPlotting/blob/master/mexico_mno_4g_towers.png"></td>
    </tr>
  </table>
</p>

* mno_clusters.py

Dataset of mobile network towers was obtained from opencellid.org. This data set of latitude and longitude coordinates is then plotted on a scatter chart and subjected to Kmeans clustering. The clusters which are larger in size indicate lesser density of mobile network towers whereas smaller and concentrated clusters are more denser with mobile network towers.


* mexico_mno_generations.py

Here we filter the mobile network tower location data based on 2G/3G/4G network technology and plot each of them seperately to show the geograhic spread across Mexico. 


* mexico.csv

This is a sample dataset of mobile network towers in Mexico. The full dataset can be downloaded from https://opencellid.org. I have randomly verified couple of coordinates on google street view and could visually see the mobile network tower. However, I cannot guarantee the accuracy of the data available on opencellid.org.
