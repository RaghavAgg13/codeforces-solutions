f_in = open("input.txt", 'r')
f_out = open("output.txt", "w")

door = f_in.readline().strip()
rail = int(f_in.readline().strip())

out = ""
if door == "front":
    out = "L" if rail == 1 else "R"
else:
    out = "L" if rail == 2 else "R"
f_out.write(out)