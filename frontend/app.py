
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Employee Management System",
    page_icon="👨‍💼",
    layout="wide"
)

st.title("👨‍💼 Employee Management System")
st.write("Manage your employees easily")

menu = st.sidebar.selectbox(
    "Choose Operation",
    ["Dashboard", "Add Employee", "View Employees",
     "Update Employee","Search Employee", "Delete Employee"]
)

if menu == "Dashboard":
    st.subheader("Dashboard")
    try:
        response = requests.get(f"{API_URL}/employees")
        if response.status_code == 200:
            employees = response.json()
            st.metric("Total Employees", len(employees))
            st.success("Backend Connected Successfully!")
        else:
            st.error("Unable to fetch employees")
    except requests.exceptions.RequestException:
        st.error("Backend is not running")

elif menu == "Add Employee":
    st.subheader("Add New Employee")

    with st.form("add_employee"):
        emp_id = st.number_input("Employee ID", min_value=1, step=1)
        name = st.text_input("Employee Name")
        department = st.text_input("Department")
        salary = st.number_input("Salary", min_value=0.0)
        email = st.text_input("Email")

        submit = st.form_submit_button("Add Employee")

        if submit:
            data = {
                "id": int(emp_id),
                "name": name,
                "department": department,
                "salary": salary,
                "email": email
            }

            try:
                response = requests.post(
                    f"{API_URL}/employees", json=data
                )
                if response.status_code == 201:
                    st.success("Employee added successfully!")
                else:
                    st.error(response.text)
            except requests.exceptions.RequestException:
                st.error("Backend connection failed")

elif menu == "View Employees":
    st.subheader("Employee List")
    try:
        response = requests.get(f"{API_URL}/employees")
        if response.status_code == 200:
            employees = response.json()
            st.dataframe(employees, use_container_width=True)
        else:
            st.error(response.text)
    except requests.exceptions.RequestException:
        st.error("Backend connection failed")

elif menu == "Update Employee":
    st.subheader("Update Employee Details")

    with st.form("update_employee"):
        emp_id = st.number_input("Employee ID", min_value=1, step=1)
        name = st.text_input("Employee Name")
        department = st.text_input("Department")
        salary = st.number_input("New Salary", min_value=0.0)
        email = st.text_input("Email")

        submit = st.form_submit_button("Update Employee")

        if submit:
            data = {
                "id": int(emp_id),
                "name": name,
                "department": department,
                "salary": salary,
                "email": email
            }

            try:
                response = requests.put(
                    f"{API_URL}/employees/{int(emp_id)}",
                    json=data
                )
                if response.status_code == 200:
                    st.success("Employee updated successfully!")
                else:
                    st.error(response.text)
            except requests.exceptions.RequestException:
                st.error("Backend connection failed")

elif menu == "Delete Employee":
    st.subheader("Delete Employee")

    emp_id = st.number_input("Employee ID", min_value=0, step=1)

    if st.button("Delete Employee"):
        try:
            response = requests.delete(
                f"{API_URL}/employees/{int(emp_id)}"
            )
            if response.status_code == 200:
                st.success("Employee deleted successfully!")
            else:
                st.error(response.text)
        except requests.exceptions.RequestException:
            st.error("Backend connection failed")


elif menu == "Search Employee":
    st.subheader("Search Employee")

    emp_id = st.number_input(
        "Enter Employee ID",
        min_value=1,
        step=1
    )

    if st.button("Search Employee"):
        try:
            response = requests.get(
                f"{API_URL}/employees"
            )

            if response.status_code == 200:
                employees = response.json()

                result = next(
                    (emp for emp in employees
                     if emp["id"] == int(emp_id)),
                    None
                )

                if result:
                    st.success("Employee Found!")
                    st.json(result)
                else:
                    st.warning("Employee not found")

            else:
                st.error(response.text)

        except requests.exceptions.RequestException:
            st.error("Backend connection failed")