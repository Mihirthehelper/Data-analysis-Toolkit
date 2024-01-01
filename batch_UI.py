from load_data import *
from sort import *
from curve_fit import *
from histogram import *



file_name = input("Please enter the file where your command is stored: ")

batch_file = open(file_name)

for line in batch_file:
    items = line.split(";")
    command = (items[0])
    
    for x in command:
        if x.upper() == 'L':
            file = items[1]
            att_l = items[2]
            value = items[3].strip('\n')
            result_l = load_data(file, (att_l, value))
            if result_l != []:
                result_l = add_average_main_memory(result_l)
            
            
            print('Data loaded.')
           
            
        elif x.upper() == 'S':
            att_s = items[1]
            order = items[2]
            display = items[3].strip('\n')
            result_s = sort(result_l, order, att_s)
            if display.upper() == 'Y':
                print(result_s)
            
            print('Data sorted.')
        elif x.upper() == 'C':
            att_c = items[1]
            order_of_poly = items[2]
            result_c = curve_fit(result_l, att_c, order_of_poly)
            
        elif x.upper() == 'H':
            att_h = items[1]
            result_h = histogram(result_l, att_h)
            
            print(result_h)
        
        elif x.upper() == 'E':
            break
        
        else:
            break
            
    
        
   

batch_file.close()
