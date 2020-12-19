#!/bin/bash
# Displays all HTTP methods accepted by server of URL
curl -sI "$1" | grep "Allow:" | tail -c +8
