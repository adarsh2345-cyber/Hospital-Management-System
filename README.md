# Hospital-Management-System

PROJECT OBJECTIVE

The goal of this project is to automate hospital front-office operations, making processes simpler, 
faster, and more cost-effective. It manages tasks such as patient registration, diagnosis recording,
staff management, and appointment scheduling.
The system is secured with role-based access, ensuring only administrators or receptionists can 
interact with sensitive data.This improves security and speeds up data processing.


____________________________________________

# SOFTWARE REQUIREMENTS

1.Frontend: Tkinter

2.Backend: Python

3.Database: SQLite (DB Browser)


____________________________________________

# FEATURES

1.User Authentication: Secure login with role-based access.

2.Patient Management: Easily register, update, and retrieve patient information.

3.Staff Management: Record and organize staff details.

4.Room Allocation

5.Appointment Booking: Schedule, search, and update appointments seamlessly.

6.Billing System: Generate and update patient bills.

____________________________________________

# USE CASES

### Use Cases

| **Use Case**          | **Actor**           | **Outcome**                                                    |
|------------------------|---------------------|----------------------------------------------------------------|
| **Login**             | Admin, Receptionist | Secure access to the system. Role-based access to features.    |
| **Patient Registration** | Admin, Receptionist | Add, update, delete, and retrieve patient details.             |
| **Book Appointment**  | Receptionist, Patient | Schedule, reschedule, or cancel appointments with doctors.     |
| **Assign Room**       | Admin               | Efficient allocation and tracking of room availability.        |
| **Generate Bill**     | Admin               | Create and manage accurate patient bills.                      |
| **View Records**      | Admin, Receptionist, Patient | Access relevant records: Admin (all data), Receptionist (operational data), Patient (personal data). |


# OUTPUTS:
1. If username and password is valid.
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/54250cb5837ec40095a79558d5f69359db89712f/login-1.jpg) 

2.If username and password are invalid. 
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/7bfa0c9770d834ee44acfb1dad07be4687350fc5/login-2.jpg) 

3. MENU

![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/8fc6aa235c0218df55db5bc7ed03c5d53088c6b9/menu.jpg)

4.Patient Registration Form

Patient Registration-SUBMIT
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/98e44a9a552a2880c35ab257d10d310aebb6d09c/pat-reg-1.jpg) 

Patient Registration- Update 
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/3b418cbb6f864c6379a1988bd2d5d4cedf4261b8/Images/pat-reg-2.jpg) 

Patient Registration-Search 
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/22455dacb12354ad46bb7039e35e04e36ef6ca7d/Images/pat-reg-3.jpg) 

Patient Registration-Delete 
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/0c4af8a1e9be1b97dd33853a38e700e4fb4ff8c1/Images/pat-reg-4.jpg) 


# Room Allocation 

Submit 

![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/b292d2334ad721c8f292adf1391805cd981e2d3e/Images/room-alloc-1.jpg) 

Update 

![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/205b9fdac7ca00cce4b28012466aa2d340fcfd95/Images/room-alloc-2.jpg) 

Room Details 
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/6ed68d408cf51136f244508a9964c9859587322f/Images/room-alloc-3.jpg) 

# Employee Registration 

Save 

![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/b3f13fc76b7d90b4ef4946b4208fcedc66fffc26/Images/emp-reg-1.jpg) 

Delete

![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/e147c7209f434f055fceaea4975d5345f7186541/Images/emp-reg-2.jpg) 

# Book Appointment 
Save 
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/c1899b50b97c3c4c33e1337119e28b770e15004f/Images/book-app-1.jpg) 

Delete
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/ae158cca375dcd5c16f4a2870daf87049232d747/Images/book-app-2.jpg) 

Search Appointment
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/ad4b0374c9dbbf6a8316bba4a33910a471fb1d96/Images/book-app-3.jpg) 

# Patient Bill

Update Data 
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/c92d45c175dc79e751f39564201532b51bcdbaaa/Images/pat-bill-1.jpg) 

Discharge Date 
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/28afc15f3a1a63e0dbfcb11c3825e8b18154dae3/Images/pat-bill-2.jpg) 

Generate Bill 
![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/cb27d267607acb28ff03564edd8ecbbdbcdf8926/Images/pat-bill-3.jpg) 


# HOW TO RUN

1. Clone the repository:

git clone
https://github.com/adarsh2345-cyber/Hospital-Management-System.git  
cd Hospital-Management-System

2. Install dependencies:

pip install -r requirements.txt


3. Run the application:

python main.py


# DATASET 

## 1. Patients Dataset

This dataset stores information about the patients.

| Patient_ID | First_Name | Last_Name | DOB        | Gender | Contact_Number | Email_Address        | Address                    | Emergency_Contact | Blood_Type | Insurance_Details  | Medical_History           |
|------------|------------|-----------|------------|--------|----------------|----------------------|----------------------------|-------------------|------------|---------------------|---------------------------|
| 1          | Aarav      | Patel     | 1990-05-14 | Male   | 9876543210     | aarav.patel@mail.com  | 45, Park Street, Mumbai     | 9876543211        | B+         | Bajaj Allianz       | Asthma                    |
| 2          | Priya      | Sharma    | 1985-09-22 | Female | 9234567890     | priya.sharma@mail.com | 12, MG Road, Bangalore     | 7890123456        | O-         | ICICI Lombard       | Hypertension              |

## 2. Doctors Dataset

This dataset contains information about the doctors working at the hospital.

| Doctor_ID | First_Name | Last_Name | Specialization    | Contact_Number | Email_Address        | Years_Of_Experience | Qualifications                | Consultation_Fee |
|-----------|------------|-----------|-------------------|----------------|----------------------|----------------------|-------------------------------|------------------|
| 1         | Dr. Ramesh | Kumar     | Cardiologist      | 9023456789     | ramesh.kumar@mail.com | 15                   | MBBS, MD (Cardiology)         | ₹1500            |
| 2         | Dr. Aditi  | Verma     | Neurologist       | 9876543210     | aditi.verma@mail.com  | 12                   | MBBS, DM (Neurology)          | ₹1200            |
| 3         | Dr. Rajesh | Desai     | Orthopedic        | 8765432109     | rajesh.desai@mail.com | 10                   | MBBS, D'Ortho (Orthopedics)   | ₹1000            |

## 3. Appointments Dataset

This dataset stores information about appointments between patients and doctors.

| Appointment_ID | Patient_ID | Doctor_ID | Appointment_Date | Appointment_Time | Reason_For_Visit    | Status    | Prescription_Issued |
|----------------|------------|-----------|------------------|------------------|---------------------|-----------|---------------------|
| 1              | 1          | 2         | 2024-11-20       | 10:00 AM         | Headache            | Scheduled | Yes                 |
| 2              | 2          | 1         | 2024-11-21       | 11:30 AM         | Chest Pain          | Completed | No                  |

## 4. Medical Records Dataset

This dataset contains medical records for each patient, including diagnostic information, treatment plans, and outcomes.

| Record_ID | Patient_ID | Doctor_ID | Diagnosis         | Treatment                | Prescription           | Date_of_Treatment | Outcome    | Follow_Up_Date |
|-----------|------------|-----------|-------------------|--------------------------|------------------------|-------------------|------------|----------------|
| 1         | 1          | 2         | Migraine          | Pain relief therapy       | Ibuprofen              | 2024-11-20        | Recovered  | 2024-12-01     |
| 2         | 2          | 1         | Angina            | Angioplasty              | Aspirin                | 2024-11-21        | Stable     | 2024-12-10     |

## 5. Billing Dataset

This dataset stores information related to the charges for each patient, including consultation fees, tests, and medicines.

| Bill_ID | Patient_ID | Appointment_ID | Consultation_Fee | Tests_Charges | Medicine_Charges | Total_Amount | Payment_Status | Payment_Method |
|---------|------------|----------------|------------------|----------------|------------------|--------------|----------------|----------------|
| 1       | 1          | 1              | ₹1500            | ₹500           | ₹200             | ₹2200        | Paid           | Credit Card    |
| 2       | 2          | 2              | ₹1200            | ₹800           | ₹250             | ₹2250        | Pending        | Insurance      |

## 6. Staff Dataset

This dataset includes information about the hospital's staff (nurses, technicians, administrative staff).

| Staff_ID | First_Name | Last_Name | Role            | Contact_Number | Email_Address        | Shift_Timing     |
|----------|------------|-----------|-----------------|----------------|----------------------|------------------|
| 1        | Sunita     | Yadav     | Nurse           | 9812345670     | sunita.yadav@mail.com | 9:00 AM - 5:00 PM |
| 2        | Manoj      | Reddy     | Receptionist    | 9898765432     | manoj.reddy@mail.com  | 8:00 AM - 4:00 PM |
| 3        | Sandeep    | Mehta     | Lab Technician  | 9345678901     | sandeep.mehta@mail.com| 10:00 AM - 6:00 PM |

## 7. Inventory Dataset

This dataset tracks medical supplies and equipment used in the hospital.

| Item_ID | Item_Name      | Category    | Quantity_in_Stock | Supplier          | Purchase_Price | Expiry_Date |
|---------|----------------|-------------|--------------------|-------------------|----------------|-------------|
| 1       | Paracetamol    | Medicine    | 500                | MedLife Pharma    | ₹5              | 2025-12-01  |
| 2       | ECG Machine    | Equipment   | 3                  | HealthTech Ltd.   | ₹2,00,000       | 2028-05-10  |
| 3       | Glucometer     | Equipment   | 20                 | MedTech Solutions | ₹1,500          | 2027-03-01  |

## 8. Emergency Contacts Dataset

This dataset stores emergency contacts for patients, typically relatives or close friends.

| Contact_ID | Patient_ID | Emergency_Contact_Name | Relationship | Contact_Number | Email_Address         |
|------------|------------|------------------------|--------------|----------------|-----------------------|
| 1          | 1          | Meera Patel            | Mother       | 9876543211     | meera.patel@mail.com  |
| 2          | 2          | Rajesh Sharma          | Husband      | 9234567891     | rajesh.sharma@mail

---



# ER DIAGRAM 

![image alt](https://github.com/adarsh2345-cyber/Hospital-Management-System/blob/f603699c89424d9ccfe534643d23626ddee18d30/Untitled%20Diagram-Page-1.drawio.png) 

# FUTURE ENHANCEMENTS 

1. Creating a Mobile Application
2. Patient Diagnosis History
3. Adding Medicine Records
4. Adding Feedback and Support System
