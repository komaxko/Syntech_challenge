#!/bin/bash

echo -e "\nTrying to book already reserved table"
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"date":"2020-04-20T19:00","table":"1","name":"test_name","email":"m@il.com"}' \
 localhost:8000/api/orders/

echo -e "\n\nTrying to book not reserved table"
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"date":"2020-05-20T18:00","table":"3","name":"test_name","email":"m@il.com"}' \
 localhost:8000/api/orders/
echo -e "\n\n"

