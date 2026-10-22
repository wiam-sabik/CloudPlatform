\# CloudPlatform



A lightweight system monitoring API built with Python and Flask, containerized with Docker and deployed on AWS EC2.



\## Live Demo

http://56.228.29.205:5000



\## Features

\- Real-time system metrics: CPU, RAM, and disk usage

\- Health status endpoint with per-metric status labels (ok/warning/critical)

\- Containerized with Docker for portable, consistent deployment

\- Deployed live on AWS EC2 (Ubuntu, free-tier instance)



\## Tech Stack

\- \*\*Language:\*\* Python

\- \*\*Framework:\*\* Flask

\- \*\*Libraries:\*\* psutil (system metrics)

\- \*\*Containerization:\*\* Docker

\- \*\*Cloud:\*\* AWS EC2 (Ubuntu)

\- \*\*Version Control:\*\* Git/GitHub



\## API Endpoints

| Endpoint | Description |

|---|---|

| `/` | Basic status check |

| `/metrics` | Raw CPU, RAM, disk usage percentages |

| `/system-status` | Metrics + per-item status (ok/warning/critical) + overall status |



\## Running Locally (without Docker)

\\`\\`\\`bash

pip install -r requirements.txt

python app.py

\\`\\`\\`

App runs on http://localhost:5000



\## Running with Docker

\\`\\`\\`bash

docker build -t cloudplatform .

docker run -d -p 5000:5000 --name cloudplatform-container cloudplatform

\\`\\`\\`



\## Deployment Architecture

\- EC2 instance (Ubuntu, t2/t3.micro, AWS free tier)

\- Docker installed directly on the EC2 server

\- Application container built and run on the instance

\- Security group configured to allow inbound traffic on port 5000

\- Publicly accessible via the instance's public IP



\## Roadmap

\- \[x] Python/Flask API

\- \[x] Git/GitHub version control

\- \[x] Dockerized application

\- \[x] Deployed on AWS EC2

\- \[ ] AWS S3 integration

\- \[ ] IAM / security best practices

\- \[ ] AWS networking / VPC

\- \[ ] CloudWatch monitoring, logs, and alarms

\- \[ ] Database / persistent data storage

\- \[ ] Infrastructure as Code (Terraform)

\- \[ ] CI/CD with GitHub Actions

\- \[ ] Kubernetes (future)

