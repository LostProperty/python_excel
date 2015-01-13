# Python Excel

Example project to show how to use Python to generate excel template to bulk import data.

## Installation
```
pip install -r requirements.txt
```

### Create your Database
```
createuser python_excel
psql -c "CREATE DATABASE python_excel WITH OWNER python_excel ENCODING 'UTF8'"
```
This assumes you're using PostgreSQL for your DB. This technique should work for other databases but you'll have to edit the settings.

### Run Migrations
```
cd python_excel
python manage.py migrate
```
I've added a data migration to populate the job titles and one member of staff.

### Create Super User for Admin
```
cd python_excel
python manage.py createsuperuser
```

## Create Excel File
```
cd python_excel
python manage.py generate_excel_file
```

# Import Excel Data
```
cd python_excel
python manage.py import_excel_file staff_populated.xlsx
```
