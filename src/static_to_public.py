import os
import shutil

def static_to_public(src_dir, dest_dir):


    #absolute paths to source and destination
    src_abs_path = os.path.abspath(src_dir)
    #results to -> juice/bootdotdev/2aproj/aiagent/functions/static
    dest_abs_path = os.path.abspath(dest_dir)
    # results to -> juice/bootdotdev/2aproj/aiagent/functions/public

    
   
    #deletes everything in public as long as path exists
    if os.path.exists(dest_abs_path) == True:
        shutil.rmtree(dest_abs_path)
    # creates the public directory no matter what, in the destination path 
    os.mkdir(dest_abs_path)


    
    if os.path.exists(src_abs_path) == True:
        #makes a list of contenst in src path 

        src_list = os.listdir(src_abs_path)

        for obj in src_list:
            #if obj in src path is a file, it copies it to target
            if os.path.isfile(os.path.join(src_abs_path, obj)):
                shutil.copy(os.path.join(src_abs_path,obj), dest_abs_path)
            else:
                #if obj is dir, create dir in destination 
                # recursion creates the dir in the call below 
                #copy over remaining items in sub dirs
                static_to_public(os.path.join(src_abs_path, obj), os.path.join(dest_abs_path, obj))


    # source = static (static_site_generator/static)
    # destination = public (static_site_generator/public)


# os.path.exists -> return true if path exists
# os.listdir -> return a list containing the names of the entries in the directory given by path
# os.path.join -> joins two paths intelligently 
# os.path.isfile -> return true if path is an existing regular file

# os.mkrdir -> creates a directory named path
# shutil.copy -> copies the file src to the file or directory dst
# shutil.rmtree -> deletes entire directory tree
