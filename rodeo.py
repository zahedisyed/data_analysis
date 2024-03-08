def rename_rodeo_columns (columns):
    # Replace this and the line below with your code...
    """
    Function to rename column names based on the following criteria:
    - Converts names to lower case
    - Replaces spaces with underscore
    - Removes the trailing word "Data" if exists
    """
    corrected_columns = []
    for col in columns:
        lower_col = col.lower()
        underscore_col = lower_col.replace(" ","_")
        if underscore_col.endswith("_data"):
            underscore_col = underscore_col[:-5]
        corrected_columns.append(underscore_col)
    return corrected_columns
        
if __name__ == "__main__":
    # Create a list of example original column names 
    original = [
        "Participant Count Data",
        "Rodeo Clown Count",
        "Hats Visible",
        "Cost Data",
    ]
    
    # Get the corrected column names
    corrected = rename_rodeo_columns (original)
    
    # Print a table to compare original and corrected names
    print("Original                  Corrected")
    print("--------                  ---------")
    for o, c in zip(original, corrected):
        print(f"{o:<25} {c:<25}")
