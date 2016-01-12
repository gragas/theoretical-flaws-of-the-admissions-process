import random

ACCEPTANCE_RATE = 0.10
POPULATION_SIZE = 10000

TRIALS_PER_N_MACHINE = 50

num_to_be_accepted = int(POPULATION_SIZE * ACCEPTANCE_RATE)

print("Population size: {}".format(POPULATION_SIZE))
print("Acceptance rate: {}".format(ACCEPTANCE_RATE))
print("Number to be accepted: {}\n".format(num_to_be_accepted))

average_false_accepts = []
number_of_machines = [
        _ for _ in range(1, num_to_be_accepted) if num_to_be_accepted % _ == 0 \
        and POPULATION_SIZE % _ == 0
]

for n_machines in number_of_machines:
    num_per_subset = POPULATION_SIZE // n_machines
    num_to_be_accepted_per_subset = num_to_be_accepted // n_machines
    perfect_acceptance_set = set(range(POPULATION_SIZE)[-num_to_be_accepted:])
    false_accepts = []
    for z in range(TRIALS_PER_N_MACHINE):
        applicant_set = set(range(POPULATION_SIZE))
        this_acceptance_set = set()
        for i in range(n_machines):
            l = random.sample(applicant_set, num_per_subset)
            subset = set(l)
            applicant_set -= subset
            accepted_set  = set(sorted(l)[-num_to_be_accepted_per_subset:])
            this_acceptance_set |= accepted_set
        false_accepts.append(len(this_acceptance_set - perfect_acceptance_set))
    avg_false_accepts = sum(false_accepts) / len(false_accepts)
    average_false_accepts.append(avg_false_accepts)
    print("Number of machines: {}".format(n_machines))
    print("Average number of false accepts: {}\n".format(avg_false_accepts))

from matplotlib import pyplot as plt
import numpy as np

average_false_accept_rate = [_ / POPULATION_SIZE for _ in average_false_accepts]

plt.plot(number_of_machines, average_false_accept_rate, "ro")
plt.xlabel("Number of Machines")
plt.ylabel("Average False Acception/Rejection Rate")
plt.title("Average False Acception/Rejection Rate vs. Number of Machines")
plt.show()

average_percent_of_class_false = [
    100.0 * _ / num_to_be_accepted for _ in average_false_accepts
]

plt.plot(number_of_machines, average_percent_of_class_false, "ro")
plt.xlabel("Number of Machines")
plt.ylabel("Average Percent of Class False")
plt.title("Average Percent of Class False vs. Number of Machines")
plt.show()
