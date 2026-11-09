#!/bin/bash
# Makes the request that gets the catch_me route to answer You got me!
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
