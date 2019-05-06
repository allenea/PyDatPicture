#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:09:32 2019

@author: ericallen

    The following code should take care of the python modules as long as you have downloaded/installed
    Anaconda (Python3) and EXIFTOOLS by Phil Harvey. Also a guide on how to install python through the source.
 
    1. Download EXIFTOOL: http://owl.phy.queensu.ca/~phil/exiftool/
        http://owl.phy.queensu.ca/~phil/exiftool/install.html    
        
    2. Download Python 3.6
        https://www.python.org/downloads/
        https://www.anaconda.com/distribution/#download-section (I personally like Anaconda)
        
    3. Grant Python/Anconda Full Disk Access (to allow it to access the Photos App on macOS)
        https://macpaw.com/how-to/full-disk-access-mojave     
        
        
    If you are using Anaconda this script should install any modules you haven't installed but need.
    If not it will tell you what you need to install and hopefully get you started.
        
    4. Install Numpy for Python
        https://scipy.org/install.html
        conda install -c anaconda numpy 

    5. Install Pandas for Python
        https://pandas.pydata.org/pandas-docs/stable/install.html  (you may need some additional packages... see link)
        conda install -c anaconda pandas 

    6. Install Cartopy for Python
        https://scitools.org.uk/cartopy/docs/latest/installing.html
        conda install -c conda-forge cartopy

    7. Install Datetime for Python (This should come preinstalled along with: os, sys, shutil, getpass.)
        https://pypi.org/project/DateTime/

"""
def setup_pyDatPicture():

    try:
        import getpass, os, sys,shutil,pathlib
    except:
        print("One or more (typically) pre-installed python modules are not installed: getpass, os, sys, shutil")
        return False
    
    USER_ID = getpass.getuser()
    OS_SYSTEM = sys.platform
    
    isEXIFTOOL = shutil.which("exiftool")
    
    
    if 'Anaconda' in sys.version:
        try:
            import conda.cli
            import numpy, pandas, matplotlib.pyplot, cartopy, datetime

        except:        
            if 'numpy' in sys.modules:  pass 
            else:   conda.cli.main('conda', 'install',  '-y', 'numpy');
            
            if 'pandas' in sys.modules:     pass
            else:   conda.cli.main('conda', 'install',  '-y', 'pandas')
            
            if 'matplotlib' in sys.modules:    pass 
            else:   conda.cli.main('conda', 'install',  '-y', 'matplotlib')
            
            if 'cartopy' in sys.modules:    pass
            else:   conda.cli.main('conda', 'install',  '-y', 'cartopy')
            
            if 'datetime' in sys.modules:    pass
            else:   conda.cli.main('conda', 'install',  '-y', 'datetime') ## Not 100% sure this is right since this usually comes pre-installed.
        
            # MAKE SURE THEY CAN BE IMPORTED AFTER THE INSTALL
            try:
                import numpy, pandas, matplotlib.pyplot, cartopy, datetime
            except:
                print("Could not import one or more of the modules - Anaconda.\nTry restarting Anaconda and re-run the program otherwise follow the documentation to download the necessary modules." )
                return False
            
    else: # Not Anaconda environment
        try:
            import numpy,pandas,matplotlib.pyplot,cartopy,datetime
        except:
            if 'numpy' in sys.modules:  pass 
            else:   print("NUMPY MODULE NOT INSTALLED")
            
            if 'pandas' in sys.modules:     pass
            else:   print("PANDAS MODULE NOT INSTALLED")
            
            if 'matplotlib' in sys.modules:    pass 
            else:   print("MATPLOTLIB MODULE NOT INSTALLED")
            
            if 'cartopy' in sys.modules:    pass
            else:   print("CARTOPY MODULE NOT INSTALLED")
            
            if 'datetime' in sys.modules:    pass
            else:   print("DATETIME MODULE NOT INSTALLED")
            return False
    
    
    
    if isEXIFTOOL == None:
        try:    import wget
        except: print("Warning: Missing the wget.py package. Not found by pDP_Setup."); return False
        
        if OS_SYSTEM == "linux" or OS_SYSTEM == "linux2":
            print("WARNING: Linux May or May Not Be a Supported System (suppressed)") 
            pass
            # linux
            
            
        elif OS_SYSTEM == "darwin": 
            APPS_DIR = os.path.join("/","Users", USER_ID, "Desktop")  #macos
            if not os.path.exists(APPS_DIR):   
                print("Invalid Path to Applications Folder....edit line 141 in pyDatPicture.py")
                return False
            getFile = "https://sno.phy.queensu.ca/~phil/exiftool/ExifTool-11.39.dmg"
            outfile = APPS_DIR+ "ExifTool-11.39.dmg" 
            try:
                os.remove(outfile) # Make sure there isn't already a file that that just hasn't been installed
            except OSError:
                pass
            wget.download(getFile, outfile)    
            print("EXIFTOOL NOT INSTALLED. SOFTWARE DOWNLOADED TO: "+APPS_DIR +"\n Follow download instructions on http://owl.phy.queensu.ca/~phil/exiftool/install.html")
            return False
            # OS X
            
            
        elif OS_SYSTEM == "win32":
            APPS_DIR = os.path.join( "C:", "Users", USER_ID,"Desktop")  #macos
            if not os.path.exists(APPS_DIR):   
                print("Invalid Path to Applications Folder....edit line 142 in pyDatPicture.py")
                return False
            
            getFile = "https://sno.phy.queensu.ca/~phil/exiftool/"
            outfile = APPS_DIR+ "exiftool-11.39.zip" 
            try:
                os.remove(outfile) # Make sure there isn't already a file that that just hasn't been installed
            except OSError:
                pass
            wget.download(getFile, outfile)    
            print("EXIFTOOL NOT INSTALLED. SOFTWARE DOWNLOADED TO: "+APPS_DIR +"\n Follow download instructions on http://owl.phy.queensu.ca/~phil/exiftool/install.html")
            return False
            # Windows...
    
    else:
        print("EXIFTOOLS by Phil Harvey is already installed on your system.... Continuing....\n\n")
        pass

    return True