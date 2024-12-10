import subprocess
import csv
import os
import shlex

# Example Programs and Flags
programs = ["data/raw/matrix_mul.c", "data/raw/bubble_sort.c"]
flags = ["-O1", "-O2", "-O3"]

# Output Directory for Compiled Binaries
output_dir = "data/processed/binaries"
os.makedirs(output_dir, exist_ok=True)

# Collect Performance Data
data = []
for program in programs:
    for flag in flags:
        # Generate Output Binary Path
        program_name = os.path.basename(program).split('.')[0]
        output = os.path.join(output_dir, f"{program_name}_{flag}.out")
        
        # Compile the Program
        compile_cmd = ["clang", flag, "-o", output, program]
        try:
            subprocess.run(compile_cmd, check=True)
        except subprocess.CalledProcessError:
            print(f"Compilation failed for {program} with {flag}")
            continue
        
        # Measure Runtime
        run_cmd = f"/usr/bin/time -f '%e' ./{output}"
        try:
            result = subprocess.run(
    shlex.split(run_cmd),
    stdout=subprocess.PIPE,  # Capture standard output
    stderr=subprocess.PIPE,  # Capture standard error
    text=True
)
            runtime = float(result.stderr.strip())

            data.append({"program": program, "flag": flag, "runtime": runtime})
        except Exception as e:
            print(f"Execution failed for {output}: {e}")
            continue

# Save Data to CSV
output_csv = "data/processed/metrics.csv"
os.makedirs(os.path.dirname(output_csv), exist_ok=True)
with open(output_csv, "w") as f:
    writer = csv.DictWriter(f, fieldnames=["program", "flag", "runtime"])
    writer.writeheader()
    writer.writerows(data)

print(f"Performance data saved to {output_csv}")

