# Airbnb Clone v2 - Deployment Setup

This README provides an overview of the steps I followed to successfully solve Task 2, which involved deploying the Airbnb Clone v2 project on my server. Below are the detailed steps:

## Step 1: Clone Airbnb Clone v2 Repository

```bash
git clone https://github.com/just337ine/AirBnB_clone_v2.git
```

I cloned the Airbnb Clone v2 repository onto my server to begin the deployment process.

## Step 2: Install Flask and Gunicorn

```bash
pip install flask gunicorn
```

I installed Flask and Gunicorn, which are necessary dependencies for running the Airbnb Clone v2 application.

## Step 3: Create systemd Service File

I created a systemd service file for the Airbnb Clone v2 application. The file is located at `/etc/systemd/system/airbnb.service` and contains the following content:

```ini
[Unit]
Description=AirBnB Clone v2
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/AirBnB_clone_v2/web_flask
Environment="PATH=/usr/local/bin"
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/AirBnB_clone_v2/0-hello_route.sock -m 007 0-hello_route:app

[Install]
WantedBy=multi-user.target
```

This service file ensures proper configuration and management of the Airbnb Clone v2 application.

## Step 4: Configure Nginx

I configured Nginx in the site-available directory and create a symbolic link to site-enable. The configuration file (`/etc/nginx/sites-available/airbnb`) includes the following:

```nginx
server {
    listen 80;
    server_name 3.84.237.21;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/AirBnB_clone_v2/0-hello_route.sock;
    }
}
```

This Nginx configuration allows proper routing to the Gunicorn server.

## Step 5: Add UFW Rule

```bash
sudo ufw allow 5000
```

I added a UFW (Uncomplicated Firewall) rule to allow traffic on port 5000, ensuring proper communication with the application.

## Step 6: Restart Server

After completing the above steps, I restarted my server to apply the changes.

_DoHardThings_
