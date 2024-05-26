from typing import BinaryIO


class WAVFile:
    def __init__(self, file: BinaryIO):
        self.file = file

    def sample_rate(self) -> int:
        self.file.seek(24)  # Set position to byte 25 (0-indexed)
        raw_bytes = self.file.read(4)  # Read 4 bytes (25-28)
        raw_number = int.from_bytes(
            raw_bytes, byteorder='little', signed=False)
        return raw_number

    def bits_per_sample(self) -> int:
        self.file.seek(34)  # Set position to byte 35 (0-indexed)
        raw_bytes = self.file.read(2)  # Read 2 bytes (35-36)
        raw_number = int.from_bytes(
            raw_bytes, byteorder='little', signed=False)
        return raw_number

    def size_of_data(self) -> int:
        self.file.seek(40)  # Set position to byte 41 (0-indexed)
        raw_bytes = self.file.read(4)  # Read 4 bytes (41-44)
        raw_number = int.from_bytes(
            raw_bytes, byteorder='little', signed=False)
        return raw_number
