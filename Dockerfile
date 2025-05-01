FROM node:23.11.0 AS angular-build
WORKDIR /app/frontend
COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build

FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
COPY service ./service
COPY --from=angular-build /app/frontend/dist ./dist
EXPOSE 8888
ENTRYPOINT ["python", "-u", "main.py"]