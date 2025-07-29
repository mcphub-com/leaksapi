```markdown
# Aigeon AI LeaksAPI

## Project Description

Aigeon AI LeaksAPI is a Python-based server application designed to interact with the LeaksAPI service. It provides a set of tools to perform various types of data breach searches, including email, domain, and phone number queries. The application leverages the FastMCP framework to create a robust and efficient microservice for handling requests and responses from the LeaksAPI.

## Features Overview

- **Email Breach Search**: Check if an email address has been involved in data breaches.
- **Domain Breach Search**: Perform a comprehensive search for breaches associated with a specific domain.
- **Phone Number Search**: Investigate if a phone number appears in any data leaks.
- **Premium Subscription Check**: Access premium subscription features for enhanced data breach insights.
- **Private Endpoint Access**: Utilize a private endpoint for specialized search queries.

## Main Features and Functionality

The application is structured to provide seamless interaction with the LeaksAPI service through several key functions. Each function serves a specific purpose in querying the API and processing the response data. The integration with FastMCP allows these functions to be registered as tools, making them easily accessible and executable.

## Main Functions Description

### `passwords_premium_subscription() -> dict`

- **Description**: Accesses premium subscription features to provide detailed insights into password leaks.
- **Returns**: A dictionary containing the response from the LeaksAPI.

### `search(check: Annotated[str, Field(description='')]) -> dict`

- **Description**: Performs a search query using a specified check parameter, which could be an email or other identifier.
- **Parameters**:
  - `check`: A string used to specify the search criteria.
- **Returns**: A dictionary containing the search results from the LeaksAPI.

### `domain_search(type: Annotated[str, Field(description='')] = None) -> dict`

- **Description**: Conducts a full domain search to identify breaches associated with a particular domain.
- **Parameters**:
  - `type`: An optional string parameter to specify the type of domain search.
- **Returns**: A dictionary with the domain search results.

### `phone_number_search() -> dict`

- **Description**: Searches for data breaches involving a specific phone number.
- **Returns**: A dictionary containing the phone number search results.

### `old_search() -> dict`

- **Description**: Accesses a private endpoint for conducting specialized search queries.
- **Returns**: A dictionary with the results from the private endpoint query.

## Technical Implementation

The server is built using the FastMCP framework, which facilitates the creation and management of microservices. Each function is decorated with `@mcp.tool()`, registering it as a tool within the FastMCP environment. The application communicates with the LeaksAPI using HTTP GET requests, handling responses and errors to ensure reliable data retrieval.

The server is designed to be executed with the `mcp.run(transport="stdio")` command, which initializes the service and listens for incoming requests via standard input/output streams.

This README provides a comprehensive overview of the Aigeon AI LeaksAPI server application, detailing its features, functionality, and technical implementation. For further information or support, please refer to the official documentation or contact the development team.
```