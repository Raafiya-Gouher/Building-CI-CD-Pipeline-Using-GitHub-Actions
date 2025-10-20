# Building CI/CD Pipeline Using GitHub Actions and deploying it on AWS EC2 Instance

## Project Overview

This project demonstrates a **full CI/CD pipeline** for a Python application using **GitHub Actions** and deployment to an **AWS EC2 instance**.  

The pipeline performs the following steps:

1. **Build and Test**
   - Installs dependencies from `requirements.txt`.
   - Runs unit tests using `pytest`.

2. **Manual Approval (Optional)**
   - Requires a designated approver to confirm deployment.

3. **Deployment**
   - Deploys the **entire repository** to an EC2 instance.
   - Sets up a **Python virtual environment** (`venv`) on EC2.
   - Installs dependencies in the virtual environment.
   - Runs the Python app in the background, ensuring it’s publicly accessible.

---

## Prerequisites

- GitHub repository with the Python application.
- AWS EC2 instance (Ubuntu) with:
  - SSH access
  - Security group allowing the app’s port (e.g., 5000)
- GitHub Secrets configured:
  - `EC2_SSH_KEY`: Your EC2 private key
  - `EC2_HOST`: EC2 public IP or hostname
  - `DEPLOY_APPROVER`: GitHub username(s) allowed to approve deployment

---

## Workflow File

The GitHub Actions workflow is located at `.github/workflows/main.yml`.  
Key steps:

- **Checkout code**: Pulls the latest code from GitHub.
- **Install dependencies**: Installs Python packages required for tests and deployment.
- **Run tests**: Uses `pytest` for automated testing.
- **Manual approval**: Waits for a designated GitHub user to approve deployment.
- **Deploy to EC2**: Copies the full repo, sets up `venv`, installs dependencies, and starts the app.

---

## Deployment Steps

1. Push changes to the `main` branch.
2. GitHub Actions triggers the workflow:
   - Installs dependencies
   - Runs tests
3. Workflow pauses for manual approval.
4. Upon approval:
   - The repo is copied to EC2 using `rsync`.
   - Virtual environment is created or reused.
   - Dependencies are installed inside `venv`.
   - The Python app starts in the background and listens on `0.0.0.0:<PORT>`.
5. Access the app at `http://<EC2_PUBLIC_IP>:<PORT>`.

---

## Folder Structure
.<br>
├── app.py<br>
├── requirements.txt<br>
├── tests/<br>
│ └── test_app.py<br>
├── .github/<br>
│ └── workflows/<br>
│ └── main.yml<br>
└── README.md<br>

---

## Project Architecture

This project demonstrates a **modern CI/CD pipeline** for a Python application. The architecture consists of three main layers:

1. **Source Code (GitHub Repository)**
   - Contains Python application, tests, and configuration.
   - All changes trigger the workflow when pushed to the `main` branch.

2. **Continuous Integration (CI)**
   - GitHub Actions checks out the code.
   - Installs dependencies in the workflow runner.
   - Runs automated **unit tests** using `pytest`.
   - Ensures that only code passing tests can be deployed.

3. **Continuous Deployment (CD)**
   - Manual approval step ensures control over production deployments.
   - Full repository is deployed to **EC2**.
   - A Python virtual environment (`venv`) is used to manage dependencies.
   - Application runs in the background on EC2, serving requests publicly.

---

## CI/CD Workflow Explanation

The workflow in `.github/workflows/main.yml` is structured into **six main steps**:

1. **Checkout Code**
   - Uses `actions/checkout@v3` to pull the latest commit.

2. **Setup Python**
   - Ensures consistent Python version (`3.12`) across workflow runners.

3. **Install Dependencies**
   - Installs project dependencies listed in `requirements.txt`.
   - Installs `pytest` for unit testing.

4. **Run Unit Tests**
   - Runs `pytest` for all tests in `tests/`.
   - Failing tests prevent deployment, ensuring only stable code is deployed.

5. **Await Manual Approval**
   - Uses `trstringer/manual-approval@v1`.
   - Requires a GitHub user (stored in `DEPLOY_APPROVER`) to approve deployment.
   - Provides a safety check before production deployment.

6. **Deploy to EC2**
   - Copies the **entire repository** using `rsync`.
   - Creates or reuses a virtual environment (`venv`) on EC2.
   - Installs dependencies in the venv.
   - Stops any running instance of the app and starts the new one.
   - Streams recent logs (`tail -n 20 app.log`) to GitHub Actions for debugging.

---

## EC2 Deployment Details

- **EC2 Instance**:
  - Ubuntu OS
  - SSH access configured with private key stored as GitHub Secret
  - Security group configured to allow inbound traffic on the application port (e.g., 5000)

- **Deployment Flow**:
  1. GitHub Actions workflow uploads the repository to `/home/ubuntu/app`.
  2. Sets up virtual environment to isolate dependencies.
  3. Installs all required Python packages.
  4. Restarts the app, ensuring the latest code is running.
  5. Logs are stored in `app.log` for monitoring.

- **Accessing the App**:
  - Open browser at: `http://<EC2_PUBLIC_IP>:<PORT>`
  - Example: `http://3.101.25.67:5000`

---

## Key Learning Outcomes

By implementing this project, the following concepts were learned:

1. **CI/CD with GitHub Actions**
   - Workflow triggers on branch push.
   - Jobs can be sequential (`needs`) or parallel.
   - Conditional deployment using `if: success()`.

2. **Python Virtual Environments**
   - Avoids global package conflicts.
   - Ensures consistent runtime for deployment.

3. **Manual Approval in CI/CD**
   - Adds an extra layer of safety for production deployments.

4. **EC2 Deployment**
   - Using `ssh` and `rsync` to deploy full application.
   - Handling process restarts and log monitoring.

5. **Troubleshooting**
   - Ensuring app listens on `0.0.0.0` for public access.
   - Managing security group rules for network access.
   - Capturing logs from background processes.