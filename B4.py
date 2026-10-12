#CONTINIOUS DISCHARGE ANALYSIS
voltage=[12.6,
         12.5,
         12.5,
         12.3,
         12.1,
         11.9,
         12.0,
         11.8,
         11.6,
         11.5,
         11.5,
         11.2]
streak_length=1
streak_start=0
streak_end=0
current_streak_length=1
current_streak_start=0

for i in range(1,len(voltage)):
    if voltage[i] < voltage[i-1]:
        current_streak_length+=1
    else:
        if current_streak_length>streak_length:
            streak_length=current_streak_length
            streak_start=current_streak_start
            streak_end=i-1
        current_streak_length=1
        current_streak_start=i

if current_streak_length>streak_length:
     streak_length=current_streak_length
     streak_start=current_streak_start
     streak_end=len(voltage)-1

print(f"Longest drop : {streak_length} minutes")
print(f"start at : {voltage[streak_start]}")
print(f"end at : {voltage[streak_end]}")
