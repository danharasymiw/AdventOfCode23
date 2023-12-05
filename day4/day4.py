def input_line_to_num_list(line):
    return list(map(lambda s: int(s.strip()),
               filter(lambda s: len(s) > 0, line.split(" "))))
    
def __main__():
    winning_cards = []
    our_cards = []
    
    with open("input.txt") as f:
        for line in f:
            card_num_end_index = line.find(":") + 1
            winning_line, our_line = line[card_num_end_index:].split("|")
            winning_cards.append(input_line_to_num_list(winning_line))
            our_cards.append(input_line_to_num_list(our_line))
            
        
    # part 1
    points = 0
    
    for winning_nums, our_nums in zip(winning_cards, our_cards):
        matching_nums = set(winning_nums).intersection(our_nums)    
        if len(matching_nums) > 0:
            points += 2 ** (len(matching_nums) - 1)
        
    
    print(f"Part 1 points: {points}")
    
    # part 2
    num_of_cards = 0
    cards_to_process = [x for x in range(0, len(winning_cards))]
    print(cards_to_process)
    while len(cards_to_process) > 0:
        num_of_cards += 1
        card_index = cards_to_process.pop()
        print(card_index)
        winning_nums = winning_cards[card_index]
        our_nums = our_cards[card_index]
        matches = set(winning_nums).intersection(our_nums)
        if len(matches) > 0:
            cards_to_process += [x for x in range(card_index + 1, card_index + 1 + len(matches))]
            
    print(f"Part 2 Num of scratch cards: {num_of_cards}")
            
        
            
__main__()
            
            