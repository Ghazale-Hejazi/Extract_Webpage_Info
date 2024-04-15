import re
import requests

OUTPUT_FILE = 'output.txt'

def main():
    while True:
        # Get user input URL
        user_url = input("Enter the URL: ").strip()
        
        # Validate the input URL
        if validate_url_input(user_url):
            # Attempt to fetch URL information
            success, status_code, headers, page_codes = get_url_info(user_url)

            if success:
                # Display information to the user
                print_info(status_code, headers, page_codes)

                # Save information to a file
                save_info_to_file(status_code, headers, page_codes)
                print(f"\nData has been saved to {OUTPUT_FILE}")
                break
            else:
                print("Error fetching the website. Please try again.")
        else:
            print("Invalid URL. Please make sure it starts with http://, https://, or www.")


def validate_url_input(url):
    # Define a regex pattern for valid URLs
    url_pattern = re.compile(r'^(http://|https://|www\.)\S+')
    
    # Check if the input matches the pattern
    return bool(url_pattern.match(url))


def get_url_info(url):
    try:
        # Make a request to the URL
        response = requests.get(url)

        # Raise an exception for bad responses (4xx or 5xx)
        response.raise_for_status()

        # Return a tuple indicating success and URL information
        return True, response.status_code, response.request.headers, response.text
    
    except requests.RequestException as e:
        # Print an error message and return a tuple indicating failure
        print(f"Error during GET request: {e}")
        return False, None, None, None


def print_info(status_code, headers, page_codes):
    # Display status code, headers, and page codes
    print(f"\nStatus Code: {status_code}")
    print("\nHeaders:")
    
    for key, value in headers.items():
        print(f"{key}: {value}")
    
    print("\nPage codes:")
    print(page_codes)


def save_info_to_file(status_code, headers, page_codes):
    # Save status code, headers, and page codes to a file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(f"Status Code: {status_code}\n\n")
        
        f.write("Headers:\n")
        for key, value in headers.items():
            f.write(f"{key}: {value}\n")
        
        f.write("\nPage codes:\n")
        f.write(page_codes)


if __name__ == "__main__":
    main()
