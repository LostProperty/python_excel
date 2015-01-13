# Python Excel

Example project to show how to use Python to generate excel template to bulk import data.

## Installation

pip install -r requirements.txt

### Create your Database
```
createuser python_excel
psql -c "CREATE DATABASE python_excel WITH OWNER python_excel ENCODING 'UTF8'"
```

### Run Migrations
```
cd python_excel
python manage.py migrate
```

### Create Super user for Admin
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
