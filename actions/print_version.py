from st2actions.runners.pythonrunner import Action

__all__ = [
    'PrintVersionAction'
]


class PrintVersionAction(Action):
    def run(self, data):
        version = 'v0.10.0'
        print version
        return version
