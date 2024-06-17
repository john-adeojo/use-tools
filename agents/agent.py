from termcolor import colored
from prompts.prompts import agent_system_prompt_template
from models.openai_models import OpenAIModel
from models.ollama_models import OllamaModel
from tools.basic_calculator import basic_calculator
from tools.reverser import reverse_string
from toolbox.toolbox import ToolBox


class Agent:
    def __init__(self, tools, model_service, model_name, stop=None):
        """
        Initializes the agent with a list of tools and a model.

        Parameters:
        tools (list): List of tool functions.
        model_service (class): The model service class with a generate_text method.
        model_name (str): The name of the model to use.
        """
        self.tools = tools
        self.model_service = model_service
        self.model_name = model_name
        self.stop = stop

    def prepare_tools(self):
        """
        Stores the tools in the toolbox and returns their descriptions.

        Returns:
        str: Descriptions of the tools stored in the toolbox.
        """
        toolbox = ToolBox()
        toolbox.store(self.tools)
        tool_descriptions = toolbox.tools()
        return tool_descriptions

    def think(self, prompt):
        """
        Runs the generate_text method on the model using the system prompt template and tool descriptions.

        Parameters:
        prompt (str): The user query to generate a response for.

        Returns:
        dict: The response from the model as a dictionary.
        """
        tool_descriptions = self.prepare_tools()
        agent_system_prompt = agent_system_prompt_template.format(tool_descriptions=tool_descriptions)

        # Create an instance of the model service with the system prompt

        if self.model_service == OllamaModel:
            model_instance = self.model_service(
                model=self.model_name,
                system_prompt=agent_system_prompt,
                temperature=0,
                stop=self.stop
            )
        else:
            model_instance = self.model_service(
                model=self.model_name,
                system_prompt=agent_system_prompt,
                temperature=0
            )

        # Generate and return the response dictionary
        agent_response_dict = model_instance.generate_text(prompt)
        return agent_response_dict

    def work(self, prompt):
        """
        Parses the dictionary returned from think and executes the appropriate tool.

        Parameters:
        prompt (str): The user query to generate a response for.

        Returns:
        The response from executing the appropriate tool or the tool_input if no matching tool is found.
        """
        agent_response_dict = self.think(prompt)
        tool_choice = agent_response_dict.get("tool_choice")
        tool_input = agent_response_dict.get("tool_input")

        for tool in self.tools:
            if tool.__name__ == tool_choice:
                response = tool(tool_input)

                print(colored(response, 'cyan'))
                return
                # return tool(tool_input)

        print(colored(tool_input, 'cyan'))
        
        return


# Example usage
if __name__ == "__main__":

    tools = [basic_calculator, reverse_string]


    # Uncoment below to run with OpenAI
    # model_service = OpenAIModel
    # model_name = 'gpt-3.5-turbo'
    # stop = None

    # Uncomment below to run with Ollama
    model_service = OllamaModel
    model_name = 'llama3:instruct'
    stop = "<|eot_id|>"

    agent = Agent(tools=tools, model_service=model_service, model_name=model_name, stop=stop)

    while True:
        prompt = input("Ask me anything: ")
        if prompt.lower() == "exit":
            break
    
        agent.work(prompt)
