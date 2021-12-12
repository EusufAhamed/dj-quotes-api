Quotes App
==========

Setting Up Development Environment
----------------------------------

Make sure to have Docker installed on your host.

First Things First.

#. Clone Project Repository ::
    git clone <Project Repository>

#. Enter into Project Directory & Open Terminal in this Derectory ::
    cd dj-quotes-api

#. Build Docker Image
    docker-compose up --build

#. Open Another Terminal & Run
    docker exec -it dj-quotes-api bash
    
    cd src
    
    python manage.py migrate
    
    python manage.py createsuperuser

#. After that Add Some Quotes & Category Data & Visit
    http://127.0.0.1:8010/

