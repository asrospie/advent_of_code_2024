def parse_rules_and_numbers(filename):
    with open(filename, 'r') as file:
        page_rules = {}
        page_numbers = []


        reading_rules = True

        while True:
            line = file.readline().strip()

            if not line and reading_rules:
                reading_rules = False
                continue

            if not line and not reading_rules:
                break


            if reading_rules:
                line = line.split('|')
                if line[0] not in page_rules:
                    page_rules[line[0]] = []

                page_rules[line[0]].append(line[1])
            else:
                page_numbers.append(line.split(','))

    return page_rules, page_numbers


def day_5_part_1(filename):
    page_rules, page_numbers = parse_rules_and_numbers(filename)
    
    result = 0
    for pg in page_numbers:
        failed = False 
        for i in range(len(pg) - 1, 0, -1):
            v = pg[i]
            if v not in page_rules:
                continue
        
            for j in range(i - 1, -1, -1):
                if pg[j] in page_rules.get(v):
                    failed = True
                    break
            if failed:
                break

        if not failed:
            result += int(pg[int(len(pg) / 2)])

    return result


def find_bad_updates(page_rules, page_updates):
    bad_updates = []
    for pg in page_updates:
        failed = False 
        for i in range(len(pg) - 1, 0, -1):
            v = pg[i]
            if v not in page_rules:
                continue
        
            for j in range(i - 1, -1, -1):
                if pg[j] in page_rules.get(v):
                    failed = True
                    bad_updates.append(pg)
                    break
            if failed:
                break

    return bad_updates


def day_5_part_2(filename):
    page_rules, page_numbers = parse_rules_and_numbers(filename)

    bad_updates = find_bad_updates(page_rules, page_numbers)

    result = 0
    for update in bad_updates:
        i = len(update) - 1
        while i >= 0:
            v = update[i]
            if v not in page_rules:
                i -= 1
                continue

            swap_idx = i
            change_needed = False 
            for j in range(i - 1, -1, -1):
                if update[j] in page_rules[v]:
                    swap_idx = j
                    change_needed = True

            if change_needed:
                update.pop(i)
                update.insert(swap_idx, v)
                i = len(update) - 1
                continue
            i -= 1


        result += int(update[int(len(update) / 2)])

    return result


def main():
    print(day_5_part_1('test5.txt'))
    print(day_5_part_1('day5.input'))
    print(day_5_part_2('test5.txt'))
    print(day_5_part_2('day5.input'))


if __name__ == '__main__':
    main()
