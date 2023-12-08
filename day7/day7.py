from collections import Counter


class Hand:
    def __init__(self, cards_str, bid):
        letter_cards = ["T", "J", "Q", "K", "A"]
        self.cards = []
        self.joker_count = 0
        for card in cards_str:
            if card == "J":
                self.joker_count += 1
                self.cards.append(0)
                continue
            try:
                letter_index = letter_cards.index(card)
                self.cards.append(10 + letter_index)
            except:
                self.cards.append(int(card))
        self.value = self._calc_value()

        self.bid = bid

    def _calc_value(self):
        """
        Determine value of card
        7. Five of a kind     - AAAAA
        6. Four of a kind     - AAAAB
        5. Full house         - AAABB
        4. Three of a kind    - AAABC
        3. Two pairs          - AABBC
        2. One Pair           - AABCD
        1. High Card          - ABCDE
        """
        counter = Counter(self.cards)
        sorted_tuples = list(
            dict(
                sorted(counter.items(), key=lambda item: item[1], reverse=True)
            ).items()
        )

        # add number of jokers to highest occuring card (that's not a joker)
        if sorted_tuples[0][0] != 0:
            sorted_tuples[0] = (
                sorted_tuples[0][0],
                sorted_tuples[0][1] + self.joker_count,
            )
        elif (
            len(sorted_tuples) != 1
        ):  # joker was highest occuring and ignore all joker hands
            sorted_tuples[1] = (
                sorted_tuples[1][0],
                sorted_tuples[1][1] + self.joker_count,
            )
            del sorted_tuples[0]  # remove jokers from first spot since we used them

        sorted_counts = [x[1] for x in sorted_tuples]

        if sorted_counts[0] >= 5:
            return 7
        elif sorted_counts[0] == 4:
            return 6
        elif sorted_counts[0] == 3:
            if sorted_counts[1] == 2:
                return 5
            return 4
        elif sorted_counts[0] == 2:
            if sorted_counts[1] == 2:
                return 3
            return 2
        return 1

    def __lt__(self, other):
        if self.value == other.value:
            for self_card, other_card in zip(self.cards, other.cards):
                if self_card != other_card:
                    return self_card < other_card
        return self.value < other.value

    def __str__(self):
        return f"Cards: {self.cards}\tValue: {self.value}\tBid: {self.bid}"


def __main__():
    hands = []

    with open("input.txt") as f:
        for line in f:
            cards_str, bids_str = line.split(" ")
            hand = Hand(cards_str, int(bids_str))

            hands.append(hand)

    sorted_hands = sorted(hands)

    answer = 0
    for i, hand in enumerate(sorted_hands):
        answer += (i + 1) * hand.bid
    print(answer)


__main__()
