<!DOCTYPE html>
<html>
<body>

<h1>App Backend Server</h1>

<p>This document provides an overview of the Docker Compose configuration defined in the <code>docker-compose.yml</code> file.</p>

<h2>Services</h2>

<h3><code>app</code> Service</h3>

<p>The <code>app</code> service defines the configuration for your Django application.</p>

<ul>
    <li><code>build</code>: Builds the Docker image for the application using the <code>DEV=true</code> build argument to install development requirements.</li>
    <li><code>ports</code>: Maps port <code>8000</code> from the host to the container.</li>
    <li><code>volumes</code>: Mounts the <code>./app</code> directory from the host to the <code>/app</code> directory in the container.</li>
    <li><code>command</code>: Executes the migration and runs the Django development server.</li>
    <li><code>environment</code>: Sets environment variables for the application, including the OpenAI API key and URL, and enabling debugging.</li>
</ul>

<h2>Volumes</h2>

<p>The <code>dev-static-data</code> volume is defined to store development static data. You can mount this volume to the appropriate directory in the container for data storage.</p>

<h2>Usage</h2>

<p>To use this Docker Compose configuration:</p>

<ol>
    <li>Make sure you have Docker and Docker Compose installed on your system.</li>
    <li>Create a <code>docker-compose.yml</code> file in your project directory.</li>
    <li>Copy and paste the contents of the provided <code>docker-compose.yml</code> into your file.</li>
    <li>Run <code>docker-compose up</code> to build and start your application.</li>
    <li>Access your Django application at <code>http://localhost:8000</code> in your web browser.</li>
</ol>

<h2>Notes</h2>




# Greenhouse Monitoring System - Database Documentation

This Django project implements a Greenhouse Monitoring System with a PostgreSQL database. Below is an overview of the database schema and relationships.

## Database Architecture

| Model            | Description                                                     | Relationships                                          |
|------------------|-----------------------------------------------------------------|--------------------------------------------------------|
| **User**         | Represents a user in the system.                                |                                                        |
|                  | Inherits from Django's `AbstractBaseUser` and `PermissionsMixin`.|                                                        |
|                  | Fields: `email`, `first_name`, `last_name`, `is_active`, `is_staff`.|                                                    |
|                  | Associated with: `Greenhouse`, `SensorRecord`, `ActuatorStatus`, `Alert`.|                                             |
| **Greenhouse**   | Represents a greenhouse with fields like `name`, `location`, `size`.|                                                |
|                  | Fields: `name`, `location`, `size`.                             |                                                        |
|                  | Connected to: `User` via Foreign Key (Many-to-One).             |                                                        |
| **SensorRecord** | Stores sensor data records.                                     |                                                        |
|                  | Fields: `temperature`, `humidity`, `luminosity`, `CO2_level`, `soil_moisture`, `pH`, `nutrient_level`.|       |
|                  | Connected to: `User` and `Greenhouse` via Foreign Key (Many-to-One).|                                             |
| **ActuatorStatus**| Manages the status of actuators.                                 |                                                        |
|                  | Fields: `required_action`, `actuator_status`.                   |                                                        |
|                  | Connected to: `User` and `Greenhouse` via Foreign Key (Many-to-One).|                                             |
| **Alert**        | Stores alerts triggered by various conditions in a greenhouse.  |                                                        |
|                  | Fields: `alert_type`, `description`.                            |                                                        |
|                  | Connected to: `User` and `Greenhouse` via Foreign Key (Many-to-One).|                                             |

## Relationships

- **User to Greenhouse:**
  - A user can own multiple greenhouses.
  - Each greenhouse is associated with a single user.

- **Greenhouse to SensorRecord:**
  - A greenhouse can have multiple sensor records.
  - Each sensor record is linked to a specific greenhouse.

- **Greenhouse to ActuatorStatus:**
  - A greenhouse can have multiple actuator statuses.
  - Each actuator status entry is associated with a specific greenhouse.

- **Greenhouse to Alert:**
  - A greenhouse can have multiple alerts.
  - Each alert is linked to a specific greenhouse.

- **User to SensorRecord, ActuatorStatus, and Alert:**
  - Each sensor record, actuator status, and alert is associated with a specific user.

## Getting Started

To set up and run the project:

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run migrations to apply the database schema: `python manage.py migrate`.
4. Create a superuser account: `python manage.py createsuperuser`.
5. Start the development server: `python manage.py runserver`.

## Contribution

Feel free to contribute to the development of this Greenhouse Monitoring System by opening issues or sending pull requests.

## License

This project is licensed under [license name]. Refer to the LICENSE.md file for more details.

<p>This Docker Compose configuration is designed to set up a development environment for your Django application. Make sure to adjust the configuration and environment variables as needed for your specific project requirements.</p>

</body>
</html>
