# CloudPlatform

A lightweight system monitoring API built with Python and Flask, containerized with Docker and deployed on AWS EC2.

## Live Demo
http://56.228.29.205:5000

## Features
- Real-time system metrics: CPU, RAM, and disk usage
- Health status endpoint with per-metric status labels (ok/warning/critical)
- Containerized with Docker for portable, consistent deployment
- Deployed live on AWS EC2 (Ubuntu, free-tier instance)

## Tech Stack
- **Language:** Python
- **Framework:** Flask
- **Libraries:** psutil (system metrics)
- **Containerization:** Docker
- **Cloud:** AWS EC2 (Ubuntu)
- **Version Control:** Git/GitHub

## API Endpoints
| Endpoint | Description |
|---|---|
| `/` | Basic status check |
| `/metrics` | Raw CPU, RAM, disk usage percentages |
| `/system-status` | Metrics + per-item status (ok/warning/critical) + overall status |

## Running Locally (without Docker)
```bash
pip install -r requirements.txt
python app.py
```
App runs on http://localhost:5000

## Running with Docker
```bash
docker build -t cloudplatform .
docker run -d -p 5000:5000 --name cloudplatform-container cloudplatform
```

## Deployment Architecture
- EC2 instance (Ubuntu, t2/t3.micro, AWS free tier)
- Docker installed directly on the EC2 server
- Application container built and run on the instance
- Security group configured to allow inbound traffic on port 5000
- Publicly accessible via the instance's public IP

## IAM & Security
- MFA enabled on the AWS Builder ID that owns the account
- IAM role `cloudplatform-ec2-role` attached to the EC2 instance (CloudWatchAgentServerPolicy), so no access keys are stored on the server
- Custom least-privilege policy `monitoring-readonly-policy`: read-only access to EC2 and CloudWatch (Describe/Get/List actions only)
- Practice IAM user `viewer-test` with only that policy, no console access and no access keys
- Note: user groups and IAM Access Analyzer were unavailable on the Free-plan account (blocked by plan limits)

Full details: [iam.documentation.md](iam.documentation.md)

## Roadmap
- [x] Python/Flask API
- [x] Git/GitHub version control
- [x] Dockerized application
- [x] Deployed on AWS EC2
- [x] IAM / security best practices
- [ ] AWS S3 integration
- [ ] AWS networking / VPC
- [ ] CloudWatch monitoring, logs, and alarms
- [ ] Database / persistent data storage
- [ ] Infrastructure as Code (Terraform)
- [ ] CI/CD with GitHub Actions
- [ ] Kubernetes (future)
