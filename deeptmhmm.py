import time
import biolib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# deeptmhmm time benchmark

try:
    dt_start = time.perf_counter()

    deeptmhmm = biolib.load('DTU/DeepTMHMM')

    # Fasta (protein):
    # './ncbi_dataset/data/GCF_000300575.1/protein.faa'

    deeptmhmm_job = deeptmhmm.cli(
        args='--fasta ./ncbi_dataset/data/GCF_000300575.1/protein.faa')

    deeptmhmm_job.save_files('result')

    dt_end = time.perf_counter()
    dt_total_time = dt_end - dt_start
    print("deeptmhmm time: ")
    print(dt_total_time)

    img = mpimg.imread('result/plot.png')
    plt.imshow(img)
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")
