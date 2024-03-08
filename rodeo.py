def rename_rodeo_columns (columns):
    # Replace this and the line below with your code...
    """
    A funciton t rename column names for the Ogedenville Rodeo data analysis.
    It converts names to lower case, replaces cases with underscores, and removes the trailing word
    "data" if present.
    """
    corrected_columns = []
    for col in columns:
        lower_col = col.lower() # convert to lower case
        underscore_col = lower_col.replace(" ","_") # Replace spaces with underscores
        # remove the trailing word, "Data" if present
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
