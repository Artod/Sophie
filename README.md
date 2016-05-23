# Sophie
A highly-customizable and modular personal assistant bot.

Version 0.1 (23/5/2016)
0.11 - TIME intents added
0.12 - Basic intent parser with highlighting
     - Parsing is slow, since we manually traverse all
       rules to find how to read the intents.
     - Need to develop an automatic LALR parser which optimizes the matches.
     - Plus, the parsing should account for various parsings,
       breakfast can be either a food or timing. We need to put both
       meanings in a stack and check if the sentence means anything for both.
0.13 - Simple tokenizer implementation for integers and floats(numbers)
0.14 - Longest prefix matching implemented

