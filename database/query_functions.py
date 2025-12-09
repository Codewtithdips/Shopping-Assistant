import asyncpg
from database.queries import user_interaction_query

import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_name = os.getenv("db_name")
db_host = os.getenv("db_host")
port = 5432


async def get_user_interactions_by_email(email: str) -> dict:
    pool = await asyncpg.create_pool(
        user=db_user, password=db_password, database=db_name, host=db_host, port=port
    )

    try:
        async with pool.acquire() as conn:
            query = user_interaction_query

            rows = await conn.fetch(query, email)

            result = {}
            for row in rows:
                interaction_type = row["interaction_type"]
                if interaction_type not in result:
                    result[interaction_type] = []

                product_info = {
                    "product_id": row["product_id"],
                    "product_link": row["product_link"],
                    "product_name": row["prodct_name"],
                    "description": row["description"],
                    "category": row["category"],
                    "current_price": float(row["current_price"])
                    if row["current_price"]
                    else None,
                    "original_price": float(row["original_price"])
                    if row["original_price"]
                    else None,
                    "discount_percentage": float(row["discount_percentage"])
                    if row["discount_percentage"]
                    else None,
                    "brand": row["brand"],
                    "availability_status": row["availability_status"],
                    "card_benefits": row["card_benefits"]
                    if row["card_benefits"]
                    else [],
                }

                result[interaction_type].append(product_info)

            return result
    finally:
        await pool.close()
