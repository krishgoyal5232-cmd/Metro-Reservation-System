# MET-RO Project Report Sections

Based on the parameters provided in the image, here is the content for the Problem Statement and Requirements sections for the MET-RO system. You can include this directly in your final project report.

## 3. Problem Statement
The current process of booking metro train tickets often involves long queues at station counters or using disjointed, inefficient platforms. This leads to wasted time and a poor experience for daily commuters. There is a need for a centralized, efficient, and digital reservation system that allows passengers to easily manage their travel. The MET-RO system addresses this issue by providing a streamlined, user-friendly platform where commuters can seamlessly register, view train availability, book tickets, and manage cancellations from a single interface, thereby saving time and reducing friction in urban transit.

## 4. Functional Requirements
- **User Registration & Login**: The system must allow new users to register an account by choosing a unique username and a password (minimum 4 characters). Registered users must be able to log in securely.
- **View Available Trains**: The system must display a comprehensive list of available metro trains, including their Train IDs, routes, and timings.
- **Ticket Booking**: Logged-in users must be able to select a specific train using its Train ID and book a specified number of tickets (between 1 and 10).
- **View Bookings**: The system must allow users to view a detailed list of all their active ticket bookings.
- **Ticket Cancellation**: Users must be able to cancel an existing booking by providing the unique Ticket ID.
- **Data Persistence**: The system must reliably store user accounts, train schedules, and booking data locally (in a `data` directory) so that information is retained across different sessions.

## 5. Non-functional Requirements
- **Usability**: The system must provide an intuitive Command Line Interface (CLI) featuring clear menus, headers, and validation prompts to ensure a smooth user experience.
- **Reliability and Robustness**: The system must handle invalid user inputs (such as out-of-range menu options, invalid Train IDs, or incorrect passwords) gracefully by displaying appropriate error messages rather than crashing.
- **Performance**: The system must execute user commands, such as retrieving train schedules or processing bookings, with minimal latency.
- **Security**: The system must enforce basic access control, ensuring users must be logged in to book or view tickets, and they can only access their own booking history.
- **Maintainability**: The application architecture must be modular, separating concerns into distinct subsystems (`user_management`, `train_management`, `booking`, and `utils`), making the codebase easier to update, test, and maintain in the future.
