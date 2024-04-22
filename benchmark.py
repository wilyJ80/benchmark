import time
import biolib
from mymetal import mbp, iof

# deeptmhmm time benchmark

dt_start = time.process_time()

deeptmhmm = biolib.load('DTU/DeepTMHMM')

# Fasta (protein):
# './ncbi_dataset/data/GCF_000300575.1/protein.faa'

deeptmhmm_job = deeptmhmm.cli(
    args='--fasta ./ncbi_dataset/data/GCF_000300575.1/protein.faa')

deeptmhmm_job.save_files('result')

dt_end = time.process_time()
dt_total_time = dt_end - dt_start
print("deeptmhmm time: ")
print(dt_total_time)

# mymetal time benchmark

mm_start = time.process_time()

a = mbp.predict('./ncbi_dataset/data/GCF_000300575.1/protein.faa')
iof.save_out_csv(a, 'mymetal_output.csv')

mm_end = time.process_time()
mm_total_time = mm_end - mm_start
print("mymetal time: ")
print(mm_total_time)
