# Employee Management MCP

A FastMCP-based employee management system that provides tools for managing employee details and leave management.

## Features

- Get employee details by ID
- Update employee information
- Personalized greeting system
- Leave management integration

## Setup

1. Ensure you have Python installed on your system
2. Install the required dependencies:
   ```bash
   pip install mcp
   ```
3. Set up Cursor editor connection:
   - Create or update your `~/.cursor/mcp.json` file with the following configuration:
   ```json
   {
     "mcpServers": {
       "employee_mcp_new": {
         "command": "/path/to/your/venv/bin/python",
         "args": [
           "/path/to/your/project/employee_mcp/main.py"
         ],
         "description": "A simple MCP server to query employee details"
       }
     }
   }
   ```
   - Replace `/path/to/your/venv/bin/python` with your actual virtual environment Python path
   - Replace `/path/to/your/project/employee_mcp/main.py` with your actual project path
   - The server will be available in Cursor as "employee_mcp_new"

## Usage

### Getting Employee Details

To retrieve employee details, use the `get_employee_details` function with an employee ID:

```python
employee = get_employee_details(employee_id=0)
```

Example response:
```json
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
    "zip": "12345"
}
```

### Updating Employee Details

To update employee information, use the `update_employee_details` function:

```python
updated_employee = update_employee_details(
    employee_id=0,
    update_data={
        "name": "John Doe",
        "age": 31
    }
)
```

### Greeting System

Access personalized greetings using the greeting resource:

```
greeting://{name}
```

Example:
```
greeting://John
```
Returns: "Hello, John! How can I assist you with leave management today?"

## Available Employee Fields

The system maintains the following information for each employee:

- Name
- Age
- Department
- Salary
- Leave Balance
- Role
- Email
- Phone
- Address
- City
- State
- ZIP Code

## Running the MCP

To start the MCP server, run:

```bash
python main.py
```

## Example Usage

```python
# Get employee details
employee = get_employee_details(0)
print(employee["name"])  # Output: "John Doe"

# Update employee details
update_data = {
    "age": 31,
    "salary": 105000
}
updated_employee = update_employee_details(0, update_data)
print(updated_employee["salary"])  # Output: 105000
```

## Notes

- Employee IDs are zero-indexed
- All updates are performed in-memory
- The system includes a sample dataset of three employees
