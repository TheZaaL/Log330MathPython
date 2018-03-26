import csv

def read_file(file_path):
  data = []
  with open(file_path) as file_data:
    reader = csv.reader(file_data, delimiter=',')

    # Skip first and second lines
    next(reader)
    next(reader)

    # Invert column and rows for better manipulation
    first_data = next(reader)

    for col in range(0, len(first_data)):
      data.append([])
      try:
        data[col].append(float(first_data[col]))
      except ValueError:
        data[col].append(first_data[col])

    for row in reader:
      for col, col_data in enumerate(row):
        data.append([])

        # Convert to float
        try:
          data[col].append(float(col_data))
        except ValueError:
          data[col].append(col_data)
    
    return data