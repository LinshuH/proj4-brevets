"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments.
#


def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An "ISO 8601 format" date string indicating the control open time.
       This will be in the "same time zone" as the brevet start time.
    """
    """
    control_dist_km = flask.request.args.get("km", type=float)
    brevet_dist_km = flask.request.args.get("km", type=float)
    """
    # use the speed, create another dictionary, calculate the time it need to pass this control point. 
    speed_dic = [(200:34), (400:32), (600: 30), (1000: 28), (1300: 26)]
    time_dic = [(200:200/34), (400:400/32), (600:600/30), (1000:1000/28), (1300:1300/26)]
    control_time = 0

    for i in range (time_dic.length()):        # go to each pair in dictionary
      if (time_dic.key()[i] < control_dist_km):  # check the key value of the pair
        control_time += time_dic.value()[j]         # add the the value of that key to the total_time. #This method is quite redundent, since it have to loop in 5 brevet_dist_km every time.    
      else:
        addition_time = (speed_dic.key()[i] - control_dist_km) / speed_dic.value()[i]
        total_time = control_time + addition_time
        break


    open_time = brevet_start_time + timedelta(hours=total_time)

    return open_time


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    return arrow.now().isoformat()
