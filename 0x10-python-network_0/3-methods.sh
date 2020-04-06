#!/bin/bash
# Dsplay all accepted HTTP methods URL server passed into program
curl -sI "$1" | sed -n 's/Allow: //p'
