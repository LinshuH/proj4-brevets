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
   
    # use the speed, create another dictionary, calculate the time it need to pass this control point. 
    speed_dic = {"0":34,"200":34, "400":32, "600": 30, "1000": 28, "1300":26}
    time_dic = {"0":0, "200":200/34, "400":100/32, "600":200/30, "1000":400/28, "1300":300/26}
    control_point = [0,200,400,600,1000,1300]

    # go to each pair in dictionary
    for i in range (len(time_dic)):
      if (control_point[i] <= brevet_dist_km):            # check whether the user input is the total distance of the brevet
          if (control_point[i] <= control_dist_km):  # check the key value of the pair
              control_time += time_dic[srt(control_point[i])]         # add the the value of that key to the total_time. #This method is quite redundent, since it have to loop in 5 brevet_dist_km every time.    
          else:
              addition_time = (control_dist_km - control_point[i]) / speed_dic[str(i)]
          total_time = control_time + addition_time
            # end of adding time when reach the brevet_dist_km, as long as reach the brevet_dist_km, do nothing to the data.
     
    control_open = brevet_start_time + timedelta(hours=total_time)

    return control_open
    #take starttime, turn to the arrow object,
    #open_tim = arrow.get(brevet_start_time)
    # open_tim.shift(hours=+total_time)
    #open_tim.isoformat()
    
    #dictionary will not sort the key by index, use a key arraylist instead.


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
    speed_dic = {"200":15, "300":15, "400":15, "600":15, "1000":11.428, "1300":13.333}
    time_dic = {"200":200/15, "300":100/15, "400":100/15, "600":200/15, "1000":400/11.428, "1300":300/13.333}
    overall_time_dic = {"200":13.5, "300":20, "400":27, "600":40, "1000":75}
    
    
    
    for i in range (len(time_dic)):
      if (int(time_dic.key()[i]) < brevet_dist_km):
          if (int(time_dic.key()[i]) <= control_dist_km):  # check the key value of the pair
              control_time += time_dic.value()[j]         # add the the value of that key to the total_time. #This method is quite redundent, since it have to loop in 5 brevet_dist_km every time.    
          else:
              addition_time = (int(speed_dic.key()[i]) - control_dist_km) / speed_dic.value()[i]
              total_time = control_time + addition_time
            # end of adding time when reach the brevet_dist_km, as long as reach the brevet_dist_km, do nothing to the data.
      elif (control_dist_km == brevet_dist_km):
          total_time = overall_time_dic.value()[i]
    control_close = brevet_start_time + timedelta(hours=total_time)
    return control_close
