cd C:\Users\vcm\Desktop\testapp 
pip install -r requirements.txt
git pull https://%TESTAPP_GIT_PAT%@github.com/JakeVestal/testapp.git
venv\Scripts\python.exe server.py
