arr = [1, 2, 1, 3, 4, 3, 3, 4]
# Find the length of the longest contiguous subarray containing no more than 2 distinct values.
seend = set()
s = e = maxl = 0
lastdistinct = None  # last distinct element from seend appears
lastdistinctloc = None  # location of last distinct element from seend

while e < len(arr):
    if arr[e] not in seend and len(seend) < 2:
        seend.add(arr[e])
        lastdistinct = arr[e]
        lastdistinctloc = e
    elif arr[e] in seend and len(seend) <= 2:
        if arr[e] != lastdistinct:
            lastdistinct = arr[e]
            lastdistinctloc = e
    elif arr[e] not in seend and len(seend) == 2:
        seend.clear()
        seend.update([lastdistinct, arr[e]])
        s = lastdistinctloc
        lastdistinctloc = e
        lastdistinct = arr[e]

    if e + 1 - s > maxl:
        maxl = e + 1 - s
    e = e + 1

print(maxl)
# ============================================================================
# LONGEST CONTIGUOUS SUBARRAY WITH AT MOST 2 DISTINCT VALUES
# ============================================================================
#
# The goal is to find the maximum length of a CONTIGUOUS subarray that contains
# no more than 2 distinct values.
#
# Example:
#
# arr = [1, 2, 1, 3, 4, 3, 3, 4]
#
# The answer is 5 because:
#
# [3, 4, 3, 3, 4]
#  └─────────────┘
# contains only 2 distinct values: 3 and 4.
#
#
# ----------------------------- VARIABLES -----------------------------------
#
# seend:
#     A set used to keep track of the distinct values currently present in
#     the current window.
#
#     IMPORTANT:
#     It can contain AT MOST 2 distinct values.
#
#     Example:
#         Current window = [1, 2, 1, 2]
#         seend = {1, 2}
#
#
# s:
#     Starting/left boundary of the current window.
#
#
# e:
#     Ending/right boundary of the current window.
#
#     The window being considered is:
#
#         arr[s : e + 1]
#
#
# maxl:
#     Stores the maximum length found so far among all valid windows.
#
#
# lastdistinct:
#     Stores the MOST RECENT DISTINCT VALUE encountered while scanning the
#     current window.
#
#     This is NOT simply the most recently encountered element.
#
#     Example:
#
#         [1, 2, 2]
#
#     The distinct values are 1 and 2.
#     The most recent DISTINCT value is 2.
#
#     The first 2 establishes 2 as the latest distinct value. The next 2 is
#     only a repetition, so lastdistinct does NOT change.
#
#
# lastdistinctloc:
#     Stores the INDEX at which lastdistinct first became the latest distinct
#     value.
#
#     Example:
#
#         [1, 2, 2]
#          0  1  2
#
#     lastdistinct = 2
#     lastdistinctloc = 1
#
#     We do NOT change lastdistinctloc to 2 when the second 2 appears because
#     that 2 is only a repetition of the existing value.
#
#
# -------------------------- IMPORTANT IDEA ----------------------------------
#
# The difficult part of this problem is handling the situation where a THIRD
# distinct value appears.
#
# Suppose the current window is:
#
#         [1, 2]
#
# and the next value is:
#
#         3
#
# We cannot simply throw away the entire previous window.
#
# The new valid window should begin from the LAST occurrence where the previous
# distinct value became the relevant boundary.
#
# For:
#
#         [1, 2, 3]
#          0  1  2
#
# lastdistinct = 2
# lastdistinctloc = 1
#
# Therefore, when 3 appears, we move:
#
#         s = lastdistinctloc
#
# giving:
#
#         [2, 3]
#          ↑  ↑
#          s  e
#
# This keeps the previous distinct value (2) and the new value (3), giving us
# a new valid window containing exactly 2 distinct values.
#
#
# -------------------------- FIRST CONDITION -------------------------------
#
# if arr[e] not in seend and len(seend) < 2:
#
# This means:
#
#     1. arr[e] is a completely new value.
#     2. We currently have fewer than 2 distinct values.
#
# Therefore, this new value can safely be added to the current window.
#
# Before changing anything, we check the current window length:
#
#     e + 1 - s
#
# If it is greater than maxl, update maxl.
#
# Then:
#
#     seend.add(arr[e])
#
# because arr[e] is a new distinct value.
#
# We also update:
#
#     lastdistinct = arr[e]
#     lastdistinctloc = e
#
# because this newly encountered value is now the latest distinct value.
#
# Finally:
#
#     e = e + 1
#
# because the current element has been completely processed.
#
#
# -------------------------- SECOND CONDITION ------------------------------
#
# elif arr[e] in seend and len(seend) <= 2:
#
# This means arr[e] is ALREADY one of the values in the current window.
#
# Therefore, it does not introduce a third distinct value.
#
# The current window is still valid.
#
# Again, we check:
#
#     e + 1 - s
#
# against maxl.
#
#
# The important part is:
#
#     if arr[e] != lastdistinct:
#
# We check whether this repeated value is different from the value currently
# stored as lastdistinct.
#
# Example:
#
#     [1, 2, 1]
#
# Initially:
#
#     lastdistinct = 2
#
# When the final 1 appears:
#
#     1 is already in seend
#     BUT 1 != lastdistinct (2)
#
# Therefore, 1 has now become the latest distinct value encountered.
#
# So we update:
#
#     lastdistinct = arr[e]
#     lastdistinctloc = e
#
# This is important because if a THIRD distinct value appears afterward, we
# need the location of this latest distinct value to know where the new window
# should begin.
#
# Example:
#
#     [1, 2, 1, 3]
#
# When 3 appears, the latest distinct value before 3 was 1, at index 2.
#
# Therefore the new valid window should become:
#
#     [1, 3]
#
# starting from index 2.
#
# After processing the repeated value:
#
#     e = e + 1
#
#
# -------------------------- THIRD CONDITION -------------------------------
#
# elif arr[e] not in seend and len(seend) == 2:
#
# This is the IMPORTANT CASE.
#
# We already have exactly 2 distinct values in the current window, and arr[e]
# is a completely NEW value.
#
# Therefore, adding arr[e] would create 3 distinct values, which is invalid.
#
# Example:
#
#     Current window:
#
#         [1, 2]
#
#     seend = {1, 2}
#
#     New value:
#
#         3
#
# We cannot keep the whole [1, 2, 3].
#
# Instead, we create a new valid window containing:
#
#     2 + 3
#
# because 2 was the latest distinct value before 3.
#
#
# First:
#
#     seend.clear()
#
# Remove the old two-value tracking.
#
# Then:
#
#     seend.update([lastdistinct, arr[e]])
#
# The new set contains exactly:
#
#     {previous latest distinct value, new value}
#
#
# Next:
#
#     s = lastdistinctloc
#
# This moves the beginning of the window to the location of the previous
# latest distinct value.
#
# Example:
#
#     [1, 2, 3]
#      0  1  2
#
#     lastdistinct = 2
#     lastdistinctloc = 1
#
# Therefore:
#
#     s = 1
#
# and the new window is:
#
#     [2, 3]
#
#
# Then we update lastdistinct information because the NEW value is now the
# latest distinct value:
#
#     lastdistinctloc = e
#     lastdistinct = arr[e]
#
#
# We then check the length of the newly formed valid window:
#
#     e + 1 - s
#
# and update maxl if necessary.
#
# Finally:
#
#     e = e + 1
#
# because the newly encountered element has now been processed.
#
#
# --------------------------- WHY THIS WORKS -------------------------------
#
# The entire trick is remembering WHERE the latest distinct value started.
#
# Consider:
#
#     [1, 2, 2, 2, 3]
#      0  1  2  3  4
#
# Before 3 appears:
#
#     seend = {1, 2}
#     lastdistinct = 2
#     lastdistinctloc = 1
#
# When 3 appears, we cannot use:
#
#     [1, 2, 2, 2, 3]
#
# because there are 3 distinct values.
#
# But we can immediately move the start to index 1:
#
#     [2, 2, 2, 3]
#      ↑           ↑
#      s           e
#
# Now the window contains only:
#
#     {2, 3}
#
# So it is valid.
#
# We do NOT need to move s one position at a time here.
# We already know exactly where the new valid window should start because
# lastdistinctloc tells us where the previous latest distinct value began.
#
#
# --------------------------- POINTER MOVEMENT -----------------------------
#
# e always moves forward.
#
# s only moves forward when a THIRD distinct value appears.
#
# Neither pointer ever moves backward.
#
# Therefore, even though the program contains several conditions, the total
# amount of pointer movement remains linear.
#
#
# --------------------------- COMPLEXITY ------------------------------------
#
# Time Complexity:
#
#     O(n)
#
# Every element is processed while e moves from the beginning to the end.
# s also only moves forward.
#
# Space Complexity:
#
#     O(1)
#
# Although a set is being used, it can contain AT MOST 2 elements because the
# problem only allows at most 2 distinct values.
#
# Therefore its size does not grow with n.
#
# The remaining variables (s, e, maxl, lastdistinct, lastdistinctloc) are
# individual scalar variables and therefore also use constant space.
#
#
# ============================================================================
# CORE MEMORY:
#
# seend          → which 2 distinct values are currently allowed
# s              → beginning of current window
# e              → end of current window
# maxl           → longest valid window found
# lastdistinct   → latest distinct value
# lastdistinctloc→ where that latest distinct value started appearing
#
# If a third distinct value appears:
#
#     keep the previous lastdistinct + new value
#     move s to lastdistinctloc
#     make the new value the latest distinct
#
# This allows the window to continue instead of restarting from scratch.
# ============================================================================