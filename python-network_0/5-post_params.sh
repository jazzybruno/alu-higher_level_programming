#!/bin/bash
# Sends a POST request with email and subject parameters and displays the body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
