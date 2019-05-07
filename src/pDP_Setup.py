#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:09:32 2019

@author: Eric Allen
Last Modified: 7 May 2019 at 12:00PM

.....DEPRICATE ONCE ON CONDA.....
    I do not like using the OS_SYSTEM because it has limited definition and I
    think that Windows is moving/moved to 64-bit. Not a windows user so not sure.
    
    ---------------------------------------------------------------------------

    The following code should take care of the python modules as long as you
    have downloaded/installed Anaconda (Python3) and EXIFTOOLS by Phil Harvey.
    Also a guide on how to install python through the source.
 
    1. Download EXIFTOOL: http://owl.phy.queensu.ca/~phil/exiftool/
        http://owl.phy.queensu.ca/~phil/exiftool/install.html    
        
    2. Download Python 3.6
        https://www.python.org/downloads/
        https://www.anaconda.com/distribution/#download-section 
        (I personally like Anaconda)
        
    3. Grant Python/Anconda Full Disk Access (to allow it to access the Photos
                                              App on macOS)
        https://macpaw.com/how-to/full-disk-access-mojave     
        
    4. Install pydatpicture with (Anaconda) conda install -c allenea pydatpicture 
        or by downloading on github and installing the required modules.
        
    If you are using Anaconda and downloaded from github, then this script 
    should help install any modules you haven't installed but need (not tested).
    
    If not it will tell you what you need to install and hopefully get you started.

#####
    Otherwise:
        
    5. Install dateutil for Python (This should come preinstalled along with:
        os, sys, shutil, getpass, and pathlib) https://pypi.org/project/DateTime/  
        
    6. Install Numpy for Python
        https://scipy.org/install.html
        conda install -c anaconda numpy 

    7. Install Pandas for Python
        https://pandas.pydata.org/pandas-docs/stable/install.html  
                (you may need some additional packages... see link)
        conda install -c conda-forge pandas

    8. Install Cartopy for Python
        https://scitools.org.uk/cartopy/docs/latest/installing.html
        conda install -c conda-forge cartopy
    
    9. Install Geopy for Python
        https://geopy.readthedocs.io/en/stable/#installation
        conda install -c conda-forge geopy 


"""
def setup_pyDatPicture():

    try:
        import getpass
        import os
        import sys
        import shutil
        import pathlib
    except:
        print("One or more (typically) pre-installed python modules are ",\
              "not installed: getpass, os, sys, shutil")
        return False
    
    USER_ID = getpass.getuser()
    OS_SYSTEM = sys.platform
    
    isEXIFTOOL = shutil.which("exiftool")
    
    #Anaconda Environment
    if 'Anaconda' in sys.version:
        try:
            import conda.cli
            import numpy
            import pandas
            import matplotlib.pyplot
            import cartopy
            import datetime
            import geopy
            import geopy.geocoders
            from geopy.geocoders import Nominatim
        except:        
            if 'numpy' in sys.modules:  pass 
            else:   conda.cli.main('conda', 'install',  '-y', '-c',\
                                   'anaconda', 'numpy');
            
            if 'pandas' in sys.modules:     pass
            else:   conda.cli.main('conda', 'install',  '-y', '-c',\
                                   'conda-forge','pandas')
            
            if 'matplotlib' in sys.modules:    pass 
            else:   conda.cli.main('conda', 'install',  '-y', '-c',\
                                   'conda-forge', 'matplotlib')
            
            if 'cartopy' in sys.modules:    pass
            else:   conda.cli.main('conda', 'install',  '-y', '-c',\
                                   'conda-forge','cartopy')
            
            if 'datetime' in sys.modules:    pass
            else:   conda.cli.main('conda', 'install',  '-y',  '-c',\
                                   'anaconda', 'dateutil'); 
        
            if 'geopy' in sys.modules:    pass
            else:   conda.cli.main('conda', 'install',  '-y', '-c',\
                                   'conda-forge','geopy')
        
            # MAKE SURE THEY CAN BE IMPORTED AFTER THE INSTALL
            try:
                import numpy
                import pandas
                import matplotlib.pyplot
                import cartopy
                import datetime
                import geopy
                import geopy.geocoders
                from geopy.geocoders import Nominatim
            except:
                print("Could not import one or more of the modules - "\
                      "Anaconda.\nTry restarting Anaconda and re-run the ",\
                      "program otherwise follow the documentation to download ",\
                      "the necessary modules." )
                return False
            
    else: # Not Anaconda environment
        try:
            import numpy
            import pandas
            import matplotlib.pyplot
            import cartopy
            import datetime
            import geopy
            import geopy.geocoders
            from geopy.geocoders import Nominatim
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
            else:   print("DATEUTIL/DATETIME MODULE NOT INSTALLED")
            
            if 'geopy' in sys.modules:    pass
            else:   print("GEOPY MODULE NOT INSTALLED")
            return False
    
    
    # Is EXIFTOOLS INSTALLED - No, then do this
    if isEXIFTOOL == None:
        try:    
            import wget
        except: 
            print("Warning: Missing the wget package. Not found by pDP_Setup.")
            return False
        # linux
        if OS_SYSTEM == "linux" or OS_SYSTEM == "linux2":
            print("WARNING: Linux May or May Not Be a Supported (suppressed)") 
            pass
            
        # OS X
        elif OS_SYSTEM == "darwin": 
            APPS_DIR = os.path.join("/","Users", USER_ID, "Desktop")  #macos
            if not os.path.exists(APPS_DIR):   
                print("Invalid Path to Applications Folder....edit line 141 ",\
                      "in pyDatPicture.py")
                return False
            getFile = "https://sno.phy.queensu.ca/~phil/exiftool/ExifTool-11.39.dmg"
            outfile = APPS_DIR+ "ExifTool-11.39.dmg" 
            try:
                os.remove(outfile) 
                # Make sure there isn't already a file that hasn't been installed
            except OSError:
                pass
            wget.download(getFile, outfile)    
            print("EXIFTOOL NOT INSTALLED. SOFTWARE DOWNLOADED TO: "+APPS_DIR +\
                  "\n Follow download instructions on ",\
                  "http://owl.phy.queensu.ca/~phil/exiftool/install.html")
            return False
            
        # Windows...
        elif OS_SYSTEM == "win32" or OS_SYSTEM == "cygwin":
            APPS_DIR = os.path.join( "C:", "Users", USER_ID,"Desktop")  #macos
            if not os.path.exists(APPS_DIR):   
                print("Invalid Path to Applications Folder....edit line 142 ",\
                      "in pyDatPicture.py")
                return False
            
            getFile = "https://sno.phy.queensu.ca/~phil/exiftool/"
            outfile = APPS_DIR+ "exiftool-11.39.zip" 
            try:
                os.remove(outfile) 
                # Make sure there isn't already a file that hasn't been installed
            except OSError:
                pass
            wget.download(getFile, outfile)    
            print("EXIFTOOL NOT INSTALLED. SOFTWARE DOWNLOADED TO: "+APPS_DIR +\
                  "\n Follow download instructions on ",\
                  "http://owl.phy.queensu.ca/~phil/exiftool/install.html")
            return False
        else:
            print("WARNING: Unknown Operating System. Please install the software")
            return False
    
    else:
        print("EXIFTOOLS by Phil Harvey is already installed on your system...",\
              " Continuing....\n\n")
        pass

    return True