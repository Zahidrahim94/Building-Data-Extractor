# Building Data Extractor

The Building Data Extractor is a Python application that allows you to extract and visualize building data from OpenStreetMap. You can either specify an area name or upload a JSON file to extract and visualize the building footprints.

## Features

- Extract and visualize building data by area name
- Upload a JSON file from the cache folder and visualize the data
- Display the name of the area on the graph
- Display the bounding box coordinates of the area

## Installation

1. Clone the repository:
   ```
   
   ```

2. Install the required dependencies:
   ```
   pip install osmnx matplotlib tkinter
   ```

## Usage

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the application:
   ```
   python bulding_extrect_ui.py
   ```

3. The application window will appear.

4. Extract and visualize building data by area name:
   - Enter the area name in the provided input field.
   - Click the "Extract and Visualize by Area Name" button.
   - The graph with the building footprints will be displayed, along with the name of the area and the bounding box coordinates.

5. Visualize a single JSON file from the cache folder:
   - Click the "Visualize Single JSON from Cache" button.
   - Select a JSON file from the cache folder using the file dialog.
   - The graph with the loaded data will be displayed.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, feel free to submit a pull request.

## License

The Building Data Extractor is open-source and is licensed under the MIT License.
