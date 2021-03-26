import os


def layout():
    # define the name of the directory to be created
    directory = input(str("please enter your project name"))
    path = "//Users//tumisangtshikare//Documents//Cookie_monster//{}".format(directory)
    # define the access rights
    access_rights = 0o755
    try:
        os.mkdir(path, access_rights)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s" % path)
        

    # Check if New path exists
    if os.path.exists(path) :
        # Change the current working Directory    
        os.chdir(path)
    else:
        print("Can't change the Current Working Directory")   
        
    try:
        os.mkdir("preprocessing",access_rights)
        os.mkdir("model",access_rights)
        os.mkdir("data",access_rights)
        os.mkdir("tests",access_rights)
    except OSError:
        print ("Creation of the directory preprocessing failed")
    else:
        print ("Successfully created the subdirectries %s" % path)

###########################################################################3
    # Check if New path exists
    if os.path.exists(path+"//preprocessing//") :
        # Change the current working Directory    
        os.chdir(path+"//preprocessing//")
    else:
        print("Can't change the Current Working Directory")   
        
        
    with open('__init__.py', 'w') as fp:
        pass
    with open('runner.py', 'w') as fp:
        pass
    with open('helpers.py', 'w') as fp:
        pass
    with open('preprocessing.py', 'w') as fp:
        pass
    with open('preprocessing_note.ipynb', 'w') as fp:
        pass
################################################################
        # Check if New path exists
    if os.path.exists(path+"//model//") :
        # Change the current working Directory    
        os.chdir(path+"//model//")
    else:
        print("Can't change the Current Working Directory")   
    with open('model.py', 'w') as fp:
        pass
    with open('__init__.py', 'w') as fp:
        pass
    with open('runner.py', 'w') as fp:
        pass
    with open('helpers.py', 'w') as fp:
        pass
    with open('model_note.ipynb', 'w') as fp:
        pass    
##################################################################
    if os.path.exists(path+"//data//") :
        # Change the current working Directory    
        os.chdir(path+"//data//")
    else:
        print("Can't change the Current Working Directory")  
        

    with open('input.csv', 'w') as fp:
        pass
    with open('output.csv', 'w') as fp:
        pass
    with open('analysis.csv', 'w') as fp:
        pass
    with open('data_note.ipynb', 'w') as fp:
        pass
    
############################################################################3
    os.chdir(path+"//tests//")
    try:
        os.mkdir("preprocessing",access_rights)
        os.mkdir("model",access_rights)
        os.mkdir("data",access_rights)
        os.mkdir("tests",access_rights)
    except OSError:
        print ("Creation of the directory preprocessing failed")
    else:
        print ("Successfully created the subdirectries %s" % path)
    if os.path.exists(path+"//tests//preprocessing") :
        # Change the current working Directory    
        os.chdir(path+"//tests//preprocessing")
    else:
        print("Can't change the Current Working Directory")  
    with open('helpers_tests.py', 'w') as fp:
        pass
    with open('preprocessing_tests.py', 'w') as fp:
        pass   
    
    if os.path.exists(path+"//tests//model") :
        # Change the current working Directory    
        os.chdir(path+"//tests//model")
    else:
        print("Can't change the Current Working Directory")  
    with open('helpers_tests.py', 'w') as fp:
        pass
    with open('model_tests.py', 'w') as fp:
        pass  
if __name__ == '__main__':
    layout()