import statistics
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
def get_file(filename):
    try:
        lines=[]
        file=open(filename, "r")
        for line in file:
            line=line.strip()
            length=len(line)
            line=line[:length-1]#strips final comma
            line_l=line.split(",")
            fl_check=True
            for val in line_l:
                if not is_float(val):
                    fl_check=False
            if fl_check:
                lines.append(line_l)
        file.close()
        return lines
    except FileNotFoundError:
        print("404")
        return
def get_y_list(values):
    y_list=[]
    for ls in values:
        y_list.append(ls[1])
    return y_list
def get_increasing(values):
    prev=0
    i=0
    while float(values[i])>=prev and i<len(values):
        prev=float(values[i])
        i+=1
        if i==len(values)-1:
            return None
    return[values[i-1],i]
def get_peaks(filename):
    data_set=get_file(filename)
    y_list=get_y_list(data_set)
    inc_ls=get_increasing(y_list)
    peaks=[float(inc_ls[0])]
    i=inc_ls[1]
    while i<len(y_list):
        check_ls=get_increasing(y_list[i:])
        if check_ls!=None:
            i+=check_ls[1]
            peaks.append(float(check_ls[0]))
        else:
            return peaks
def main():
    peaks=get_peaks("pokit_try.csv")
    mean=statistics.mean(peaks)
    stdev=statistics.stdev(peaks)
    print("For this data set:", "mean=",mean,"stdev=",stdev,"Number of peaks=",len(peaks))
main()
