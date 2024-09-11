import argparse

def parse_args() -> argparse.Namespace:
    """Parse arguments for given program."""
    # Create parser
    parser = argparse.ArgumentParser(
        prog = "extract_n_lines",
        description = "Extract n lines form a given log file",
    )

    # Add argument
    parser.add_argument('logIn', help='path to input log file')
    parser.add_argument('logOut', help='path to output log file')
    parser.add_argument('n', help='number of lines to extract')
    
    # Parse arguments and return
    return parser.parse_args()

def main() -> None:
    """Main method executed when program is run."""
    # Parse arguments
    args = parse_args()
    
    try:
        # read
        with open(args.logIn, 'r') as i_f:
            lines = i_f.readlines()
        
        # extract
        n = int(args.n)
        extracted_lines = lines[:n]
        
        # write
        with open(args.logOut, 'w') as o_f:
            o_f.writelines(extracted_lines)
        
        print(f"Extracted {args.n} lines from {args.logIn} and saved to {args.logOut}")
    except:
        print(f"Error: file '{args.logIn}' not found.")
        
if __name__ == "__main__":
    main()