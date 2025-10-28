import pandas as pd

# ===========================================
# 🧾 Description:
# This script reads an Excel file that contains product barcodes
# and matches each barcode with its corresponding URL from a predefined list.
# If a barcode is found inside one of the URLs, that URL will be assigned
# to the "URL" column in the Excel data.
# ===========================================

# ✅ Step 1: Load the Excel file
# file_path → The full path to your Excel file
# sheet_name → The worksheet that contains your data
# header=0 → Means the first row contains column names
file_path = r"D:\final.xlsx"
df = pd.read_excel(file_path, sheet_name='Sheet1', header=0)

# Example structure of your Excel file:
# ------------------------------------------
# |   BARCODE   |
# |--------------|
# |   12345      |
# |   67890      |
# |   54321      |
# ------------------------------------------

# ✅ Step 2: Example list of URLs to match
# (In a real-world case, you can load this list from another file or API)
urls = [
    "https://example.com/product/12345",
    "https://example.com/product/67890",
    "https://example.com/product/54321"
]

# ✅ Step 3: Define a function to find a matching URL for each barcode
def find_url(barcode):
    # Loop through each URL in the list
    for url in urls:
        # Check if the barcode (as string) exists inside the URL
        if str(barcode) in url:
            return url  # Return the matched URL
    return None  # Return None if no match is found

# ✅ Step 4: Apply the function to the DataFrame
# .apply() runs the function on every value in the "BARCODE" column
# and saves the result in a new column called "URL"
df["URL"] = df["BARCODE"].apply(find_url)

# ✅ Step 5: Copy the final table to clipboard (you can paste it directly in Excel)
df.to_clipboard(index=False)

# ✅ Step 6: Print confirmation message
print("✅ Done! URLs matched and copied to clipboard.")

# Example output after running this script:
# --------------------------------------------------
# | BARCODE |                URL                  |
# |----------|-------------------------------------|
# | 12345   | https://example.com/product/12345   |
# | 67890   | https://example.com/product/67890   |
# | 54321   | https://example.com/product/54321   |
# --------------------------------------------------
