from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.tools import QuerySQLDatabaseTool
import os
from langchain_core.output_parsers import SimpleJsonOutputParser
from shopsense_llm.prompts import generate_query_pormpt
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_name = os.getenv("db_name")
db_host = os.getenv("db_host")
port = 5433


async def extract_json_from_braces(text):
    # Find the first opening brace
    start_index = text.find("{")
    if start_index == -1:
        return None

    # Count braces to find the corresponding closing brace
    count = 1
    end_index = start_index + 1
    while end_index < len(text) and count > 0:
        if text[end_index] == "{":
            count += 1
        elif text[end_index] == "}":
            count -= 1
        end_index += 1

    # Extract the substring
    json_string = text[start_index:end_index]
    return json_string


async def retrieve_input_data(email, question, llm):
    db = SQLDatabase.from_uri(
        f"postgresql://{db_user}:{db_password}@{db_host}:5433/{db_name}"
    )
    table_info = db.table_info
    llm_chain = generate_query_pormpt | llm | SimpleJsonOutputParser()
    llm_response = await llm_chain.ainvoke(
        {
            "table_info": table_info,
            "input": f"My email is {email}. Now " + question,
        }
    )
    query = llm_response["Query"]
    execute_query = QuerySQLDatabaseTool(db=db)
    answer = await execute_query.ainvoke(query)
    input_data = {"question": question, "query": query, "answer": answer}
    return input_data
