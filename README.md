# AI-Powered Shopping Assistant

## Project Overview

ShopSense is an AI-driven shopping assistant designed to enhance user experience by providing personalized product recommendations, retrieving shopping interactions, and offering real-time discounts. The chatbot leverages FastAPI for backend processing, LangChain for dynamic query generation, and Groq Llama-3.3-70B for generating conversational responses.


## 🎥 Demo

[![Watch the video](https://img.youtube.com/vi/jmplmsxggxo/maxresdefault.jpg)](https://youtu.be/nDdps-DpMRo)

A quick demonstration of ShopSense features including:

- Product tracking across e-commerce sites
- Chatbot interactions
- Credit card recommendations
- Real-time price tracking

## Features of ShopSense: AI-Powered Shopping Assistant
## AI-Powered Shopping Chatbot

- Retrieves user-specific shopping interactions (product views, wishlists, applied offers).Generates intelligent, context-aware responses using Groq Llama-3.3-70B.

- FastAPI-Based Backend: High-performance, asynchronous API development for seamless request handling.Uses Jinja2 for templating and structured responses.

- PostgreSQL Database Integration: Stores user interactions efficiently for real-time recommendations.Ensures data persistence and optimized query performance.

- Asynchronous Query Execution (AsyncPG): Improves database interaction speed by handling multiple queries simultaneously.Reduces response time for a smoother user experience.

- Dynamic SQL Query Generation (LangChain): Uses LangChain SQLDatabase utilities to securely generate and execute SQL queries based on user input.Enhances flexibility in retrieving shopping-related data.

- Secure User Authentication (FastAPI Auth): Implements session-based authentication for secure login/logout.Ensures only authenticated users can access personalized recommendations.

- Custom Chatbot Response Generator: Formats chatbot replies for improved readability and user experience.Ensures structured responses based on retrieved shopping data.

- Reusable LLM Chains & Prompts:Enhances chatbot accuracy by refining AI-generated responses.Improves contextual understanding of user queries.


# 🚀 Technology Stack
- Backend Framework: 🚀 FastAPI – High-performance, asynchronous web framework for API development.
- Database: 🛢 PostgreSQL – Relational database to store user interactions, product views, and applied offers.
- Database Querying: ⚡ AsyncPG – Asynchronous PostgreSQL client for efficient query execution.
- AI & LLM Integration: 🤖 LangChain – Used for dynamically generating SQL queries and enhancing chatbot capabilities.
- Large Language Model (LLM): 🔗 Groq Llama-3.3-70B – Powers the AI chatbot to generate intelligent and context-aware responses.
- Templating Engine: 🏗 Jinja2 – Renders structured chatbot responses for better readability.
- Environment Management: 🔐 dotenv – Manages environment variables securely.
- Authentication: 🔑 FastAPI Auth – Implements secure session-based login/logout functionalities.

### Database Schema

```sql
CREATE TABLE Users (
   user_id INT PRIMARY KEY,
   email VARCHAR(255),
   name VARCHAR(100),
   created_at TIMESTAMP
);

CREATE TABLE Products (
   product_id INT PRIMARY KEY,
   product_link TEXT,
   website_company_name VARCHAR(100),
   prodct_name VARCHAR(255),
   description TEXT,
   category VARCHAR(100),
   current_price DECIMAL(10,2),
   original_price DECIMAL(10,2),
   discount_percentage DECIMAL(5,2),
   brand VARCHAR(100),
   availability_status BOOLEAN,
   last_updated TIMESTAMP
);

CREATE TABLE UserProductInteractions (
   interaction_id INT PRIMARY KEY,
   user_id INT,
   product_id INT,
   interaction_type VARCHAR(100),
   interaction_date TIMESTAMP,
   FOREIGN KEY (user_id) REFERENCES Users(user_id),
   FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE CreditCards (
   card_id INT PRIMARY KEY,
   card_name VARCHAR(100),
   bank_name VARCHAR(100),
   reward_rate DECIMAL(4,2),
   cashback_categories JSON,
   annual_fee DECIMAL(10,2),
   special_offers TEXT
);

CREATE TABLE ProductCardBenefits (
   benefit_id INT PRIMARY KEY,
   product_id INT,
   card_id INT,
   benefit_type VARCHAR(50),
   benefit_value DECIMAL(5,2),
   valid_until DATE,
   FOREIGN KEY (product_id) REFERENCES Products(product_id),
   FOREIGN KEY (card_id) REFERENCES CreditCards(card_id)
);
```

## 🔧 Setup and Installation

1. Clone the repository:
   ```sh
   https://github.com/Codewtithdips/Shopping-Assistant.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Shopping-Assistant
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables
   - ENTER YOUR API KEY
   - DATABASE NAME , PASSWORD
  
5. Initialize the database

6. Run the application
 ```sh
   uvicorn main:app --reload
   ```
7. Access the application
   ```sh
   Navigate to http://127.0.0.1:8000/login to reach the login page
   ```

   
   
