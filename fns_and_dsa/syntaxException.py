#!/usr/bin/env python3
import os


def read_file(path_to_file):
    
    try:
        file = open(path_to_file, 'r')
        content = file.read()
    except FileExistsError as e:
        print(f"An Error occured as: {e}")
    except IOError as e:
        print(f"An Error occured as: {e}")
    else:
        # print(f"\nThe File Contents is:\n\n")
        print(content)
    finally:
        try:
            file.close()
        except UnboundLocalError:
            pass
        # print("\n\nFile Operation Completed.")


path_to_file = os.path.join(os.getcwd(), "__pycache__")
read_file(path_to_file)