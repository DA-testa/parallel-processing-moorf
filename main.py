def parallel_processing(n, m, runtimes):
    output = []
    elapsed_time = [0] * n
    thread = 0
    
    for i in range(m):
        output.append((thread, elapsed_time[thread]))
        elapsed_time[thread] += runtimes[i]
        thread = elapsed_time.index(min(elapsed_time))
    
    return output

def main():
    n, m = map(int, input().split())
    runtimes = list(map(int, input().split()))
    assert(m == len(runtimes))
    
    result = parallel_processing(n, m, runtimes)
    
    for thread, time_moment in result:
        print(thread, time_moment)

if __name__ == "__main__":
    main()
