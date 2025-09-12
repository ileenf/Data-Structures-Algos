class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        functions = [] 
        prev_timestamp = -1
        function_to_time = defaultdict(int)

        for log in logs:
            function, action, timestamp = log.split(':')
            function = int(function)
            timestamp = int(timestamp)
            if action == 'start':
                if functions:
                    latest_function = functions[-1]
                    time_elapsed = (timestamp - prev_timestamp)
                    function_to_time[latest_function] += time_elapsed

                functions.append(function)
                prev_timestamp = timestamp
            elif action == 'end':
                latest_function = functions[-1]
                functions.pop(len(functions)-1)
                
                time_elapsed = timestamp - prev_timestamp + 1
                function_to_time[latest_function] += time_elapsed

                prev_timestamp = timestamp + 1

        return list(function_to_time.values())
