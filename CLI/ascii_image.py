"""
Joshua Jackson
March 18, 2025,
ASCII Art for MCAD Command Line Interface
input: joshuajackson@VackSealed-MacBook-Air mcad_beta % source .venv/bin/activate
result: (.venv) joshuajackson@VackSealed-MacBook-Air mcad_beta %
"""
###################################
##### Output ASCII NASA Image #####
###################################
# import os
# import ascii_magic
#
# # Define the absolute path to the image
# image_path = os.path.expanduser("~/PycharmProjects/mcad_beta/app/frontend/nasa_logo.png")
#
# # Make sure the file exists before proceeding
# if not os.path.exists(image_path):
#     print(f"Error: Image not found at {image_path}")
#     exit(1)
#
# # First create the ASCII art object
# output = ascii_magic.from_image(image_path)
#
# # Then adjust size when displaying to terminal
# output.to_terminal(
#     columns=130,         # Width in characters (default is 120)
#     width_ratio=3.0,     # Adjusts the character aspect ratio (default is 2.2)
# )


##########################################
#### Output and Save ASCII NASA Image ####
###### Run With cat In The Terminal ######
##########################################
import os
import ascii_magic

# Define the absolute path to the image
image_path = os.path.expanduser("~/PycharmProjects/mcad_beta/app/frontend/mcad_nasa.png") # Input File
output_file_path = os.path.expanduser("~/PycharmProjects/mcad_beta/app/frontend/mcad_nasa_colored.txt") # Output File

# Make sure the file exists before proceeding
if not os.path.exists(image_path):
    print(f"Error: Image not found at {image_path}")
    exit(1)

# First create the ASCII art object
output = ascii_magic.from_image(image_path)

# Save to file with ANSI color codes - pass the path directly, not a file object
output.to_file(output_file_path, columns=240, width_ratio=2.3) # 👈🏾That's it Boss 👍🏾✅

# Also display in terminal (optional)
output.to_terminal(
    columns=200,         # Width in characters (Note: default is 120)
    width_ratio=2.0,     # Adjusts the character aspect ratio (Note: default is 2.2)
)

print(f"\nColored ASCII art saved location: {output_file_path}")
