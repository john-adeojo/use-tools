class ToolBox:
    def __init__(self):
        self.tools_dict = {}

    def store(self, functions_list):
        """
        Stores the literal name and docstring of each function in the list.

        Parameters:
        functions_list (list): List of function objects to store.

        Returns:
        dict: Dictionary with function names as keys and their docstrings as values.
        """
        for func in functions_list:
            self.tools_dict[func.__name__] = func.__doc__
        return self.tools_dict

    def tools(self):
        """
        Returns the dictionary created in store as a text string.

        Returns:
        str: Dictionary of stored functions and their docstrings as a text string.
        """
        tools_str = ""
        for name, doc in self.tools_dict.items():
            tools_str += f"{name}: \"{doc}\"\n"
        return tools_str.strip()