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

<p>This Docker Compose configuration is designed to set up a development environment for your Django application. Make sure to adjust the configuration and environment variables as needed for your specific project requirements.</p>

</body>
</html>
