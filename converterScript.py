from PIL import Image
import os
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def convert_image_format():
    try:
        # Greet the user
        print(f"{Fore.CYAN}{Style.BRIGHT}Welcome to the Image Format Converter!{Style.RESET_ALL}")
        
        # Prompt the user for file path
        print(f"{Fore.YELLOW}Please enter the path to your image file:")
        input_path = input(f"{Fore.GREEN}>>> ").strip()
        
        # Validate if the file exists
        if not os.path.exists(input_path):
            print(f"{Fore.RED}Error: File not found. Please check the path and try again.")
            return
        
        # Open the image
        img = Image.open(input_path)
        print(f"{Fore.GREEN}Image loaded successfully!{Style.RESET_ALL}")
        
        # Prompt the user for the desired output format
        print(f"\n{Fore.YELLOW}Available formats: {Fore.BLUE}PNG, JPEG, JPG, BMP, WEBP, GIF, TIFF")
        print(f"{Fore.YELLOW}Enter the desired format for the image:")
        output_format = input(f"{Fore.GREEN}>>> ").strip().upper()
        
        # Validate format
        valid_formats = ["PNG", "JPEG", "JPG", "BMP", "WEBP", "GIF", "TIFF"]
        if output_format not in valid_formats:
            print(f"{Fore.RED}Invalid format! Please select from the available formats.")
            return
        
        # Prepare output file path
        base_name, _ = os.path.splitext(input_path)
        output_path = f"{base_name}_converted.{output_format.lower()}"
        
        # Save the image in the desired format
        img.save(output_path, format=output_format)
        print(f"{Fore.GREEN}Image successfully converted to {output_format}!")
        print(f"{Fore.CYAN}Saved at: {Fore.WHITE}{output_path}")
    
    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}")

# Run the converter
if __name__ == "__main__":
    convert_image_format()
