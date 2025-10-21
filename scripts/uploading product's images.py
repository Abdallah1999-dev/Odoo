import pandas as pd

# List of product image links (uploaded to PostImage)
imgs_links = [
    "https://i.postimg.cc/7YB7g9Yr/Burger.webp",
    "https://i.postimg.cc/ZKf3rHKS/Hot-Dog.webp",
    "https://i.postimg.cc/BQhDxpQq/Pizza.webp"
]

data = []

# Loop through each image link to extract product information
for img in imgs_links:
    # Extract the product name from the image URL (e.g., "Burger" from ".../Burger.webp")
    product_name = img.split('/')[-1].split('.')[0]
    # Append a dictionary with the product name and image URL to the data list
    data.append({"Product Name": product_name, "Image URL": img})

# Create a DataFrame from the data list
df = pd.DataFrame(data)

# Copy the DataFrame to clipboard (so it can be pasted into Excel or another app)
df.to_clipboard(index=False)

# Print confirmation message
print("DataFrame copied to clipboard!")
