# EZventory Backend

EZventory is an Mobile App I designed to help small organizations keep track of their inventory ([Now available on the app store](https://play.google.com/store/apps/details?id=com.dinuw.firstapp)). The app was originally designed to support my high school's student council organize their invenotry of items for different school events. 

The REST API Backend for the Android app includes a web server created with Flask and a MySQL Database managed with SQLAlchemy. Authentication of users is handled with tokens and communication with the frontend is done via HTTP requests (initally tested on Postman).

The database and web server were containerized with Docker and are currently hosted on an AWS EC2 instance.
