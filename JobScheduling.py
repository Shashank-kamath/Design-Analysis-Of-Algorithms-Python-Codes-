class job:
    def __init__(self,taskID,deadLine,profit):
        self.taskID,self.deadLine,self.profit=taskID,deadLine,profit

def scheduleJobs(jobs,T):
    profit=0
    slot=[0]*T
    jobs.sort(key=lambda x:x.profit,reverse=True)
    for jobs in jobs:
        for j in reversed(range(jobs.deadLine)):
            if j<T and slot[j]==0:
                slot[j]=jobs.taskID
                profit+=jobs.profit
                break
    print("\nThe Scheduled Jobs are:",list(filter(lambda x:x!=0,slot)))
    print("The Total Profit earned is:",profit)

if __name__=="__main__":
    jobs=[]
    n=int(input("Enter the number of Jobs: "))
    for i in range(n):
        taskID=int(input(f"Enter the Task ID of Job {i+1}: "))
        deadLine=int(input(f"Enter the Dead Line of Job {i+1}: "))
        profit=int(input(f"Enter the profit earned by Job {i+1}: "))
        jobs.append(job(taskID,deadLine,profit))
    T=int(input("Enter the Dead Line limit: "))
    scheduleJobs(jobs,T)


    