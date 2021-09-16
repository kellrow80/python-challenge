import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

change_list = []
month_list = []


with open (csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
 
    csv_header = next(csvreader)
              
    num_rows = 0
    total = 0
    row1 = next(csvreader)
    previous_row = int(row1[1])



     
    
    for row in csvreader:
        num_rows += 1  
        total += int(row[1])
        monthly_change = int(row[1]) - previous_row
        previous_row = int(row[1])
        change_list += [monthly_change]
        month_list += [row[0]]
    
    month_average = sum(change_list)/len(month_list)

    
    print("Total # of months: " + str(num_rows))
    print("Total Profit/Loss: " + str(total))
    print("Average Change: "+ str(month_average))






    # for row in csvreader:
    #     profit_loss = [row[1]]        
    #     for x in profit_loss:
            
    #         print(x)



    
    
    

     

        

        

            

    
    




       

   










        


    









        










        



    