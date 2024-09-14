# Rbnb's Backend
## 🏠Using Flask and PostgreSQL to realize Rbnb's backend functions.
## Introduction
This project is the backend implementation for Rbnb, a platform inspired by Airbnb. It provides RESTful API endpoints to support frontend functionalities such as displaying tabs, icons, and other resources.

## Features
* RESTful API endpoints for frontend consumption
* Data management using PostgreSQL
* Data models for tabs, icons, and related entities
* Cross-Origin Resource Sharing (CORS) enabled
* Error handling and input validation

## Technologies Used
* Flask: A lightweight WSGI web application framework for Python.
* PostgreSQL: An advanced open-source relational database.
* SQLAlchemy: An ORM for Python to interact with the database.
* Flask-Migrate: Handles database migrations for Flask applications using Alembic.
* Flask-CORS: A Flask extension for handling Cross-Origin Resource Sharing (CORS).
* Python 3.7+

## Four API Endpoints
### Tabs
* GET /api/tabs - Retrieve all tabs.

Response:
```
[
  {
    "id": 1,
    "name": "Home",
    "iconImgUrl": "http://example.com/icon1.png"
  },
  {
    "id": 2,
    "name": "Explore",
    "iconImgUrl": "http://example.com/icon2.png"
  }
  // ...
]
```

### Icons
* GET /api/icons - Retrieve all icons.
Response:
```
[
  {
    "itemId": 0,
    "icons": "true",
    "title": "Sample Title",
    "otherInfo": "Some info",
    "detailHTML": "<p>Details</p>",
    "host": {
      "hostName": "Host Name",
      "hostImgUrl": "http://example.com/host.jpg",
      "hostProfession": "Profession"
    },
    "imgUrl": ["http://example.com/image1.jpg", "http://example.com/image2.jpg"],
    "meetInfo": {
      "startHostYear": "2024",
      "iconSvg": ["<svg>...</svg>"],
      "hostDesc": ["Description 1", "Description 2"]
    }
  }
  // ...
]
```

### Past-Experience
* GET /api/past-experience - Retrieve all past-experience data.
Response:
```
[
  {
    "itemId": 0,
    "icons": "true",
    "past": "true",
    "title": "Live like Bollywood star Janhvi Kapoor",
    "host": "Hosted by Janhvi Kapoor",
    "otherInfo": "Sold out",
    "imgUrl": [
      "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTEzMTA4NjI3OTI1MjIxNDQyOA%3D%3D/original/bc989f2d-eca8-4bcf-a9b0-b70b8e685a64.jpeg?im_w=1440&im_q=highq",
      "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTEzMTA4NjI3OTI1MjIxNDQyOA%3D%3D/original/acb7c0e1-5e3d-4f12-9aea-f9ee71a9035a.jpeg?im_w=1440&im_q=highq",
      "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTEzMTA4NjI3OTI1MjIxNDQyOA%3D%3D/original/1e05770b-cfb9-4484-aa14-8fd4d14ee7b3.jpeg?im_w=1440&im_q=highq",
      "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTEzMTA4NjI3OTI1MjIxNDQyOA%3D%3D/original/b6288ffe-0bc2-4b01-b2f6-d0d0b78d0959.jpeg?im_w=1440&im_q=highq",
      "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTEzMTA4NjI3OTI1MjIxNDQyOA%3D%3D/original/400678f7-fbed-4f07-80b3-ba2fd03c66b1.jpeg?im_w=1440&im_q=highq",
      "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTEzMTA4NjI3OTI1MjIxNDQyOA%3D%3D/original/46e12a73-947b-4a95-a70c-d4c80334eeb9.jpeg?im_w=1440&im_q=highq"
    ]
  },
  {
    "itemId": 1,
    "icons": "true",
    "past": "true",
    "title": "Open the Olympic Games at Musée d’Orsay",
    "host": "Hosted by Mathieu Lehanneur",
    "otherInfo": "Sold out",
    "imgUrl": [
      "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTE2MjI1MjI0NDQ0MzYzMjM4Mg%3D%3D/original/ae3426d1-fba4-44d4-bed2-690426f25f7a.jpeg?im_w=1440&im_q=highq",
      "https://a0.muscache.com/im/pictures/hosting/Hosting-U3RheVN1cHBseUxpc3Rpbmc6MTE2MjI1MjI0NDQ0MzYzMjM4Mg%3D%3D/original/bf7a757d-9352-4b37-a8c2-9656427bc7fb.jpeg?im_w=1440&im_q=highq"
    ]
  },
  // ...
]
```

### Home-Footer
* GET /api/home-footer - Retrieve all home-footer data.
Response:
```
[
  {
    "key": "0",
    "label": "Popular",
    "children": [
      {
        "id": "0",
        "title": "Canmore",
        "text": "Flat rentals"
      },
      {
        "id": "1",
        "title": "Benalmádena",
        "text": "House rentals"
      },
      {
        "id": "2",
        "title": "Marbella",
        "text": "House rentals"
      },
      {
        "id": "3",
        "title": "Whistler",
        "text": "Cabin rentals"
      },
      {
        "id": "4",
        "title": "Vancouver",
        "text": "Apartment rentals"
      },
      {
        "id": "5",
        "title": "Banff",
        "text": "Cabin rentals"
      },
      {
        "id": "6",
        "title": "Tofino",
        "text": "Beach house rentals"
      },
      {
        "id": "7",
        "title": "Jasper",
        "text": "Mountain lodge rentals"
      },
      // ...
    ]
  },
  // ...
]
```

