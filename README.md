# NMAP_SCANNER

## Description

*NMAP_SCANNER* is a Python-based script designed to automate the process of scanning networks using the Nmap tool. This script simplifies the use of Nmap, allowing users to quickly scan targets and generate reports without needing extensive knowledge of Nmap’s command-line options.

## Features

- *Customizable Scans*: Perform various types of Nmap scans by modifying the script parameters.
- *Automation*: Automate repetitive scanning tasks with ease.
- *Reporting*: Generate and save scan reports in a user-friendly format.

## Requirements

- *Python 3.x*
- *Nmap* installed on the system

## Installation

1. Clone the repository:
   
   git clone https://github.com/SusmitaBarua/NMAP_SCANNER.git
   
2. Navigate to the project directory:
   
   cd NMAP_SCANNER
   
3. Install the required Python packages:
   
   pip install -r requirements.txt
   

## Usage

1. Ensure Nmap is installed on your system. You can install it using the following command:

   - For Debian/Ubuntu:
     
     sudo apt-get install nmap
     
   - For Red Hat/CentOS:
     
     sudo yum install nmap
     
   - For Arch Linux:
     
     sudo pacman -S nmap
     

2. Run the script by executing the following command:
   bash
   python nmap_scanner.py [target] [options]
   
   Replace [target] with the IP address or domain you want to scan, and [options] with any additional Nmap options you wish to use.

## Examples

- Basic scan:
  
  python nmap_scanner.py 192.168.1.1
  

- Scan with specific Nmap options:
  
  python nmap_scanner.py 192.168.1.1 -p 80,443
  
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
