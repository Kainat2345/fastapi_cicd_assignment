python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn main:app --reload

pytest -v

git init

git add .

git commit -m "Initial commit"

git remote add origin REPO_URL

git push -u origin main
