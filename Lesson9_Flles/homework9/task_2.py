# Copy column with email.
import csv
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w', newline='') as new_csv_file:
        fieldnames = ['email']
        csv_writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for elements in csv_reader:
            del elements['first_name']
            del elements['last_name']
            csv_writer.writerow(elements)
