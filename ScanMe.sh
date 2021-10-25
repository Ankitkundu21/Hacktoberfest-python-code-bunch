#!/bin/bash
echo "Starting Pentest... Just Wait"
#Some Inputs
read -p "Enter IP or URL :" ip;
echo "We are Pentesting on '$ip'"
rm -rf nMap nikto.log
mkdir nMap
echo "Running Nmap Scan Wait..."
nmap -p- -Pn -T4 -oN nMap/initial $ip;
echo "Nmap Scan Completed goto nMap/initial";
sleep 5;
echo "Running enum4linux...";
enum4linux -a $ip | tee enum.log;
echo "Scan Completed.. full result in enum.log";
echo "Running Nikto Scan...";
nikto -h $ip | tee nikto.log;
echo "Nikto Scan Completed view full result in 'nikto.log'";
