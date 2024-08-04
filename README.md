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
The microservice is hosted by **Render** at this address and enpoint https://microservicea.onrender.com/convert
Note: A common issue with free-tier servers is a timeout. If there's an issue with access, wait 50 sec before attemping to access again.   

## Request    
This microservice accepts HTTP GET requests in order to issue a valid response.   
Example: https://microservicea.onrender.com/convert?units=cups&amount=4&target=tsp     
Formatting: `.../convert?units={units}&amount={amount}&target={targetunits}`   
Units: `'cups', 'tbs', 'tsp'`
Code example:   
```
import requests
response = requests.get('https://microservicea.onrender.com/convert', 
                    params={"units": "cups", "amount": 4, "target": "tsp"}) 
```

## Response   
This microservice will send a response with a valid HTTP GET request. The Status Code needs to be verified as 200 in order to prevent errors
Example: https://microservicea.onrender.com/convert?units=cups&amount=4&target=tsp     
Formatting: `{"units":"tsp", "amount":192.0}`   
Code example:   
```
import requests
response = requests.get('https://microservicea.onrender.com/convert', 
                    params={"units": "cups", "amount": 4, "target": "tsp"})
if response.status_code == 200:
    json_response = response.json()
    print("New unit: ", json_response["units"])
    print("New amount: ", json_response["amount"])
```

## Sequence Diagram   
sequenceDiagram   
   participant User
   participant UnitConversion
   Note left of User: Unit must be formatted:<br/>'cups', 'tsp', 'tbs'
   User->>UnitConversion: HTTP GET request<br/> {"units": "cups", "amount":4, "target":"tsp"}
   UnitConversion->>UnitConversion: Convert amount to the target units
   Note right of UnitConversion: incorrect units trigger a<br/> response with unit spellings
   UnitConversion->>User: JSON response<br/> {"units": "tbs", "amount":192.0}
    
## Citations
1. FastAPI module - https://fastapi.tiangolo.com
2. Requests module - https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
3. Render host- https://render.com,
4. Starter code - https://github.com/render-examples/fastapi
