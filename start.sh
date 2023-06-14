#!/bin/bash
port=$1

if [[ ! $port =~ ^[0-9]+$ ]]; then
  echo "Invalid port. Please provide a valid numeric port number."
  exit 1
fi

streamlit run app.py --server.port $port
