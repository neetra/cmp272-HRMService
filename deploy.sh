git clone https://neetra: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@github.com/neetra/cmp272-HRMService.git
sudo apt-get update
sudo apt-get install python3.8
sudo apt install python3-pip

sudo apt install python3-virtualenv
cd cm
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
sudo apt-get install gunicorn
