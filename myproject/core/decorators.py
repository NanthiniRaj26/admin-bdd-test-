import time

class LogExecutionTime:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.perf_counter()
        result = self.func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Method '{self.func.__name__}' executed in {execution_time:.4f} seconds.")
        return result

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return type(self)(self.func.__get__(instance, owner))
