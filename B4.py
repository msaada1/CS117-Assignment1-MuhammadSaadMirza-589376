# Finding the longest streak of decreasing voltage readings

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

longest_streak = 1
current_streak = 1
start = 0
decr_start_index = 0

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        current_streak += 1
    else:
        current_streak = 1
        start = i

    if current_streak > longest_streak:
        longest_streak = current_streak
        decr_start_index = start

end_index = decr_start_index + longest_streak - 1

print(f"Longest Continuous Drop: {longest_streak} minutes")
print(f"Started at: {voltages[decr_start_index]} V")
print(f"Ended at: {voltages[end_index]} V")