import typer, os
import re

def getAllBytesInFile(filepath: str):
    return os.path.getsize(filepath)

def getAllLinesInFile(filepath: str):
    try:
        with open(filepath, "r") as fp:
            return sum(1 for line in fp)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        exit(1)
    except PermissionError:
        print(f"Error: You do not have permission to access '{filepath}'.")
        exit(1)

def getAllWordsInFile(filepath: str):
    try:
        with open(filepath, "r") as fp:
            return len(re.findall(r'\S+', fp.read()))
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        exit(1)
    except PermissionError:
        print(f"Error: You do not have permission to access '{filepath}'.")
        exit(1)

def getAllCharactersInFile(filepath: str):
    try:
        with open(filepath, "r") as fp:
            return sum(len(line) for line in fp)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        exit(1)
    except PermissionError:
        print(f"Error: You do not have permission to access '{filepath}'.")
        exit(1)

def main(filepath: str, c: bool = False, l: bool = False, w: bool = False, m: bool = False):
    if not c and not l and not w and not m:
        print(f"{getAllBytesInFile(filepath)} {getAllLinesInFile(filepath)} {getAllWordsInFile(filepath)} {filepath.rsplit('/',1)[-1]}")
    else:
        if(c):
            print(getAllBytesInFile(filepath))
        if(l):
            print(getAllLinesInFile(filepath))
        if(w):
            print(getAllWordsInFile(filepath))
        if(m):
            print(getAllCharactersInFile(filepath))

if __name__ == "__main__":
    typer.run(main)