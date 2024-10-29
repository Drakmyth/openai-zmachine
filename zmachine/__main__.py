import sys
from builder import ZMachineBuilder
from dotenv import load_dotenv

def main():
    load_dotenv()
    builder = ZMachineBuilder(sys.argv[1])
    builder.start()


if __name__ == '__main__':
    main()
