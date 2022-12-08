from dataclasses import dataclass

@dataclass
class Job:

    job_id : str
    deadline : int
    profit : int

    
def jobSequencing(jobs):
# sort jobs by profit in descending order
    jobs.sort(key=lambda x: x.profit, reverse=True)

    #printing total jobs after sorting
    #in decreasing order of profit
    jobs_sorted = []
    print("Sorted job list:")
    for item in jobs:
        jobs_sorted.append((item.job_id, item.deadline, item.profit))
    print(jobs_sorted,"\n\nThe scheduled jobs:")
        
    # initialize result array with None
    # for schedules where jobs can not be
    # performed it will return 'None' at that place
    result = ['None'] * len(jobs)

    # traverse jobs in sorted order
    for job in jobs:
        # find the first empty slot from the deadline
        for i in range(min(job.deadline, len(jobs))-1, -1, -1):
            # if slot is empty, add job to it
            if result[i] == 'None':
                result[i] = job.job_id 
                break
  
    return result


#test the function
jobs = [Job('J1', 2, 100), Job('J2', 1, 19), Job('J3', 2, 27),
        Job('J4', 1, 25), Job('J5', 3, 15)]

print(jobSequencing(jobs))