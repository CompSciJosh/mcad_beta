# Joshua Jackson
# Senior Design Spring '25: Multiscale Crater Analysis and Detection (MCAD)
# February 13, 2025

##########################################################
######### ✅Upload PNG files to the Internal Stage #######
##########################################################
import snowflake.connector
import os

# Establish the connection to Snowflake
conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse="JAMS_WH",
    database="JAMS_DB",
    schema="JAMS"
)
cur = conn.cursor()

# Set database and schema
# cur.execute("USE DATABASE JAMS_DB;") # Old DB
# cur.execute("USE SCHEMA JAMS;") # Old Schema

# Path where PNG files are stored
data_folder = "/Users/joshuajackson/Downloads/mcad_moon_data"

# Upload PNG files to Snowflake with unique subfolder paths
for root, _, files in os.walk(data_folder):
    subfolder_name = os.path.basename(root)  # Extract folder name (000, 001, ..., 275)

    for file in files:
        if file.endswith(".png"):  # Upload only PNG files
            file_path = os.path.join(root, file)
            stage_file_path = f"@original_png_internal_stage/{subfolder_name}"  # Unique path

            # Debugging prints
            print(f"Uploading: {file_path} --> {stage_file_path}")

            stage_command = f"PUT file://{file_path} {stage_file_path} AUTO_COMPRESS=FALSE"

            try:
                cur.execute(stage_command)
                print(f"Uploaded: {file} to {stage_file_path}")
            except snowflake.connector.errors.ProgrammingError as e:
                print(f"Error uploading {file}: {e}")

print("✅ All PNG files uploaded to Snowflake Internal Stage!")

conn.commit()
cur.close()
conn.close()


##############################################################################
############### No Longer Needed - PNG-JSON Dictionary Mapping ###############
######################## Updated Code Used At Top ############################
##############################################################################
# import os
# import snowflake.connector
# from collections import defaultdict
#
# # Define the path where extracted files are stored
# data_folder = "/Users/joshuajackson/Downloads/mcad_moon_data"
#
# # Dictionary to store PNG -> JSON mapping
# png_to_json_mapping = defaultdict(str)
#
# # Iterate through all folders
# for root, _, files in os.walk(data_folder):
#     json_files = {file.replace(".json", ""): file for file in files if file.lower().endswith(".json")}
#
#     for file in files:
#         if file.lower().endswith(".png"):
#             base_name = file.replace(".png", "")
#             if base_name in json_files:
#                 # Use full path to ensure uniqueness
#                 png_to_json_mapping[os.path.join(root, file)] = os.path.join(root, json_files[base_name])
#
# # Debugging: Print first 20 mappings
# print("\nFirst 20 mappings:")
# for i, (png, json_file) in enumerate(png_to_json_mapping.items()):
#     if i < 20:
#         print(f"PNG: {png} -> JSON: {json_file}")
#
# print(f"\nTotal mappings created: {len(png_to_json_mapping)}")

#######################################################################
######## 👇🏾👉🏾✅ Upload JSON files to the Internal Stage ✅👈🏾👇🏾 #######
########################################################################
# import snowflake.connector
# import os
#
# # Establish the connection to Snowflake
# conn = snowflake.connector.connect(
#     user=os.getenv("SNOWFLAKE_USER"),
#     password=os.getenv("SNOWFLAKE_PASSWORD"),
#     account=os.getenv("SNOWFLAKE_ACCOUNT"),
#     warehouse="JAMS_WH",
#     database="JAMS_DB",
#     schema="JAMS"
# )
# cur = conn.cursor()
#
# # Set database and schema
# # These lines are redundant
# # cur.execute("USE DATABASE JAMS_DB;")
# # cur.execute("USE SCHEMA JAMS;")
#
# # Path where JSON files are stored
# data_folder = "/Users/joshuajackson/Downloads/mcad_moon_data"
#
# # Upload JSON files to Snowflake with unique subfolder paths
# for root, _, files in os.walk(data_folder):
#     subfolder_name = os.path.basename(root)  # Extract folder name (000, 001, ..., 275)
#
#     for file in files:
#         if file.endswith(".json"):
#             file_path = os.path.join(root, file)
#             stage_file_path = f"@original_json_internal_stage/{subfolder_name}"  # Unique path
#
#            # Debugging prints
#             print(f"Uploading: {file_path} --> {stage_file_path}")
#
#             stage_command = f"PUT file://{file_path} {stage_file_path} AUTO_COMPRESS=FALSE" # Changed from TRUE to FALSE
#
#             try:
#                 cur.execute(stage_command)
#                 print(f"Uploaded: {file} to {stage_file_path}")
#             except snowflake.connector.errors.ProgrammingError as e:
#                 print(f"Error uploading {file}: {e}")
#
# print("👍🏾🚀All JSON files uploaded correctly to Snowflake Internal Stage!👍🏾🚀")
#
# conn.commit()
# cur.close()
# conn.close()

#####################################
###### For uploading JSON files #####
#### Below is for reference only ####
#####################################
# import snowflake.connector
# import os
#
# # Establish connection
# conn = snowflake.connector.connect(
#     user=os.getenv("SNOWFLAKE_USER"),
#     password=os.getenv("SNOWFLAKE_PASSWORD"),
#     account=os.getenv("SNOWFLAKE_ACCOUNT"),
#     warehouse="JAMS_WH",
#     database="JAMS_DB",
#     schema="JAMS"
# )
# cur = conn.cursor()
#
# # Set database and schema
# These lines are redundant
# cur.execute("USE DATABASE JAMS_DB;")
# cur.execute("USE SCHEMA JAMS;")
#
# # Path where JSON files are stored
# data_folder = "/Users/joshuajackson/Downloads/mcad_moon_data"
#
# # Upload JSON files to Snowflake
# for root, _, files in os.walk(data_folder):
#     subfolder_name = os.path.basename(root)  # Extracts "000", "001", etc.
#
#     for file in files:
#         if file.endswith(".json"):
#             # file_name = os.path.basename(file)  # Ensure only filename (this is an extra, ut unused variable)
#             file_path = os.path.join(root, file)
#
#             # EXPLICITLY define the target as a file
#             stage_file_path = f"@original_json_internal_stage/{subfolder_name}"
#
#             # Debugging prints
#             print(f"Uploading: {file_path} --> {stage_file_path}")
#
#             # Modified PUT command (explicitly treating as a file)
#             stage_command = f"PUT file://{file_path} {stage_file_path} AUTO_COMPRESS=FALSE"
#
#             try:
#                 cur.execute(stage_command)
#                 print(f"Uploaded: {file} to {stage_file_path}")
#             except snowflake.connector.errors.ProgrammingError as e:
#                 print(f"Error uploading {file}: {e}")
#
# print("All JSON files uploaded correctly to Snowflake Internal Stage!")
#
# conn.commit()
# cur.close()
# conn.close()


##############################################################################
######### No Longer Needed - Insert PNG-JSON Mappings Into Snowflake #########
######################## Updated Code Used At Top ############################
##############################################################################
# conn = snowflake.connector.connect(
#     user="",
#     password="",
#     account="",
#     warehouse="",
#     database="",
#     schema=""
# )
# cur = conn.cursor()
#
# # Insert PNG-JSON mappings
# for png, json_file in png_to_json_mapping.items():
#     sql_query = f"""
#         INSERT INTO MCAD.MCAD_DATA.PNG_JSON_MAPPING (PNG_FILE, JSON_FILE)
#         VALUES ('{png}', '{json_file}')
#     """
#     try:
#         cur.execute(sql_query)
#     except snowflake.connector.errors.ProgrammingError as e:
#         print(f"Error inserting {png}, {json_file}: {e}")
#
# conn.commit()
# cur.close()
# conn.close()
#
# print("PNG-JSON mapping successfully stored in Snowflake!")

#####################################################################
####### 🤔Updated - Insert PNG-JSON Mappings Into Snowflake #########
#####################################################################

# import os
# import snowflake.connector
# import json
# from collections import defaultdict
#
# # Connect to Snowflake using environment variables
# conn = snowflake.connector.connect(
#     user=os.getenv("SNOWFLAKE_USER"),
#     password=os.getenv("SNOWFLAKE_PASSWORD"),
#     account=os.getenv("SNOWFLAKE_ACCOUNT"),
#     warehouse="mcad_warehouse",
#     database='MCAD',
#     schema='mcad_data'
# )
# cur = conn.cursor()
#
# # Define the path where extracted files are stored
# data_folder = "/Users/joshuajackson/Downloads/mcad_moon_data"
#
# # Dictionary to store PNG -> JSON mapping
# png_to_json_mapping = defaultdict(str)
#
# # Iterate through all folders and create mappings
# for root, _, files in os.walk(data_folder):
#     subfolder_name = os.path.basename(root)  # Extracts folder name (e.g., "001")
#
#     json_files = {file.replace(".json", ""): os.path.join(root, file) for file in files if file.lower().endswith(".json")}
#
#     for file in files:
#         if file.lower().endswith(".png"):
#             base_name = file.replace(".png", "")
#             if base_name in json_files:
#                 png_to_json_mapping[f"{subfolder_name}/{file}"] = json_files[base_name]
#
# # Insert JSON data into MOON_CRATER_DATA with PNG mapping
# for png_file, json_path in png_to_json_mapping.items():
#     try:
#         # Read JSON file contents
#         with open(json_path, "r") as f:
#             json_data = json.load(f)
#
#         # Extract JSON values with NULL as default for missing keys
#         # Snowflake can later reconvert these into arrays using PARSE_JSON(column_name)
#         time_in_seconds = json_data.get("Time (s)", None)
#         sun_los = json.dumps(json_data.get("SUN LoS", None)) # Convert to string
#         cam_pos_in_meters = json.dumps(json_data.get("Cam Pos (m)", None)) # Convert to string
#         cam_quat_scalar = json_data.get("Cam Quat (s)", None)  # s - Scalar
#         cam_quat_vector = json.dumps(json_data.get("Cam Quat (v)", None))  # v - Vector ... Convert to string
#         cam_los = json.dumps(json_data.get("Cam LoS", None)) # Convert to string
#         fov_x_rads = json_data.get("FOV X (rad)", None)
#         fov_y_rads = json_data.get("FOV Y (rad)", None)
#         nrows_cam_snsr = json_data.get("Nrows", None)
#         ncols_cam_snsr = json_data.get("Ncols", None)
#
#         # SQL Insert Statement (Parameterized)
#         sql_query = """
#             INSERT INTO MCAD.MCAD_DATA.MOON_CRATER_DATA
#             ("Time (s)", "SUN LoS", "Cam Pos (m)", "Cam Quat (s)", "Cam Quat (v)", "Cam LoS",
#              "FOV X (rad)", "FOV Y (rad)", "Nrows", "Ncols", "PNG File")
#             SELECT (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#             WHERE NOT EXISTS (
#                 SELECT 1 FROM MCAD.MCAD_DATA.MOON_CRATER_DATA WHERE "PNG File" = %s
#             )
#         """
#
#         # Execute Insert
#         cur.execute(sql_query, (
#             time_in_seconds, sun_los, cam_pos_in_meters, cam_quat_scalar, cam_quat_vector,
#             cam_los, fov_x_rads, fov_y_rads, nrows_cam_snsr, ncols_cam_snsr, png_file
#         ))
#
#     except snowflake.connector.errors.ProgrammingError as e:
#         print(f"Error inserting {json_path}: {e}")
#
# # Commit and Close Connection
# conn.commit()
# cur.close()
# conn.close()
#
# print("👍🏾🚀PNG-JSON mapping successfully stored in Snowflake!🚀👍🏾")

##################################################################################
############################# 🎉🚀Step Updated 🎉🚀 #############################
################## Avoids duplicates using the WHERE NOT EXISTS ##################
########### 👍🏾Insert JSON data into MOON_CRATER_DATA with PNG mapping 👍🏾##########
###################################################################################
# import os
# import snowflake.connector
# import json
# from collections import defaultdict
#
# # Connect to Snowflake using environment variables
# conn = snowflake.connector.connect(
#     user=os.getenv("SNOWFLAKE_USER"),
#     password=os.getenv("SNOWFLAKE_PASSWORD"),
#     account=os.getenv("SNOWFLAKE_ACCOUNT"),
#     warehouse="JAMS_WH",
#     database="JAMS_DB",
#     schema="JAMS"
# )
# cur = conn.cursor()
#
# # Define the path where extracted files are stored
# data_folder = "/Users/joshuajackson/Downloads/mcad_moon_data"
#
# # Dictionary to store PNG -> JSON mapping
# png_to_json_mapping = defaultdict(str)
#
# # Iterate through all folders and create mappings
# for root, _, files in os.walk(data_folder):
#     subfolder_name = os.path.basename(root)  # Extracts folder name (e.g., "001")
#
#     json_files = {file.replace(".json", ""): os.path.join(root, file) for file in files if file.lower().endswith(".json")}
#
#     for file in files:
#         if file.lower().endswith(".png"):
#             base_name = file.replace(".png", "")
#             if base_name in json_files:
#                 png_to_json_mapping[f"{subfolder_name}/{file}"] = json_files[base_name]
#
# # Insert JSON data into MOON_CRATER_DATA with PNG mapping
# for png_file, json_path in png_to_json_mapping.items():
#     try:
#         # Read JSON file contents
#         with open(json_path, "r") as f:
#             json_data = json.load(f)
#
#         # Extract JSON values with NULL as default for missing keys
#         # Snowflake can later reconvert these into arrays using PARSE_JSON(column_name)
#         time_in_seconds = json_data.get("Time (s)", None)
#         sun_los = json.dumps(json_data.get("SUN LoS", None)) # Convert to string
#         cam_pos_in_meters = json.dumps(json_data.get("Cam Pos (m)", None)) # Convert to string
#         cam_quat_scalar = json_data.get("Cam Quat (s)", None)  # s - Scalar
#         cam_quat_vector = json.dumps(json_data.get("Cam Quat (v)", None))  # v - Vector ... Convert to string
#         cam_los = json.dumps(json_data.get("Cam LoS", None)) # Convert to string
#         fov_x_rads = json_data.get("FOV X (rad)", None)
#         fov_y_rads = json_data.get("FOV Y (rad)", None)
#         nrows_cam_snsr = json_data.get("Nrows", None)
#         ncols_cam_snsr = json_data.get("Ncols", None)
#
#         # SQL Insert Statement with WHERE NOT EXISTS to prevent duplicates
#         sql_query = """
#             INSERT INTO JAMS_DB.JAMS.MOON_CRATER_DATA
#             ("Time (s)", "SUN LoS", "Cam Pos (m)", "Cam Quat (s)", "Cam Quat (v)", "Cam LoS",
#              "FOV X (rad)", "FOV Y (rad)", "Nrows", "Ncols", "PNG File")
#             SELECT %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
#             WHERE NOT EXISTS (
#                 SELECT 1 FROM JAMS_DB.JAMS.MOON_CRATER_DATA WHERE "PNG File" = %s
#             )
#         """
#
#         # Execute Insert
#         cur.execute(sql_query, (
#             time_in_seconds, sun_los, cam_pos_in_meters, cam_quat_scalar, cam_quat_vector,
#             cam_los, fov_x_rads, fov_y_rads, nrows_cam_snsr, ncols_cam_snsr, png_file, png_file
#         ))
#
#         # Check if any row was inserted (cur.rowcount will be 0 if the file already exists)
#         if cur.rowcount > 0:
#             print(f"Inserted: {png_file}")
#         else:
#             print(f"Skipped duplicate: {png_file}")
#
#     except snowflake.connector.errors.ProgrammingError as e:
#         print(f"Error inserting {png_file}: {e}")
#
# # Commit and Close Connection
# conn.commit()
# cur.close()
# conn.close()
#
# print("👍🏾🚀 PNG-JSON mapping successfully stored in Snowflake! 🚀👍🏾")
