#!/bin/bash
# Sends a GET request with the user id header set to 98 and displays the body
curl -s -H "X-HolbertonSchool-User-Id: 98" -H "X-School-User-Id: 98" "$1"
