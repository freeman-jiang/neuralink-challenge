import os
import wave

# Get list of WAV files in data folder
data_folder = 'data'
wav_files = [f for f in os.listdir(data_folder) if f.endswith('.wav')]

# Print number of files
print(f"Number of WAV files: {len(wav_files)}")

wav_file = wav_files[0]

# read byte by byte
file_path = os.path.join(data_folder, wav_file)
with open(file_path, 'rb') as file:
    file.seek(24)  # Set position to byte 25 (0-indexed)
    raw_bytes = file.read(4)  # Read 4 bytes (25-28)
    raw_number = int.from_bytes(raw_bytes, byteorder='little', signed=False)
    print(raw_number)


# all_numbers = []

# # Read raw bytes from all WAV files and collect all numbers
# for wav_file_name in wav_files:
#     file_path = os.path.join(data_folder, wav_file_name)
#     with wave.open(file_path, 'rb') as wav_file:
#         raw_bytes = wav_file.readframes(wav_file.getnframes())
#         all_numbers.extend(list(raw_bytes))
#         print(wav_file_name)

# # Find the max and min of all the numbers
# max_number = max(all_numbers)
# min_number = min(all_numbers)

# # Print the max and min numbers
# print(f"Max number: {max_number}")
# print(f"Min number: {min_number}")
