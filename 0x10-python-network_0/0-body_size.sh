#!/bin/bash
# Sends request to URL and displays size of body
curl -sI "$1" | awk '/Content-Length/{print $2}'
