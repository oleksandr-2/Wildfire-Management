#!/bin/bash

# PostgreSQL variables
PG_HOST="localhost"
PG_PORT="5432"
PG_USER="postgres"
PG_DB="wildfire_db"
PG_USER_NAME="wildfire_user"
PG_USER_PASSWORD="wildfire_password"

# MongoDB variables
MONGO_HOST="localhost"
MONGO_PORT="27017"
MONGO_DB="wildfire_db"
MONGO_COLLECTION="data"

# Initialize PostgreSQL database
echo "Initializing PostgreSQL database..."

# Create PostgreSQL user and database
psql -h ${PG_HOST} -p ${PG_PORT} -U ${PG_USER} -c "CREATE DATABASE ${PG_DB};"
psql -h ${PG_HOST} -p ${PG_PORT} -U ${PG_USER} -c "CREATE USER ${PG_USER_NAME} WITH ENCRYPTED PASSWORD '${PG_USER_PASSWORD}';"
psql -h ${PG_HOST} -p ${PG_PORT} -U ${PG_USER} -c "GRANT ALL PRIVILEGES ON DATABASE ${PG_DB} TO ${PG_USER_NAME};"

echo "PostgreSQL database and user created successfully."

# Initialize MongoDB database and collection
echo "Initializing MongoDB database..."

# Create MongoDB database and collection
mongo <<EOF
use ${MONGO_DB}
db.createCollection("${MONGO_COLLECTION}")
EOF

echo "MongoDB database and collection created successfully."

echo "Database initialization completed."

# Make the script executable: chmod +x scripts/init_databases.sh
# Run the script: ./scripts/init_databases.sh
