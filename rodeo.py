def rename_rodeo_columns (columns):
    # Replace this and the line below with your code...
    """
    Function to rename column names for the Ogdenville Rodeo data analysis.
    It converts names to lower case, replaces spaces with underscores, and removes
    the trailing word "Data" if present.
    """
    corrected_columns = []
    for col in columns:
        # Convert to lower case
        lower_col = col.lower()
        # Replace spaces with underscores
        underscore_col = lower_col.replace(" ", "_")
        # Remove the trailing word "Data" if present
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