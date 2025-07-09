# try and except explanation
try:
    print('raman')
    # print(raman)
except NameError:
    print("error occured")#run when error in try
else:
    print("done")#run when try is correct
finally:
    print("code done")# run everytime
