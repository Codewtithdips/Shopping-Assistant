from langchain_core.output_parsers import StrOutputParser
from shopsense_llm.prompts import shopsense_prompt_template


async def retireve_answer(input_data, llm):
    chain = shopsense_prompt_template | llm | StrOutputParser()
    return await chain.ainvoke(input_data)
