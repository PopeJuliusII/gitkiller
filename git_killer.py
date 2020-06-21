import os
from contextlib import contextmanager


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


if __name__ == "__main__":
    root = os.path.dirname(os.path.abspath(__file__))
    for item in os.listdir(root):
        path = os.path.join(root, item)
        if os.path.isdir(path):
            with change_dir(path):
                replace = f"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}"
                try:
                    os.system('rm -rf .git .gitignore')
                    print(f'Git files removed from {path.replace(replace, "..")}.')
                except Exception:
                    print(Exception)
