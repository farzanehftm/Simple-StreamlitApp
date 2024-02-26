import os
import sys

from setting import FILES_DIR


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        print(f'Opening file: {filename}')
        os.system("start excel " + os.path.join(FILES_DIR, filename))
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")


if __name__ == "__main__":
    main()
