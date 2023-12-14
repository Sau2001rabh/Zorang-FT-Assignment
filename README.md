# Zorang-FT-Assignment

<h3>Problem Statement</h3>
Design and create algorithm for finding the optimal routes for delivery agents to deliver
parcels from a store to consumers. <br><br>
<b>Requirements and constraints:</b><br>
● There are 100 orders which are to be delivered by 10 delivery agents<br>
● There is one store location from where all orders will be delivered and after finishing the deliveries, the agents will come back to the store<br>
● You are given 100 random addresses where parcels are to be delivered<br>
● Map an optimal route for each delivery person for doing the deliveries and in what order they will do the deliveries<br>
● It is not required that all delivery agents will deliver the same number of orders<br>
● Each delivery agent can pick multiple orders in one trip. Each agent will deliver at least one order. <br><br>
<b>Assumptions: </b> <br>
● All 100 orders are ready at the same time <br>
● All delivery agents go at the same speed <br>
● Consider straight line distance between any two coordinates<br><br>
<b>Problem: </b> <br>
Design optimal routes for all 10 delivery agents so that all packages are delivered and delivery agents return to the store in shortest amount of time.<br><br>
<b>Input: </b><br>
Store location: Latitude - 28.9428, Longitude - 77.2276 <br>
Addresses to deliver: https://zorang-recrutment.s3.ap-south-1.amazonaws.com/addresses.json <br> <br>

<b> Output :</b><br>
Return array of location id each agent will deliver. <br>
Consider agents at index 0-9. <br>
Each subarray will contain addresses id that agent will deliver and in order they deliver. <br>
[[1,2,3,9...] , [33, 45, 56], ....., [99], [100, 23]]
<br>
<br>
<h3>Approach</h3>
<ul type="circle">
<li> Got the data from the given URL and stored it in the variable "response". Stored the coordinates of the store in x_store(Latitude) and y_store(Longitude).</li>
  <li> Separately stored the Latitudes, Longitudes & address ids of delivery locations in the array 'order'.</li>
  <li>Objective: Find the minimum distance that a delivery agent has to cover to deliver parcels from the store to customers and return to the store in the minimum time. </li>
  <li>Utilized binary search to determine the least maximum distance covered by delivery agents.</li>
  <li>Used 'mid' to store the minimum of the maximum distance covered by the delivery agent. Set variables 'start' to the least possible distance and 'end' to the maximum possible distance that delivery agents can cover.</li>
  <li> If the condition is true, store the order in 'currorder', and finally, it gets stored in 'deliveries'. Otherwise, repeat this process for different values of 'mid'.</li>
  <li>Print 'deliveries' once the loop ends.</li>
</ul>
