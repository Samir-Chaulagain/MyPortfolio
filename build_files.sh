#!/bin/bash

echo "Collecting static files"
python3 manage.py collectstatic --noinput

echo "Compiling SCSS to CSS"
npm run build:css
