# Metro-Reservation-System[README.md](https://github.com/user-attachments/files/32868136/README.md)
# MET-RO: Metro Train Reservation System

MET-RO is a comprehensive terminal-based Metro Train Reservation System designed as part of the project evaluation. It meets and exceeds all outlined functional and technical expectations.

## 2.1 Functional Requirements

### Three Major Functional Modules
1. **User Management Module (`modules/user_management.py`)**: Handles user registration and authentication, keeping credentials securely managed in JSON format.
2. **Train Management Module (`modules/train_management.py`)**: Manages the available metro trains, routes, available seats, and fare information. 
3. **Booking & Ticketing Module (`modules/booking.py`)**: Allows users to book tickets, automatically calculates total fares, updates seat availability, issues unique Ticket IDs, and supports full ticket cancellation and seat refunds.

### Clear Input/Output Structure
- **Inputs**: User prompts for navigation choices (integers), text inputs for usernames/passwords, and specific inputs like Train IDs and number of tickets. 
- **Outputs**: Colored terminal outputs, formatted tables for displaying schedules and booking history, and clear success/error prompts.

### Logical Workflow
1. The user launches the application and is presented with a login/register screen.
2. After successful authentication, the user accesses the Dashboard.
3. The user can view available trains in a tabular format.
4. The user books a ticket by specifying the Train ID and number of seats.
5. The system confirms the booking, updating the JSON data files.
6. The user can review their past bookings or cancel them, which automatically refunds the seats to the system.

## 2.2 Non-Functional Requirements

1. **Usability**: The application provides an intuitive, smart terminal UI featuring ANSI color codes, clear screen transitions, and formatted tables, making it aesthetically pleasing and easy to navigate.
2. **Error Handling Strategy**: Comprehensive error handling is implemented. The system gracefully catches `ValueError` exceptions during input, validates bounds (e.g., ensuring ticket count > 0), and ensures invalid Train IDs or out-of-stock scenarios are met with friendly error messages instead of crashes.
3. **Maintainability**: The codebase is highly modular. Core logic is separated from UI components and data management. Adding new features (like an Admin dashboard) requires minimal changes to existing code.
4. **Data Persistence (Reliability)**: Instead of using volatile memory, the system uses JSON file storage (`data/`) to persistently store users, trains, and bookings, ensuring reliability between application sessions.

## 3. Technical Expectations

- **Modular and Clean Implementation**: The project is split into 6 meaningful Python files across dedicated directories (`modules/` and `utils/`), ensuring Separation of Concerns (SoC).
  - `main.py`
  - `modules/user_management.py`
  - `modules/train_management.py`
  - `modules/booking.py`
  - `utils/validation.py`
  - `utils/ui.py`
- **Appropriate Documentation**: Code includes necessary structures, and this README comprehensively documents the architecture.
- **Validation and Error Handling**: The `validation.py` module centralizes data validation, preventing invalid inputs from corrupting the program flow.

## How to Run
Ensure you have Python installed. Navigate to the project directory and run:
```bash
python main.py
```
