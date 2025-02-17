

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python package installer) ### Setting Up a Python Virtual Environment

To avoid conflicts with other Python projects, it's recommended to use a virtual environment. Follow these steps to set up and activate a virtual environment:

1. **Create a virtual environment:**

   `python -m venv venv`

2. **Activate virtual window:**
	- for windows:
		`venv\bin\activate`

	- forLinux
		`venv/bin/activate`
3. **Installing rquirements:**
Once your virtual environment is activated, you can install the project dependencies from the requirements.txt file:
	`pip install requirement.txt`

4. **Seting up .env file:**
	- Template of env file

``` 
    SUBABASE_URL=[YOUR SUPABASE URL]
    SUPBASE_KEY=[YOUR SUPABASE ROLE KEY]
    DB_USER=[POSTGRES USERNAME PORVIDED BY SUPA BASE]
    DB_PASSWORD=[YOUR SUPABASE PASSWORD]
    DB_HOST=[POSTGRES HOST NAME PROVIDED BY SUPABASE]
    DB_PORT=[YOUR DB PORT PROVIDE BY SUPABASE]
    DB_NAME=[YOUR DB NAME PROVIDED BY SUPABASE]
    MAIL_USERNAME= [YOUR MAIL]
    MAIL_PASSOWRD=[YOUR MAIL PASSWORD]
    MAIL_FROM=[YOUR MAIL]
```
	
> 1. Use supabase role key not the anon key on SUPABASE_KEY
> 2.  Choose sqlalchemy as type and get the inforamtion of database from session pooler
> 3. You can find all those inforamtion on supabase connection of your project or database


** Startin Server: **
Make sure Your are not python virtual environement and use following command to start server
`uvicorn app.main:app --reload` `--reload` is for automatic reload the server after changes it is optional
visit `http://localhost/8000/docs ` for API documentation



