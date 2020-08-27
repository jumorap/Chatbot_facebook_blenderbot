import subprocess

# IF DOESN'T WORKS, YOU CAN COPY PAST THE VARIABLES IN YOUR CMD. THIS CAN BE OPEN
# WITH THE KEYS "WINDOWS" + "R", AND AFTER WRITE 'CMD'. REMEMBER SELECT JUST ONE OF THE
# THREE MODELS. I RECOMMEND TO USE [use_90M_model] TO START

# In this case we are using Facebook BlenderBot 2.7B, but we can change to
# the FacebookIA into Small model [use_90M_model], Medium model [use_3B_model]
# and Big model [use_9B_model]
#
# The command lines be saved in variables like "plain strings" to be saved in
# an array [work_list], and is generated an empty array [queue] to pass it in a loop
verify = f'nvidia-smi'
git_clone = f'git clone https://github.com/facebookresearch/ParlAI.git'
to_parl = f'cd ParlAI'
execute_py = f'python setup.py develop'
install_git_repo = f'pip install "git+https://github.com/rsennrich/subword-nmt.git#egg=subword-nmt"'
use_90M_model = f'python parlai/scripts/interactive.py -t blended_skill_talk -mf zoo:blender/blender_90M/model'
use_3B_model = f'python parlai/scripts/interactive.py -t blended_skill_talk -mf zoo:blender/blender_3B/model'
use_9B_model = f'python parlai/scripts/interactive.py -t blended_skill_talk -mf zoo:blender/blender_9B/model'
work_list = [verify, git_clone, to_parl, execute_py, install_git_repo, use_3B_model]
queue = []

# Ingress into the "for loop" the array with the strings [work_list] to after
# use comprehension and separate word to word the string in the array, this is necessary
# because 'subprocess.call', that was imported before require pass in an array
# word to word the command that gonna use
for ingress in work_list:
    queue.append([x for x in ingress.split()])

# To make easy the work of execute line to line the strings into the terminal, was
# used 'subprocess.call' with comprehension. This permit execute like a command the
# strings taught before
processing = [subprocess.call(execute, shell=True) for execute in queue]


