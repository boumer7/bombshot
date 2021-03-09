import pkg_resources
import subprocess

packages = [dist.project_name for dist in pkg_resources.working_set]

subprocess.call("pip install --upgrade " + ' '.join(packages), shell=True)
subprocess.call("pip3 install --upgrade " + ' '.join(packages), shell=True)

