import sys
import subprocess
# Delete this maybe 
def main():
    command = [sys.executable, "-m", "deepeval"] + sys.argv[1:]
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

if __name__ == "__main__":
    main()
