#!/bin/bash

echo "Deploying infrastructure..."
terraform init
terraform apply -auto-approve

echo "Setting up application..."
python3 src/auth/user_auth.py
python3 src/ids/ids_engine.py

echo "Deployment completed!"
