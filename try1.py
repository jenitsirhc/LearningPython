import DVDclass
DVDstock = []
try:
    data = open("DVDList.cvs")
    for line in data:
            columns = line.split(',')
            titlenew = columns [0]
            star1new = columns [1]
            star2new = columns [2]
            producernew = columns [3]
            directornew = columns [4]
            compnew = columns [5]
            nonew = int(columns [6])

            info = DVDclass.dvdType(titlenew, star1new, star2new, producernew, directornew, compnew, nonew)
            DVDstock.append(info)

except Exception as e:
        print(e)
        
finally:
        data.close()