from models.conversor import Conversor
import sys

if __name__ == "__main__":
    conversor = Conversor()
    if len(sys.argv) != 2:
        print(f'Usage: youtube2mp3 <file-path>')
    conversor.install_from_file(sys.argv[1])