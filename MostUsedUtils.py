# The purpose of this function is to refactor similar logic to save myself some time
def Most_Used_By(target: int, data: list[list[str]]) -> str:
    """
        Finds the most frequently occurring value at a specified index in the data.

        Args:
            target (int): The index of the value to count in each sublist.
            data (list[list[str]]): A list of sublists containing string values.

        Returns:
            str: The value that occurs most frequently at the specified index.
                 If multiple values share the highest frequency, returns the
                 first one encountered.
        """
    Nosferatu = 0
    Splash = ""
    LotsOfCounters = {}
    for fabric in data:
        LotsOfCounters[fabric[target]] = LotsOfCounters.get(fabric[target], 0) + 1
    for item, count in LotsOfCounters.items():
        if count > Nosferatu:
            Nosferatu = count
            Splash = item
    return Splash

# The purpose of this function is to determine which pokemon does the most clicking of moves
def Most_Active_Pokemon(data: list[list[str]]) -> str:
    """
        Determines which Pokémon performs the most move clicks.

        Args:
            data (list[list[str]]): A list of sublists containing Pokémon battle
                                    data, with the acting Pokémon at index 0.

        Returns:
            str: The name of the Pokémon that appears most frequently as the
                 acting Pokémon. Returns an empty string if data is empty.
        """
    target = 0
    return Most_Used_By(target, data)

# The purpose of this function is titular
def Most_Targeted_Pokemon(data: list[list[str]]) -> str:
    """
       Determines which Pokémon is targeted most frequently by moves.

       Args:
           data (list[list[str]]): A list of sublists containing Pokémon battle
                                   data, with the targeted Pokémon at index 1.

       Returns:
           str: The name of the Pokémon that is targeted most frequently.
                Returns an empty string if data is empty.
       """
    target = 1
    return Most_Used_By(target, data)

# The purpose of this function is titular
def Most_Used_Move(data: list[list[str]]) -> str:
    """
        Determines which move is used most frequently.

        Args:
            data (list[list[str]]): A list of sublists containing Pokémon battle
                                    data, with the move name at index 2.

        Returns:
            str: The name of the most frequently used move. Returns an empty
                 string if data is empty.
        """
    target = 2
    return Most_Used_By(target, data)