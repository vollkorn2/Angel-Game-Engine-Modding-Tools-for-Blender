#   BlenderHelper by                vollkorn2   (Github: vollkorn2 / YT: SoGTA in UE5)
#   dave.py by                      EdnessP     (Github: EdnessP )
#   Description:                    Run dave.py easily without installing Python or reading lots of Tutorials just to run this Script.
#   Supported:                      Extracting and Building Dave/DAVE Archives made with Angel Game Engine. (.dat/.zip)
#   Alternative Tools:              ar_extract by Volky (Extracting Only) 

#   v1.0    07.02.2026

Operation = "Extract_Dave"    # "Extract_Dave"   /   "Build_Dave"



# All Paths must end with "/" and all other Slashes must be also this direction "/"

PathToEdnessP = "D:/This/Could/Be/Your/FilePath/Leading/To/EdnessP_Dave.py"
MainInputPath = "D:/This/Could/Be/Your/FilePath/Leading/To/FoldersToBuildDats"
OutputPath = "D:/This/Could/Be/Your/FilePath/Leading/To/NewDatsFolder"

# The SubFolder leading to your DAT Files to Build/Extract. (Directory of YOUR Extracted DATs (Build)   OR   of the Original Game Files (Extract))
SubFolder = "LVLS_M2/BRIDGE2"    # "BANKS"   /   "LVLS_SNG/PERFNEW"


# Extract Dat Options.  *****************************************************************************************

# Not yet Supported


# Build Dat Options.    *****************************************************************************************
#   for Red Dead Revolver: 
#   SWAT.DAT and All Levels including FRONT.DAT are Dave Compressed
#   All other .DATs are DAVE Uncompressed

# The Name of the .dat is taken from the Folder.
FileExt = ".DAT"            # ".DAT" / ".dat" / ".ZIP" / ".zip"     (ZIP must be in DAVE, CompressNames = False)
CompressFiles = False
CompressNames = False        # False = DAVE / True = Dave
BuildDirectories = True

ForceComp = 0           
CompressionLevel = 6    # (1-9)
Align = 128             # (16 or 128)
CompAlign = False       





# ****************************************************************************************************************************************************************************************************************

import re
import sys                      # Add Temporary SystemPath to find External Modules 
sys.path = [PathToEdnessP]      # This makes External Python Scripts run without installation
from dave import build_dave, read_dave


print("*** Start ********************************************************************************")

InputPath = MainInputPath+SubFolder
DatName = re.split(r'/', InputPath)
DatName = DatName[len(DatName)-1]+".DAT"   # Get Last Folder for DAT Name

if Operation == "Build_Dave":
    #         (inpath, output, compfiles=False, forcecomp=0, complevel=9, compnames=False, dirs=False, align=128, compalign=False)
    build_dave(InputPath, OutputPath+DatName, CompressFiles, ForceComp, CompressionLevel, CompressNames, BuildDirectories, Align, CompAlign) 

if Operation == "Extract_Dave":
    #        (path, output=str())
    read_dave(InputPath+".DAT", OutputPath+SubFolder)
    

print("Finished!   (EdnessBlenderHelper)")
