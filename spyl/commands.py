def dedup(generator):
    s = set()
    for result in generator:
        if result in s:
            continue
        s.add(result)
        yield result


def print_gen(generator):
    for event in generator:
        print(event)
        yield event
