"""
Cobra | Module.py

Module type class for dealing with module imports
"""

class Module(object):
    def __init__(self, name, **kwargs):
        for i in kwargs.keys(): # Detect if 
            if i == "requiredFunctions":
                self.fromImport = True
                self.funcs = kwargs[i]
        
        self.name = name # Module Name

    def get_function(self, name):
        if self.fromImport:
            if name not in self.funcs:
                raise Exception(f'Function "{name}" was never imported from "{self.name}"')