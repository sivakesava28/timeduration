import source_code

def main():
    
    str_created_time =  "2017-2-29T08:30:27.119045211Z"
    str_current_time =  "2019-5-19T04:40:47.119045211Z"
    elapsed_str = source_code.Exact_time(str_created_time,str_current_time)
    print(elapsed_str)
    
if (__name__ == "__main__"):
   main()