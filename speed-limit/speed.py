
import sys 


def parse_sample(idx, n, samples): 
    return list(map(str.split, samples[idx + 1 : idx + n + 1]))
    

def extract_speed(sample): 
    return [int(sample[x][0]) for x in range(len(sample))]


def extract_time(sample):
    time_diff = [int(sample[x+1][1]) - int(sample[x][1]) for x in range(len(sample) - 1)]
    return [int(sample[0][1])] + time_diff


def total_dist(speed, time):
    return sum(speed[i]*time[i] for i in range(len(time)))


def main():
    sample_input = tuple(map(str.strip, sys.stdin.readlines())) 
    
    idx = 0
    n = int(sample_input[0])
    while n > 0:
        sample = parse_sample(idx, n, sample_input)
        dist = total_dist(extract_speed(sample), extract_time(sample))
        print("{} miles".format(dist))
        idx += (n + 1)
        n = int(sample_input[idx])
    

if __name__ == "__main__":
    main()
