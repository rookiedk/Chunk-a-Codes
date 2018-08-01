def all_files_under(path):
    """Iterates through all files in the given path."""
    for cur_path, dirnames, filenames in os.walk(path):
        for filename in filenames:
            yield os.path.join(cur_path, filename)

path = 'Complete Path To Your Directory'
last_updated file = max(all_files_under(realised_stats_report), key=os.path.getmtime)