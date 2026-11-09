#!/bin/bash
# Sends the contents of a JSON file as a POST request body and displays the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
