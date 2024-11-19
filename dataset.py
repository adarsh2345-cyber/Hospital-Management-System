import csv

# Data for the Patients table
patients = [
    ["Patient_ID", "Name", "Age", "Gender", "Address", "Contact_No", "Email", "Blood_Type", "Emergency_Contact"],
    ["P001", "John Doe", 34, "Male", "123 Main St, City, Country", "123-4567890", "john.doe@email.com", "O+", "987-6543210"],
    ["P002", "Jane Smith", 27, "Female", "456 Oak St, City, Country", "987-6543210", "jane.smith@email.com", "A+", "654-3219870"]
]

# Write to CSV
with open('patients.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(patients)
