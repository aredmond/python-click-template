class cli_global_class():

    def __init__(self, global_constructor_param):
        self.global_value = global_constructor_param

    def print_global(self):
        print(self.global_value)