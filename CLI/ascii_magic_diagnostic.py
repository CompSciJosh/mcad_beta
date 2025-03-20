import ascii_magic
import inspect

# Print the module's functions and their parameters
print("Available functions in ascii_magic:")
for name, func in inspect.getmembers(ascii_magic, inspect.isfunction):
    print(f"- {name}{inspect.signature(func)}")

# Check if there's an AsciiArt class
if hasattr(ascii_magic, 'AsciiArt'):
    print("\nAsciiArt class methods:")
    for name, method in inspect.getmembers(ascii_magic.AsciiArt, inspect.isfunction):
        if not name.startswith('_'):  # Skip private methods
            print(f"- {name}{inspect.signature(method)}")