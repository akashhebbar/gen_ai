# Generative AI Projects Collection

This repository contains a collection of simple generative AI projects. Each project demonstrates different aspects of AI and machine learning applications.

## Projects

### 1. Employee Management Project (employee_mcp)

A FastMCP-based employee management system that provides tools for managing employee details and leave management.

#### Features
- Get employee details by ID
- Update employee information
- Personalized greeting system
- Leave management integration
- Comprehensive employee data management including:
  - Personal details (name, age, contact info)
  - Professional details (department, role, salary)
  - Leave balance tracking
  - Address information

#### Setup
1. Ensure Python is installed on your system
2. Install the required dependencies:
   ```bash
   pip install fastmcp
   ```
3. Configure Cursor editor connection in `~/.cursor/mcp.json`
4. Run the MCP server:
   ```bash
   python main.py
   ```

## Project Structure

```
gen_ai/
├── employee_mcp/      # Employee Management Project
│   ├── main.py       # Main application file
│   ├── README.md     # Project-specific documentation
│   └── ...           # Other project files
└── README.md         # This file
```

## Getting Started

Each project in this repository is self-contained and can be run independently. Follow the specific instructions in each project's directory for setup and execution.

## Contributing

Feel free to contribute to this repository by adding new projects or improving existing ones. Each project should be self-contained and well-documented.

## License

This project is open source and available under the MIT License.
