def job_sequencing(job_deadline, job_profit):
    jobs = []
    for i in range(len(job_deadline)):
        job = []
        job.append(i)
        job.append(job_deadline[i])
        job.append(job_profit[i])
        jobs.append(job)

    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)
    time = 0
    max_profit = 0
    ans_job = []
    for i in range(len(jobs)):
        if jobs[i][1] > time:
            max_profit += jobs[i][2]
            ans_job.append(jobs[i])
            time += 1

    print(ans_job)
    print(max_profit)


job_deadline = [4, 1, 1, 1]
job_profit = [20, 10, 40,30]
job_sequencing(job_deadline,job_profit)
