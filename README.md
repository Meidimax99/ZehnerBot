# ZehnerBot

## Setup the project
### virtual environment
1. Create the environment
```
python -m venv venv
```
2. activate the environment
Windows:
```
venv\Scripts\activate.bat
```
Unix:
```
source venv/bin/activate
```

3. Install requirements
```
pip install -r requirements.txt
```

### Save your API key
1. create a file called .env in the working directory 
2. save your discord & Open AI api key like this
```
DISCORD_API_KEY='your-api-key'
OPENAI_API_KEY='your-api-key'
```