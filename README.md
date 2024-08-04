# Guide for Unit Conversion API  

>Revision: 1.0.0   
>Date: August 4, 2024   
>Author: Andrew Bottom   

This microservice will allow a user to convert from units of cups, tablespoons, or teaspoons into another of those same units.    
The request must contain:  
* Units (string type)   
* Amount (float type)  
* Target units (float or integer type)   
   
The response will provide a JSON with the following fields:    
* Units (these are the target units as a string)   
* Amount (the converted amount in the target units as a float)
    
Errors:    
* If the formatting is not valid then the response will be "details not found"
* If the units are not valid then the response will be "invalid units - must be 'cups', 'tbs', 'tsp'"   
    
## Server Location   
The microservice is hosted by **Render** at this address and enpoint (https://microservicea.onrender.com/convert)[https://microservicea.onrender.com/convert]  
A common issue with free-tier servers is a timeout. If there's an issue with access, wait 50 sec before attemping to access again.   

## Requests
This microservice accepts HTTP GET requests in order to issue a valid response.   

   
## Citations
1. FastAPI module - https://fastapi.tiangolo.com
2. Render host- https://render.com,
3. Starter code - https://github.com/render-examples/fastapi
