import os

def get_filenames():
    all_files = os.listdir()
    matching = [file for file in all_files if file.startswith('weekly_attendance_')]
    return matching
