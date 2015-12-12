from subprocess import *
import random
import sys

class ImproperFormatError(Exception):
    pass

def main():
    if len(sys.argv) < 3:
        print(
            "Invalid # of arguments. Usage: AutoTester.py #cases exe_path", file=sys.stderr)
        return
    try:
        N_TESTCASES = int(sys.argv[1])
    except ValueError:
        print("Incorrect  #cases formatting.", file=sys.stderr)
        return
    # Generate the testcases
    print("Generating Test Cases...")
    test_cases = []
    N_MAXNUMS = 12  # maximum number of integer terms in the input
    N_MAXINT = 50  # maximum value of an integer
    BRACKET_PROB = 0.44  # probability of a bracket appearing
    for i in range(N_TESTCASES):
        # create list of rand numbers
        num_seq = random.sample(range(1,N_MAXINT), random.randint(1,N_MAXNUMS))
        num_seq = list(map(str, num_seq))
        # randomly insert operators
        operators = ('*', '/', '+', '-')
        for i in range(1, len(num_seq) * 2 - 1, 2):
            num_seq.insert(i, random.choice(operators))

        # randomly insert brackets
        for i, item in enumerate(num_seq):
            if item in operators:
                if (random.random() < BRACKET_PROB):
                    # insert first bracket
                    num_seq.insert(i + 1, "(")
                    # insert its complementary pair
                    while True:
                        j = random.randint(i + 1, len(num_seq) - 1)
                        if num_seq[j] != "(" and num_seq[j] not in operators:
                            num_seq.insert(j + 1, ")")
                            break
        test_cases.append("".join(num_seq))
    print("Done.\nRunning Program...")
    try:
        output = getOutput(test_cases, sys.argv[2])
    except FileNotFoundError:
        print("'" + sys.argv[2] + "' Not found.", file=sys.stderr)
        return
    except ImproperFormatError:
        print("Program does not have the correct output format.",file=sys.stderr)
        return
    print("Done.\nEnumerating Test Cases...")
    wrong = 0
    for i, test in enumerate(test_cases):
        print("Test #", i + 1)
        print("Expression:\t", test)
        print("Program Answer:\t", output[i])
        correct = float("{:.2f}".format(eval(test)))
        print("Correct Answer:\t", correct)
        error = abs(output[i] - correct)
        if error == 0:
            print("PASS")
        elif error < 0.1:
            print("PASS, WARNING!", error, "error detected")
        elif error < 1:
            print("WARNING! Large error of", error, "detected")
        else:
            print("FAIL! Extreme error of", error,
                  "detected")  # ,file=sys.stderr)
            wrong += 1
        print("-----------------------------------------")
    print("Finished. {}/{} Correct ({} wrong). {:.2f}% Failure Rate".format(
        N_TESTCASES - wrong, N_TESTCASES, wrong, wrong / N_TESTCASES * 100))


def getOutput(testcases, fname):
    proc = Popen(fname, stdin=PIPE, stdout=PIPE,
                 stderr=PIPE, universal_newlines=True)
    proc.stdin.write("\n".join(testcases) + "\n#")
    proc.stdin.close()
    # take only the non-empty lines and remove the trailing newline
    output = [line.rstrip()
              for line in proc.stdout.readlines() if len(line) > 1]
    proc.kill()
    output.pop()  # remove last useless string
    for i, string in enumerate(output):
        index = string.find('=')
        if (index == -1):
            raise ImproperFormatError
        output[i] = string[index+2:]
    return tuple(map(float, output))

if __name__ == '__main__':
    main()
