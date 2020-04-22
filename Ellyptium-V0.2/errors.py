from os import sys
def launch_error(*args):
    try:
        raise Exception

    except Exception:
        lines = ""
        for a in args:
            lines += a
            lines += "\n"
        
        print(lines)
        sys.exit()