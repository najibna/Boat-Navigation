
LEFT = -1
RIGHT = 1


def is_outside_list(letter_list, index):
        """
        Given a list of letters and an index, returns True if the index
            is outside the bounds of the list, False otherwise.

        Args:
        - letter_list (List[str]): A list of letters.
        - index (int): The index to check.

        Returns:
        - bool: True if the index is outside the bounds 
        of the list, False otherwise.

        Example:
        >>> is_outside_list(['a', 'b', 'c'], -1)
        True
        >>> is_outside_list(['a', 'b', 'c'], 0)
        False
        >>> is_outside_list(['a', 'b', 'c'], 3)
        True
        """
        # Check if the index is less than zero or greater 
        # than or equal to the length of the list
        if index < 0 or index >= len(letter_list):
                # If the index is outside the bounds of the list, return True
                return True
        else:
                # If the index is within the bounds of the list, return False
                return False



def letter_positions(letter_list, character):
        """
        Given a list of letters and a character, returns a list of
            indices where the character appears in the list.

        Args:
        - letter_list (List[str]): A list of letters.
        - character (str): The character to search for.

        Returns:
        - List[int]: A list of indices where the character appears in the list.

        Example:
        >>> letter_positions(['a', 'b', 'c', 'a'], 'a')
        [0, 3]
        >>> letter_positions(['a', 'b', 'c', 'a'], 'b')
        [1]
        >>> letter_positions(['a', 'b', 'c', 'a'], 'd')
        []

        """
        # Initialize an empty list to store the indices 
        # where the character appears
        indices = []
        
        # Loop through each letter in the list
        for i in range(len(letter_list)):
                # If the current letter matches the character 
                # we're searching for, add its index to the list
                if letter_list[i] == character:
                        indices.append(i)
        
        # Return the list of indices where the character appears
        return indices



def valid_word_pos_direction(letter_list, word, index, direction):
    """
    Given a list of letters, a word, an index, and a direction 
    (LEFT or RIGHT), returns True if the word can be found starting
      from the given index in the given direction, False otherwise.

    Args:
    - letter_list (List[str]): A list of letters.
    - word (str): A word to search for.
    - index (int): The index in the letter_list where 
    the search should start.
    - direction (int): The direction in which to 
    search for the word (LEFT or RIGHT).

    Returns:
    - bool: True if the word can be found starting from the 
    given index in the given direction, False otherwise.

    Example:
    >>> valid_word_pos_direction(['a', 'b', 'c', 'd', 'e'], 'ab', 0, RIGHT)
    True
    >>> valid_word_pos_direction(['a', 'b', 'c', 'd', 'e'], 'ab', 1, LEFT)
    True
    >>> valid_word_pos_direction(['a', 'b', 'c', 'd', 'e'], 'cd', 2, RIGHT)
    True
    """
    # Calculate the end index based on the direction
    end_index = index + direction * (len(word) - 1)
    
    # Check if the end index is within the bounds of the list
    if end_index < 0 or end_index >= len(letter_list):
        return False
    
    # Check if the letters in the list match the letters in the word
    for i in range(len(word)):
        if letter_list[index + i * direction] != word[i]:
            return False
    
    # If all letters match, return True
    return True

from typing import List


def direction_word_given_position(letter_list, word, index):
    """
    Given a list of letters, a word, and an index, returns a list
      of directions (LEFT or RIGHT) in which the word can be found 
      starting from the given index.

    Args:
    - letter_list (List[str]): A list of letters.
    - word (str): A word to search for.
    - index (int): The index in the letter_list where 
      the search should start.

    Returns:
    - List[int]: A list of directions (LEFT or RIGHT) 
    in which the word can be found starting from the given index.

    Example:
    >>> direction_word_given_position(['a', 'b', 'c', 'd', 'e'], 'ab', 0)
    [RIGHT]
    >>> direction_word_given_position(['a', 'b', 'c', 'd', 'e'], 'ab', 1)
    [LEFT]
    >>> direction_word_given_position(['a', 'b', 'c', 'd', 'e'], 'cd', 2)
    [LEFT, RIGHT]
    """
    # Check if the first letter of the word is found 
    # at the given index in the list of letters
    if letter_list[index] != word[0]:
        return []
    
    # Check if the word can be found in both directions
    if valid_word_pos_direction(letter_list, word, index, LEFT) and \
        valid_word_pos_direction(letter_list, word, index, RIGHT):
        return [LEFT, RIGHT]
    
    # Check if the word can be found in the left direction only
    if valid_word_pos_direction(letter_list, word, index, LEFT):
        return [LEFT]
    
    # Check if the word can be found in the right direction only
    if valid_word_pos_direction(letter_list, word, index, RIGHT):
        return [RIGHT]
    
    # If the word cannot be found in either direction, return an empty list
    return []



def position_direction_word(letter_list, word):
    """
    Given a list of letters and a word, returns a list of 
    positions and directions where the word can be found in the list.

    Args:
    - letter_list (List[str]): A list of letters.
    - word (str): A word to search for.

    Returns:
    - List[List[int]]: A list of positions and directions where 
    the word can be found in the list.

    Example:
    >>> position_direction_word(['a', 'b', 'c', 'd', 'e'], 'ab')
    [[0, 1]]
    >>> position_direction_word(['a', 'b', 'c', 'd', 'e'], 'cd')
    [[2, -1], [2, 1]]
    >>> position_direction_word(['a', 'b', 'c', 'd', 'e'], 'f')
    []
    """
    positions = []
    for i in range(len(letter_list)):
        # get the directions where the word can be found starting from the current position
        directions = direction_word_given_position(letter_list, word, i)
        for direction in directions:
            # append the position and direction to the positions list
            positions.append([i, direction])
    return positions



def cross_word_position_direction(bool_letter_list, length_word, index,
                                   direction):
    """
    Given a boolean list, the length of a word, an index, and a 
    direction (LEFT or RIGHT), updates the values in the boolean 
    list to True for the positions where the word crosses.

    Args:
    - bool_letter_list (List[bool]): A boolean list.
    - length_word (int): The length of the word.
    - index (int): The index in the boolean list where the word starts.
    - direction (int): The direction in which 
      the word crosses (LEFT or RIGHT).

    Returns:
    - None

    Example:
    >>> bool_letter_list = [False] * 5
    >>> cross_word_position_direction(bool_letter_list, 2, 0, RIGHT)
    >>> bool_letter_list
    [True, True, False, False, False]
    >>> bool_letter_list = [False] * 5
    >>> cross_word_position_direction(bool_letter_list, 2, 3, LEFT)
    >>> bool_letter_list
    [False, False, True, True, False]
    """
    # Update the values in bool_letter_list
    #based on the given index, length_word, and direction
    for i in range(length_word):
        bool_letter_list[index + i*direction] = True



def cross_word_all_position_direction(bool_letter_list, length_word,
                                      list_position_direction):
    """
    Given a boolean list, the length of a word, and a list of positions and
    directions where the word can be found in the list, updates the values in
    the boolean list to True for all positions where the word crosses.

    Args:
    - bool_letter_list (List[bool]): A boolean list.
    - length_word (int): The length of the word.
    - list_position_direction (List[List[int]]): A list of positions and
    directions where the word can be found in the list.

    Returns:
    - None

    Example:
    >>> bool_letter_list = [False] * 5
    >>> cross_word_all_position_direction(bool_letter_list, 2, [[0, 1]])
    >>> bool_letter_list
    [True, True, False, False, False]
    >>> bool_letter_list = [False] * 5
    >>> cross_word_all_position_direction(bool_letter_list, 2, [[2, -1],
    [2, 1]])
    >>> bool_letter_list
    [False, False, True, True, False]
    """
    # loop through each position and direction in the list
    for position_direction in list_position_direction:
        # get the index and direction
        index, direction = position_direction
        # call the cross_word_position_direction function to update the boolean list
        cross_word_position_direction(bool_letter_list, length_word, index,
                                      direction)




def word_search(letter_list, word_list):
    """
    Finds a magic word in a letter list by searching for words in a word list.

    Args:
        letter_list (list): A list of strings 
        representing the letters to search through.
        word_list (list): A list of strings representing
        the words to search for.

    Returns:
        str: The magic word found in the letter list.

    Examples:
        >>> word_search(['a', 'b', 'c', 'd', 'e'], ['bad', 'cab', 'dad'])
        'cab'
        >>> word_search(['a', 'b', 'c', 'd', 'e'], ['bad', 'bed', 'dad'])
        'bad'
        >>> word_search(['a', 'b', 'c', 'd', 'e'], ['bee', 'ebb', 'add'])
        'add'
    """

    # Initialize a boolean list to keep track of 
    # which positions in the letter list have been used
    bool_letter_list = [False] * len(letter_list)

    # Iterate through each word in the word list
    for word in word_list:
        # Iterate through each position in the letter list
        for i in range(len(letter_list)):
            # Check if the current word can be found starting from the 
            # current position
            positions = direction_word_given_position(letter_list, word, i)
            if positions:
                # If the word can be found, mark the positions 
                # as used in the boolean list
                valid_word_pos_direction(letter_list, word, i, positions[0])
                cross_word_all_position_direction(bool_letter_list, len(word), 
                                                   [[i, positions[0]]])
    # Find the magic word using the boolean list
    magic_word = find_magic_word(letter_list, bool_letter_list)
    return magic_word



def find_magic_word(letter_list, bool_letter_list):
    """
    This function takes in two lists of the same length, one 
    containing letters and the other containing boolean values.
    It returns a string that is formed by concatenating all
    the non-crossed letters in the order they appear in the input list,
    except for the letters that appear between two crossed 
    letters, which are not included in the output.

    Args:
    - letter_list (list[str]): A list of letters
    - bool_letter_list (list[bool]): A list of boolean values 
    indicating whether the corresponding letter in 
    letter_list is crossed or not

    Returns:
    - str: A string formed by concatenating all the non-crossed 
    letters in the order they appear in the input list,
    except for the letters that appear between two crossed letters, 
    which are not included in the output.

    Example:
    >>> find_magic_word(['a', 'b', 'c', 'd'], [False, True, False, True])
    'ad'
    >>> find_magic_word(['a', 'b', 'c', 'd'], [True, False, True, False])
    'bd'
    >>> find_magic_word(['a', 'b', 'c', 'd'], [False, False, False, False])
    'abcd'
    """

    # Check if both lists have the same size
    if len(letter_list) != len(bool_letter_list):
        raise ValueError('Both lists should have the same size')
    
    # Initialize variables
    magic_word = '' # initialize an empty string to hold the magic word
    current_word = '' # initialize an empty string to hold the current word
    i = 0 # initialize a counter variable
    
    # Iterate through each letter and its corresponding boolean value
    while i < len(letter_list):
        crossed = bool_letter_list[i] 
        # get the boolean value of the current letter
        
        # If the letter is not crossed, add it to the current word
        if not crossed:
            current_word += letter_list[i]
            i += 1
        
        # If the letter is crossed and the current word 
        # is not empty, add it to the magic word
        elif current_word:
            magic_word += current_word
            current_word = ''
            i += 1
        
        # If the letter is crossed and the current word is empty,
        # skip it and move on to the next letter
        else:
            i += 1
    
    # Add the last current word to the magic word if it is not empty
    if current_word:
        magic_word += current_word
    
    return magic_word




def word_search_main(letters, words):
    """
    This function takes a string of letters and a string of words 
    separated by '-' and returns a magic word that can be formed 
    using the given letters.

    Args:
    letters (str): A string of letters.
    words (str): A string of words separated by '-'.

    Returns:
    str: A magic word that can be formed using the given letters.

    Examples:
    >>> word_search_main("EERHTT", "TREE-HOUSE-TEST")
    'TREEHOUSE'
    >>> word_search_main("ABDEFGHILMNOPRSTUWY", "WORD-SEARCH-PUZZLE")
    'WORDPUZZLE'
    >>> word_search_main("AEIOUY", "QUIZ-YOU-A")
    'QUIZ'
    """
    # Convert letters to uppercase and create a list of characters
    letter_list = list(letters.upper())
    
    # Create an empty list to store the words
    word_list = []
    
    # Create an empty string to store the current word
    word = ""
    
    # Loop through each character in the words string
    for char in words:
        # If the character is a '-', the current word is complete
        if char == "-":
            # Add the current word to the word list
            word_list.append(word.upper())
            # Reset the current word
            word = ""
        # If the character is not a '-', add it to the current word
        else:
            word += char
    # Add the final word to the word list
    word_list.append(word.upper())
    
    # Call word_search function and return the magic word
    return word_search(letter_list, word_list)
