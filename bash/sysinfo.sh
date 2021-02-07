#!/bin/bash
#This script will email us our user, IP, hostname and today's date
emailaddress=wildowac@mail.uc.edu
today=$(date +"%d-%m-%Y %H:%M:%S")
ip=$(ip a | grep 'dynamic ens192' | awk '{print $2}')

content="User $USER
Server Name is $HOSTNAME
IP address is $ip
Date and Time is $today"

echo "Email will contain:$content"
mail -s "IT3038C Linux IP" $emailaddress<<<$(echo -e $content)