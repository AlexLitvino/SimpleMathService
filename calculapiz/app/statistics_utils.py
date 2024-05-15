"""This module contains utilities functions to work with statistics"""
import csv


def log_statistics(stat_file_path, stat_data):
    with open(stat_file_path, 'a') as csv_file:
        csw_writer = csv.writer(csv_file)
        csw_writer.writerow(stat_data)
