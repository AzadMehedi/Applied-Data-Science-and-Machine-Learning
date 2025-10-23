# A dictionary containing nested dictionaries.

company = {
    "HR": {"employees": 5, "manager": "Sarah"},
    "IT": {"employees": 10, "manager": "John"},
    "Finance": {"employees": 3, "manager": "David"}
}

if __name__ == '__main__':
    for dept, info in company.items():
        print(f"{dept} Department -> Manager: {info['manager']}, Employees: {info['employees']}")