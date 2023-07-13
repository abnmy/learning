from inspect import getmembers, isfunction
from pathlib import Path
from string import Template
from timeit import timeit


def loop(functions_list, stmt_tmpl, setup_tmpl, number):
    # Run
    results = []
    for function_name, _ in functions_list:
        stmt = stmt_tmpl.safe_substitute(dict(f=function_name))
        setup = setup_tmpl.safe_substitute(dict(f=function_name))
        elapsed_time = timeit(stmt, setup, number=number)
        results.append((function_name, elapsed_time))

    # Display
    for function, elapsed_time in sorted(results, key=lambda n:n[1]):
        print("time %s: %.3f seconds" % (function, elapsed_time))


if __name__ == "__main__":

    for module_name in filter(Path.is_file, Path(".").glob("speed*.py")):
        print(">>", module_name)
        speed_module = __import__(module_name.stem)

        loop(
            getmembers(speed_module, isfunction), 
            Template(speed_module.STMT_TMPL), 
            Template(f"from {module_name.stem} import $f"), 
            speed_module.ITERATION
        )
