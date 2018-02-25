from datetime import datetime

with open("input_data/demo_input_data.txt", "r") as infile, open("input_data/customer.csv", "w") as cust_file, open("input_data/purchase.csv", "w") as purchase_file:
    i = 0;
    load_time = str(datetime.now())
    for line in infile:
        ## outfile.write(line.split("<_|_>")[0])
        ## print (i, line)

        tmp_list = line.strip().split("\t")

        cust_id  = tmp_list[0]
        cust_first_name = tmp_list[1]
        cust_last_name  = tmp_list[2]
        cust_address    = tmp_list[3]
        cust_state      = tmp_list[4]
        cust_zip        = tmp_list[5]

        purchase_status = tmp_list[6]   # 'new' or 'canceled'
        product_id      = tmp_list[7]
        product_name    = tmp_list[8]
        purchase_amt    = tmp_list[9]
        date_time       = tmp_list[10]

        date_time = date_time[0:10] + " " + date_time[10:]

        print (i, tmp_list)
        print (i, cust_id, cust_first_name, cust_last_name, cust_address, cust_state, cust_zip, date_time, load_time )
        print (i, purchase_status, product_id, product_name, purchase_amt, date_time, load_time)

        cust_line = ",".join([str(cust_id), cust_first_name, cust_last_name, cust_address, cust_state, cust_zip, date_time, load_time]) + '\n'
        purchase_line = ",".join([str(cust_id), purchase_status, str(product_id), product_name, str(purchase_amt), date_time, load_time]) + '\n'

        cust_file.write(cust_line)
        purchase_file.write(purchase_line)

        i = i + 1
