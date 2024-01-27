# 0x1A. Application Server

## Application Server vs Web Server
In the realm of web development, understanding the distinction between application servers and web servers is crucial. Both serve distinct purposes, and their collaboration is integral to delivering web applications efficiently.

### Web Server
A web server primarily handles HTTP requests and responses. It's responsible for serving static content like HTML, CSS, and images to clients. Popular web servers include Apache and Nginx.

### Application Server
On the other hand, an application server is tasked with executing the application code. It processes dynamic content, interacts with databases, and performs business logic. Examples of application servers include Gunicorn, uWSGI, and mod_wsgi.

In a typical deployment scenario, a web server acts as a reverse proxy, forwarding requests to the application server, which then processes them and returns the results to the web server for delivery.

## Serving a Flask Application with Gunicorn and Nginx on Ubuntu 16.04
To ensure optimal performance and scalability, it's recommended to use Gunicorn as the application server and Nginx as the web server. Below are step-by-step instructions:

1. **Installation (Global):**
   - Install Gunicorn and Nginx globally, avoiding the use of virtualenv for Gunicorn.

2. **Running Gunicorn:**
   - Start Gunicorn to serve your Flask application. This can be achieved by running a command similar to:
     ```bash
     gunicorn -w 4 your_app:app
     ```
     Adjust the number of workers ("-w") based on your server's resources.

3. **Dealing with Strict Slashes:**
   - Flask has a behavior regarding trailing slashes in routes. Be mindful of the `strict_slashes` option, ensuring it aligns with your application's requirements.

### Resources:
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Gunicorn Documentation](https://docs.gunicorn.org/en/stable/)
- [Nginx Documentation](https://nginx.org/en/docs/)
- [Upstart Documentation](https://wiki.ubuntu.com/SystemdForUpstartUsers)
