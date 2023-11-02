FROM node:lts-alpine3.17

WORKDIR /app

COPY package*.json ./
COPY .env ./

RUN npm install 

COPY . .

RUN npm run build

EXPOSE 8080
CMD [ "npm", "run", "preview" ]