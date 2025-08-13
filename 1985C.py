import sys
 
data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
idx = 1
 
out_lines = []
append_out = out_lines.append
for _ in range(t):
    n = data[idx]
    idx += 1
    count = 0
    prefix_sum = 0
    seen = set()
    add_seen = seen.add
    contains_seen = seen.__contains__
    end_idx = idx + n
 
    while idx < end_idx:
        num = data[idx]
        idx += 1
        prefix_sum += num
        add_seen(num)
        if not prefix_sum & 1 and contains_seen(prefix_sum >> 1):
            count += 1
 
    append_out(str(count))
 
sys.stdout.write("\n".join(out_lines))