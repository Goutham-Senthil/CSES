from dataclasses import dataclass
from typing import List


@dataclass
class Sample:
    t: float
    stack: List[str]


def reconstruct_trace(samples: List[Sample]) -> List[str]:
    """
    Given a list of sampling profiler snapshots ordered by timestamp,
    reconstruct the most likely sequence of function call and return events.

    Each Sample contains:
      - t: timestamp
      - stack: call stack at that moment

    The stack is ordered from outermost function to innermost currently
    executing function.

    An arbitrary number of function calls and returns may occur between
    consecutive samples.

    Return a list of strings representing events in chronological order.

    Example event strings:
        "call foo"
        "return foo"
    """
    events = []

    prev_stack = []


    for t,curr_stack in [(s.t, s.stack) for s in samples]:
        i = 0 


        # this is basically 
        # finding the first point of 
        # difference 
        # so anything 
        # at the difference point 
        # so everyting after that ended and everything after that started
        while (
            i<len(curr_stack)
            and i<len(prev_stack)
            and curr_stack[i] == prev_stack[i]
        ):
            i+=1

        # functions that have returned 
        for func in prev_stack[i:]:
            events.append(f"return {func} at time {t}")
        
        for func in curr_stack[i:]:
            events.append(f"call {func} at time {t}")
        
        prev_stack = curr_stack
    
    return events


def main():
    samples = [
        Sample(0.0, ["main"]),
        Sample(1.0, ["main", "foo"]),
        Sample(2.0, ["main", "foo", "bar","main"]),
        Sample(3.0, ["main", "baz"]),
        Sample(4.0, ['main2'])
    ]
    events = reconstruct_trace(samples)
    
    for ev in events:
        print(ev)

if __name__ == "__main__":
    main()