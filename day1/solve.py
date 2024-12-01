def solve(file):
    left = []
    right = []
    with open(file, "r") as f:
        for line in f:
            line.strip()
            l, r = line.strip().split()
            if l and r:
                left.append(int(l))
                right.append(int(r))

    # Part 1
    l_sorted = sorted(left)
    r_sorted = sorted(right)
    dist = 0
    for i in range(len(l_sorted)):
        dist += abs(l_sorted[i] - r_sorted[i])

    # Part 2
    sim_score = 0
    for a in left:
        num_seen = 0
        for b in right:
            if a == b: num_seen += 1
        sim_score += a * num_seen
        
    print(f"Part1: {dist}")
    print(f"Part2: {sim_score}")


if __name__ == "__main__":
    solve("input")
