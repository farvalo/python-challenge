import os
import csv

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')


total_votes = 0
candidate_votes = {}


with open(csvpath, mode='r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  
    
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

winner = max(candidate_votes, key=candidate_votes.get)

lines = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {total_votes}",
    "-------------------------"
]
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    lines.append(f"{candidate}: {percentage:.3f}% ({votes})")
lines.append("-------------------------")
lines.append(f"Winner: {winner}")
lines.append("-------------------------")

analysis_report = "\n".join(lines)

print(analysis_report)

output_path = os.path.join('PyPoll', 'analysis', 'election_analysis.txt')

with open(output_path, mode='w') as outputfile:
    outputfile.write(analysis_report)
