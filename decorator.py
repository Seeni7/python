def output_decorator(f):
    def f_(f):
        f()
        print("Ran f....")
        return f_
