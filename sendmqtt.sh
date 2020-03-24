#!/bin/bash
mydate=$(date +"%d-%m-%Y")
mytime=$(date +"%r")
message="Hi, Peter, securely on $mydate at $mytime"
#echo $message
mosquitto_pub -h postman.cloudmqtt.com -t test/testTopic -u bffxqpeu -P wbbkSHY0_fRn -p 20945 --cafile /etc/ssl/certs/ca-certificates.crt -m "$message"

