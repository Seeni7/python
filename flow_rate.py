def flow_rate(weight_diff, time_diff):
    return weight_diff / time_diff

weight_diff = .5
time_diff = 3
flow = flow_rate(weight_diff, time_diff)
print("%.3f kg per second" %flow)