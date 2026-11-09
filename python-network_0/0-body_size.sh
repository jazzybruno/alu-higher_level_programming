#!/bin/bash
# Displays the size in bytes of the body of the response to a request to a URL
curl -s "$1" | wc -c
