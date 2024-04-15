# Web Page Information Extractor
This simple Python script allows users to input a URL, fetch information about the web page, and save relevant details to a text file.

## How to Use

1. **Install Dependencies:**
   Ensure you have the required dependencies installed by running:
      pip install -r requirements.txt
   

2. **Run the Script:**
   Execute the script by running the following command:
      python main.py
   

3. **Enter the URL:**
   When prompted, enter the URL of the web page you want to extract information from.

4. **View Output:**
   The script will display the status code, headers, and page content. The information will also be saved to an output.txt file.

## Requirements
Make sure to have the required Python packages installed. You can install them using the following command:
   pip install -r requirements.txt


## Script Details

### File Structure
- `main.py`: The main Python script.
- `requirements.txt`: List of Python packages required by the script.

### Code Overview
- `main()`: The main function that orchestrates the script.
- `validate_url_input(url)`: Function to validate user-inputted URLs.
- `get_url_info(url)`: Function to fetch information from the provided URL.
- `print_info(status_code, headers, page_codes)`: Function to display fetched information.
- `save_info_to_file(status_code, headers, page_codes)`: Function to save information to a text file.


## Example
Enter the URL: https://example.com
Output details will be displayed, and information will be saved to output.txt.

