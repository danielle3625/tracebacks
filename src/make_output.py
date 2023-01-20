
# Establish base directory, use the r bc Willie did
# but, i guess i don't have to do this here, because it's really going to be given when you call the function
base_dir = r"c:\Users\Admin\desktop\pythonstuff\tracebacks\tests"

output_dir = r"c:\Users\Admin\desktop\pythonstuff\tracebacks\output"

def make_output(filepaths, base_dir, output_dir):
    """
    :param filepaths: A list of filepaths for files to produce output for
    :param base_directory: The anchor / "root" to consider 'filepaths' relative to
    :param output_directory: THe directory to write generated HTML files relative to (within)
    """
    ...

    for file in base_dir:
        # Take a list of filepaths
        for path in filepaths:
            # Extract the base directory from those file paths? 
            # Or, am I supposed to PROVIDE the base directory?

            # if 1, setup base directory and output directory variables above this for loop
            # let's just go ahead and assume this is the case

            if path.endswith('.txt'):
                path.replace('.txt', '.html')
            
            with open("output", 'w') as outfile:
                    outfile.write(path)
  


