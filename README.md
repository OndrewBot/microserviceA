# Guide for Unit Conversion API
-------------------------------
>Revision: 1.0.0
>Date: August 4, 2024
>Author: Andrew Bottom

This microservice will allow a user to convert from units of cups, tablespoons, or teaspoons into another of those same units.
The request must contain:
*Units
*Amount
*Target units
The response will provide a JSON with the following fields:
*Units (these are the target units)
*Amount (the converted amount in the target units)

## Sources
1. FastAPI module - https://fastapi.tiangolo.com
2. Render host- https://render.com,
3. Starter code - https://github.com/render-examples/fastapi
