import requests
from datetime import datetime
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")
from pydantic import BaseModel, Field
from typing import Union
from typing import Annotated


mcp = FastMCP('leaksapi')

headers = {'host': 'leaksapi.p.rapidapi.com', 'x-forwarded-port': "443", 'x-forwarded-proto': 'https', 'user-agent': 'axios/1.9.0', 'accept-encoding': 'identity', 'x-rapidapi-host': 'leaksapi.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}

@mcp.tool()
def passwords_premium_subscription(email: Annotated[str, Field(description='')]) -> dict:
    '''costs 1 token'''
    url = 'https://leaksapi.p.rapidapi.com/api/v2/query/%s'%email
    payload = {
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def search(check: Annotated[str, Field(description='')]) -> dict: 
    '''search endpoint'''
    url = 'https://leaksapi.p.rapidapi.com/api/public'
    payload = {
        'check': check,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def domain_search(type: Annotated[str, Field(description='')], domain: Annotated[str, Field(description='')]) -> dict:
    '''full domain search rather than individual emails'''
    url = 'https://leaksapi.p.rapidapi.com/api/v2/query/%s'%domain
    payload = {
        'type': type,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def phone_number_search(phone: Annotated[str, Field(description='')]) -> dict:
    '''searches phone numbers'''
    url = 'https://leaksapi.p.rapidapi.com/api/v2/query/%s'%phone
    payload = {
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def old_search(email: Annotated[str, Field(description='')]) -> dict:
    '''private endpoint'''
    url = 'https://leaksapi.p.rapidapi.com/api/v2/private/query/%s'%email
    payload = {
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")