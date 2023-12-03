import os
import sys
import subprocess
import glob


def run_test(prog, test_name):
    input_file = f"test/{prog}.{test_name}.in"
    expected_output_file = f"test/{prog}.{test_name}.out"
    map_file = "quest.map"

    with open(input_file, 'r') as infile:
        command = ['python', f'{prog}.py', map_file]
        result = subprocess.run(command, stdin=infile,
                                stdout=subprocess.PIPE, text=True)

    if result.returncode != 0:
        return "TestResult.NonZeroExit"

    try:
        with open(expected_output_file, 'r') as outfile:
            expected_output = outfile.read()
    except FileNotFoundError:
        return "TestResult.MissingOutputFile"

    if result.stdout != expected_output:
        return f"TestResult.OutputMismatch Expected: {expected_output} Got: {result.stdout}"

    return "OK"


def main():
    test_files = glob.glob('test/*.in')
    results = {"OK": 0, "TestResult.OutputMismatch": 0,
               "TestResult.NonZeroExit": 0, "TestResult.MissingOutputFile": 0}

    for test_file in test_files:
        basename = os.path.basename(test_file)
        prog, test_name = basename.split('.')[0], basename.split('.')[1]

        result = run_test(prog, test_name)
        results[result] += 1
        if result != "OK":
            print(f"\nFAIL: {prog} {test_name} failed ({result})")

    # Print summary
    print("\nOK:", results["OK"])
    for key, value in results.items():
        if key != "OK":
            print(f"{key}: {value}")
    print("total:", sum(results.values()))

    # Exit with non-zero status if any tests failed
    if sum(results.values()) - results["OK"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
