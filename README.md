# Test Service

# Quickstart

## Install project

Clone project in your home directory

```bash
git clone https://github.com/marodriguezvi/test_service
```

Create virtual environment

```bash
cd test_service
python3 -m venv venv
```

Activate virtual environment

```bash
source venv/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

Disable virtual environment

```bash
deactivate
```

## Create service

Change the `USER` value to your user in the test.service file

Add service

```bash
sudo cp test.service /etc/systemd/system/
```

Start the services

```bash
sudo systemctl start test.service
```

Check the service status

```bash
sudo systemctl status test.service
```

Make the service start with server startup

```bash
sudo systemctl enable test.service
```
