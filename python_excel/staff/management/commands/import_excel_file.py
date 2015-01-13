# -*- encoding: utf-8 -*-
from openpyxl import load_workbook

from django.core.management.base import BaseCommand

from ...models import Staff, Job


class Command(BaseCommand):

    option_list = BaseCommand.option_list
    help = 'Import Excel File into the database'

    def handle(self, *args, **options):
        rows = get_excel_data(args[0])
        save_staff(rows)
        self.stdout.write('{0} members of staff created'.format(len(rows)))


def get_excel_data(excel_file, first_data_row=1):
        """
        Convert Excel data into simple Python data types
        Note: openpyxl counts rows from 0. Excel counts rows from 1
        """
        workbook = load_workbook(filename=excel_file)
        worksheet_rows = list(workbook.worksheets[0].rows)
        rows = []
        for row_number, row in enumerate(worksheet_rows):
            if row_number < first_data_row:
                continue
            rows.append([cell.value for cell in row])
        return rows


def save_staff(rows):
    """
    Save the staff to the database
    """
    for row in rows:
        employee = Staff()
        employee.title = row[0]
        employee.first_name = row[1]
        employee.surname = row[2]
        employee.job = Job.objects.get(title=row[3])
        employee.save()
