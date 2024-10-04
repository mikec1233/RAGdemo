FROM node:18 AS builder

# Install OpenJDK 17 -- THIS IS NEEDED FOR GENERATE API CLIENT 
#RUN apt-get update && apt-get install -y openjdk-17-jre && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY rag_frontend/package*.json ./

RUN npm install

COPY rag_frontend/src ./src

# API CLIENT -- THIS WILL BREAK DOCKER, ISSUE WITH RUNNING THIS, MIGHT NEED TO RUN IT AS SCRIPT AFTER NPM RUN DEV
#RUN npm run generate-api-client


FROM node:18

WORKDIR /app

COPY --from=builder /app ./

EXPOSE 8000

CMD ["npm", "run", "dev"]
