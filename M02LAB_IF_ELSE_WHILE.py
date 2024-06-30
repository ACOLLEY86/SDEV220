# Anthony Colley
# M02LAB_IF_ELSE_WHILE.py
# Description: This app accepts student names and GPAs and checks if they qualify for the Dean's List or the Honor Roll.

def main():
    last_name = ""
    while last_name != "ZZZ":
        # Get the student's last name
        last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")
        
        if last_name != "ZZZ":
            # Get the student's first name
            first_name = input("Enter the student's first name: ")
            
            # Get the student's GPA
            gpa_input = input("Enter the student's GPA: ")
            
            # Check if the GPA input is a valid float
            if gpa_input.replace('.', '', 1).isdigit() and gpa_input.count('.') < 2:
                gpa = float(gpa_input)
                
                # Check if the student qualifies for the Dean's List or Honor Roll
                if gpa >= 3.5:
                    print(f"{first_name} {last_name} has made the Dean's List.")
                elif gpa >= 3.25:
                    print(f"{first_name} {last_name} has made the Honor Roll.")
                else:
                    print(f"{first_name} {last_name} has not qualified for the Dean's List or Honor Roll.")
            else:
                print("Invalid input for GPA. Please enter a valid float number.")
main()