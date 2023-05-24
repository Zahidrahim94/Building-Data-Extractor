import osmnx as ox
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Function to extract and visualize building data by area name
def extract_and_visualize_buildings_by_name():
    # Get the area name from the input field
    area_name = entry.get()

    if area_name:
        try:
            # Retrieve the boundary of the area by its name
            place = ox.geocode_to_gdf(area_name)

            # Retrieve the building data for the specified area
            buildings = ox.geometries_from_place(area_name, tags={'building': True})

            # Create a plot and display the building footprints
            fig, ax = ox.plot_footprints(buildings)

            # Display the name of the area on the graph
            ax.set_title(area_name, fontsize=12)

            # Display the bounding box coordinates
            bbox = place.bounds
            bbox_text = f"Bounding Box: \nMin Latitude: {bbox.miny}\nMax Latitude: {bbox.maxy}\nMin Longitude: {bbox.minx}\nMax Longitude: {bbox.maxx}"
            ax.text(0.05, 0.95, bbox_text, transform=ax.transAxes, fontsize=8, verticalalignment='top', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

            # Display the plot
            plt.show()
        except ValueError:
            messagebox.showinfo("Invalid Area Name", "Please enter a valid area name.")
    else:
        messagebox.showinfo("No Area Name", "Please enter an area name.")

# Create the main window
window = tk.Tk()
window.title("Building Data Extractor")
window.geometry("400x250")

# Create a label for the application description
label_description = tk.Label(window, text="Building Data Extractor", font=("Helvetica", 16, "bold"), fg="navy")
label_description.pack(pady=10)

# Create a label with application details
label_details = tk.Label(window, text="This application allows you to extract and visualize building data.\nYou can enter an area name to extract buildings by name.\nPlease enter an area name below.", font=("Helvetica", 10), wraplength=350, justify="center")
label_details.pack(pady=5)

# Create a label and entry field for area name
label_area = tk.Label(window, text="Enter Area Name:", font=("Helvetica", 10))
label_area.pack()
entry = tk.Entry(window)
entry.pack(pady=5)

# Create a button to trigger the extraction and visualization by area name
button_name = tk.Button(window, text="Extract and Visualize by Area Name", command=extract_and_visualize_buildings_by_name, bg="lightblue")
button_name.pack(pady=10)

# Run the main event loop
window.mainloop()
