# Image & Inventory Repository Backend

EZventory is an Mobile App I designed to help small organizations keep track of their inventory, [now available on the Play Store](https://play.google.com/store/apps/details?id=com.dinuw.firstapp)! The app was originally designed to support my high school's student council organize their inventory of items for different school events, and features image saving and deleting, user accounts/login, cloud saving, CRUD operations on inventory items, and CSV exports. 

The REST API Backend for the Android app includes a web server created with Flask and a MySQL Database managed with SQLAlchemy. Authentication of users is handled with tokens and communication with the frontend is done via HTTP requests (initally tested on Postman).

The database and web server were containerized with Docker and are currently hosted on an AWS EC2 instance.

## Architecture Diagram
![EZventory Diagram](https://user-images.githubusercontent.com/50289930/132991052-c8288757-2a0a-40a5-a82c-1f778340d8c0.jpeg)

## Demo!
Use Swagger to [try a brief demo](https://image-repo-2021.herokuapp.com/) of image upload/download endpoints! For full functionality tests, download the app from [Google Play Store](https://play.google.com/store/apps/details?id=com.dinuw.firstapp)!

