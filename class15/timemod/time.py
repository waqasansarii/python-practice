import time

class Timer:
    def __init__(self,func) -> None:
        self.func = func
        
    def __call__(self,*arg,**kwargs ) -> None:
        start = time.perf_counter()
        result = self.func(*arg,**kwargs)
        end = time.perf_counter()
        print(f'function {self.func.__name__} took {end - start} seconds')
        print(result, **kwargs)
        return result