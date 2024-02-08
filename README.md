Sure, here's the updated README file for your Django CRM app repository:

---

# DCRM - Django CRM App

## Description
DCRM is a Django-based customer relationship management (CRM) app developed to demonstrate how to build a fully-functional CRM application using Django, Python, and MySQL.

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/harsh721827/DCRM.git
```

### 2. Install Dependencies
Navigate to the project directory and install the required dependencies using pip:
```bash
cd DCRM
pip install -r requirements.txt
```

### 3. Database Configuration
Set up the MySQL database according to the instructions provided.

### 4. Configure Django Settings
Update the database settings in `DCRM/settings.py` to connect to your MySQL database.

### 5. Run Migrations
Run the Django migrations to create the necessary database tables:
```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)
You can create a superuser to access the Django admin interface:
```bash
python manage.py createsuperuser
```
Follow the prompts to create a superuser account.

### 7. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

### 8. Access the CRM App
Open your web browser and navigate to the following URL to access the CRM app:
```
http://127.0.0.1:8000/
```

## Usage
Once the setup is complete, you can use the CRM app to perform various tasks related to customer relationship management, including registering users, adding records, viewing records, updating records, and deleting records.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- 
