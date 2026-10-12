voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

# current streak trackers
current_len = 0
current_start = voltages[0]
current_end = voltages[0]

# best streak trackers
best_len = 1
best_start = voltages[0]
best_end = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        # still decreasing, extend streak
        current_len = current_len + 1
        current_end = voltages[i]
    else:
        # streak broke, check if it was the best
        if current_len > best_len:
            best_len = current_len
            best_start = current_start
            best_end = current_end
        # start a new streak from this reading
        current_len = 1
        current_start = voltages[i]
        current_end = voltages[i]

# check the last streak after the loop ends
if current_len > best_len:
    best_len = current_len
    best_start = current_start
    best_end = current_end

print("Longest continuous drop:", best_len, "minutes")
print("Started at:", best_start, "V")
print("Ended at:", best_end, "V")
