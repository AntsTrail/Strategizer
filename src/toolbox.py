import importlib
import os
import sys
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI


class Toolbox:
    

    def __init__(self):
        """
        Initializes the Toolbox instance and loads all tools from the 'tools' directory.
        """
        self.tools = {}
        self._load_tools()

    def _load_tools(self):
        
        try:
            # Optionally, add the project root to sys.path.
            project_root = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..")
            )
            sys.path.insert(0, project_root)

            # List all Python files in the 'src/tools' directory.
            tool_dir = os.path.join("src", "tools")
            tool_files = [f for f in os.listdir(tool_dir) if f.endswith(".py")]

            for file in tool_files:
                # Remove '.py' to get the module name.
                module_name = file[:-3]
                try:
                    # Import using the full package name: 'src.tools.<module_name>'
                    module = importlib.import_module(f"src.tools.{module_name}")

                    # Look for the tool class (assuming it's named like <tool_name>Tool).
                    tool_class_name = f"{module_name.capitalize()}Tool"
                    if hasattr(module, tool_class_name):
                        tool_class = getattr(module, tool_class_name)
                        if issubclass(tool_class, Tool):
                            # Store the tool class in the 'tools' dictionary.
                            self.tools[module_name] = tool_class()

                except ImportError as e:
                    raise ImportError(f"Error importing tool '{module_name}': {e}")
        except FileNotFoundError:
            raise FileNotFoundError("The 'src/tools' directory was not found.")

    def call_tool(self, name, *args, **kwargs):
        
        if name in self.tools:
            try:
                tool = self.tools[name]
                return tool.run(*args, **kwargs)
            except TypeError as e:
                raise TypeError(f"Error calling tool '{name}': {e}")
        else:
            raise ValueError(f"Tool '{name}' not found!")

    def get_all_tools(self):
        
        tools_list = []
        for tool_name, tool in self.tools.items():
            tools_list.append({
                "tool_name": tool_name,
                "description": tool.description,
            })
        return tools_list


if __name__ == "__main__":
    # Create an instance of Toolbox
    tb = Toolbox()

    # Print all tools in structured format
    tools_list = tb.get_all_tools()
    print(tools_list)  # This can be used in an API response

    try:
        # Call the 'modulo' tool with two numbers.
        result = tb.call_tool("modulo", 11, 3)
        print(f"Modulo Result: {result}")

    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
