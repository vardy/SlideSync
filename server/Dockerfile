# Base image
FROM node:10

# Setting the directory in the container we're working in
WORKDIR /usr/src/slide_server

# Installing dependencies
COPY package*.json ./
RUN npm install

# Copying source into project
COPY . .

# Exposing port 3000 to be bound publicly at runtime
EXPOSE 3000

# Running the server
CMD [ "npm", "run", "start" ]