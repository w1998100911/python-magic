
import subprocess
import os.path
import sys

this_dir = os.path.dirname(sys.argv[0])

new_env = {
    'LC_ALL': 'en_US.UTF-8',
    'PYTHONPATH': os.path.join(this_dir, ".."),
}

def has_py(version):
    ret = subprocess.run("which %s" % version, shell=True, stdout=subprocess.DEVNULL)
    return ret.returncode == 0

def run_test(versions):

    found = False
    for i in versions:
        if not has_py(i):
            # if this version doesn't exist in path, skip
            continue
        found = True
        print("Testing %s" % i)
        subprocess.run([i, os.path.join(this_dir, "test.py")], env=new_env, check=True)

    if not found:
        sys.exit("No versions found: " + str(versions))

run_test(["python2", "python2.7"])
run_test(["python3.5", "python3.6", "python3.7", "python3.8"])
