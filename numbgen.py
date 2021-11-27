import numpy as np

all_chars = '0123456789+'

num_features = len(all_chars)

char_to_index = dict((c, i) for i, c in enumerate(all_chars))
index_to_char = dict((i, c) for i, c in enumerate(all_chars))


def generate_data():
    first_num = np.random.randint(low=0, high=100)
    second_num = np.random.randint(low=0, high=100)
    example = str(first_num) + '+' + str(second_num)
    label = str(first_num + second_num)
    return example, label


f = open("demo.txt", "w")  # a - Append, w - write

for i in range(2000):
    example, label = generate_data()
    f.write(str(generate_data()))
    f.write('\n')

f.close()
