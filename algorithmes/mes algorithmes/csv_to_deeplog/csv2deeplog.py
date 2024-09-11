import csv
import argparse

def parse_args() -> argparse.Namespace:
    """Parse arguments for given program."""
    # Create parser
    parser = argparse.ArgumentParser(
        prog = "csv2deeplog",
        description = "Convert a csv-compatible file to a DeepLog-compatible file with 3 columns: 'timestamp', 'machine' and 'eventID'",
    )

    # Add argument
    parser.add_argument('csvIn', help='path to input csv file')
    parser.add_argument('csvOut', help='path to output DeepLog csv file')
    parser.add_argument('format', help='format of the log file in [HDFS, OpenSSh, Apache, Hadoop, HealthApp, HPC, Linux, Mac, OpenStack, Proxifier, BGL]')
    
    # Parse arguments and return
    return parser.parse_args()

def main() -> None:
    """Main method executed when program is run."""
    # Parse arguments
    args = parse_args()
    
    # Read data
    with open(args.csvIn) as file:
        csv_reader = csv.reader(file)
        
        # Skip the header
        next(csv_reader)
    
        if args.format == "HDFS" or args.format == "Hadoop" or args.format == "OpenSSH":
            with open(args.csvOut, 'w', newline='') as outfile:
                fieldnames = ["timestamp", "machine", "event"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
            
                # Loop
                for row in csv_reader:
                    event_id = row[7].replace("E", "")
                    
                    timestamp = row[0]       
                    
                    writer.writerow({"timestamp": timestamp, "machine": "", "event": event_id})
                    
        elif args.format == "Apache" or args.format == "Proxifier":            
            with open(args.csvOut, 'w', newline='') as outfile:
                fieldnames = ["timestamp", "machine", "event"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
            
                # Loop
                for row in csv_reader:
                    event_id = row[4].replace("E", "")
                    
                    timestamp = row[0]       
                    
                    writer.writerow({"timestamp": timestamp, "machine": "", "event": event_id})
                    
        elif args.format == "HealthApp":
            with open(args.csvOut, 'w', newline='') as outfile:
                fieldnames = ["timestamp", "machine", "event"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
            
                # Loop
                for row in csv_reader:
                    event_id = row[5].replace("E", "")
                    
                    timestamp = row[0]       
                    
                    writer.writerow({"timestamp": timestamp, "machine": "", "event": event_id})
                    
        elif args.format == "HPC" or args.format == "Linux":
            with open(args.csvOut, 'w', newline='') as outfile:
                fieldnames = ["timestamp", "machine", "event"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
            
                # Loop
                for row in csv_reader:
                    event_id = row[8].replace("E", "")
                    
                    timestamp = row[0]       
                    
                    writer.writerow({"timestamp": timestamp, "machine": "", "event": event_id})
                    
        elif args.format == "Mac" or args.format == "OpenStack":
            with open(args.csvOut, 'w', newline='') as outfile:
                fieldnames = ["timestamp", "machine", "event"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
            
                # Loop
                for row in csv_reader:
                    event_id = row[9].replace("E", "")
                    
                    timestamp = row[0]       
                    
                    writer.writerow({"timestamp": timestamp, "machine": "", "event": event_id})
                    
        elif args.format == "Zookeeper":
            with open(args.csvOut, 'w', newline='') as outfile:
                fieldnames = ["timestamp", "machine", "event"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
            
                # Loop
                for row in csv_reader:
                    event_id = row[6]
                    
                    timestamp = row[0]       
                    
                    writer.writerow({"timestamp": timestamp, "machine": "", "event": event_id})
                    
        elif args.format == "BGL":
            with open(args.csvOut, 'w', newline='') as outfile:
                fieldnames = ["timestamp", "machine", "event"]
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
            
                # Loop
                for row in csv_reader:
                    event_id = row[11].replace("E", "")
                    
                    timestamp = row[0]       
                    
                    writer.writerow({"timestamp": timestamp, "machine": "", "event": event_id})
                    
        else:
            print("Format not available")
                
if __name__ == "__main__":
    main()
