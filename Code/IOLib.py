import csv

def read_file(file_path):
  data = []
  with open(file_path) as file_data:
    reader = csv.reader(file_data, delimiter=';')

    # Skip first line
    next(reader)

    # Invert column and rows for better manipulation
    first_data = next(reader)

    for col in range(0, len(first_data)):
      data.append([])
      data[col].append(float(first_data[col].replace(',', '.')))

    for row in reader:
      for col, col_data in enumerate(row):
        data.append([])

        # Convert to float
        data[col].append(float(col_data.replace(',', '.')))
    
    return data