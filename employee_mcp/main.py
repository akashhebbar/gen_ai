from mcp.server.fastmcp import FastMCP
from typing import List



employees_details =[
    {
        "name": "John Doe",
        "age": 30,
        "department": "Engineering",
        "salary": 100000,
        "leave_balance": 10,
        "role": "Software Engineer",
        "email": "john.doe@example.com",
        "phone": "+1234567890",
        "address": "123 Main St, Anytown, USA",
        "city": "Anytown",
        "state": "CA",
        "zip": "12345",
    },
    {
        "name": "Jane Smith",
        "age": 25,
        "department": "Marketing",
        "salary": 50000,
        "leave_balance": 5,
        "role": "Marketing Manager",
        "email": "jane.smith@example.com",
        "phone": "+1234567890",
        "address": "456 Market St, Anytown, USA",
        
    },
    {
        "name": "Jim Beam",
        "age": 40,
        "department": "Sales",
        "salary": 70000,
        "leave_balance": 7,
        "role": "Sales Manager",
        "email": "jim.beam@example.com",
        "phone": "+1234567890",
        "address": "789 Sales St, Anytown, USA",
    },
]



mcp =FastMCP('Employee MCP')

@mcp.tool()
def get_employee_details(employee_id: int) -> dict:
    '''
    Get employee details by ID
    Input: employee_id (int)
    Output: employee details (dict)
    Example:
    Input: 0
    Output: {
        "name": "John Doe",
        "age": 30,
        "department": "Engineering",
    }
    '''
    return employees_details[employee_id]


@mcp.tool()
def update_employee_details(employee_id: int, update_data: dict) -> dict:
    '''
    Update employee details by ID
    Input: employee_id (int), update_data (dict)
    Output: updated employee details (dict)
    Example:
    Input: 0, {"name": "John Doe", "age": 30}
    Output: {
        "name": "John Doe",
        "age": 30,
    }
    '''
    employees_details[employee_id].update(update_data)
    return employees_details[employee_id]



@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! How can I assist you with leave management today?"
if __name__ == '__main__':
    mcp.run()
