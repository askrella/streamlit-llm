#!/bin/bash
host=$1
port=$2

if ! echo "$host" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "Invalid host. Please provide a valid IPv4 address."
  exit 1
fi

if ! echo "$port" | grep -qE '^[0-9]+$'; then
  echo "Invalid port. Please provide a valid numeric port number."
  exit 1
fi

streamlit run app.py --browser.serverAddress $host --server.port $port --server.enableCORS=false
