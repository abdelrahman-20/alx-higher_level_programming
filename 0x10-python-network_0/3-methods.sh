#!/bin/bash
# A Script To Displays All HTTP Methods
curl -s -I "${1}" | grep "^Allow: .*" | cut -d " " -f 2-
