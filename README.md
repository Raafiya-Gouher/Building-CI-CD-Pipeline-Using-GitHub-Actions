# Building-CI-CD-Pipeline-Using-GitHub-Actions

###  Project Overview

This project demonstrates a full CI/CD pipeline for a Python application using GitHub Actions and deployment to an AWS EC2 instance.

The pipeline performs the following steps:

- Build and Test

    1. Installs dependencies from requirements.txt.
    2. Runs unit tests using pytest.

- Manual Approval (Optional)
    1. Requires a designated approver to confirm deployment.

- Deployment
    1. Deploys the entire repository to an EC2 instance.
    2. Sets up a Python virtual environment (venv) on EC2.
    3. Installs dependencies in the virtual environment.
    4. Runs the Python app in the background, ensuring it’s publicly accessible.

### Prerequisites
 GitHub repository with the Python application.

AWS EC2 instance (Ubuntu) with:

SSH access

Security group allowing the app’s port (e.g., 5000)

GitHub Secrets configured:

EC2_SSH_KEY: Your EC2 private key

EC2_HOST: EC2 public IP or hostname

DEPLOY_APPROVER: GitHub username(s) allowed to approve deployment

Workflow File

The GitHub Actions workflow is located at .github/workflows/main.yml.
Key steps:

Checkout code: Pulls the latest code from GitHub.

Install dependencies: Installs Python packages required for tests and deployment.

Run tests: Uses pytest for automated testing.

Manual approval: Waits for a designated GitHub user to approve deployment.

Deploy to EC2: Copies the full repo, sets up venv, installs dependencies, and starts the app.

Deployment Steps

Push changes to the main branch.

GitHub Actions triggers the workflow:

Installs dependencies

Runs tests

Workflow pauses for manual approval.

Upon approval:

The repo is copied to EC2 using rsync.

Virtual environment is created or reused.

Dependencies are installed inside venv.

The Python app starts in the background and listens on 0.0.0.0:<PORT>.

Access the app at http://<EC2_PUBLIC_IP>:<PORT>.

