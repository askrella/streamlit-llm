#!/bin/bash
host=$1
port=$2

if [[ ! $host =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Invalid host. Please provide a valid IPv4 address."
  exit 1
fi

if [[ ! $port =~ ^[0-9]+$ ]]; then
  echo "Invalid port. Please provide a valid numeric port number."
  exit 1
fi

streamlit run app.py --browser.serverAddress $host --server.port $port
