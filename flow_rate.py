def flow_rate(weight_diff, time_diff, period=5):
    return (weight_diff / time_diff) * period

weight_diff = .5
time_diff = 3
flow = flow_rate(weight_diff, time_diff, 5)
print("%.4f kg per second" %flow)