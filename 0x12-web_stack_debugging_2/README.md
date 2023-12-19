# 0x12. Web Stack Debugging #2

## Introduction

This guide outlines the concept of configuring a container to meet specific requirements related to Nginx setup. The objective is to ensure that Nginx is running as the "nginx" user, listening on all active IPs on port 8080. Additionally, the solution must not involve using `apt-get remove`.

## Configuration Concept

### 1. User Configuration for Nginx

To configure Nginx to run as the "nginx" user:

- The configuration file for Nginx (`nginx.conf`) needs to be modified to set the user as "nginx." This is typically achieved using a tool like `sed` to replace the existing user (e.g., "www-data") with "nginx."

### 2. Port Configuration for Nginx

To configure Nginx to listen on all active IPs on port 8080:

- The Nginx site configuration file (e.g., `sites-available/default`) should be modified to change the listening port from the default (e.g., port 80) to the desired port (8080).

### 3. Restarting Nginx

After making these changes, Nginx needs to be restarted to apply the new configurations. This can be accomplished using the `service` command or an equivalent service management tool.

## Important Notes

- Don't forget to backup your default settings
