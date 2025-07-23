monday_visitors = {"user1", "user2", "user3", "user4", "user5"}
tuesday_visitors = {"user2", "user4", "user6", "user7", "user8"}
wednesday_visitors = {"user1", "user3", "user6", "user9", "user10"}

# Unique Visitors Across All Days
unique_visitors = monday_visitors | tuesday_visitors | wednesday_visitors

# Returning Visitors on Tuesday (Monday & Tuesday)
returning_tuesday = monday_visitors & tuesday_visitors

# New Visitors Each Day
day1_new = monday_visitors
day2_new = tuesday_visitors - monday_visitors
day3_new = wednesday_visitors - (monday_visitors | tuesday_visitors)

# Loyal Visitors (All Three Days)
loyal_visitors = monday_visitors & tuesday_visitors & wednesday_visitors

# Daily Visitor Overlap Analysis
monday_tuesday_overlap = monday_visitors & tuesday_visitors
tuesday_wednesday_overlap = tuesday_visitors & wednesday_visitors
monday_wednesday_overlap = monday_visitors & wednesday_visitors

print("Unique Visitors:", unique_visitors)
print("Returning Tuesday Visitors:", returning_tuesday)
print("New on Monday:", day1_new)
print("New on Tuesday:", day2_new)
print("New on Wednesday:", day3_new)
print("Loyal Visitors:", loyal_visitors)
print("Monday-Tuesday Overlap:", monday_tuesday_overlap)
print("Tuesday-Wednesday Overlap:", tuesday_wednesday_overlap)
print("Monday-Wednesday Overlap:", monday_wednesday_overlap)
