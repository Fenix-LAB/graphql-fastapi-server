#!/bin/bash

# Function to check if the database exists
database_exists() {
    psql -U postgres -lqt | cut -d \| -f 1 | grep -wq "$1"
}

# Check if the database exists
if database_exists "db_GQ"; then
    echo "Database 'db_GQ' already exists."
else
    echo "Creating database 'db_GQ'..."
    # Create the database
    psql -U postgres -c "CREATE DATABASE db_GQ;"
    echo "Database 'db_GQ' created."
fi