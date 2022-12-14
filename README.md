# rest-order-items-service
### Group members: 

**Name** Josef Marc Pedersen **Github** [@josefmarcc ](https://github.com/josefmarcc) **Email** cph-jp325@cphbusiness.dk  
**Name** Frederik Dinsen **Github**[@fdinsen](https://github.com/fdinsen) **Email** cph-fd77@cphbusiness.dk  
**Name** Sebastian Bentley **Github** [@sebastianbentley ](https://github.com/SebastianBentley) **Email** cph-sb287@cphbusiness.dk  
**Name** Frederik Dahl **Github** [@dahlfrederik ](https://github.com/dahlfrederik) **Email** cph-fd76@cphbusiness.dk  

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/f2js/rest-order-items-service/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/f2js/rest-order-items-service/tree/main)


This servive provides information about items and orders, as well as the ability to change status of an order.

## REST API
### GET /items/<o_id>
Gets items in an order, provided an order ID as parameter.

### GET /orders/<rest_id>
Gets orders for a restaurant, given a restaurant ID/name

### PUT /status
Changes the status of an order, like 'Pending' to 'Accepted.

##### Body
- row_key (String): The ID of a row in the Hbase database 
- status (String): must be one of following: "Processing", "Pending", "Rejected", "Accepted", "ReadyForPickup", "OutForDelivery", "Delivered"


 #### Response
 - 200 OK
 - 404 Not Found
 - 500 Internal Server Error: An error occurred on the server side.

#### Response
- 200 OK: The orders were successfully found. The response body contains a list of the orders for t
