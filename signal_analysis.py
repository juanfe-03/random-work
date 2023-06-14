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
def get_dict(filename):
    file_list=get_file(filename)
    dict={}
    for ls in file_list:
        dict[float(ls[1])]=float(ls[0])
    return dict

def get_y_list(filename):
    values=get_file(filename)
    y_list=[]
    for ls in values:
        y_list.append(ls[1])
    return y_list
def get_times(filename):
    values=get_file(filename)
    times_list=[]
    for ls in values:
        times_list.append(ls[0])
    return times_list
def is_notdecreasing(prev,current):
    check_1= current>=prev
    check_2= current<0.55*prev#makes sure there is a real value drop
    return (check_1 or not(check_2))
def get_increasing(values):
    prev=0
    i=0
    while is_notdecreasing(prev,float(values[i])) and i<len(values):
        prev=float(values[i])
        i+=1
        if i==len(values)-1:
            return
    return[prev,i]
def get_peaks(filename):
    y_list=get_y_list(filename)
    i=0
    peaks=[]
    while i<len(y_list):
        temp_increasing=get_increasing(y_list[i:])
        if temp_increasing!=None:
            i+=(temp_increasing[1])
            peaks.append(float(temp_increasing[0]))
        else:
            return peaks
def get_frequency(filename):
    y_list=get_y_list(filename)
    times_list=get_times(filename)
    peaks=get_peaks(filename)
    peak_1=peaks[0]
    peak_2=peaks[len(peaks)-1]
    first_i=y_list.index(str(peak_1))
    rev_y=y_list[::-1]
    second_i=rev_y.index(str(peak_2))
    rev_time=times_list[::-1]
    time_1=float(times_list[first_i])*(0.001)#millisecond to second
    time_2=float(rev_time[second_i])*(0.001)
    period=(len(peaks)-1)/(time_2-time_1)
    freq=1/period
    return freq
def analyze(filename,new_file="results.csv"):
    peaks=get_peaks(filename)
    freq=get_frequency(filename)
    mean=statistics.mean(peaks)
    stdev=statistics.stdev(peaks)
    number_peaks=len(peaks)
    list=[filename,str(freq),str(mean),str(stdev),str(number_peaks)]
    list_str=",".join(list)
    line="filename,frequency,mean,stdev,number peaks"
    try:
        new=open(new_file,"r")
        new.close()
        new_file=open(new_file,"a")
    except FileNotFoundError:
        new_file=open(new_file,"w")
        print(line,file=new_file)
    print(list_str,file=new_file)
    new_file.close()
    return list_str
def main():
    filename="hello"
    new_file=input("Type in the result filename you desire:")
    while filename!="Q":
        filename=input("insert data filename, Q to quit:")
        try:
            file=open(filename,"r")
            file.close()
        except FileNotFoundError:
            print("file not found")
        if filename!="Q":
            analyze(filename,new_file)
main()
