def copy_dir(dir1, dir2):
    import shutil
    try:
        shutil.copytree(dir1, dir2)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)