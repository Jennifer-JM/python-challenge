import os
import csv
from collections import defaultdict

# File path
election_data_csv = os.path.join(r"Resources/election_data.csv")
output_file = os.path.join(r"Resources", "election_data_results.txt")

# Add variable list here
no_of_votes = 0
vote_count_per_candidate = defaultdict(int)

# Open & read election_data.csv
with open(election_data_csv) as csv_file:
    # Read the CSV file
    df = csv.reader(csv_file, delimiter=",")
    # Skip header
    csv_header = next(df)
    
    # Loop through each row after the header
    for row in df:
        # Get election data results
        no_of_votes += 1

        if len(row) > 2: 
                candidate_name = row[2].strip() 
                vote_count_per_candidate[candidate_name] += 1
                winner = max(vote_count_per_candidate, key=vote_count_per_candidate.get)
percentage_counts = {candidate: (count / no_of_votes) * 100 if no_of_votes > 0 else 0 
                     for candidate, count in vote_count_per_candidate.items()}

 

# Print the results
election_data_results = (
f"Election Results \n\n"
f"---------------------------- \n\n"
f"Total Votes: {no_of_votes} \n\n"
f"---------------------------- \n\n")
for candidate, count in vote_count_per_candidate.items():
    percentage = percentage_counts[candidate]
    election_data_results +=f"{candidate}: {percentage:.3f}% ({count})\n\n"
election_data_results += (
f"---------------------------- \n\n"
f"Winner: {winner} \n\n"
f"---------------------------- \n\n"
)
print(election_data_results)

# Write results to a text file
with open(output_file, 'w') as file:
    file.write(election_data_results)

