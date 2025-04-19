# Q5. Develop a formal specification for a job scheduling system and verify correctness.

from typing import List
from dataclasses import dataclass

@dataclass
class Job:
    job_id: int
    arrival_time: int
    burst_time: int

@dataclass
class ScheduledJob:
    job_id: int
    start_time: int
    finish_time: int

def sjf_schedule(jobs: List[Job]) -> List[ScheduledJob]:
    time = 0
    scheduled_jobs = []
    remaining_jobs = sorted(jobs, key=lambda x: (x.arrival_time, x.burst_time, x.job_id))

    while remaining_jobs:
        available_jobs = [job for job in remaining_jobs if job.arrival_time <= time]

        if not available_jobs:
            time = remaining_jobs[0].arrival_time
            continue

        next_job = min(available_jobs, key=lambda x: (x.burst_time, x.arrival_time, x.job_id))
        remaining_jobs.remove(next_job)

        start_time = max(time, next_job.arrival_time)
        finish_time = start_time + next_job.burst_time
        scheduled_jobs.append(ScheduledJob(next_job.job_id, start_time, finish_time))

        time = finish_time

    return scheduled_jobs

def verify_schedule(jobs: List[Job], schedule: List[ScheduledJob]) -> None:
    job_ids = set(job.job_id for job in jobs)
    scheduled_ids = set(job.job_id for job in schedule)
    assert job_ids == scheduled_ids, "Not all jobs scheduled correctly"

    for i in range(len(schedule)):
        for j in range(i + 1, len(schedule)):
            assert schedule[i].finish_time <= schedule[j].start_time or schedule[j].finish_time <= schedule[i].start_time, \
                f"Jobs {schedule[i].job_id} and {schedule[j].job_id} overlap"

    job_map = {job.job_id: job for job in jobs}
    for sched in schedule:
        assert sched.start_time >= job_map[sched.job_id].arrival_time, \
            f"Job {sched.job_id} started before arrival"

    print("All verification checks passed!")

if __name__ == "__main__":
    job_list = [
        Job(job_id=1, arrival_time=0, burst_time=8),
        Job(job_id=2, arrival_time=1, burst_time=4),
        Job(job_id=3, arrival_time=2, burst_time=9),
        Job(job_id=4, arrival_time=3, burst_time=5)
    ]

    schedule = sjf_schedule(job_list)
    for job in schedule:
        print(f"Job {job.job_id}: Start {job.start_time}, Finish {job.finish_time}")

    verify_schedule(job_list, schedule)
