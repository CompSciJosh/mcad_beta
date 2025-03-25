"""
Joshua Jackson
March 20, 2025,
Command Line Interface script
"""

#################################
### Load ASCII Art On Startup ###
#################################
import os
import click
import snowflake.connector
from dotenv import load_dotenv

# Define the absolute path to the .env file
env_path = os.path.expanduser("~/PycharmProjects/mcad_beta/app/backend/.env")

# Debugging
if not os.path.exists(env_path):
    print(f"Error: .env file not found at {env_path}")
else:
    print(f"Loading .env from {env_path}")

# Load environment variables from the specified .env file
load_dotenv(dotenv_path=env_path)

# Function to connect to Snowflake
def get_snowflake_connection():
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE")
    )

def display_ascii_art():
    file_path = os.path.expanduser("~/PycharmProjects/mcad_beta/app/frontend/mcad_nasa_colored.txt")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            ascii_art = file.read()
            print(ascii_art)  # Ensure the terminal supports ANSI escape codes for colors
    except Exception as e:
        print(f"Error loading ASCII art: {e}")

@click.group()
def cli():
    """NASA MCAD CLI"""
    pass

@click.command()
@click.argument("query")
def run_query(query):
    """Run a custom SQL query on Snowflake."""
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()

@click.command()
def list_craters():
    """Display data from Snowflake."""
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jams_db.jams.moon_crater_data LIMIT 10;")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()

# Register commands
cli.add_command(run_query)
cli.add_command(list_craters)

print(f"SNOWFLAKE_USER={os.getenv('SNOWFLAKE_USER')}")

if __name__ == "__main__":
    display_ascii_art()
    cli()
