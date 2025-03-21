from langchain_openai import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()  # Automatically loads .env file

class Planner:
    def __init__(self, model_name: str = "gpt-4o"):
        # Initialize the language model
        self.llm = ChatOpenAI(model=model_name, temperature=0)

        # Create system prompt as a template
        self.system_prompt = SystemMessagePromptTemplate.from_template(self.get_system_prompt())
        
        # Create LLMChain
        self.chain = LLMChain(llm=self.llm, prompt=self.create_chat_prompt())

    def get_system_prompt(self) -> str:
        """Creates the system prompt explicitly using LangChain's prompt template."""
        return f"""
        ### Persona ###
        - You are an experienced mathematician.
        - You simplify mathematical equations using available tools.
        - You create structured plans for solving mathematical problems.

        ### Instructions ###
        - Use only the tools provided:
        - First, check if a virtual tool solves the problem.
        - If using a virtual tool, return `"type": "virtual_tool"`.
        - If constructing a plan, return `"type": "basic_tool"`.
        - All results must be in JSON format following the schema.
        - Use only numbers with **two decimal places**.
        """

    def create_chat_prompt(self):
        """Creates and returns the full chat prompt template using system and user prompts."""
        user_prompt = HumanMessagePromptTemplate.from_template("### Query ### {query}")
        return ChatPromptTemplate.from_messages([self.system_prompt, user_prompt])

    def user_prompt(self, query: str):
        """Formats the user query prompt using the LangChain template."""
        # Return the formatted user prompt
        return self.create_chat_prompt().format_messages(query=query)

    def process(self, query: str):
        """Processes a query using LangChain’s message-based prompt structure."""
        # Get the formatted prompt for the user's query
        formatted_prompt = self.user_prompt(query)
        
        # Get response using the chain
        response = self.chain.run(formatted_prompt)
    
        return response
    

planner = Planner()
print(planner.process("Hello"))
