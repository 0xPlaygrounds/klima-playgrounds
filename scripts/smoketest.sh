#!/bin/bash

FAILING=0

python index.py &
DASH_PID=$!
sleep 15
RESP_CODE=$(curl --head --location --write-out %{http_code} --silent --output /dev/null http://127.0.0.1:8050/)
echo $RESP_CODE
kill `lsof -w -n -i tcp:8050 | awk '$2!="PID" {print $2;}'`
if [ "$RESP_CODE" != "200" ];
then
echo "FAILED! ($RESP_CODE)"
FAILING=1
else
echo "OK ($RESP_CODE)"
fi

if [ $FAILING -eq 1 ];
then
  echo "ERROR"
  exit 1
else
  echo "SUCCESS"
  exit 0
fi
