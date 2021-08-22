def swapFileData():
    
        file1 = input("enter the original file: ")
        file2 = input("enter the file to be swapped: ")
        
# r for read only 
# r+ for read and write

  with open(file1, 'r') as a:
       data_a = a.read()
  with open(file2, 'r') as b:
    data_b = b.read()
  

# w for write only
# w+ for write and read 

  with open(file1, 'w+') as a:
      a.write(data_)
 with open(file2, 'w+') as b:
      b.write(data_a)


swapFileData()
