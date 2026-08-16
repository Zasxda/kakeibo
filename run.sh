#!/bin/sh

docker build -t my-kakeibo-app .
docker run -p 8000:8000 my-kakeibo-app
