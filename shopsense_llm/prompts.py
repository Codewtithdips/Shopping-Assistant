from langchain_core.prompts import ChatPromptTemplate


user_prompt_shopsense = """  
    This is the question  which I received : {question}
    This is the SQL query : {query}
    This is the answer which I was able to fetch: {answer}


    Frame this into a proper chatbot response. If there is any questions regarding card or offers please while mentioning the value like 50 or 40 add a percentage as well after it. If nothing is mentioned about cards or offer just dont mention anything
 
    leave a line before this <br>


    Also generate them in the below format
    <br><br>
    <b>Product 1:</b> if any product name<br>  -> Send this response only if there is something like that with respect to question and answer
    <b>Price:</b>If any price<br>   -> Send this response only if there is something like that with respect to question and answer
    <b>Link:</b> <a href="if it contains any link" target="_blank">Towel Terry Crew</a><br>    -> Send this response only if there is something like that with respect to question and answer
    This is because I will be sending the response to front end to it should look organised   -> Send this response only if there is something like that with respect to question and answer


    Make sure answer Product, Link, Price only if they are mentioned in the question and answer or else do not send any irrelevant data.


    If there is no information then just say you dont have information and dont send anything related to Links, Products, Card, Offers or anything
"""


shopsense_prompt_template = ChatPromptTemplate(
    [
        ("system", "You are a chatbot who responds like a chatbot"),
        ("user", user_prompt_shopsense),
    ]
)


generate_query_pormpt = ChatPromptTemplate.from_template("""Given an input question, first create a syntactically correct  query to run. Then recheck if the query is 100 percent right query.
Make sure you add public."table_name" before using the query as they are stored in a workspace called public. A sample example would be 'SELECT * FROM public.users'
ORDER BY id ASC 
Use the following format json data:

{{
    "Question": "the question  which user is sending",
    "Query" :"The Query you will be analysing and returning",
}}

Make sure to return only the json output and nothing else

Use following tables data:

{table_info}.

Question: {input}""")
