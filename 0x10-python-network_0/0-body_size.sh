#!/usr/bin/env bash
# A Script To Get The Response of URL

curl -s "$1" | wc -c
