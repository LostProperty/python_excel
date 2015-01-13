# -*- encoding: utf-8 -*-
import xlsxwriter

from django.core.management.base import BaseCommand

from ...models import Job


class Command(BaseCommand):

    option_list = BaseCommand.option_list
    help = 'Generate Excel File for user to populate'

    def handle(self, *args, **options):
        filename = 'staff.xlsx'
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()

        # NOTE: you could introspect the staff model here to get the fields
        worksheet.write(0, 0, 'Title')
        worksheet.write(0, 1, 'First Name')
        worksheet.write(0, 2, 'Surname')
        worksheet.write(0, 3, 'Job')

        input_rows = 10
        title_list = ['Mr', 'Ms', 'Miss', 'Mrs']
        worksheet.data_validation(1, 0, input_rows, 0,
            {'validate': 'list',
            'input_title': 'Select value',
            'source': title_list})

        firstname_max_length = 20
        worksheet.data_validation(1, 1, input_rows, 1,
            {'validate': 'length',
            'input_title': 'Enter value',
            'criteria': '<',
            'value': firstname_max_length,
            'error_message': 'Max Length is {0}'.format(firstname_max_length)})

        surname_max_length = 20
        worksheet.data_validation(1, 2, input_rows, 2,
            {'validate': 'length',
            'input_title': 'Enter value',
            'criteria': '<',
            'value': surname_max_length,
            'error_message': 'Max Length is {0}'.format(surname_max_length)})

        job_list = list(Job.objects.values_list('title', flat=True))
        worksheet.data_validation(1, 3, input_rows, 3,
            {'validate': 'list',
            'input_title': 'Select value',
            'source': job_list})

        workbook.close()
        self.stdout.write('File {0} created'.format(filename))
