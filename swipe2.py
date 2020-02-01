import datetime

date_format = "%Y-%m-%d %H:%M:%S"

def get_hours(st, et):
    """calculates the hours worked from start day 
    to end day.
    returns the difference of hours between the two days.
    #TODO: implement daily limit hours from 8am to 6 pm
    """
    h = datetime.datetime(1,1,1,0,0)
    s_lim_time = str(st.date())+" 08:00:00"
    e_lim_time = str(et.date())+" 17:00:00"
    s_lim = datetime.datetime.strptime(s_lim_time, date_format)
    e_lim = datetime.datetime.strptime(e_lim_time, date_format)

    sday = st.weekday()
    eday = et.weekday()

    # Check for weekend, remove weekend hours
    sod_lim = datetime.datetime.strptime(str(et.date())+" 08:00:00", date_format)
    eod_lim = datetime.datetime.strptime(str(st.date())+" 17:00:00", date_format)
    if sday == 4 and eday == 0:
        h = (eod_lim - st) + (et - sod_lim)
    else:
        # When the days are same
        if st.date() == et.date():
	    # Check for weekday hours, either employee is early or late.
            if s_lim > st:
	        new_st = s_lim
            elif s_lim < st:
                new_st = st
	     # Check for weekday hours, either employee leaves early or late.
	    if et < e_lim:
                new_et = et
	    elif e_lim < et:
                new_et = e_lim
            h = new_et - st
        # When the days are different
        else:
	    # Check for weekday hours, either employee is early or late.
	    if st < s_lim:
	        h += (eod_lim - s_lim)
	    elif s_lim < st:
	        h += (eod_lim - st)
	    # Check for weekday hours, either employee leaves early or late.
	    if et < e_lim:
	        h += (et - sod_lim)
	    elif e_lim < et:
	        h += (e_lim - sod_lim)
    return h

def main():
    start = raw_input("Enter the swipe in time:%Y-%m-%d %H:%M:%S")
    end = raw_input("Enter the swipe out time:%Y-%m-%d %H:%M:%S")
    date_format = "%Y-%m-%d %H:%M:%S"
    start = datetime.datetime.strptime(start, date_format)
    end = datetime.datetime.strptime(end, date_format)
    h = get_hours(start, end)
    print("Your billable time: %s"%h)

if __name__=='__main__':
    main()
