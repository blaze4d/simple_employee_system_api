"""Helper utility"""

from .models import Employee
from datetime import datetime

# def co
class Converter:
    """Class for performing common conversions/transformtions
    
    """
    def employee_to_archive(emp: Employee):
        """Converter class to convert the Employee object to archive dict

        Parameters
        ----------
        emp : Employee
            The Employee object to be converted

        Returns
        -------
        dict
            A dict representation of EmployeeArchive 
        """
        
        print(emp)
        archive = {
            "first_name": emp.first_name,
            "last_name": emp.last_name,
            "date_employed": emp.date_employed,
            "salary_level": emp.salary_level,
            "department": emp.department,
            "last_promotion_date": emp.last_promotion_date,
            "archive_date": datetime.now()
        }
        print(archive)

        return archive