from models import Usage
from base_manager import BaseManager


name = 'lesson6_orm\example.db'


BaseManager.set_connection(db_name = name)

employees = Usage.objects.select('salary', 'grade')  # employees: List[Employee]
print(employees)
employees = Usage.objects.select('first_name', 'last_name', 'salary', 'grade')  # employees: List[Employee]

print(f"First select result:\n {employees} \n")


# SQL: INSERT INTO employees (first_name, last_name, salary)
#  	VALUES ('Yan', 'KIKI', 10000), ('Yoweri', 'ALOH', 15000);
employees_data = [
    {"first_name": "Yan", "last_name": "KIKI", "salary": 10000},
    {"first_name": "Yoweri", "last_name": "ALOH", "salary": 15000}
]
Usage.objects.insert(rows=employees_data)

employees = Usage.objects.select('first_name', 'last_name', 'salary', 'grade')
print(f"Select result after bulk insert:\n {employees} \n")


# SQL: UPDATE employees SET salary = 17000, grade = 'L2';
Usage.objects.update(
    new_data={'salary': 17000, 'grade': 'L2'}
)

employees = Usage.objects.select('first_name', 'last_name', 'salary', 'grade')
print(f"Select result after update:\n {employees} \n")


# SQL: DELETE FROM employees;
# Usage.objects.delete()

employees = Usage.objects.select('first_name', 'last_name', 'salary', 'grade')
print(f"Select result after delete:\n {employees} \n")
