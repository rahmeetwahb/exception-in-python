try:
    #open file
    f = open('data.txt', 'w')

    try:
        #write data from file
        f.write('Pemrograman')
    finally:
        f.close() #closed file

except IOError:
    print('Error file not found')