if [ ! -d .venv ]; then
	virtualenv .venv
	pip install -r requirements.txt
fi
source .venv/bin/activate
uvicorn app.main:app
