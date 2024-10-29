import sys, os, re, subprocess

subject_list_path = '/media/labs/rsmith/lab-members/cgoldman/Wellbeing/advise_task/fitting_actual_data/advise_subject_IDs_prolific.csv'
results = '/mnt/dell_storage/labs/rsmith/lab-members/fli/advise_task/results/'

if not os.path.exists(results):
    os.makedirs(results)
    print(f"Created results directory {results}")

if not os.path.exists(f"{results}/logs"):
    os.makedirs(f"{results}/logs")
    print(f"Created results-logs directory {results}/logs")

subjects = []
with open(subject_list_path) as infile:
    for line in infile:
        if 'ID' not in line:
            subjects.append(line.strip())

ssub_path = '/mnt/dell_storage/labs/rsmith/lab-members/fli/advise_task/Active-Inference-Model-for-Advise-Task/run_advise_identifiability.ssub'

for idx_candidate in [1,2,3,4,5,6,7,8,9,10]:
    for subject in subjects:
        stdout_name = f"{results}/logs/{subject}-%J.stdout"
        stderr_name = f"{results}/logs/{subject}-%J.stderr"
        jobname = f'advise-fit-{subject}'
        os.system(f"sbatch -J {jobname} -o {stdout_name} -e {stderr_name} {ssub_path} {subject} {results} {idx_candidate}")

        print(f"SUBMITTED JOB [{jobname}]")