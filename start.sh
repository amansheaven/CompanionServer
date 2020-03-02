#!/bin/sh
if [ "$DEBUG" == "True" ]; then
	python app.py
else
	gunicorn app:app -w 3 
fi
