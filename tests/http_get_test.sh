#!/bin/bash -x
exp_response='200'
if [ $(curl -o /dev/null -s -w "%{http_code}\n" http://localhost:80) = $exp_response ]; then
  exit 0
else
  exit 1
fi
