#TeachAPI

## Overview
This project is to build a REST API from scratch to better understand the innerworking of how API's are made and configured.

### Requirements
- Python 3
- Flask

## How it works

The API is built with **Flask** and servers data from a local json.

## Endpoints

This API only servers GET requests.

**`GET /`**
Returns a welcome message confirming the API is running.

**`GET /all`**
Returns all districts with their full data

**`GET /districts?name=Northside ISD`**
Returns a single district by name. Pass the district name as a query parameter.
If the district is not found, it returns an error message.
