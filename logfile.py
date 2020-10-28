import sys

def apache_output(line):
    split_line = line.split()
    return {'remote_host': split_line[0],
            'apache_status': split_line[8],
            'data_transfer': split_line[9],
            
    }


def final_report(logfile):
    for line in logfile:
        line_dict = apache_output(line)
        print(line_dict)


#if __name__ == "__main__":
    if not len(sys.argv) > 1 :
        print (__doc__)
        sys.exit(1)
    infile_name = sys.argv[1]
    try:
        infile = open('access.2020-08-12_1900.log', 'r')
    except IOError:
        print ("You must specify a valid file to parse")
        print (__doc__)
        sys.exit(1)
    log_report = final_report(infile)
    print (log_report)
    infile.close()