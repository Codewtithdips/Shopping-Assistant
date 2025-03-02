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
